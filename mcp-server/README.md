# Naturepedia MCP Server

Stateless, read-only Model Context Protocol server for Naturepedia, Robbie's Razor, and GC-MRD-v2.0 discovery.

## Architecture

This project deploys as a separate Cloudflare Worker. It does not replace or modify `cold-bird-7036`. The MCP tools read the live Naturepedia AI catalog at:

`https://www.robbiegeorgephotography.com/.well-known/ai-catalog.json`

## Initial tools

- `about_naturepedia` — returns the publisher, authority, access model, and licensing boundary.
- `search_naturepedia` — searches the live catalog for canonical pages and machine-readable resources.
- `resolve_naturepedia_resource` — resolves an exact catalog ID, identifier, slug, or URL.

## Routes

- `/health` — ordinary HTTP health response.
- `/mcp` — stateless Streamable HTTP MCP endpoint.

## Development

```bash
npm install
npm run typecheck
npm run dev
```

## Deployment

Connect this repository to Cloudflare Workers Builds and set the root directory to `mcp-server`.

- Build command: `npm install && npm run typecheck`
- Deploy command: `npm run deploy`
- Production Worker name: `naturepedia-mcp`
- Intended custom domain: `mcp.robbiegeorgephotography.com`

The first release intentionally contains no paid MCP tools. Existing x402 endpoints remain canonical. Paid MCP tools should be added only after the cold-bird payload builder can be invoked without triggering a second settlement.
