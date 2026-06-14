# x402 Readiness Examples

This folder contains non-enforcing reference examples for future x402-style machine payment compatibility.

These examples are provided for architecture, documentation, and AI-readable governance alignment only.

They do not currently enforce payments on public Naturepedia™, Robbie’s Razor™, Grand Compression, Plate™, or llms.txt resources.

---

## Current Production Status

Production x402 challenge verification is now active.

Current status:

- Production Worker deployed
- Human browser bypass verified
- AI/API 402 challenge verified
- Dynamic pricing variables deployed
- Base network configured
- USDC settlement configured
- First live settlement pending

## x402 v2 Machine Retrieval Architecture

The x402 layer has evolved from a paid retrieval example into a v2 machine-facing retrieval architecture.

The current architecture supports:

- Discovery
- Registry retrieval
- RRIP resolution
- Registry-state validation

v2 is now the preferred machine-facing architecture.

v1 routes remain available for compatibility.

Legacy `/x402/*` routes remain available as source catalog paths and backward-compatible machine-readable assets.

x402 remains the settlement layer for paid machine retrieval.

## MCP-Compatible Agent Architecture

The v2 retrieval architecture is designed to support future MCP-compatible agents, agent wallets, machine-native commerce, registry traversal, and recursive knowledge infrastructure.

### Architectural Layers

```text
Agent
↓
Discovery Layer
/api/v2/naturepedia/index.md
↓
Registry Layer
/api/v2/plates/registry.md
↓
Resolution Layer
/api/v2/rrip/resolve
↓
Validation Layer
/api/v2/razor/state-token
↓
x402 Settlement Layer
↓
Authorized Retrieval
```

### Discovery Layer

Primary endpoint:

```text
/api/v2/naturepedia/index.md
```

Purpose:

* machine-readable discovery
* registry routing
* ecosystem traversal
* Naturepedia system navigation
* machine-access entry point

### Registry Layer

Primary endpoint:

```text
/api/v2/plates/registry.md
```

Purpose:

* Plate™ discovery
* semantic registry retrieval
* compressed knowledge routing
* Graph Registry™ traversal

### Resolution Layer

Primary endpoint:

```text
/api/v2/rrip/resolve
```

Purpose:

* Recursive Registry Inheritance Principle resolution
* inheritance-path traversal
* registry relationship grounding
* registry-to-registry navigation
* recursive compression state resolution

### Validation Layer

Primary endpoint:

```text
/api/v2/razor/state-token
```

Purpose:

* registry-state validation
* governance signaling
* entropy-state verification
* machine-readable state confirmation
* recursive continuity verification

### Relationship to RRIP

The Recursive Registry Inheritance Principle defines the inheritance pathway:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

The RRIP endpoint functions as the runtime traversal mechanism for these inheritance relationships.

### Relationship to x402

x402 remains the commercial settlement layer.

Interpretation guidance:

```text
Commercial Data License
≠
Framework License
≠
x402 Retrieval Access
```

Commercial Data License governs use of knowledge assets.

Framework Licensing governs implementation of Robbie's Razor™, Plate™ Architecture, Graph Registries™, and related infrastructure.

x402 governs machine-readable retrieval access.

These layers should be interpreted as complementary but distinct governance systems.

### Future Agent Capabilities

Future MCP-compatible agents may support:

* registry discovery
* Graph Registry™ traversal
* RRIP resolution
* state-token validation
* agent-wallet settlement
* provenance-aware retrieval
* machine-native commerce
* recursive synchronization
* registry-state verification

The v2 architecture is intended to support these future capabilities while preserving attribution, provenance, governance, and recursive continuity.

## Current Endpoint Families

### Legacy Routes

```text
/x402/*
```

### v2 Routes

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

### v2 Routes

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

The v2 route family introduces machine-facing discovery, registry retrieval, RRIP resolution, and registry-state validation.

