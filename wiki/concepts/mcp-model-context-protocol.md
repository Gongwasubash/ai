---
tags:
  - concept
  - protocol
  - ai
  - mcp
created: 2026-09-04
sources:
  - "The Ultimate MCP Toolkit is here!"
  - "AI Second Brain for Hermes Agent"
---

# MCP (Model Context Protocol)

A protocol that allows AI assistants (Claude, ChatGPT, Gemini) to connect to external tools and data sources.

## What It Is

MCP = **Model Context Protocol** — a standard way for AI models to:
1. Discover available tools
2. Call those tools with structured input
3. Receive structured output
4. Render UI components (views)

## Why It Matters

Before MCP, each AI app had its own plugin system:
- ChatGPT had Plugins
- Claude had its own system
- No standardization

MCP creates a **universal standard** that works across all AI apps.

## How It Works

```
AI App (Claude/ChatGPT) → MCP Client → MCP Server → Tools/Data
```

1. **MCP Server** — Hosts tools and data
2. **MCP Client** — Built into AI apps
3. **Transport** — HTTP/SSE or stdio
4. **Tools** — Functions the AI can call

## Building MCP Servers

### Options
1. **Manual** — Build from scratch with MCP SDK
2. **Manufact** — Full toolkit with deployment
3. **Claude Desktop** — Local stdio servers

### Key Concepts
- **Tools** — Functions the AI can call
- **Views** — React components to render
- **Schema** — Input/output validation with Zod
- **Transport** — HTTP/SSE (remote) or stdio (local)

## Deployment

### Local Development
- Use tunneling (Manufact provides this)
- Test with ChatGPT Developer Mode

### Production
- Deploy to cloud (Manufact Cloud, Vercel, etc.)
- Connect custom domains
- Monitor usage and logs

## Platform Support

| Platform | MCP Support |
|----------|-------------|
| Claude Desktop | ✅ Full |
| Claude.ai | ✅ Remote connectors |
| Claude Mobile | ✅ Remote connectors |
| ChatGPT | ✅ Developer Mode |
| Cursor IDE | ✅ Full |
| DeepSeek | ❌ Not yet |
| Gemini | ❌ Not yet |

## Our Implementation

We built a custom MCP server:
- **Location:** `E:\second-brain-mcp\`
- **Remote:** `E:\second-brain-mcp-remote\`
- **Deployed:** https://second-brain-mcp-remote-two.vercel.app
- **Tools:** 7 tools for knowledge base access
- **Auth:** OAuth + PIN (1234)

## Related

- [[Manufact MCP Toolkit]]
- [[Claude Desktop MCP]]
- [[ChatGPT Connectors]]
- [[AI Tool Integration]]