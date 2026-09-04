---
tags:
  - concept
  - ai-memory
  - knowledge-management
created: 2026-09-04
sources:
  - "[[Vaibhav Sisinty Second Brain Systems]]"
---

# Graph Memory

A memory architecture that preserves relationships between data points, solving the "context rot" problem in LLMs. Used by [[Vaibhav Sisinty]] via **Cogni**.

## The Problem: Context Rot

- Flat context windows lose relevance over time
- Per-chat memory doesn't connect across conversations
- LLM context windows (even 1M tokens) can't hold everything at once
- Like a notepad — you need an index, not the whole book open

## How Graph Memory Works

- Builds an index of all data (YouTube summaries, Slack conversations, meeting transcripts, AI conversations)
- Retrieves only the relevant "book" needed for the current task
- Preserves relationships between data points (not just flat storage)
- Uses graph structure to connect related concepts across different data sources

## Cogni Architecture

```
YouTube daily wrapper → JSON cards
Slack triage → conversation summaries
Meeting transcripts → GitHub repo
AI conversations → raw thought exports
         ↓
    Graph Memory (Cogni)
         ↓
    Agent retrieves relevant context on demand
```

## Why It Matters

Without graph memory, agents compete with humans who have years of passive context accumulation. With graph memory, agents can access the right context at the right time, getting closer to human-level judgment.

## Related

- [[Second Brain]]
- [[Tokens and Context Window]]
- [[Vaibhav Sisinty]]
