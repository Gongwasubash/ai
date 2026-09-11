---
title: "Set Up Hermes Agent for FREE & Unlimited | Complete Tutorial"
source_file: "Clippings/Set Up Hermes Agent for FREE & Unlimited  Complete Tutorial.md"
date_ingested: 2026-09-11
tags:
  - hermes-agent
  - omniroute
  - ai-agent
  - free-ai
  - tutorial
---

# Set Up Hermes Agent for FREE & Unlimited (Ai with Rajpalsinh)

**Source:** YouTube video by [[Ai with Rajpalsinh]], 2026-09-10
**URL:** https://www.youtube.com/watch?v=sp75R7u6QIw

## Summary

Step-by-step guide to installing [[Hermes Agent]] (free open-source desktop AI agent by [[Nous Research]]) and connecting it to [[OmniRoute]] local gateway for 352+ AI providers with auto-fallback. Covers Node.js setup, API key generation, provider combos, and permanent configuration.

## Key Takeaways

### Installation
- Download Hermes Agent desktop app (Windows/macOS/Linux) from official site
- App automatically installs Python and prerequisites
- Alternative: manual install via terminal (requires Node.js, Git, Python)

### OmniRoute Setup
- Install Node.js and OmniRoute globally (
pm install -g omniroute)
- Start OmniRoute server, access web UI with default password
- Configure providers: Antigravity, AgentRouter, OpenRouter, Kiro, NVIDIA NIM, Ollama Cloud

### Provider Configuration
- **Antigravity:** Google login, free models (Gemini 3.7, Sonnet 4.6, GPT models)
- **AgentRouter:** GitHub login,  free credits, Claude Opus 4.8/5, GPT-5.6
- **OpenRouter:** Google login, 21 free models
- **Kiro:** Google login, free models
- **NVIDIA NIM:** Email login, GLM 5.2, Minimax M2.7, JMA 4
- **Ollama Cloud:** API key, 6 free models

### Provider Combo Creation
- Create "Hermes Combo" with all providers
- Set round-robin strategy for load balancing
- Test combo to verify which models work

### Hermes Agent Configuration
- Settings → Provider → Custom Endpoint
- Endpoint name = combo name, provider ID = same
- Endpoint URL from HTML guide
- Default model: auto
- Context: 13172 (critical for OmniRoute compatibility)
- Paste OmniRoute API key

### Use Cases
- Import/export document audit agent
- Real estate lead research agent
- Competitive analysis agent
- Custom automation workflows

## Contradictions / Notes
- Previous knowledge about paid providers; this shows free unlimited path via OmniRoute
- Requires 64K+ context model for Hermes Agent to function properly