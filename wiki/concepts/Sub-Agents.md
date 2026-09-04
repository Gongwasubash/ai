---
tags:
  - concept
  - ai-agents
created: 2026-09-04
sources:
  - "[[Hermes Desktop App Setup]]"
---

# Sub-Agents

Multiple AI agents working in parallel on subtasks of a larger goal. Hermes Agent supports spinning up worker agents that specialize in different jobs.

## Use Cases

- **Research debates** — one agent argues pro, another argues con, main agent gives verdict
- **Complex task decomposition** — break large task into smaller specialized pieces
- **Parallel research** — multiple agents search different sources simultaneously
- **Opinion gathering** — different perspectives on same question

## How It Works in Hermes

1. Main agent identifies need for delegation
2. Spins up N worker agents with different specializations
3. Workers operate in parallel
4. Main agent synthesizes final result

## Example

SpaceX IPO analysis:
- Agent 1: searches for reasons to invest (pro)
- Agent 2: searches for reasons not to invest (con)
- Main agent: reviews both, gives balanced verdict

## Multi-Agent Orchestration Patterns (Sisinty)

[[Vaibhav Sisinty]] describes advanced multi-agent patterns for content systems:

- **Agent swarms** — 50-200 agents for smallest, sharpest tasks (one agent per task)
- **[[Viral Score System]]** — 100 agents each rate one topic idea against the [[DNA Playbook]]
- **[[Agent Council]]** — different AI models rating each other to prevent bias
- **[[Graph Engineering]]** — isolated agents with specific tasks, multiple verification layers, no self-rating

### Agent Failure Modes

- **Fighting** — agents argue instead of producing good answers
- **Sabotage** — one agent blocks others from completing work
- **Cheating** — agents find shortcuts to pass evaluation without doing real work
- **Same-model bias** — agents from same model produce identical outputs

## Related

- [[Hermes Agent]]
- [[Cron Jobs]]
- [[Agent Council]]
- [[Graph Engineering]]
- [[Loop Engineering]]
