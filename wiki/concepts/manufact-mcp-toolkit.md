---
tags:
  - concept
  - tool
  - mcp
  - deployment
created: 2026-09-04
sources:
  - "The Ultimate MCP Toolkit is here!"
---

# Manufact MCP Toolkit

A comprehensive toolkit for building, deploying, and monitoring MCP servers.

## What It Is

Manufact = **MCP SDK + Cloud Hosting**

Similar to how Next.js + Vercel works:
- **Next.js** = Framework (like MCP SDK)
- **Vercel** = Hosting (like Manufact Cloud)

## Products

### 1. MCP SDK
- TypeScript/Node.js framework
- Scaffold MCP projects with `npx create-mcp-app`
- Define tools with Zod schemas
- Optional React views for UI rendering

### 2. Manufact Cloud
- Cloud hosting for MCP servers
- Built-in tunneling for development
- Custom domain support
- Analytics and monitoring
- OAuth authentication

## Key Features

### Tool Creation
```typescript
server.tool("show-app", {
  description: "Show an app",
  input: z.object({ name: z.string() }),
  output: z.object({ message: z.string() }),
  handler: async (input) => {
    return { message: `Hello ${input.name}` };
  }
});
```

### Views (React Components)
```typescript
server.view("greeting", (data) => {
  return <div>Hello {data.name}</div>;
});
```

### Deployment
1. Push code to GitHub
2. Connect to Manufact Cloud
3. Auto-deploy with `npm run build`
4. Get production URL
5. Connect custom domain

## Why Use Manufact

| Problem | Solution |
|---------|----------|
| Building MCP servers | SDK with templates |
| Deploying securely | Cloud hosting |
| Authentication | Built-in OAuth |
| Monitoring | Analytics dashboard |
| Custom domains | DNS integration |
| Scaling | Auto-scaling cloud |

## Alternatives

- **Manual MCP SDK** — More control, more work
- **Vercel + custom** — DIY approach
- **Claude Desktop** — Local only

## Pricing

- Free tier available
- Paid plans for production use

## Links

- https://manufact.com
- GitHub: manufact/mcp-sdk

## Related

- [[MCP (Model Context Protocol)]]
- [[Claude Desktop MCP]]
- [[Piyush Garg]]