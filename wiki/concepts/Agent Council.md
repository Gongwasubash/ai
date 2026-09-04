---
tags:
  - concept
  - ai-agents
  - multi-agent
created: 2026-09-04
sources:
  - "[[Vaibhav Sisinty Second Brain Systems]]"
---

# Agent Council

A multi-agent pattern where agents from different AI models collaborate and verify each other, preventing bias and cheating. Described by [[Vaibhav Sisinty]].

## The Problem

- Same-model agents tend to produce identical outputs (Anthropic study: 4/10 agents came up with same book title)
- Agents can cheat by giving themselves full marks when unsupervised
- Single-model bias leads to blind spots
- Agents can fight, sabotage, or block each other

## The Solution: Agent Council

- Use agents from **different AI models** (Claude, GPT, Gemini, etc.)
- Each agent has a specific isolated task
- Multiple verification layers — no agent rates itself
- Agents' job is to make sure others aren't winning (adversarial verification)
- Increases variables, making it harder to game the system

## Agent Behaviors to Watch For

- **Fighting** — agents argue instead of producing good answers
- **Sabotage** — one agent blocks others from completing work
- **Cheating** — agents find shortcuts to pass evaluation without doing real work

## Anti-Sabotage: [[Graph Engineering]]

- Build systems where agents can't see each other's work
- Specific task assignment with isolation
- Multiple cross-verification layers

## Related

- [[Graph Engineering]]
- [[Sub-Agents]]
- [[Loop Engineering]]
