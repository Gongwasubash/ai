---
tags:
  - concept
  - ai
  - costs
created: 2026-09-05
sources:
  - "Hermes Agent - Full Tutorial & Setup Guide (For Beginners)"
---

# Context Economics

Why capable agents stay cheap: every turn resends instructions + memory + tools + history (~38K tokens/message), but providers cache the unchanged prefix (~75%), so 4M tokens cost 13¢ and $5 covers ~4,000 messages.

## Rules of Thumb

- The bill is the *model* bill (server is fixed) — watch it per-key with spending limits
- Cheap daily driver (DeepSeek-V4-Flash) + strong model for hard tasks only
- Free-tier models are rate-limited experiments, not production brains

## Related

- [[Hermes Agent]]
- [[OpenRouter]]
- [[Tokens and Context Window]]
