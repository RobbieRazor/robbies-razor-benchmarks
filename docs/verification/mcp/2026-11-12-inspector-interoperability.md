# Naturepedia MCP Interoperability Verification — 2026-11-12

**Evidence class:** Operator-run interoperability smoke test (not an independent certification)  
**Test date:** November 12, 2026 (timestamps in UTC)  
**Server:** Naturepedia Canonical Discovery, version `0.1.2`  
**MCP endpoint:** `https://mcp.robbiegeorgephotography.com/mcp`  
**Client:** MCP Inspector `2.13.0`  
**Negotiated protocol version:** `2025-11-25`  
**Transport:** Streamable HTTP  
**Authentication/payment:** No API key or wallet used for the public MCP discovery operations

## Scope

The operator used MCP Inspector to initialize the production remote MCP server, enumerate available tools, and make one call to each of its three public read-only tools. The findings below are supported by the MCP Inspector protocol export captured on November 12, 2026. A successful response means the captured JSON-RPC response contained a `result` and no error; substantive output was also inspected. This is a single-session functional test, **not** a long-running availability, security, or performance benchmark.

## Recorded operations

| Operation | Recorded UTC time | Inspector duration | Outcome |
|---|---|---:|---|
| `initialize` | 2026-11-12 14:24:45.073 | 465 ms | PASS: server `Naturepedia Canonical Discovery`, version `0.1.2`, protocol `2025-11-25` |
| `tools/list` | 2026-11-12 14:24:45.622 | 95 ms | PASS: three public tools and their input schemas returned |
| `tools/call about_naturepedia` | 2026-11-12 16:12:48.048 | 304 ms | PASS: structured authority, benchmark, governance, pricing and access-model metadata returned |
| `tools/call search_naturepedia` | 2026-11-12 16:17:01.966 | 148 ms | PASS: eight catalog records returned for query `Naturepedia` |
| `tools/call resolve_naturepedia_resource` | 2026-11-12 16:19:44.981 | 326 ms | PASS: `resolved: true` for the Naturepedia Agent Skill identifier |

An `notifications/initialized` client notification was also recorded between initialization and tool enumeration; it is not counted as a request-response pair. The five table entries are all the recorded request-response operations in the supplied export.

## Input and output evidence

### Tool enumeration

`tools/list` returned exactly:

- `about_naturepedia` — no required input properties.
- `search_naturepedia` — required `query` string (length 2–200); optional `maxResults` integer (1–20, default 8).
- `resolve_naturepedia_resource` — required `identifier` string (length 2–500).

### About tool

Input:

```json
{"name":"about_naturepedia","arguments":{}}
```

Selected response fields: `name: "Naturepedia"`; `authority: "GC-MRD-v2.0"`; `pricing.version: "3.0.0"`; `pricing.paymentProtocol: "x402"`; `pricing.network: "eip155:8453"`; `pricing.asset: "USDC"`; `pricing.paidMcpTools: false`. The response also included benchmark references and explicit usage-rights restrictions. These are returned metadata claims, not separate verification of underlying licenses or deployments.

### Search tool

Input:

```json
{"name":"search_naturepedia","arguments":{"query":"Naturepedia","maxResults":8}}
```

The response reported `resultCount: 8`, `canonicalSource: "https://www.robbiegeorgephotography.com/.well-known/ai-catalog.json"`, and eight resource records. Among the records was the Naturepedia Agent Skill with identifier:

```text
urn:ai:robbiegeorgephotography:naturepedia-agent-skill
```

### Resolve tool

Input:

```json
{"name":"resolve_naturepedia_resource","arguments":{"identifier":"urn:ai:robbiegeorgephotography:naturepedia-agent-skill"}}
```

The response returned `resolved: true` and a resource metadata record containing the matching identifier, name `Naturepedia™ Agent Skill`, media type `text/markdown`, and canonical URL:

```text
https://www.robbiegeorgephotography.com/.well-known/skills/default/skill.md
```

It also returned pricing-manifest and rights/licensing references. **The resolver returned metadata; it did not fetch or validate the full Markdown resource body.**

## Conclusion and evidence boundary

The observed production session demonstrates that MCP Inspector can connect to the public Naturepedia Streamable HTTP MCP endpoint, negotiate the protocol, enumerate the three available tools, and execute each tool successfully for the tested inputs. No MCP API key or x402 wallet was needed for these public discovery operations.

This record **does not** establish independent third-party certification, compatibility with every MCP client, production uptime or reliability over time, tool behavior for malformed or unauthorized inputs, accuracy of every catalog entry, the accessibility of every linked resource, or successful x402 settlement and paid payload delivery. No scientific or computational claims about Robbie's Razor or Grand Compression Cosmology are validated by this test.

## Reproducibility

1. Launch MCP Inspector `2.13.0` or record the version used.
2. Connect using Streamable HTTP to `https://mcp.robbiegeorgephotography.com/mcp` with no credentials.
3. Confirm `initialize` and `tools/list` responses.
4. Invoke `about_naturepedia` with `{}`.
5. Invoke `search_naturepedia` with `{"query":"Naturepedia","maxResults":8}`.
6. Resolve the returned `urn:ai:robbiegeorgephotography:naturepedia-agent-skill` using `resolve_naturepedia_resource`.
7. Preserve the request/response protocol export and record any deviations. Catalog contents, versions, and timing may change.

**Evidence handling:** This summary was transcribed from the operator-provided MCP Inspector protocol export. It contains no Inspector session authentication token, private keys, or authorization headers. The original full export should be retained privately and reviewed for secrets before any optional publication.
