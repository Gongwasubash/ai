---
tags:
  - tool
  - ai-agent
created: 2026-09-04
sources:
  - "[[Hermes Desktop App Setup]]"
  - "[[AI Second Brain for Hermes Agent]]"
  - "[[Obsidian Agentic AI Access Controls]]"
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

## Related

- [[OpenRouter]]
- [[Second Brain]]
- [[LLM Wiki]]
- [[Sub-Agents]]
- [[Cron Jobs]]
