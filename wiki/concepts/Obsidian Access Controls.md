---
tags:
  - concept
  - ai-agents
created: 2026-09-04
sources:
  - "[[Obsidian Agentic AI Access Controls]]"
---

# Obsidian Access Controls

Three-tier access control system for AI agents accessing Obsidian vaults. Controls which notes an agent can see and modify.

## Three Levels

1. **Private** — agent cannot see at all
   - Docker: mount empty folder over private vault folder (masking)
   - Agent sees empty directory

2. **Read Only** — agent can read but not modify
   - Docker: mount with `:ro` flag
   - Agent can search, read, follow links

3. **Read + Write** — full access (default)
   - Agent can create, edit, delete notes
   - Agent can add wiki links

## Implementation Methods

### Docker Mount Controls (Strongest)
- `config.yml` → `mcpasshrough` section
- Bind mounts with mode: nothing, read-only, or read-write
- Enforced at system level — agent cannot bypass

### Skills (Weakest)
- Add rules to Obsidian skill markdown
- Agent might ignore after context compression
- Best practices layer, not security layer

### Host OS Level
- OS-level commands to limit agent access
- Most secure but complex

## Profile-Based Controls

Different Hermes profiles can have different access levels:
- Cloud API profile (OpenAI) = no vault access
- Local model profile (Ollama) = full access

## Why It Matters

- Keeps human notes private from AI
- Protects book quotes, journals, business strategy
- Allows shared knowledge layer without full exposure
- Foundation for safe agentic AI + Obsidian integration

## Related

- [[Hermes Agent]]
- [[LLM Wiki Pattern]]
- [[Second Brain]]
