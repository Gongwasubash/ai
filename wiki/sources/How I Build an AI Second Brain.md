---
title: "How I build an AI Second Brain in 11 Minutes"
source_file: "Clippings/How I build an AI Second Brain in 11 Minutes (Obsidian + Claude CodeCodex).md"
date_ingested: 2026-09-02
tags:
  - tutorial
  - second-brain
  - obsidian
  - karpathy
---

# How I build an AI Second Brain in 11 Minutes

YouTube tutorial by [[Praful Sharma]] demonstrating how to build a second brain following [[Andrej Karpathy]]'s LLM Wiki pattern using Obsidian + ChatGPT Codex.

## Key Takeaways

- Three-layer architecture: **raw/** (immutable inputs), **wiki/** (LLM-maintained), and an **outputs/** folder for query results
- Tools: Obsidian, Obsidian Web Clipper (browser extension), ChatGPT Codex (or PlotCode)
- The AI agent auto-generates the folder structure and AGENTS.md from Karpathy's gist link
- Web Clipper can pull YouTube video transcripts directly into Obsidian
- After ingesting a few sources, the wiki builds cross-references and a graph view emerges
- Two extra features beyond Karpathy's base pattern: **journal entries** and a **CRM** for tracking people you meet

## Architecture Described

1. `raw/` — dump everything here (articles, video transcripts, research)
2. `wiki/` — LLM processes and structures the knowledge here
3. `outputs/` — saved query results
4. One file (AGENTS.md) — tells the LLM how to operate

## Setup Steps

1. Install Obsidian, create vault named "Second Brain"
2. Install Obsidian Web Clipper extension
3. Open ChatGPT Codex, point it at the vault folder
4. Paste Karpathy's gist link, tell it to build the wiki architecture
5. Use Web Clipper to clip articles/transcripts into `raw/`
6. In Codex, type "process the raw file" to trigger ingest
7. Query the wiki via Codex chat

## Extra Modifications Mentioned

- Added a `processed/` subfolder — after ingest, raw files move there to reduce clutter
- Added cross-linking: wiki pages generated/updated get linked back to the original source page
- Added journal and CRM prompts for daily life tracking
