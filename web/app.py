#!/usr/bin/env python3
"""
Second Brain AI — Chat with your Obsidian data using Gemini.

Usage:
  python app.py                  # Run on localhost:5000
  python app.py --port 8080      # Run on custom port
  python app.py --host 0.0.0.0   # Expose to network
"""

import os
import json
import glob
import hashlib
import argparse
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, Response, stream_with_context

# ─── Config ─────────────────────────────────────────────────────────────

VAULT_ROOT = Path(__file__).parent.parent
WIKI_DIR = VAULT_ROOT / "wiki"
CRM_DIR = VAULT_ROOT / "crm"
JOURNAL_DIR = VAULT_ROOT / "journal"
RAW_DIR = VAULT_ROOT / "raw"
CONFIG_PATH = Path("E:/second-brain/config.json")

# Load Gemini API key
GEMINI_API_KEY = ""
GEMINI_MODEL = "gemini-2.5-flash"
try:
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
        GEMINI_API_KEY = cfg.get("llm", {}).get("api_key", "")
        GEMINI_MODEL = cfg.get("llm", {}).get("model", "gemini-2.5-flash")
except:
    pass

# Fallback: try .env
if not GEMINI_API_KEY:
    env_path = Path("E:/New folder (2)/.env")
    try:
        for line in env_path.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY="):
                GEMINI_API_KEY = line.split("=", 1)[1]
                break
    except:
        pass

app = Flask(__name__, template_folder="templates", static_folder="static")

# ─── File Helpers ───────────────────────────────────────────────────────

def read_md(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except:
        return ""

def list_md_files(directory: Path) -> list[dict]:
    files = []
    if not directory.exists():
        return files
    for f in sorted(directory.glob("*.md")):
        content = read_md(f)
        lines = content.split("\n")
        title = lines[0].lstrip("# ").strip() if lines else f.stem
        preview = ""
        for line in lines[1:5]:
            if line.strip() and not line.startswith("---") and not line.startswith("tags:"):
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

# ─── RAG: Search + Context Building ────────────────────────────────────

def search_vault(query: str, max_results: int = 8) -> list[dict]:
    """Search all markdown files, return ranked results with content."""
    results = []
    query_lower = query.lower()
    keywords = [w for w in query_lower.split() if len(w) > 2]

    for md_file in VAULT_ROOT.rglob("*.md"):
        # Skip web UI files
        if "web" in str(md_file):
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
            content_lower = content.lower()

            # Score: count keyword matches
            score = 0
            for kw in keywords:
                score += content_lower.count(kw)

            if score == 0:
                continue

            # Extract relevant sections
            lines = content.split("\n")
            relevant_lines = []
            for i, line in enumerate(lines):
                if any(kw in line.lower() for kw in keywords):
                    # Get surrounding context (2 lines before/after)
                    start = max(0, i - 2)
                    end = min(len(lines), i + 3)
                    for j in range(start, end):
                        if lines[j].strip():
                            relevant_lines.append(lines[j].strip())

            # Deduplicate while preserving order
            seen = set()
            unique_lines = []
            for line in relevant_lines:
                if line not in seen:
                    seen.add(line)
                    unique_lines.append(line)

            results.append({
                "file": md_file.name,
                "path": str(md_file.relative_to(VAULT_ROOT)),
                "score": score,
                "content": "\n".join(unique_lines[:20]),
                "full_content": content[:3000],
            })
        except:
            continue

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_results]


def build_context(query: str) -> tuple[str, list[str]]:
    """Build RAG context from vault search results."""
    results = search_vault(query, max_results=6)

    if not results:
        return "No relevant data found in the second brain.", []

    context_parts = []
    sources = []
    for r in results:
        context_parts.append(f"=== {r['path']} ===\n{r['full_content'][:1500]}\n")
        sources.append(r["path"])

    context = "\n\n".join(context_parts)
    return context, sources

# ─── Gemini API ─────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are Subash's Second Brain AI assistant. You have access to his entire Obsidian knowledge base including:
- Wiki pages (sources, entities, concepts, analyses)
- CRM contacts
- Journal entries
- Raw source summaries

RULES:
1. Answer ONLY based on the provided context. If the data doesn't contain the answer, say so.
2. Be concise and direct. Use bullet points when helpful.
3. When referencing data, mention the source file name.
4. You can synthesize information across multiple pages.
5. For CRM questions, provide contact details if available.
6. For journal questions, summarize entries.
7. Use markdown formatting for readability.
8. If asked to "add" or "create" something, explain what you'd need to do it.

You know about Subash's interests: AI automation, content creation, Nepal history (Mahispal dynasty), video production, and building systems."""


def call_gemini(prompt: str, context: str = "") -> str:
    """Call Gemini API for response."""
    if not GEMINI_API_KEY:
        return "Gemini API key not configured. Please set GEMINI_API_KEY in config.json or .env"

    full_prompt = f"{SYSTEM_PROMPT}\n\n--- SECOND BRAIN DATA ---\n{context}\n\n--- USER QUESTION ---\n{prompt}"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4096,
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        resp = urllib.request.urlopen(req, timeout=60)
        result = json.loads(resp.read())
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Gemini API error: {e}"


