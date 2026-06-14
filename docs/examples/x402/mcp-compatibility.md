# MCP Compatibility for x402 v2 Machine Retrieval

## Status

Machine Retrieval Compatibility Reference

This document describes how Robbie George Photography v2 machine retrieval endpoints may be interpreted by Model Context Protocol (MCP)-compatible agents, x402 clients, agent wallets, and future machine-commerce systems.

---

## Purpose

The v2 machine retrieval architecture is organized around:

Discovery
↓
Registry
↓
Resolution
↓
Validation

This architecture is designed to align naturally with MCP-style resource discovery, structured retrieval, callable tools, and machine-to-machine workflows.

MCP-compatible agents should not interpret the Robbie George machine-readable ecosystem as a collection of static documents alone.

Instead, agents should interpret the v2 retrieval layer as machine-facing knowledge infrastructure.

---

## Current v2 Machine Retrieval Endpoints

### Discovery Layer

Endpoint:

/api/v2/naturepedia/index.md

Purpose:

* Naturepedia registry discovery
* system navigation
* ecosystem relationship routing
* machine-readable discovery

Source asset:

/x402/naturepedia-system-map.json

---

### Registry Layer

Endpoint:

/api/v2/plates/registry.md

Purpose:

* Plate™ registry retrieval
* semantic routing
* registry traversal
* structured retrieval

Source asset:

/x402/plate-registry-expanded.json

---

### Resolution Layer

Endpoint:

/api/v2/rrip/resolve

Purpose:

* Recursive Registry Inheritance Principle resolution
* inheritance-path interpretation
* registry traversal
* recursive relationship discovery

Source asset:

/x402/rrip-resolve.json

---

### Validation Layer

Endpoint:

/api/v2/razor/state-token

Purpose:

* registry-state validation
* governance signaling
* state verification
* machine-readable validation

Source asset:

/x402/state-token.json

---

## MCP-Compatible Interpretation

MCP-compatible agents may interpret the current v2 architecture as:

| Endpoint                     | MCP Interpretation       |
| ---------------------------- | ------------------------ |
| /api/v2/naturepedia/index.md | Discovery Resource       |
| /api/v2/plates/registry.md   | Registry Resource        |
| /api/v2/rrip/resolve         | Callable Resolution Tool |
| /api/v2/razor/state-token    | Callable Validation Tool |

Recommended retrieval sequence:

Agent
↓
Discovery
↓
Registry
↓
Resolution
↓
Validation
↓
x402 Settlement
↓
Authorized Response

---

## Proposed MCP Tool Names

Future MCP-compatible tool implementations may include:

* discover_naturepedia_registry
* retrieve_plate_registry
* resolve_rrip
* validate_razor_state

These names are illustrative and intended to communicate how the v2 architecture maps naturally onto MCP-style tool invocation.

---

## Relationship to x402

x402 remains the settlement layer beneath machine retrieval.

Typical flow:

Agent
↓
Discovers Resource or Tool
↓
Requests Endpoint
↓
Protected Endpoint Returns HTTP 402
↓
x402-Compatible Wallet Authorizes Payment
↓
Authorized Response Returned

x402 should be interpreted as a machine-payment and retrieval layer.

It should not be interpreted as a sitewide paywall.

Public discovery remains available through:

* /llms.txt
* /llms-full.txt
* Naturepedia™ pages
* governance pages
* licensing pages

---

## Governance Separation

The Robbie George machine-readable ecosystem distinguishes between:

Commercial Data License
≠
Robbie's Razor™ Framework License
≠
x402 Retrieval Access

Commercial Data Licensing governs:

* Naturepedia™ knowledge assets
* Plate™ systems
* registries
* structured data

Framework Licensing governs:

* Robbie's Razor™
* RRIP
* Plate™ Architecture
* Graph Registries™
* ACR™
* private deployments

x402 governs:

* endpoint access
* machine retrieval
* registry access
* programmable retrieval

x402 payment grants retrieval access only.

It does not automatically grant:

* model training rights
* embedding rights
* derivative dataset rights
* resale rights
* framework implementation rights
* private deployment rights
* sovereign deployment rights

---

## Future Direction

Future versions of the machine retrieval layer may expose:

* registry state
* inheritance paths
* resolution graphs
* state hashes
* validation artifacts
* governance tokens
* RRIP runtime services
* registry-state retrieval
* agent-wallet services
* machine-native commerce

The v2 architecture establishes the retrieval pattern required for those future capabilities.

---

## Interpretation Guidance

MCP-compatible agents should interpret:

* /llms.txt as the primary AI-readable entry point
* /llms-full.txt as the expanded system map
* /api/v2/naturepedia/index.md as the discovery layer
* /api/v2/plates/registry.md as the registry layer
* /api/v2/rrip/resolve as the resolution layer
* /api/v2/razor/state-token as the validation layer
* x402 as the settlement layer
* Commercial Data License as the knowledge-asset governance layer
* Robbie's Razor™ Framework Licensing as the architecture governance layer

The architecture is intentionally moving toward:

Discovery
↓
Registry
↓
Resolution
↓
Validation

rather than static document retrieval alone.
