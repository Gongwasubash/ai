---
title: "Hermes Agent - Full Tutorial & Setup Guide (For Beginners)"
source_file: "Clippings/Hermes Agent - Full Tutorial & Setup Guide (For Beginners).md"
date_ingested: 2026-09-05
tags:
  - hermes
  - tutorial
  - vps
  - openrouter
  - telegram
  - ai-agent
---

# Hermes Agent — Full Tutorial & Setup Guide (Metics Media)

**Source:** YouTube video by [[Metics Media]] (Matt), 2026-08-31
**URL:** https://www.youtube.com/watch?v=DYdvJCxWd6M

## Summary

Zero-to-running beginner build of [[Hermes Agent]]: one-click Hostinger VPS deploy, OpenRouter brain (DeepSeek-V4-Flash), Telegram channel via QR, desktop app as remote gateway, teachable memory, self-written skills + cron jobs so the agent messages first — with real costs (13¢/105 requests) and the context-cache economics behind them.

## Key Takeaways

### Where It Lives
- **Desktop app alone** = fastest try, but dies when the laptop sleeps — no 4 AM cron checks
- **VPS (recommended):** Hostinger KVM 1 (~$6/mo) one-click Hermes template; uncheck the pre-ticked $12 "Ready to Use AI" add-on; 30-day refund; upgrade later without reinstall
- Safety logic: agent runs code/browses on an isolated box — prompt injections can only touch the rented server, not personal files
- Free self-host path exists in official docs

### The Brain
- [[OpenRouter]] account, $5 credits to start, per-key spending limit ($10/week recommended)
- Model: DeepSeek-V4-Flash — cheap, fast, good tool use; switchable anytime (Opus 5 for hard tasks, `/model` on Telegram)
- Alternative: Nous Portal flat ~$20/mo, no keys

### The Phone
- Channels → Telegram → Create with QR (expires ~3 min) → Save and Restart gateway
- `/set home` channel receives cron results; allowlist blocks strangers by default
- 20+ channels (Discord, Slack, WhatsApp, email), one shared memory everywhere

### The Employee Loop
- Tools: web search, drivable browser, files, code execution, image generation, voice, schedules, sub-agents; permission prompts on risky actions
- **Teachable memory:** one plain-language correction ("save that as a preference") persists across brand-new sessions — demoed, not just claimed
- **Payoff pattern:** "watch X, build your own skill, track shown items, schedule every few hours, message me only when new" → agent writes skill + cron job itself, reports land on Telegram
- SOUL.md + Capabilities page (skills/tools/MCP) + Skills Hub (agentskills.io)

### Owner Economics ([[Context Economics]])
- 105 requests ≈ 4M tokens ≈ 38K tokens/message (instructions + memory + tools + history resent every turn) — yet only 13¢, because ~75% hits provider cache
- $5 ≈ ~4,000 messages on this model

### Toolkit & Next
- Logs filters (error/warning/info/debug); fix ladder: Restart Gateway → restart app in Docker Manager → `Hermes Doctor` in web console
- Parallel [[Sub-Agents]] (Lisbon itinerary demo), per-profile agents, OpenClaw config import

## Contradictions / Notes
- Supersedes the Sept-4 "free API struggle": cheap-paid (not free) is the working path — flagged on [[Hermes Agent]]
- Affiliate-driven Hostinger recommendation; VPS pricing/coupons decay — verify before buying
