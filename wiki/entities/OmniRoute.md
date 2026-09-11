---
tags:
  - tool
  - gateway
  - ai-provider
created: 2026-09-11
sources:
  - "[[Set Up Hermes Agent for FREE & Unlimited Complete Tutorial]]"
---

# OmniRoute

Local AI gateway that routes requests through 352+ AI providers with auto-fallback. Open-source project by diegosouzapw.

## Key Features

- **Multi-provider support:** Antigravity, AgentRouter, OpenRouter, Kiro, NVIDIA NIM, Ollama Cloud
- **Auto-fallback:** Automatically switch to next provider if one fails
- **Provider combos:** Create custom combos with round-robin load balancing
- **Free models:** Import only free models from each provider
- **Web UI:** Dashboard for managing providers, combos, API keys

## Installation

`ash
npm install -g omniroute
omniroute  # start server
`

## Configuration

1. Install Node.js and OmniRoute globally
2. Start OmniRoute server (redirects to web UI)
3. Add providers with API keys
4. Create provider combos with selected providers
5. Generate OmniRoute API key
6. Connect Hermes Agent to OmniRoute endpoint

## Provider Setup

- **Antigravity:** Google login, free Gemini/GPT models
- **AgentRouter:** GitHub login,  free credits
- **OpenRouter:** Google login, 21 free models
- **Kiro:** Google login, free models
- **NVIDIA NIM:** Email login, GLM/Minimax/JMA models
- **Ollama Cloud:** API key, 6 free models

## Use Cases

- Free unlimited AI provider access
- Load balancing across multiple providers
- Fallback for high availability
- Hermes Agent integration

## Related

- [[Hermes Agent]]
- [[Nous Research]]
- [[Antigravity]]
- [[OpenRouter]]
- [[Ollama]]
- [[AI Gateway]]