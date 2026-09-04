---
tags:
  - concept
  - content-systems
  - ai-automation
created: 2026-09-04
sources:
  - "[[Vaibhav Sisinty Second Brain Systems]]"
---

# Viral Score System

A content scoring system that rates topic ideas from 1-100 on viral potential, built by [[Vaibhav Sisinty]] for his 100M views content pipeline.

## How It Works

1. **Data sources** scan for 100+ topic ideas (Product Hunt, X, Instagram, YouTube, Reddit, podcasts, research papers)
2. **100 AI agents** spin up — each attached to one idea
3. Each agent checks two evidential layers:
   - Has similar content worked for us before?
   - Has similar content worked for others?
4. Each agent rates topic 1-100 using [[DNA Playbook]] + secondary data
5. Top 10 topics selected
6. Each topic gets 10 angles → re-scored → top 5 topics × 2-3 angles
7. **Human judgment** makes final call

## Weighted Scoring

- Ideas from viral Instagram reels get higher default scores
- News topics get lower default scores
- Human layer data (team annotations on past winners) adds tagging

## Key Insight

70/30 rule: 70% data-driven bread and butter, 30% experimentation. Without the experimentation layer, you go into a silo and eventually stop working.

## Related

- [[DNA Playbook]]
- [[Second Brain]]
- [[Sub-Agents]]
