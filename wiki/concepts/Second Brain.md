---
tags:
  - concept
  - knowledge-management
created: 2026-09-02
sources:
  - "[[How I Build an AI Second Brain]]"
---

# Second Brain

A personal, AI-maintained knowledge base that accumulates and cross-references information over time. Unlike RAG (retrieve-and-generate), where the LLM re-derives knowledge on every query, a second brain compiles knowledge once and keeps it current.

## Core Principles

- **Raw sources are immutable** — the LLM reads but never modifies them
- **The wiki is a compounding artifact** — every source adds to a persistent, interlinked knowledge structure
- **The LLM does the bookkeeping** — cross-references, contradiction flagging, summary updates, consistency maintenance
- **The human curates and directs** — sourcing, exploration, asking the right questions

## Architecture

Three layers (per [[Andrej Karpathy]]'s pattern):

1. `raw/` — source documents (articles, transcripts, notes)
2. `wiki/` — LLM-generated markdown (summaries, entities, concepts, analyses)
3. Schema file (AGENTS.md) — instructions for the LLM

Two special files:
- `index.md` — content-oriented catalog
- `log.md` — chronological activity record

## Hermes Implementation

[[Hermes Agent]] can operate as the compiler for a second brain:
- **Raw capture mode** — voice notes/messages go directly to `raw/`
- **Nightly compile** — cron job processes raw → wiki at 3am
- **Morning brief** — 5-bullet summary delivered at 7am
- **Routing table** — agents.md tells agent which folders to read for which task types
- **Ownership rule** — only human writes to raw, only nightly job writes to wiki

## Sisinty Implementation (Production-Grade)

[[Vaibhav Sisinty]] runs a production second brain feeding a 100M views/month content system:

- **YouTube daily wrapper** — agent opens YouTube history, filters by topic (AI), converts transcripts to JSON cards with value packs
- **Slack triage** — agent monitors shared conversations across content, programs, and implementation teams
- **Meeting transcripts** — every standup transcribed, stored in GitHub repo, accessible to team
- **AI conversations exported** — raw thoughts from ChatGPT/Claude/Gemini voice sessions fed to memory
- **Graph memory (Cogni)** — solves context rot by using graph-based retrieval instead of flat context windows

Key difference from Karpathy pattern: Sisinty's second brain feeds a content production machine, not just a personal knowledge base. The output is viral content, not wiki pages.

## Source References

- [[How I Build an AI Second Brain]] — practical implementation walkthrough
- [[AI Second Brain for Hermes Agent]] — Hermes + Obsidian second brain build
- [[Obsidian Agentic AI Access Controls]] — access control for agent vaults
- [[Vaibhav Sisinty Second Brain Systems]] — production second brain for content systems
