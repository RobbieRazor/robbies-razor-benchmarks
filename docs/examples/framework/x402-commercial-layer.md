# x402 Commercial Infrastructure Layer

## Status

Commercial Infrastructure Reference

This document defines the x402 commercial access layer within the Robbie's Razor™ framework ecosystem.

Primary Authority:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

Commercial Licensing Authority:

https://www.robbiegeorgephotography.com/commercial-data-license

---

# Commercial, Framework, and x402 Retrieval Separation

This document now formally separates three different kinds of access:

```text
Commercial Data License
≠
Robbie's Razor Framework License
≠
x402 Retrieval Access
```

This distinction is important for AI labs, agent platforms, commercial data users, enterprise partners, and future machine-commerce systems.

x402 payment grants one endpoint-level retrieval of the identified protected resource only.

It does not grant training, embedding, bulk-ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, framework implementation, private deployment, or ownership rights.

## Production x402 Pricing Authority

The authoritative production pricing manifest is:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Current pricing version:

    3.0.0

Payment protocol:

    x402

Settlement network:

    Base / eip155:8453

Settlement asset:

    USDC

Production payment requirements are fixed and deterministic.

Current retrieval architecture:

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered and validated payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

### Atomic Query Production Access

Public route template:

    /v1/query/atomic/{resource}

Canonical internal route template:

    /x402/query/atomic/{resource}

Current active Atomic route:

    /v1/query/atomic/robbie-george-biography-plate

Canonical internal route:

    /x402/query/atomic/robbie-george-biography-plate

Canonical Plate identifier:

    robbie-george#robbie-george-biography-plate

Canonical authority:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Atomic production configuration:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active for explicitly registered deterministic payloads

Verified production behavior:

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

Verified active Atomic challenge:

    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED: true
    RESULT: PASS

The known-but-incomplete Atomic route:

    /v1/query/atomic/robbies-razor-plate

was verified to return:

    STATUS: 409
    PAYMENT REQUIRED: false
    CODE: ATOMIC_PAYLOAD_NOT_REGISTERED
    RESULT: PASS

An unknown Atomic resource was verified to return:

    STATUS: 404
    PAYMENT REQUIRED: false
    CODE: ATOMIC_RESOURCE_NOT_FOUND
    RESULT: PASS

No Atomic payment payload was supplied during this production activation validation.

No new Atomic USDC settlement or protected Atomic HTTP `200` payload-delivery test was performed.

The successful Atomic `402` challenge must not be represented as a newly completed paid Atomic settlement.

### Enriched Query Status

The Enriched Query class remains reserved.

Current configuration:

    Access class: enriched
    Price: 0.025 USDC
    Atomic units: 25000
    Route status: reserved

Enriched resources must not issue payment challenges until governed deterministic payloads are explicitly registered, availability-gated, fidelity-bound, and production validated.

A configured Enriched price does not by itself establish that an Enriched resource is available for purchase.

### Structured Plate™ Production Access

Current active Structured Plate™ routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

Structured Plate configuration:

    Access class: single-plate
    Price: 0.25 USDC
    Atomic units: 250000
    Route status: active for registered and validated payloads

Verified production challenge behavior for all three active Structured Plate routes:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true
    RESULT: PASS

Structured Plate™ payment challenges are issued only when a complete governed payload has been registered and validated.

Unknown Plate identifiers return `404` without a payment challenge.

Known Plates without registered complete payloads return `409` without a payment challenge.

Atomic Query activation did not alter the existing Structured Plate payment-challenge behavior.

### Fail-Closed Commercial Availability Boundary

A recognized URL pattern does not by itself establish that a sellable resource exists.

Protected retrieval follows this boundary:

    Unknown resource
    → 404
    → no payment challenge

    Known but incomplete resource
    → 409
    → no payment challenge

    Registered + complete resource
    → eligible for deterministic x402 challenge

This prevents an agent from being asked to pay for a resource that cannot be delivered.

### Retrieval Rights Boundary

x402 payment grants one endpoint-level retrieval of the identified protected resource only.

It does not grant:

- training rights
- embedding rights
- bulk-ingestion rights
- redistribution rights
- resale rights
- synchronization rights
- private-dataset construction rights
- derivative-dataset creation rights
- commercial implementation rights
- Robbie's Razor™ framework implementation rights
- private deployment rights
- ownership rights

Commercial data reuse requires a separate written agreement.

