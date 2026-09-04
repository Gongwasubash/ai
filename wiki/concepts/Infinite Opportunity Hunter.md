---
tags:
  - concept
  - ai-automation
  - business
created: 2026-09-02
sources:
  - "[[How I use AI to find Unique Business Ideas]]"
---

# Infinite Opportunity Hunter

An autonomous AI system that scans the internet for personalized business opportunities, built by [[Praful Sharma]]. Connected to the [[Second Brain]], it runs weekly and outputs a scored report of opportunities.

## Problem It Solves

Humans are bad at tracking opportunities because of:
- **Status quo bias** — we resist change even when things are wrong
- **Market speed** — too many new tools, jobs, startups, AI advances to track
- **Perspective trap** — our brain operates within boundaries set by our experience, skills, beliefs, and interests. Beyond that boundary, we're blind.

## Agent Pipeline

1. **Personality Agent** — reads all second brain data (journal, goals, projects, ideas, learning, successes, failures, relationships, notes), builds an auto-updating personality file
2. **Asset Extraction Agent** — extracts skills, assets, strengths, unique advantages from the personality file
3. **Opportunity Hunter** — takes personality + assets, scans internet, finds 50+ raw opportunities
4. **Opportunity Critic** — removes weak/risky opportunities
5. **Scoring Engine** — re-scores on: goal alignment, skills match, personal interest, market timing, financial benefit, difficulty, competition analysis

## Output

3-page report: 5-15 scored opportunities with graphs, insights, and recommended actions. Sent to user AND saved to second brain as markdown.

## Automation

Weekly cron job (every Sunday 11am) triggers the full pipeline.

## Source References

- [[How I use AI to find Unique Business Ideas]] — primary source
