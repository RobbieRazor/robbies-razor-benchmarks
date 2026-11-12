# Naturepedia MCP — Grok-Assisted Boundary Test (2026-11-12)

**Evidence class:** User-directed, externally reported client functional and boundary observations; **not** an independent certification or a raw network trace  
**Date reported:** 2026-11-12  
**Target:** `https://mcp.robbiegeorgephotography.com/mcp`  
**Reported server:** Naturepedia Canonical Discovery v0.1.2  
**Related primary operator-recorded evidence:** [MCP Inspector interoperability test (2026-11-12)](2026-11-12-inspector-interoperability.md)

## Evidence provenance and independence

The operator opened a new Grok conversation and supplied a neutral test prompt requesting an unscripted evaluation of the remote endpoint. The prompt instructed the evaluator not to assume successful operation, to distinguish observation from metadata claims, to avoid paid requests, and to record successful and negative-path outcomes. The prompt explicitly named the target endpoint and the testing tasks; it did **not** supply expected tool count, expected latency, or expected results.

The evidence available for this record is **Grok's user-supplied textual report**, titled *Independent Naturepedia MCP Interoperability & Boundary Test Report*. This record preserves that report's material findings as **reported**, not as separately verified facts. Grok claimed to use (1) direct `curl` HTTP/2 requests for initialization and tool listing and (2) a connected Naturepedia MCP tool proxy for actual tool invocations. The complete raw curl transcript, request/response headers, full output payloads for every invocation, and proxy audit log were not provided. The connected proxy also means the phrase “no prior server-specific configuration” was not demonstrated for the proxy portion.

Because the report is user-directed and does not include independent, complete wire-level evidence, it should **not** be labeled an independently certified audit or used to substantiate security, statelessness, continuous uptime, or paid delivery.

## Test design supplied to Grok

The operator's new-conversation prompt requested:
1. Fresh Streamable HTTP initialization, capabilities, version and authentication requirements.
2. `tools/list`, including tool descriptions and input schemas.
3. Valid invocation of each public read-only tool with actual inputs and responses.
4. Multiple searches, and canonical resolution using discovered IDs.
5. Negative cases: nonexistent ID, unlikely search query, short schema-invalid fields.
6. Distinction between free public MCP calls and advertised paid x402 resources, **without** initiating payment.
7. Cross-response metadata consistency, limitations, and PASS/FAIL/INCONCLUSIVE/NOT TESTED/BLOCKED classification.
8. Raw protocol transcript or closest available evidence, without inventing results.

## Reported direct transport and protocol operations

Grok described a direct HTTP/2 `curl` request to the target using `Accept: application/json, text/event-stream`.

Reported initialization request:
```json
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}
```

Reported SSE response payload:
```json
{"result":{"protocolVersion":"2025-06-18","capabilities":{"tools":{"listChanged":true}},"serverInfo":{"name":"Naturepedia Canonical Discovery","version":"0.1.2"}},"jsonrpc":"2.0","id":1}
```

The direct `tools/list` response was reported to include three tools, each with a JSON Schema 2020-12 input schema:
- `about_naturepedia`: object; no properties.
- `search_naturepedia`: required string `query`, minimum 2, maximum 200 characters; optional `maxResults`, integer 1–20, default 8.
- `resolve_naturepedia_resource`: required string `identifier`, minimum 2, maximum 500 characters.

**Protocol-version scope:** Grok reported negotiating `2025-06-18` on its direct client. The separate Inspector record negotiated `2025-11-25`. This is evidence of *reported* success for two versions during two tests, not a comprehensive protocol compatibility matrix.

## Reported proxy tool executions and boundary results