def call_gemini_stream(prompt: str, context: str = ""):
    """Call Gemini API with streaming."""
    if not GEMINI_API_KEY:
        yield "Gemini API key not configured."
        return

    full_prompt = f"{SYSTEM_PROMPT}\n\n--- SECOND BRAIN DATA ---\n{context}\n\n--- USER QUESTION ---\n{prompt}"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:streamGenerateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4096,
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        resp = urllib.request.urlopen(req, timeout=120)
        buffer = ""
        for chunk in resp:
            buffer += chunk.decode("utf-8", errors="replace")
            # Try to parse complete JSON objects
            while True:
                try:
                    # Find next complete object
                    start = buffer.find('{"candidates"')
                    if start == -1:
                        buffer = buffer[-100:]
                        break
                    end = buffer.find("}", start)
                    if end == -1:
                        break
                    # Check if this is complete
                    obj_str = buffer[start:end+1]
                    obj = json.loads(obj_str)
                    text = obj.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    if text:
                        yield text
                    buffer = buffer[end+1:]
                except json.JSONDecodeError:
                    break
    except Exception as e:
        yield f"\n\n[Gemini API error: {e}]"


# ─── API Routes ─────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/stats")
def api_stats():
    return jsonify({
        "wiki_pages": len(list(WIKI_DIR.rglob("*.md"))),
        "crm_contacts": max(0, len(list(CRM_DIR.glob("*.md"))) - 1),
        "journal_entries": max(0, len(list(JOURNAL_DIR.glob("*.md"))) - 1),
        "raw_sources": len(list(RAW_DIR.rglob("*.md"))),
        "total_files": len(list(VAULT_ROOT.rglob("*.md"))),
    })


@app.route("/api/wiki")
def api_wiki():
    all_files = []
    for subdir in ["sources", "entities", "concepts", "analyses"]:
        files = list_md_files(WIKI_DIR / subdir)
        for f in files:
            f["category"] = subdir
        all_files.extend(files)
    return jsonify(all_files)


@app.route("/api/wiki/read/<path:filepath>")
def api_wiki_read(filepath):
    for base in [WIKI_DIR, VAULT_ROOT]:
        full = base / filepath
        if full.exists():
            return jsonify({"path": filepath, "content": read_md(full)})
    return jsonify({"error": "Not found"}), 404


@app.route("/api/crm")
def api_crm():
    return jsonify({"contacts": list_md_files(CRM_DIR), "index": read_md(CRM_DIR / "index.md")})


@app.route("/api/crm/read/<name>")
def api_crm_read(name):
    full = CRM_DIR / f"{name}.md"
    if full.exists():
        return jsonify({"name": name, "content": read_md(full)})
    return jsonify({"error": "Not found"}), 404


@app.route("/api/journal")
def api_journal():
    return jsonify({"entries": list_md_files(JOURNAL_DIR), "index": read_md(JOURNAL_DIR / "index.md")})


@app.route("/api/journal/read/<name>")
def api_journal_read(name):
    full = JOURNAL_DIR / f"{name}.md"
    if full.exists():
        return jsonify({"name": name, "content": read_md(full)})
    return jsonify({"error": "Not found"}), 404


@app.route("/api/log")
def api_log():
    return jsonify({"content": read_md(WIKI_DIR / "log.md")})


@app.route("/api/search")
def api_search():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    return jsonify(search_vault(query))


# ─── AI Chat Routes ────────────────────────────────────────────────────

@app.route("/api/chat", methods=["POST"])
def api_chat():
    """AI-powered chat with RAG."""
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])

    if not message:
        return jsonify({"error": "No message"}), 400

    # RAG: search vault for context
    context, sources = build_context(message)

    # Build conversation with history
    conversation = ""
    for h in history[-6:]:  # Last 6 messages
        role = h.get("role", "user")
        conversation += f"{role}: {h.get('content', '')}\n"
    conversation += f"user: {message}"

    # Call Gemini
    answer = call_gemini(conversation, context)

    return jsonify({
        "response": answer,
        "sources": sources,
    })


@app.route("/api/chat/stream", methods=["POST"])
def api_chat_stream():
    """AI-powered chat with streaming."""
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])

    if not message:
        return jsonify({"error": "No message"}), 400

    # RAG: search vault for context
    context, sources = build_context(message)

    # Build conversation
    conversation = ""
    for h in history[-6:]:
        role = h.get("role", "user")
        conversation += f"{role}: {h.get('content', '')}\n"
    conversation += f"user: {message}"

    def generate():
        # First send sources
        yield json.dumps({"sources": sources}) + "\n"
        # Then stream answer
        for chunk in call_gemini_stream(conversation, context):
            yield json.dumps({"text": chunk}) + "\n"

    return Response(stream_with_context(generate()), content_type="application/x-ndjson")


# ─── Main ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  SECOND BRAIN AI")
    print(f"  Vault:  {VAULT_ROOT}")
    print(f"  LLM:    {GEMINI_MODEL}")
    print(f"  API:    {'Set' if GEMINI_API_KEY else 'MISSING'}")
    print(f"  URL:    http://{args.host}:{args.port}")
    print(f"{'='*60}\n")

    app.run(host=args.host, port=args.port, debug=args.debug)
