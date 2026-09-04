---
title: "The Ultimate MCP Toolkit is here!"
source_file: "Clippings/The Ultimate MCP Toolkit is here!.md"
date_ingested: 2026-09-04
tags:
  - mcp
  - toolkit
  - manufact
  - deployment
  - piyush-garg
---

# The Ultimate MCP Toolkit — Manufact

**Source:** YouTube video by [[Piyush Garg]]
**Date:** 2026-09-03
**URL:** https://www.youtube.com/watch?v=r05pQRR1dQg

## Summary

Piyush Garg introduces **Manufact** — a comprehensive toolkit for building, deploying, and monitoring [[MCP (Model Context Protocol)]] servers. Manufact simplifies the entire MCP lifecycle from development to production.

## Key Takeaways

### What is Manufact?
- A full-stack [[MCP]] toolkit for building and deploying MCP servers
- Think of it like "Next.js for MCP" — provides framework + cloud hosting
- Handles authentication, deployment, monitoring, and scaling

### Two Products Under Manufact
1. **MCP SDK** — The framework for building MCP tools (like Next.js)
2. **Manufact Cloud** — Cloud hosting for MCP servers (like Vercel)

### How to Build MCP Tools
1. Scaffold a project: `npx create-mcp-app`
2. Choose "MCP App" template
3. Define tools with:
   - **Name** — tool identifier
   - **Description** — what it does
   - **Input Schema** — using Zod for type safety
   - **Output Schema** — return format
   - **View** — optional React component to render
4. Run `npm run dev` to test locally

### Views Feature (Unique)
- MCP tools can return **React components** as views
- These render inside ChatGPT, Claude, or custom frontends
- Example: A "show-app" tool that renders a greeting card

### Deployment Options
1. **Local tunneling** — Built-in tunnel for testing with ChatGPT/Claude
2. **Manufact Cloud** — Deploy to Manufact's cloud infrastructure
3. **Custom domains** — Connect your own domain via Cloudflare

### Connecting to ChatGPT
1. Enable Developer Mode in ChatGPT settings
2. Add a Connector
3. Paste the tunnel or production URL
4. No authentication needed (or configure OAuth)
5. Tools appear automatically in ChatGPT

### Connecting to Claude
1. Similar process — add connector with URL
2. Works with Claude Desktop and Claude.ai
3. Tools show up in the tools list

## Technical Details

- **Language:** TypeScript/Node.js
- **Schema Validation:** Zod
- **Views:** React components
- **Deployment:** Manufact Cloud or custom
- **Domains:** Custom domain support via Cloudflare

## Why It Matters

The main problem with [[MCP]] isn't building servers — it's:
1. **Structuring** them properly
2. **Deploying** securely
3. **Authenticating** users
4. **Monitoring** usage

Manufact solves all four problems in one toolkit.

## Links

- [Manufact Website](https://manufact.com)
- [MCP SDK GitHub](https://github.com/manufact/mcp-sdk)
- [Piyush Garg](https://www.piyushgarg.dev)