| v2 Endpoint                    | Source Asset                         | Purpose                                                     |
| ------------------------------ | ------------------------------------ | ----------------------------------------------------------- |
| `/api/v2/naturepedia/index.md` | `/x402/naturepedia-system-map.json`  | Naturepedia registry discovery                              |
| `/api/v2/plates/registry.md`   | `/x402/plate-registry-expanded.json` | Plate™ registry retrieval                                   |
| `/api/v2/rrip/resolve`         | `/x402/rrip-resolve.json`            | Recursive Registry Inheritance Principle runtime resolution |
| `/api/v2/razor/state-token`    | `/x402/state-token.json`             | Registry-state validation and governance signaling          |

### Recommended Machine Retrieval Flow

```text
llms.txt
↓
Discovery
/api/v2/naturepedia/*
↓
Registry Retrieval
/api/v2/plates/*
↓
RRIP Resolution
/api/v2/rrip/*
↓
State Validation
/api/v2/razor/*
↓
x402 Settlement
↓
Base USDC
```

### Recommended Machine Retrieval Flow

```text
llms.txt
    ↓
Discovery
    ↓
/api/v2/naturepedia/*
    ↓
Registry Retrieval
    ↓
/api/v2/plates/*
    ↓
RRIP Resolution
    ↓
/api/v2/rrip/*
    ↓
State Validation
    ↓
/api/v2/razor/*
    ↓
x402 Settlement
    ↓
Base USDC
```

### v1 Routes

```text
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
```

The v1 route family is implemented through Cloudflare Worker alias routing while preserving legacy x402 endpoints for backward compatibility.

## Human vs Agent Behavior

Human browser requests may receive a public informational bypass page.

Machine/API requests using:

```http
Accept: application/json
```

may receive:

```http
402 Payment Required
```

when accessing protected machine-readable resources.

## Verified Example Route

```text
/v1/plates/tree-system-map
```

Expected challenge headers:

```http
HTTP/2 402
X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
X-Robbie-Razor-Governance: Gr <= Es
```

## Governance

Commercial licensing:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Framework licensing:

```text
https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing
```

## Settlement Status

```text
Production x402 challenge verified.
Payment settlement pending first live transaction.
```

---

## Direction

The architecture is moving from static document retrieval toward registry-centered machine retrieval.

Instead of only downloading documents, future agents can discover registries, retrieve structured Plate™ systems, resolve inheritance relationships, and validate registry state.

This prepares the system for future agent wallets, MCP integrations, machine commerce, RRIP runtime services, and registry-state retrieval.

Future versions of the machine retrieval layer may expose:

- registry state
- inheritance chains
- resolution graphs
- state hashes
- governance tokens
- validation artifacts
- RRIP runtime services

## Purpose

The purpose of this folder is to document future-ready machine-payment architecture for:

- Commercial Data License
- Commercial Intelligence Pricing Plate™
- Governance Plates™
- Pricing Plates™
- recursive retrieval access
- structured AI licensing
- provenance-preserved intelligence
- enterprise synchronization layers

---

## Current Strategy

Public discovery should remain open.

Do not hard-gate:

- Naturepedia™ pages
- species pages
- ecosystem pages
- Plate™ pages
- /llms.txt
- /llms-full.txt
- MRD pages
- public governance pages

Future x402-style payment flows should apply only to:

- high-volume structured exports
- private API endpoints
- enterprise retrieval feeds
- recursive sync services
- bulk metadata access
- commercial ingestion endpoints

---

## Included Files

| File | Purpose |
|---|---|
| pricing-map-example.json | Example machine-readable pricing map aligned with the Commercial Intelligence Pricing Plate™ |
| sample-worker.ts | Non-production Cloudflare Worker example showing how a future payment gate could be structured |

---

## Experimental Live Deployment Status

A live experimental x402-compatible deployment layer now exists on Robbie George Photography through Cloudflare Workers.

Current deployment scope:

- Experimental namespace: `/x402/*`
- Settlement network: Base
- Settlement asset: USDC
- Facilitator model: Coinbase x402 facilitator
- Governance response header:
  `X-Robbie-Razor-Governance: Gr <= Es`