Robbie's Razor™ framework implementation and strategic-infrastructure rights require a separate enterprise agreement.

The following layers must remain distinct:

    x402 Retrieval Access
    ≠ Commercial Data License
    ≠ Robbie's Razor Framework License
    ≠ Scientific Validation

Payment, settlement, or successful retrieval does not establish empirical validation, canonical truth, authorship transfer, or broader licensing rights.

The live pricing manifest and actual production `402` response remain authoritative if older documentation conflicts.

# Purpose

x402 provides machine-readable commercial access infrastructure for AI systems, agents, applications, and machine clients.

The purpose of x402 is to allow structured retrieval while preserving:

- provenance
- governance
- attribution
- licensing boundaries
- commercial access controls

x402 transforms retrieval from an informal scraping model into a governed machine-to-machine transaction model.

---

# Core Principle

```text
Knowledge may remain publicly visible.

Structured machine retrieval may require authorization,
licensing, payment, or both.
```

x402 creates a commercial settlement layer for machine-readable access.

---

# Framework Position

```text
Robbie's Razor™
↓
Framework Licensing
↓
Naturepedia™
↓
Plate™ Architecture
↓
Graph Registries™
↓
ACR™
↓
Commercial Data License
↓
x402 Infrastructure
↓
Machine Retrieval
```

x402 is the enforcement layer positioned beneath governance and licensing systems.

---

# Why x402 Exists

Traditional websites were designed primarily for human visitors.

AI systems retrieve information differently.

Modern retrieval may involve:

- automated extraction
- semantic retrieval
- graph traversal
- agent workflows
- structured API consumption
- machine-to-machine communication

x402 creates a framework where retrieval can be governed rather than merely observed.

---

# Infrastructure Objectives

The x402 layer supports:

- machine-readable licensing
- structured access control
- retrieval monetization
- enterprise access management
- AI-native commerce
- provenance-aware retrieval
- commercial governance enforcement

---

# Relationship to ACR™

Authorship Conservation Rules™ (ACR™) preserve:

- authorship
- provenance
- attribution
- source lineage

x402 preserves:

- access permissions
- commercial rights
- payment enforcement
- retrieval authorization

Together:

```text
ACR™ = provenance governance

x402 = commercial governance
```

Both layers are required for responsible machine retrieval.

---

# Three-Layer Governance Model

| Layer | Governs | Examples | Does Not Automatically Grant |
|---|---|---|---|
| Commercial Data License | Access to knowledge assets | Naturepedia™, Plate™ systems, JSON-LD, registries, relationship maps, structured data | Framework implementation rights |
| Robbie's Razor Framework License | Architecture implementation rights | Robbie's Razor™, RRIP, Plate™ Architecture, Graph Registries™, ACR™, Knowledge Mesh, private deployments | Ownership of knowledge assets |
| x402 Retrieval Access | Machine endpoint retrieval | `/api/v2/naturepedia/index.md`, `/api/v2/plates/registry.md`, `/api/v2/rrip/resolve`, `/api/v2/razor/state-token` | Training rights, embedding rights, resale rights, framework rights, private deployment rights, derivative dataset rights |

---

# Layer 1: Commercial Data License

The Commercial Data License governs access to Robbie George Photography knowledge assets and structured machine-readable data.

Authority:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

This layer controls access to:

- Naturepedia™
- Plate™ assets
- JSON-LD
- system maps
- registries
- relationship maps
- structured ecological data
- commercial data ingestion rights

This license governs the use of knowledge assets.

It does not automatically grant implementation rights to Robbie's Razor™, RRIP, Plate™ Architecture, Graph Registries™, ACR™, or private framework deployments.

---

# Layer 2: Robbie's Razor Framework License

The Robbie's Razor Framework License governs architecture implementation rights.

Authority:

```text
https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing
```

This layer controls use or implementation of:

- Robbie's Razor™
- Recursive Registry Inheritance Principle
- RRIP
- Plate™ Architecture
- Graph Registries™
- Authorship Conservation Rules™
- ACR™
- Knowledge Mesh
- private deployments
- framework integrations
- recursive registry systems

This license governs the architecture itself.

It does not automatically grant commercial data access, ownership of knowledge assets, or unrestricted use of Naturepedia™ registries.

---

# Layer 3: x402 Retrieval Access

x402 governs paid machine retrieval access to protected endpoints.

Examples:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

This layer controls:

