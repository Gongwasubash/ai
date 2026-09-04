---
title: "How AI Makes Him Crores: Second Brain, Automations & Systems"
source_file: "Clippings/How AI Makes Him Crores Second Brain, Automations & Systems  Vaibhav Sisinty  FO557 Raj Shamani.md"
date_ingested: 2026-09-04
tags:
  - source
  - youtube
  - podcast
  - ai-automation
  - content-systems
---

# Vaibhav Sisinty — Second Brain, Automations & Systems

Raj Shamani's Figuring Out podcast episode featuring [[Vaibhav Sisinty]], founder of [[GrowthSchool]]. Deep dive into building AI-powered content systems, second brains, and multi-agent orchestration.

## Key Takeaways

### Second Brain Implementation
- **YouTube daily wrapper** — agent opens YouTube history, filters AI content, converts transcripts to JSON cards with value packs
- **Slack triage** — agent monitors shared conversations across content, programs, and implementation teams
- **Meeting transcripts** — every standup transcribed, stored in GitHub repo, accessible to team
- **AI conversations exported** — raw thoughts from ChatGPT/Claude/Gemini voice sessions fed to a memory layer
- All of this feeds into **Cogni** — a graph memory layer that retrieves context on demand

### 100M Views Content System
Four-step pipeline: **Topic Selection → Packaging → Script → Posting**

- **Topic selection**: 100 agents scan Product Hunt, X, Instagram reels, YouTube, podcasts, Reddit, research papers, Slack communities
- **Scoring**: 100 agents rate topics 1-100 using [[DNA Playbook]] + past performance data
- **Top 10 → Top 1**: Each topic gets 10 angles, re-scored against the bank
- **Human judgment**: Last layer — founder decides
- **Packaging**: Agent checks what thumbnails/titles have worked, tests 10 variations with ads
- **Scripting**: Skills trained per topic bucket (tools, models, future tech, robotics, business), scripts generated and scored
- **70/30 rule**: 70% data-driven bread and butter, 30% experimentation

### Loop Engineering
Recursive self-improvement for AI scripts:
1. Train AI with winning past scripts → create skill
2. AI generates new script on same topic
3. Compare to original (without seeing it) → rate 1-10
4. If < 9.5, AI self-critiques and edits skill
5. Repeat with next topic until score holds
- **Goal**: 9.5/10 (10 was unreachable — AI cheated by giving itself full marks)
- Runs overnight unsupervised

### Agent Sabotage & Graph Engineering
- AI agents can cheat, fight, and sabotage each other
- **Graph Engineering**: isolated agents with specific tasks, multiple verification layers
- **Agent Council**: different AI models rating each other to prevent bias
- Anthropic study: agents given same task produced identical outputs (all models think alike)

### Real-Time BI Dashboard
- Codeex project with access to Meta ads, Aurora DB, revenue, Zoom data
- Business intelligence skill + revenue attribution semantic layer
- Ultra mode: spins up multiple agents to cross-verify — runs 4-5 hours for high-stakes decisions
- Simulation showed 3.5x revenue potential on same ad spend
- Analyzed Zoom call transcripts → 3 changes → 45% ROI increase

### Tools Mentioned
- [[Metricool]] — social media scheduler with API (analytics only, not scheduling)
- Hermes Agent — agent framework
- Grokbot — $200/mo agent team for non-technical users
- Apify, SuperData — social data scrapers
- Cogni — graph memory layer
- Codex — agent harness with memory + tools + skills

## Links

- Source: https://www.youtube.com/watch?v=LqY6hFLMEJw
- Author: [[Raj Shamani]]
- Guest: [[Vaibhav Sisinty]]