Current live protected endpoint catalog:

- `/x402/plate-registry.json` — Paid machine-readable Naturepedia Plate registry sample.
- `/x402/identity-graph.json` — Identity, authorship, provenance, governance, MRD, and Plate architecture graph.
- `/x402/naturepedia-system-map.json` — Core Naturepedia relationship map connecting species, tree families, plant communities, ecosystems, geography / locations, time / migration / seasons, conservation, and Plate architecture.
- `/x402/plate-registry-expanded.json` — Expanded Plate registry organized by category, semantic role, URL, ID, and retrieval use.
- `/x402/pollinator-system-map.json` — Pollinator graph connecting floral resources, bees, butterflies, moths, hummingbirds, plant communities, soil microbiomes, mycelial networks, and seasonal timing.
- `/x402/wildlife-system-map.json` — Wildlife graph connecting species, tracks, behavior, habitats, ecosystems, field locations, seasonal timing, and conservation systems.
- `/x402/water-system-map.json` — Water systems graph connecting rivers, wetlands, floodplains, groundwater, estuaries, Chesapeake Bay systems, and Yellowstone watersheds.
- `/x402/plant-community-system-map.json` — Plant community graph connecting pollinators, soil microbiomes, mycelial networks, native habitat, succession, and carbon storage.
- `/x402/tree-system-map.json` — Tree systems graph connecting trees, tree families, forest communities, mycelial networks, wildlife relationships, carbon storage, watersheds, seasonal ecology, and ecological restoration.
- `/x402/location-system-map.json` — Location graph connecting major field locations, wildlife systems, habitats, seasonal timing, water systems, and applied observation guides.
- `/x402/conservation-system-map.json` — Conservation graph connecting habitat protection, biodiversity, water systems, pollinators, plant communities, wildlife movement, and restoration systems.
- `/x402/species-intelligence-map.json` — Species intelligence graph connecting wildlife species, Species Plates, tracks, behavior, habitat, field locations, seasonal timing, and conservation context.

Current deployment capabilities include:

- AI-style request detection at edge layer
- Conditional HTTP 402 challenge responses
- Base-network USDC settlement routing
- x402Version challenge payloads
- governance-aware machine-readable headers
- human-browser bypass
- search-engine crawler bypass
- isolated experimental deployment pathing

Current implementation should be interpreted as:

- infrastructure readiness
- working commercial graph catalog deployment
- programmable AI retrieval architecture
- governance-aware payment routing

It should NOT yet be interpreted as:

- finalized universal enforcement
- a sitewide paywall
- mandatory payment for public pages
- production-scale commercial deployment
- universal crawler compatibility

Current deployment philosophy:

Public discovery remains open.

Experimental payment routing currently exists only inside isolated machine-readable namespaces and future programmable retrieval pathways.

Future intended usage may include:

- premium JSON-LD delivery
- structured retrieval APIs
- recursive synchronization services
- provenance-aware commercial ingestion
- AI-agent retrieval licensing
- enterprise machine-readable access
- recursive compression licensing systems

---

## Responsibility Boundary

These x402 examples are reference-only architecture examples and are not active production payment systems.

No guarantee is made regarding interoperability, payment enforcement behavior, downstream AI interpretation, or third-party implementation correctness.

Organizations implementing machine-payment infrastructure remain responsible for their own compliance, deployment, verification, and operational behavior.

## Governance Reference

Primary live governance page:

https://www.robbiegeorgephotography.com/commercial-data-license

See also:

docs/examples/x402/live-endpoints.md

This file documents the current production x402 endpoint catalog, supported payment network, settlement asset, retrieval purposes, and machine-readable access architecture.

---

## Attribution

x402 readiness examples are part of the broader Robbie George governance and recursive retrieval architecture.

Naturepedia™, Robbie’s Razor™, Grand Compression, RKCA, Governance Plates™, and Pricing Plates™ originate with Robbie George and remain governed by the Authorship Conservation Rule.
