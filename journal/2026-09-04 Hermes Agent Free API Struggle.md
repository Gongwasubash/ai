---
title: "Trying to Build Hermes Agent with Free API Keys"
date: 2026-09-04
tags:
  - journal
  - hermes
  - free-api
  - problem-solving
---

# Trying to Build Hermes Agent with Free API Keys

## Context

Trying to set up [[Hermes Agent]] using free API providers — OpenCode, NVIDIA, Ollama — but the free models aren't good enough to run Hermes properly. Need to find a solution.

## The Problem

Hermes is a self-improving agent framework that needs a capable "brain" (AI model). Free tiers have limitations:
- **Ollama** — local models, limited by hardware, smaller models lack agent capabilities
- **NVIDIA NIM** — free tier has rate limits, model quality varies
- **OpenCode** — free tier restrictions
- **OpenRouter** — pay-as-you-go but still costs money

Hermes needs models that can:
- Follow complex multi-step instructions
- Use tools and skills effectively
- Maintain context across conversations
- Make decisions about sub-agents and delegation

## What I've Learned

From the [[AI Second Brain for Hermes Agent]] source:
- Hermes got higher completion rates than Claude Code and Codex in benchmarks
- It's the most token-efficient agent harness
- But it still needs a capable model underneath

From [[Hermes Desktop App Setup]]:
- OpenRouter is the recommended provider (pay-as-you-go)
- Claude Sonnet recommended as a good balance of cost/quality
- Need $5-10 minimum credits to start

## Possible Solutions

1. **Ollama with larger models** — if hardware allows, run Llama 3 70B or similar locally
2. **OpenRouter free tier** — some models have free tiers with limits
3. **Google Colab** — free GPU access for running larger models
4. **GitHub Models** — free API access to some models
5. **Groq** — fast inference with free tier limits
6. **Combine providers** — use free tiers across multiple providers to stay within limits
7. **Start with Claude Code** — use existing subscription, then migrate to Hermes later

## Next Steps

- Research which free models are capable enough for agent tasks
- Test Ollama with largest model hardware can handle
- Check OpenRouter free tier options
- Consider if a small monthly cost ($5-10) is worth it for the capability

## Reflection

The pattern keeps appearing: AI tools need capable models, and capable models cost money. The "free" alternative is often time spent troubleshooting instead of building. Sometimes the cheapest solution is paying for the right tool.
