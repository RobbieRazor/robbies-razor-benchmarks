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

x402 remains the settlement layer beneath protected Naturepedia™ machine retrieval.

The official Naturepedia MCP interface is a public discovery and resolution layer. MCP tool invocation does not itself initiate x402 settlement.

Official MCP endpoint:

    https://mcp.robbiegeorgephotography.com/mcp

Health endpoint:

    https://mcp.robbiegeorgephotography.com/health

MCP server card:

    https://www.robbiegeorgephotography.com/.well-known/mcp/server-card.json

Authoritative x402 pricing manifest:

    https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

The architecture should be interpreted as:

    MCP Discovery
    ↓
    Resource Resolution
    ↓
    Public Resource OR Protected Resource
    ↓
    If protected:
    x402 Availability Validation
    ↓
    Payment Challenge
    ↓
    Verification
    ↓
    Settlement
    ↓
    Fidelity Validation
    ↓
    Authorized Response

MCP discovery and x402 settlement are therefore complementary but distinct layers.

    MCP discovery
    ≠ x402 payment
    ≠ commercial licensing
    ≠ framework licensing
    ≠ scientific validation

### Current x402 Retrieval Classes

Current production pricing version:

    3.0.0

Network:

    Base / eip155:8453

Asset:

    USDC

Current retrieval classes:

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered and validated payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

### Active Atomic Query Route

Public route:

    /v1/query/atomic/robbie-george-biography-plate

Canonical internal route:

    /x402/query/atomic/robbie-george-biography-plate

Canonical Plate identifier:

    robbie-george#robbie-george-biography-plate

Canonical authority:

    https://www.robbiegeorgephotography.com/who-is-robbie-george

Production Atomic configuration:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active for registered deterministic payloads

Verified production challenge:

    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED: true
    RESULT: PASS

No Atomic payment payload was supplied during this activation validation.

No new Atomic settlement or protected Atomic HTTP 200 payload-delivery test was performed.

### Atomic Availability Boundary

MCP-compatible agents MUST NOT assume that every URL matching the Atomic route family represents a payable resource.

Required production behavior:

    Registered + complete Atomic resource
    → HTTP 402 Payment Required
    → amount 5000
    → gateway tier atomic

    Known + incomplete Atomic resource
    → HTTP 409 Conflict
    → no payment challenge

    Unknown Atomic resource
    → HTTP 404 Not Found
    → no payment challenge

Known-but-incomplete production test:

    /v1/query/atomic/robbies-razor-plate
    → 409
    → ATOMIC_PAYLOAD_NOT_REGISTERED
    → no payment challenge
    → PASS

Unknown Atomic resource test:

    → 404
    → ATOMIC_RESOURCE_NOT_FOUND
    → no payment challenge
    → PASS

This fail-closed model prevents an MCP-compatible agent or wallet from being asked to pay for a resource that is not actually available for delivery.

### Enriched Query Status

The Enriched Query class remains reserved.

Current configuration:

    Access class: enriched
    Price: 0.025 USDC
    Atomic units: 25000
    Route status: reserved

MCP-compatible agents MUST NOT treat Enriched Query retrieval as active merely because its price is published.

Enriched payment challenges must remain disabled until governed deterministic payloads are explicitly registered and production validated.

### Structured Plate Retrieval

Current active Structured Plate™ routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

Production configuration:

    Access class: single-plate
    Price: 0.25 USDC
    Atomic units: 250000

Verified challenge behavior for all three:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true
    RESULT: PASS

Unknown Plate identifiers return `404` without a payment challenge.

Known Plates without registered complete payloads return `409` without a payment challenge.

### Recommended MCP-to-x402 Flow

A future MCP-compatible agent-wallet workflow may operate as:

    Agent
    ↓
    MCP discovery
    ↓
    Resolve Naturepedia resource
    ↓
    Inspect canonical pricing manifest
    ↓
    Determine whether resource is public or protected
    ↓
    Validate resource availability
    ↓

    Public
    → retrieve directly

    Protected but unknown
    → 404
    → stop

    Protected but incomplete
    → 409
    → stop

    Protected and available
    → 402 Payment Required
    ↓
    Agent or wallet evaluates price and policy
    ↓
    Payment authorization
    ↓
    Verification
    ↓
    Settlement
    ↓
    Protected payload fidelity validation
    ↓
    Authorized retrieval

x402 should be interpreted as a machine-payment and endpoint-retrieval layer.

It should not be interpreted as a sitewide paywall.

Public discovery remains available through:

- `/llms.txt`
- `/llms-full.txt`
- AI Catalog
- AI Root
- MCP discovery
- MCP health metadata
- Naturepedia™ public pages
- governance pages
- licensing pages
- public v2 control-plane resources

### Retrieval Rights Boundary

An x402 payment grants one endpoint-level retrieval of the identified protected resource only.

It does not automatically grant:

- model training rights
- embedding rights
- bulk-ingestion rights
- redistribution rights
- resale rights
- synchronization rights
- private-dataset construction rights
- derivative-dataset rights
- commercial implementation rights
- Robbie's Razor™ framework implementation rights
- private deployment rights
- sovereign deployment rights
- ownership rights

Commercial data reuse requires a separate written agreement.

Framework implementation and strategic-infrastructure rights require a separate enterprise agreement.

MCP discovery, MCP tool invocation, x402 payment, successful settlement, and successful retrieval do not by themselves establish empirical validation, scientific confirmation, or transfer of authorship.

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
