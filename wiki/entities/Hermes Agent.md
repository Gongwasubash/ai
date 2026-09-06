---
tags:
  - tool
  - ai-agent
created: 2026-09-04
sources:
  - "[[Hermes Desktop App Setup]]"
  - "[[AI Second Brain for Hermes Agent]]"
  - "[[Obsidian Agentic AI Access Controls]]"
  - "[[Hermes Agent Beginner Tutorial]]"
---

# Hermes Agent

Self-improving AI agent framework by Nous Research. Available as desktop app. Learns from conversations and improves over time through persistent memory.

## Key Features

- **Self-improving** — learns from conversations, gets better over time
- **Persistent memory** — remembers across sessions
- **71+ built-in skills** — computer use, browser automation, PowerPoint, file ops
- **Custom skills** — create your own for repetitive tasks
- **Sub-agents** — spin up multiple agents for parallel work
- **Cron jobs** — scheduled automations
- **Multiple model support** — OpenRouter, Claude, GPT, local models via Ollama

## Desktop App

- Download: [hermes-agent.nousresearch.com/desktop](https://hermes-agent.nousresearch.com/desktop)
- Connect via OpenRouter for pay-as-you-go model access
- Customize persona via Soul.md

## Architecture

- **Harness** (like Claude Code, Codex) — provides tools and skills
- **Brain** (AI model) — user supplies via OpenRouter or direct API
- **Memory** — persistent, self-improving
- **Skills** — markdown instruction files for specific tasks

## Benchmark Performance

- Higher completion rates than Claude Code and Codex
- Cheapest cost per task (most token-efficient)
- One of the fastest agents

## Access Control

- Docker-based execution for safety
- Three-tier access: private, read-only, read-write
- Profile-based access for different models

## Proven VPS Path (Metics Media, Aug 2026)

- Hostinger KVM 1 (~$6/mo) one-click template; desktop app attaches as remote gateway (server URL before `/endpoints`)
- OpenRouter $5 start, $10/week key limit, DeepSeek-V4-Flash main; Nous Portal ~$20/mo flat alternative
- Measured: 105 requests ≈ 4M tokens ≈ 13¢ (75% cache hits) — see [[Context Economics]]
- Telegram QR channel + allowlist; `/set home` for cron results; permission prompts on risky actions
- Correction-to-memory demo verified; self-written skills + cron ("messages first"); `Hermes Doctor` for health

## Contradiction Flag

- Sept-4 journal bet on free providers (Ollama/NVIDIA/OpenCode) and found them too weak for agent work — this source resolves it: the working path is cheap-paid, not free

## Related

- [[OpenRouter]]
- [[Nous Research]]
- [[Metics Media]]
- [[Context Economics]]
- [[Second Brain]]
- [[LLM Wiki]]
- [[Sub-Agents]]
- [[Cron Jobs]]
