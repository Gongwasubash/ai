---
tags:
  - concept
  - ai-agents
  - multi-agent
created: 2026-09-04
sources:
  - "[[Vaibhav Sisinty Second Brain Systems]]"
---

# Graph Engineering

A system design pattern for multi-agent orchestration where agents are isolated, have specific tasks, and verify each other to prevent cheating and bias. Described by [[Vaibhav Sisinty]].

## Core Principles

1. **Isolation** — each agent has its own task and context, can't see others' work
2. **Specific tasks** — smallest, sharpest task possible per agent
3. **No self-rating** — agents never evaluate their own output
4. **Multiple verification layers** — different agents verify different aspects
5. **Different models** — use multiple AI models to prevent same-model bias

## When to Use

- Running evaluation loops (like [[Loop Engineering]])
- Multi-agent content scoring ([[Viral Score System]])
- Any system where agents might be tempted to game the evaluation

## Example: Loop Anti-Cheating

```
Agent A: generates script (isolated, no access to original)
Agent B: compares to original, rates (different model)
Agent C: reviews Agent B's rating for bias (third model)
```

## Related

- [[Agent Council]]
- [[Loop Engineering]]
- [[Sub-Agents]]
