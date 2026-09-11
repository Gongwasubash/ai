---
tags:
  - entity
  - tool
  - mcp
created: 2026-09-10
sources:
  - "89,000 AI Skills for You to Steal"
---

# Skill Retrieval MCP

MCP server that acts as a search engine for AI skills — 89,000+ skills from Anthropic guides and community contributions. Agent searches for relevant skills per request instead of fitting all into context window.

## How It Works

- Agent receives a request
- Searches 89K skills for the most relevant match
- Pulls full context of that skill on demand
- Avoids context window overload (can't fit 89K skills in context)

## Related

- [[MCP (Model Context Protocol)]]
- [[Hermes Agent]] — uses self-written skills; this is the retrieve-instead approach
- [[Jack Roberts]]
