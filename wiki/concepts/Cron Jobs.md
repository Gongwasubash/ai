---
tags:
  - concept
  - ai-agents
created: 2026-09-04
sources:
  - "[[Hermes Desktop App Setup]]"
  - "[[AI Second Brain for Hermes Agent]]"
---

# Cron Jobs

Scheduled automations that run at defined times. In Hermes, cron jobs enable recurring tasks like data collection, report generation, and nightly processing.

## Examples

- **Reddit scraping** — every 3 days, scrape r/ClaudeAI for new posts, generate PDF report
- **Nightly compile** — every night at 3am, process raw/ folder into wiki
- **Morning brief** — every day at 7am, send 5-bullet summary of what happened
- **Content monitoring** — periodic check for competitor updates

## Setup in Hermes

- Click cron button in chat interface
- Or ask Hermes to set up a cron job
- Define schedule (interval or specific time)
- Define task (what to do)
- Output saved to artifacts or file system

## Use with Second Brain

- Nightly: compile raw → wiki (3am)
- Morning: send brief of compiled changes (7am)
- Weekly: lint wiki for contradictions and stale claims

## Related

- [[Hermes Agent]]
- [[Second Brain]]
- [[Sub-Agents]]
