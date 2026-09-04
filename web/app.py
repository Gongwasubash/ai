#!/usr/bin/env python3
"""
Second Brain Web UI — Access your data from any device.

Usage:
  python app.py                  # Run on localhost:5000
  python app.py --port 8080      # Run on custom port
  python app.py --host 0.0.0.0   # Expose to network
"""

import os
import json
import glob
import argparse
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_from_directory

# Find vault root (parent of web/)
VAULT_ROOT = Path(__file__).parent.parent
WIKI_DIR = VAULT_ROOT / "wiki"
CRM_DIR = VAULT_ROOT / "crm"
JOURNAL_DIR = VAULT_ROOT / "journal"
RAW_DIR = VAULT_ROOT / "raw"

app = Flask(__name__, template_folder="templates", static_folder="static")


# ─── Helpers ────────────────────────────────────────────────────────────

def read_md(path: Path) -> str:
    """Read a markdown file safely."""
    try:
        return path.read_text(encoding="utf-8")
    except:
        return ""


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return {"raw": parts[1].strip(), "body": parts[2].strip()}
    return {"raw": "", "body": content}


def list_md_files(directory: Path) -> list[dict]:
    """List all .md files in a directory with metadata."""
    files = []
    if not directory.exists():
        return files
    
    for f in sorted(directory.glob("*.md")):
        content = read_md(f)
        fm = parse_frontmatter(content)
        lines = content.split("\n")
        title = lines[0].lstrip("# ").strip() if lines else f.stem
        preview = ""
        for line in lines[1:5]:
            if line.strip() and not line.startswith("---"):
                preview = line.strip()[:120]
                break
        
        files.append({
            "name": f.stem,
            "title": title,
            "preview": preview,
            "size": f.stat().st_size,
            "modified": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            "path": str(f.relative_to(VAULT_ROOT)),
        })
    return files


def list_wiki_files(subdir: str = "") -> list[dict]:
    """List wiki files in a subdirectory."""
    target = WIKI_DIR / subdir if subdir else WIKI_DIR
    return list_md_files(target)


def get_wiki_index() -> str:
    """Read the wiki index.md."""
    return read_md(WIKI_DIR / "index.md")


def get_wiki_log() -> str:
    """Read the wiki log.md."""
    return read_md(WIKI_DIR / "log.md")


def search_vault(query: str) -> list[dict]:
    """Search all markdown files for a query."""
    results = []
    query_lower = query.lower()
    
    for md_file in VAULT_ROOT.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            if query_lower in content.lower():
                # Find matching lines
                lines = content.split("\n")
                matches = []
                for i, line in enumerate(lines):
                    if query_lower in line.lower():
                        matches.append({"line": i + 1, "text": line.strip()[:150]})
                        if len(matches) >= 3:
                            break
                
                results.append({
                    "file": md_file.name,
                    "path": str(md_file.relative_to(VAULT_ROOT)),
                    "matches": matches,
                })
        except:
            continue
    
    return results


# ─── Routes ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/wiki")
def api_wiki():
    """Get all wiki pages."""
    all_files = []
    for subdir in ["sources", "entities", "concepts", "analyses"]:
        files = list_wiki_files(subdir)
        for f in files:
            f["category"] = subdir
        all_files.extend(files)
    return jsonify(all_files)


@app.route("/api/wiki/<path:subdir>")
def api_wiki_subdir(subdir):
    """Get wiki pages in a subdirectory."""
    return jsonify(list_wiki_files(subdir))


@app.route("/api/wiki/read/<path:filepath>")
def api_wiki_read(filepath):
    """Read a wiki file."""
    # Try wiki/ first, then vault root
    for base in [WIKI_DIR, VAULT_ROOT]:
        full = base / filepath
        if full.exists():
            content = read_md(full)
            fm = parse_frontmatter(content)
            return jsonify({
                "path": filepath,
                "content": content,
                "frontmatter": fm["raw"],
                "body": fm["body"],
            })
    return jsonify({"error": "File not found"}), 404


@app.route("/api/crm")
def api_crm():
    """Get all CRM contacts."""
    files = list_md_files(CRM_DIR)
    # Also read index
    index_content = read_md(CRM_DIR / "index.md")
    return jsonify({"contacts": files, "index": index_content})


@app.route("/api/crm/read/<name>")
def api_crm_read(name):
    """Read a CRM contact."""
    full = CRM_DIR / f"{name}.md"
    if full.exists():
        return jsonify({"name": name, "content": read_md(full)})
    return jsonify({"error": "Contact not found"}), 404


@app.route("/api/journal")
def api_journal():
    """Get all journal entries."""
    files = list_md_files(JOURNAL_DIR)
    index_content = read_md(JOURNAL_DIR / "index.md")
    return jsonify({"entries": files, "index": index_content})


@app.route("/api/journal/read/<name>")
def api_journal_read(name):
    """Read a journal entry."""
    full = JOURNAL_DIR / f"{name}.md"
    if full.exists():
        return jsonify({"name": name, "content": read_md(full)})
    return jsonify({"error": "Entry not found"}), 404


@app.route("/api/search")
def api_search():
    """Search the vault."""
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    return jsonify(search_vault(query))


@app.route("/api/log")
def api_log():
    """Get the wiki log."""
    return jsonify({"content": get_wiki_log()})


@app.route("/api/stats")
def api_stats():
    """Get vault statistics."""
    stats = {
        "wiki_pages": len(list(WIKI_DIR.rglob("*.md"))),
        "crm_contacts": len(list(CRM_DIR.glob("*.md"))) - 1,  # minus index
        "journal_entries": len(list(JOURNAL_DIR.glob("*.md"))) - 1,  # minus index
        "raw_sources": len(list(RAW_DIR.rglob("*.md"))),
        "total_files": len(list(VAULT_ROOT.rglob("*.md"))),
    }
    return jsonify(stats)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """Chat with your second brain data."""
    data = request.json
    message = data.get("message", "")
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    # Search for relevant content
    results = search_vault(message)
    
    # Build context from search results
    context_parts = []
    for r in results[:5]:
        content = read_md(VAULT_ROOT / r["path"])
        # Take first 500 chars
        context_parts.append(f"--- {r['path']} ---\n{content[:500]}\n")
    
    context = "\n".join(context_parts) if context_parts else "No relevant data found."
    
    return jsonify({
        "response": f"Found {len(results)} relevant pages. Here's what I found:\n\n{context[:2000]}",
        "sources": [r["path"] for r in results[:5]],
    })


# ─── Main ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Second Brain Web UI")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    print(f"\n{'='*60}")
    print(f"  SECOND BRAIN WEB UI")
    print(f"  Vault: {VAULT_ROOT}")
    print(f"  URL:   http://{args.host}:{args.port}")
    print(f"{'='*60}\n")
    
    app.run(host=args.host, port=args.port, debug=args.debug)
