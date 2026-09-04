---
title: "How To Build The ULTIMATE AI Second Brain for Hermes Agent"
source_file: "Clippings/How To Build The ULTIMATE AI Second Brain for Hermes Agent.md"
date_ingested: 2026-09-04
tags:
  - hermes
  - second-brain
  - obsidian
  - llm-wiki
  - automation
---

# AI Second Brain for Hermes Agent

Source: [YouTube](https://www.youtube.com/watch?v=wvYAuHfJRo0) by [[Tom Crawshaw]]

## Summary

Build a second brain (context layer) using Obsidian + Hermes Agent. The second brain turns scattered information (transcripts, calls, notes, messages) into a searchable system so every AI task starts with context instead of a blank slate.

## Architecture

Two parts:
1. **Archive (raw/)** — all raw data: transcripts, documents, PDFs, calls
2. **Compiler (wiki/)** — insights and summaries distilled from raw data

Key insight from [[Andrej Karpathy]]'s LLM Wiki: take raw data, pull out insights so AI doesn't search through all raw transcripts.

## The Ownership Rule

- Only the human writes to `raw/`
- Only the nightly compile job writes to `wiki/`
- This prevents AI from polluting source material

## Build Steps

1. Create Obsidian vault
2. Set up folders: raw/, wiki/, identity.md, projects.md, tasks.md
3. Write agents.md at vault root (ownership rule)
4. Populate identity.md with business context (use prompt interview)
5. Create context_rule.md — "if vault has the answer, never answer from training data"
6. Add routing table to agents.md — which folders to read for which task types
7. Turn on capture mode — voice notes/messages go to raw/ for processing
8. Feed YouTube transcripts into raw/
9. Run compile skill to process raw → wiki
10. Set up nightly cron job (3am compile, 7am brief)

## Why Hermes Over Claude Code

- Higher completion rates in benchmarks
- Cheapest cost per task (more token-efficient)
- One of the fastest agents
- Self-improving with persistent memory

## Related

- [[Hermes Agent]]
- [[LLM Wiki]]
- [[Second Brain]]
- [[Tom Crawshaw]]
- [[Cron Jobs]]
