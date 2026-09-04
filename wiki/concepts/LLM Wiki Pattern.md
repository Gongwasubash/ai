---
tags:
  - concept
  - knowledge-management
created: 2026-09-02
sources:
  - "[[How I Build an AI Second Brain]]"
---

# LLM Wiki Pattern

The pattern described by [[Andrej Karpathy]] for building personal knowledge bases using LLMs. Instead of RAG (retrieve raw docs per query), the LLM incrementally builds and maintains a persistent wiki.

## How It Differs from RAG

| Aspect | RAG | LLM Wiki |
|--------|-----|----------|
| Knowledge | Re-derived every query | Compiled once, kept current |
| Cross-references | Missing | Pre-built by LLM |
| Contradictions | Not flagged | Flagged on ingest |
| Synthesis | Per-query | Persistent and evolving |
| Maintenance cost | Near zero | Near zero (LLM does it) |

## Operations

1. **Ingest** — LLM reads source, creates/updates 10-15 wiki pages, updates index and log
2. **Query** — LLM reads index, finds relevant pages, synthesizes answer with citations; valuable answers filed back as new pages
3. **Lint** — Periodic health check for contradictions, stale claims, orphan pages, missing cross-references

## Why It Works

The tedious part of knowledge management is bookkeeping — updating cross-references, keeping summaries current, noting contradictions. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored and can touch 15 files in one pass.

## Hermes Integration

[[Hermes Agent]] has a built-in LLM Wiki skill. The pattern works well with Hermes because:
- Hermes runs 24/7 on VPS (can process overnight)
- Persistent memory means it learns from previous compilations
- Skills system allows custom compile workflows
- Sub-agents can parallelize the ingest process

## Source References

- [[How I Build an AI Second Brain]] — implementation tutorial
- [[AI Second Brain for Hermes Agent]] — Hermes-specific implementation
- [[Obsidian Agentic AI Access Controls]] — safe agent access to wiki vaults
