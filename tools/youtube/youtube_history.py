import re
import json
import os
import sys
import time as time_mod
from pathlib import Path
from html import unescape

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

API_KEY = os.getenv("API_KEY")
RAW_DIR = Path(__file__).resolve().parent.parent.parent / "raw"


def extract_video_id(url: str) -> str | None:
    match = re.search(r"(?:v=|/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None


def load_watch_history_html(takeout_path: str) -> list[dict]:
    entries = []
    with open(takeout_path, "r", encoding="utf-8") as f:
        for line in f:
            if "youtube.com/watch" not in line:
                continue
            pattern = r'href="(https?://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]{11})">([^<]+)</a>'
            for m in re.finditer(pattern, line):
                url = m.group(1)
                title = unescape(m.group(2).strip())
                video_id = extract_video_id(url)

                after = line[m.end():m.end()+300]
                channel_m = re.search(r'youtube\.com/(?:channel|user)/[^"]*">([^<]+)</a>', after)
                channel = channel_m.group(1).strip() if channel_m else "Unknown"

                entries.append({
                    "title": title,
                    "url": url,
                    "video_id": video_id,
                    "channel": channel,
                    "time": "",
                })
    return entries


def load_watch_history(takeout_path: str) -> list[dict]:
    with open(takeout_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    entries = []
    for item in data:
        video_id = None
        url = item.get("titleUrl", "")
        if url:
            video_id = extract_video_id(url)
        entries.append({
            "title": item.get("title", "Unknown"),
            "url": url,
            "video_id": video_id,
            "channel": item.get("subtitles", [{}])[0].get("name", "Unknown") if item.get("subtitles") else "Unknown",
            "channel_url": item.get("subtitles", [{}])[0].get("url", "") if item.get("subtitles") else "",
            "time": item.get("time", ""),
        })
    return entries


def enrich_with_api(video_ids: list[str], api_key: str) -> dict:
    youtube = build("youtube", "v3", developerKey=api_key)
    enriched = {}
    for i in range(0, len(video_ids), 50):
        batch = [vid for vid in video_ids[i:i+50] if vid]
        if not batch:
            continue
        try:
            response = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=",".join(batch)
            ).execute()
            for item in response.get("items", []):
                vid = item["id"]
                snippet = item.get("snippet", {})
                content = item.get("contentDetails", {})
                stats = item.get("statistics", {})
                enriched[vid] = {
                    "description": snippet.get("description", "")[:500],
                    "tags": snippet.get("tags", []),
                    "category": snippet.get("categoryId", ""),
                    "duration": content.get("duration", ""),
                    "view_count": stats.get("viewCount", "0"),
                    "like_count": stats.get("likeCount", "0"),
                }
        except HttpError as e:
            print(f"API error on batch {i//50}: {e}")
            time_mod.sleep(5)
        time_mod.sleep(0.5)
    return enriched


def process_takeout(takeout_path: str):
    print(f"Loading watch history from: {takeout_path}")

    if takeout_path.endswith(".html"):
        entries = load_watch_history_html(takeout_path)
    else:
        entries = load_watch_history(takeout_path)

    print(f"Found {len(entries)} entries")

    video_ids = list(set(e["video_id"] for e in entries if e["video_id"]))
    print(f"Extracted {len(video_ids)} unique video IDs")

    enriched = {}
    if API_KEY and video_ids:
        print(f"Enriching with YouTube Data API (this may take a while)...")
        enriched = enrich_with_api(video_ids, API_KEY)
        print(f"Enriched {len(enriched)} videos")
    elif not API_KEY:
        print("No API_KEY set -- skipping metadata enrichment")

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    md_lines = []
    md_lines.append("---")
    md_lines.append(f'title: "YouTube Watch History"')
    md_lines.append("tags:")
    md_lines.append("  - youtube")
    md_lines.append("  - clippings")
    md_lines.append(f"entries: {len(entries)}")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("# YouTube Watch History")
    md_lines.append("")

    for entry in entries:
        meta = enriched.get(entry["video_id"], {})
        md_lines.append(f"## {entry['title']}")
        md_lines.append("")
        md_lines.append(f"**Channel:** {entry['channel']}")
        md_lines.append(f"**URL:** {entry['url']}")
        if entry["time"]:
            md_lines.append(f"**Watched:** {entry['time']}")
        if meta:
            if meta.get("duration"):
                md_lines.append(f"**Duration:** {meta['duration']}")
            if meta.get("tags"):
                md_lines.append(f"**Tags:** {', '.join(meta['tags'][:5])}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    filepath = RAW_DIR / "YouTube Watch History.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Wrote {filepath}")
    print(f"Total entries: {len(entries)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_history.py <path_to_watch-history.json or .html>")
        sys.exit(1)
    process_takeout(sys.argv[1])