| Operation or input | Reported output | Evidence boundary |
|---|---|---|
| `about_naturepedia({})` | Naturepedia publisher, `GC-MRD-v2.0`, pricing manifest v3.0.0, `paidMcpTools:false`, rights references | Response excerpt provided; metadata not independently verified |
| `search_naturepedia({"query":"water systems","maxResults":5})` | 5 results; water systems resource and advertised paid registries/maps/meshes | Result summary, not complete payload |
| `search_naturepedia({"query":"hopf fibration","maxResults":3})` | 1 result, `urn:ai:robbiegeorgephotography:hopf-fibration` | Result summary |
| `search_naturepedia({"query":"earth systems","maxResults":20})` | 20 results; public and advertised paid resource types | Result summary; limit honored for this query |
| `resolve_naturepedia_resource({"identifier":"urn:ai:robbiegeorgephotography:water-systems"})` | `resolved:true`; matching canonical ID and resource URL | Result summary |
| `resolve_naturepedia_resource({"identifier":"hopf-fibration"})` | `resolved:true`; canonical Hopf Fibration resource | Result summary |
| `resolve_naturepedia_resource({"identifier":"urn:ai:robbiegeorgephotography:nonexistent-resource-12345"})` | `resolved:false`, an identifier and catalog source | Negative outcome; excerpt only |
| `search_naturepedia({"query":"xyzzy nonexistent supercalifragilistic","maxResults":5})` | `resultCount:0`, empty `results` array | Negative outcome; excerpt only |
| `search_naturepedia` with `query:"a"` | Input validation error for minimum length 2 | May have been rejected by the proxy, not the production server |
| `resolve_naturepedia_resource` with `identifier:"x"` | Corresponding short-identifier validation error | May have been rejected by the proxy, not the production server |

The report states there were no failures on valid read-only tool calls. It claimed the `/health` endpoint returned HTTP 200 with `{"ok":true,"service":"naturepedia-mcp","version":"0.1.2","mcpEndpoint":"https://mcp.robbiegeorgephotography.com/mcp"}` and about 0.37-second wall time; underlying curl output was not attached. It provided no instrumented per-call latency for proxy tools.

### Payment and governance distinction

Grok reported that discovery and resolution calls completed without a wallet or paid request. The `about_naturepedia` response advertised an x402 pricing manifest (`3.0.0`), Base network `eip155:8453`, USDC, and `paidMcpTools:false`. Search metadata reportedly exposed paid resources. These observations support a bounded claim that **public discovery worked without payment and paid resources were advertised in metadata**.

They do **not** verify protection of paid endpoints, settlement, resource delivery after payment, nor legal enforceability of rights notices. No payments were attempted.

## Reported result matrix

| Area | Report's classification | Our evidence interpretation |
|---|---|---|
| Direct initialize and `tools/list` | PASS | Reported direct HTTP observations; no complete raw transcript |
| `about_naturepedia` | PASS | Proxy call reported successful |
| Three searches | PASS | Proxy searches reported with limits and matching records |
| Canonical resolution by URN and slug | PASS | Proxy resolutions reported successful |
| Nonexistent ID / unlikely query | PASS | Reported distinct negative results |
| Short schema-invalid inputs | PASS | Rejection observed through proxy; enforcement location uncertain |
| Public tool calls without payment | PASS | Reported successful without credentials or settlement |
| x402 paid-route enforcement | NOT TESTED | No payment or protected endpoint test |
| Security certification / scientific claims | NOT TESTED | Outside the scope |

## Findings and limitations

The report provides useful supplementary observations that differ from the first Inspector pass: several thematic catalog queries, full URN and slug resolution, explicit missing-resource and empty-result paths, and negative schema inputs. It did not report material inconsistencies.

**Not established:** universal MCP compatibility, statelessness (`S_persistent = 0`), zero computing/network cost (“zero entropy”), load tolerance, security certification, persistence controls, full catalog correctness, rights compliance by downstream clients, x402 settlement, paid protected delivery, or validity of Robbie's Razor or GC-MRD scientific/computational propositions. Apparent schema validation could originate from the proxy.

## Reproducibility follow-up

An independent evaluator can rerun the above queries with a fresh MCP client and retain complete time-stamped request/response traces. For invalid-input tests, distinguish local/proxy schema validation from validation performed by the server by using a controlled raw MCP call where permitted.

**Publication note:** This record is a carefully attributed summary of the user-supplied Grok report. It is not the original raw trace, and no claim of independent third-party certification is made.