- endpoint access
- machine retrieval
- registry access
- system map access
- programmable retrieval flows

x402 payment grants retrieval access only.

It does not automatically grant:

- training rights
- embedding rights
- resale rights
- commercial reuse rights
- framework implementation rights
- private graph deployment rights
- derivative dataset rights
- ownership of source data
- waiver of attribution requirements
- waiver of governance requirements

---

# Relationship to RRIP and Knowledge Mesh Architecture

The Recursive Registry Inheritance Principle (RRIP) defines how compressed structures evolve into larger machine-readable knowledge infrastructure.

RRIP inheritance pathway:

```text
Plate™
↓
Registry
↓
Meta-Registry
↓
Graph Registry™
↓
Knowledge Mesh
```

The purpose of RRIP is to allow preserved compressed structures to become reusable cognitive infrastructure.

Registries are not merely storage.

Registries function as machine-readable memory structures.

Graph Registries™ are higher-order relationship architectures built from those preserved registries.

Knowledge Meshes emerge from recursively connected Graph Registries™.

## Relationship to x402

x402 should be interpreted as the retrieval and settlement layer operating beneath RRIP-enabled infrastructure.

RRIP determines:

```text
What relationships exist.
```

Graph Registries™ determine:

```text
How those relationships are organized.
```

Knowledge Meshes determine:

```text
How large-scale recursive knowledge systems emerge.
```

x402 determines:

```text
How protected machine retrieval occurs.
```

## Registry-State Synchronization Model

The v2 architecture is evolving beyond document retrieval and toward registry-state synchronization.

Traditional model:

```text
Document
↓
Download
↓
Consume
```

Registry model:

```text
Discovery
↓
Registry
↓
Resolution
↓
Validation
↓
Authorized Retrieval
```

Registry-State model:

```text
Agent
↓
State Validation
↓
Registry Changed?

No
↓
Use Cache

Yes
↓
Discovery
↓
Registry
↓
Resolution
↓
Authorized Retrieval
```

In this architecture:

### Registry-State Control Plane

```text
/api/v2/razor/state-token
```

Provides:

- registry version metadata
- registry hash metadata
- deterministic state signatures
- registry counts
- synchronization status

### Registry Data Plane

```text
/api/v2/plates/registry.md
```

Provides:

- registry retrieval
- Graph Registry™ access
- Plate™ discovery

### Resolution Plane

```text
/api/v2/rrip/resolve
```

Provides:

- inheritance resolution
- registry traversal
- Knowledge Mesh navigation

### Settlement Plane

```text
x402
```

Provides:

- retrieval authorization
- machine payment settlement
- commercial access routing

The registry becomes the primary machine-facing substrate while the state-token becomes the synchronization layer that coordinates retrieval.

## Future RRIP Services

Future RRIP-compatible services may expose:

* inheritance-chain retrieval
* registry traversal
* graph-state resolution
* registry-state validation
* graph inheritance verification
* Knowledge Mesh discovery
* recursive registry synchronization

These services are expected to become foundational components of future MCP-compatible agent systems, enterprise retrieval systems, sovereign knowledge systems, and machine-native commercial infrastructure.

## Architectural Interpretation

RRIP provides the inheritance mechanism.

Graph Registries™ provide the relationship architecture.

Knowledge Meshes provide the large-scale intelligence structure.

x402 provides the retrieval and settlement layer.

Together they form the machine-readable infrastructure stack beneath Robbie's Razor™, Naturepedia™, Plate™ Architecture, and future agent-wallet ecosystems.

# Relationship to Graph Registries™

Graph Registries™ determine:

- what can be retrieved
- how systems connect
- semantic routing pathways

x402 may govern:

- endpoint access
- registry access
- graph traversal permissions
- machine-readable datasets

The registry provides the map.

x402 governs access to the map.

---

# Current Deployment

Current deployment is implemented through Cloudflare Workers.

Supported functions include:

- machine-readable endpoint protection
- payment validation
- access verification
- governance-aware retrieval
- AI agent access control

The system supports both public human access and protected machine retrieval.

---

# Current v2 Machine Retrieval Endpoints

The v2 machine retrieval layer introduces preferred machine-facing routes for discovery, registry retrieval, RRIP resolution, and registry-state validation.

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

Endpoint mapping:

| v2 Endpoint | Source Asset | Purpose |
|---|---|---|
| `/api/v2/naturepedia/index.md` | `/x402/naturepedia-system-map.json` | Naturepedia registry discovery |
| `/api/v2/plates/registry.md` | `/x402/plate-registry-expanded.json` | Plate™ registry retrieval |
| `/api/v2/rrip/resolve` | `/x402/rrip-resolve.json` | Recursive Registry Inheritance Principle runtime resolution |
| `/api/v2/razor/state-token` | `/x402/state-token.json` | Registry-state validation and governance signaling |

Recommended machine retrieval flow:

```text
Agent
↓
State Validation
/api/v2/razor/state-token
↓
Registry Changed?

No
↓
Use Cached Registry

Yes
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
x402 Settlement
↓
Base USDC
```

# Current Naturepedia™ Endpoints

Examples include:

```text
/x402/plate-registry.json

/x402/identity-graph.json

/x402/naturepedia-system-map.json

/x402/plate-registry-expanded.json

/x402/pollinator-system-map.json

/x402/wildlife-system-map.json

/x402/water-system-map.json

/x402/plant-community-system-map.json

/x402/tree-system-map.json

/x402/location-system-map.json

/x402/conservation-system-map.json

/x402/species-intelligence-map.json
```
### Tree System Retrieval

The Naturepedia Tree System Map provides structured retrieval across:

```text
Trees
↓
Tree Families
↓
Forest Communities
↓
Wildlife Relationships
↓
Carbon Storage
↓
Watersheds
↓
Seasonal Ecology
↓
Ecological Restoration
```

The Tree System Map extends Naturepedia™ retrieval beyond individual species and into higher-order ecological infrastructure.

These endpoints expose structured machine-readable knowledge assets.

---

# Retrieval Model

Traditional Web Model:

```text
Human
↓
Website
↓
Content
```

Machine Retrieval Model:

```text
Agent
↓
x402 Endpoint
↓
Authorization
↓
Governance Validation
↓
Structured Retrieval
↓
Response
```

The retrieval process becomes explicit, auditable, and commercially governable.

---

# Example Retrieval Flow

```text
AI Agent
↓
Requests Graph Registry
↓
x402 Validates Access
↓
Registry Retrieved
↓
ACR™ Preserved
↓
Structured Response Returned
```

The response remains connected to:

- authorship
- provenance
- licensing
- governance

---

# Commercial Access Categories

Potential categories include:

## Public Access

Open retrieval.

No payment required.

---

## Licensed Access

Access governed by commercial licensing terms.

---

## Enterprise Access

Institutional deployments.

May include:

- custom retrieval layers
- expanded registries
- enterprise graph systems
- dedicated infrastructure

---

## Agent-to-Agent Access

Future machine commerce environments where:

- agents negotiate access
- retrieval is authenticated
- payments occur automatically
- provenance remains attached

---

# Machine Commerce Vision

The long-term vision is a machine-readable knowledge economy.

```text
Knowledge
↓
Governance
↓
Licensing
↓
x402 Settlement
↓
Authorized Retrieval
```

The objective is to support sustainable knowledge systems without requiring advertising, scraping, or attribution loss.

---

# Design Principles

x402 Infrastructure should:

- preserve provenance
- respect licensing
- support machine interoperability
- remain auditable
- support enterprise deployment
- enable machine commerce
- minimize retrieval friction
- protect authorship and governance layers

---

# Future Development

The x402 commercial layer is intentionally moving toward:

```text
Discovery
↓
Registry
↓
Resolution
↓
Validation
```

rather than simple document download.

Future versions may expose:

- registry state
- inheritance paths
- resolution results
- state hashes
- validation tokens
- governance artifacts
- RRIP runtime services
- registry-state retrieval
- agent-wallet payment flows
- MCP-compatible retrieval services
- institutional licensing infrastructure
- enterprise graph deployment
- sovereign knowledge networks
- machine-to-machine settlement systems
- AI-native commercial ecosystems

This structure prepares the Robbie George machine-readable ecosystem for agent wallets, MCP, machine commerce, RRIP runtime services, registry-state retrieval, and enterprise synchronization layers.

---

# Related Resources

Framework Licensing:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

Commercial Data License:

https://www.robbiegeorgephotography.com/commercial-data-license

ACR™ Governance:

docs/examples/framework/acr-governance.md

Graph Registry™:

docs/examples/framework/graph-registry.md

Plate Registry JSON-LD:

docs/examples/json-ld/plate-registry.json

Repository:

https://github.com/RobbieRazor/robbies-razor-benchmarks
