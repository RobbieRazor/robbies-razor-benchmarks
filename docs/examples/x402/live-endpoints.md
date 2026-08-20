# Naturepedia x402 Live Endpoints

# x402 Live Endpoint Architecture

Status: Production Infrastructure Live
Verified Settlement Status: Live
First Successful Settlement: Confirmed

Machine Flags:

x402-status: verified-live
x402-network: eip155:8453
x402-asset: USDC
x402 Challenge Status: Verified
Settlement Status: Verified Live Settlement
x402-status: verified-live
x402-network: eip155:8453
x402-asset: USDC
x402-production-status: active
x402-first-settlement: successful
Network: Base
Network ID: eip155:8453
Asset: USDC
Governance Header: X-Robbie-Razor-Governance: Gr <= Es

Deployment State:

- Cloudflare Worker Active
- v1 Machine Retrieval Active
- v2 Control Plane Active
- Discovery Plane Active
- Registry Plane Active
- RRIP Resolution Plane Active
- State Validation Plane Active
- Human Browser Bypass Active
- AI/API Challenge Active
- Expanded Plate Registry Updated
- Registered Individual Plate Retrieval Active
- $0.25 Single-Plate Challenge Verified
- Naturepedia Systems Expansion Active
- AI Catalog Discovery Active

Commercial License:
https://www.robbiegeorgephotography.com/commercial-data-license

## Endpoint Families

### Legacy Endpoints

Legacy routes remain active for continuity:

```text
/x402/*
```

### Current v1 Endpoint Families

The production v1 machine-retrieval namespace includes:

    /v1/query/atomic/*
    /v1/taxonomy/*
    /v1/plates/*
    /v1/registries/*
    /v1/knowledge-mesh/*
    /v1/sovereign/*

#### Atomic Query Family

Public route template:

    /v1/query/atomic/{resource}

Canonical internal route template:

    /x402/query/atomic/{resource}

Current active Atomic route:

    /v1/query/atomic/robbie-george-biography-plate

Canonical internal route:

    /x402/query/atomic/robbie-george-biography-plate

Current Atomic production state:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active for registered deterministic payloads

The Atomic route family uses explicit resource registration and does not treat the existence of the route pattern as proof that a payable resource exists.

Production behavior:

    Registered + complete Atomic resource
    → 402 Payment Required
    → amount 5000
    → tier atomic

    Known + incomplete Atomic resource
    → 409
    → no payment challenge

    Unknown Atomic resource
    → 404
    → no payment challenge

The current active route was production-validated on 2026-08-20.

No Atomic payment or post-settlement Atomic HTTP 200 payload-delivery test was performed during that activation validation.

#### Other v1 Retrieval Families

The remaining v1 route families provide compatibility and public aliases for protected Naturepedia resources including:

- taxonomy and identity resources
- Structured Plate™ resources
- bounded registries
- System Maps
- Knowledge Meshes
- higher-order protected resources

Applicable v1 routes normalize to their canonical internal resource paths through the Cloudflare Worker before pricing, availability validation, payment enforcement, and protected delivery.

Legacy `/x402/*` paths remain active for backward compatibility and historical route continuity.

The first historical live x402 settlement has been successfully completed and verified on an existing protected route.

That historical settlement must not be interpreted as a completed settlement for every current pricing class or every newly activated endpoint.

### Current v2 Endpoint Families

```text
/api/v2/naturepedia/*
/api/v2/plates/*
/api/v2/rrip/*
/api/v2/razor/*
```

#### Current v2 Infrastructure Status

```text
Status:

Live
Verified Settlement Route
x402-status: verified-live
Deployment: Cloudflare Worker
Architecture State: Active
Governance Headers: Enabled
Registry-State Synchronization: Enabled
Machine Retrieval Status: Live
Control Plane Status: Live
Knowledge Mesh Routing: Active
```

The following v2 infrastructure endpoints are now served directly by the Cloudflare Worker before x402 settlement routing:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

## Registry-State Infrastructure Layer

These endpoints collectively provide:

### Discovery Plane

```text
/api/v2/naturepedia/index.md
```

Purpose:

- Naturepedia™ discovery
- ecosystem traversal
- registry routing
- machine-access entry point

### Registry Data Plane

```text
/api/v2/plates/registry.md
```

Purpose:

- Plate™ registry retrieval
- Graph Registry™ access
- compressed knowledge routing
- registry navigation

### RRIP Resolution Plane

```text
/api/v2/rrip/resolve
```

Purpose:

- inheritance-path resolution
- registry traversal
- recursive registry grounding
- Knowledge Mesh navigation

### Registry-State Control Plane

```text
/api/v2/razor/state-token
```

Purpose:

- registry version tracking
- registry hash validation
- deterministic state signatures
- registry count metadata
- synchronization signaling
- cache validation
- machine-readable continuity

The state-token endpoint should be interpreted as the Registry-State Control Plane for the Robbie's Razor™ machine retrieval architecture.

## Canonical Retrieval Workflow

```text
Agent
↓
State Validation
/api/v2/razor/state-token
↓
Discovery
/api/v2/naturepedia/index.md
↓
Registry Retrieval
/api/v2/plates/registry.md
↓
RRIP Resolution
/api/v2/rrip/resolve
↓
Knowledge Mesh Traversal
↓
Conditional Retrieval
↓
x402 Settlement
↓
Authorized Response
```

x402 should be interpreted as the settlement architecture beneath protected machine-readable retrieval.

## Registry-State Synchronization Model

The Robbie's Razor™ v2 architecture now separates:

### Control Plane

```text
/api/v2/razor/state-token
```

Provides:

- registry version metadata
- registry hash metadata
- deterministic state signatures
- registry counts
- synchronization state

### Data Plane

```text
/api/v2/plates/registry.md
```

Provides:

- Plate™ registry retrieval
- Graph Registry™ traversal
- registry discovery

### Resolution Plane

```text
/api/v2/rrip/resolve
```

Provides:

- inheritance resolution
- registry traversal
- Knowledge Mesh routing

### Settlement Plane

```text
x402
```

Provides:

- machine payment settlement
- retrieval authorization
- commercial access routing

Future agent workflows may compare registry state before retrieval occurs, allowing cache-aware synchronization and reducing unnecessary machine retrieval requests.

## Production Retrieval Pricing

Authoritative pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Production `402` responses use deterministic Base USDC prices. Pricing is assigned by the delivered resource class—not solely by its URL family.

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | 0 | Active |
| Atomic canonical query | $0.005 USDC | 5000 | Active for registered payloads |
| Enriched relationship query | $0.025 USDC | 25000 | Reserved |
| Structured Plate™ payload | $0.25 USDC | 250000 | Active for registered payloads |
| Bounded subtree, registry, or System Map | $5.00 USDC | 5000000 | Active |
| Full registry or Knowledge Mesh snapshot | $25.00 USDC | 25000000 | Active |

### Active Atomic Query Route

Current active Atomic route:

    /v1/query/atomic/robbie-george-biography-plate

Reference price:

    0.005 USDC

Atomic units:

    5000

Access class:

    atomic

Verified production behavior:

- Registered and complete Atomic resource → `402 Payment Required`
- Amount → `5000` USDC atomic units
- Access class → `atomic`
- Reference price → `0.005 USDC`
- `PAYMENT-REQUIRED` challenge header → present
- Known but incomplete Atomic resource → `409` with no payment challenge
- Unknown Atomic resource → `404` with no payment challenge

The active Atomic route resolves the registered Robbie George Biography Plate™ identifier to its canonical authority at:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Payment grants one endpoint-level retrieval of the registered Atomic Query result only. It does not grant training, embedding, bulk ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, or framework implementation rights.

### Enriched Query Status

The Enriched Query class remains reserved.

    Price: 0.025 USDC
    Atomic units: 25000
    Access class: enriched
    Route status: reserved

Enriched Query routes must not issue payment challenges until their governed deterministic payloads are explicitly registered and available.

### Active Structured Plate Routes

Current active single-Plate routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

All three registered Plates return deterministic `402 Payment Required` responses for `250000` USDC atomic units on Base and are classified as `single-plate`.

Verified Structured Plate challenge behavior:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true

These tests verified payment challenges only; no new `$0.25` settlement or protected payload-delivery test was performed during this validation round.

Unknown Plate identifiers return `404` without a payment challenge.

Known Plates without registered complete payloads return `409` without a payment challenge.

### Current Retrieval Safety Model

Naturepedia x402 retrieval follows a fail-closed availability model:

    Registered + complete resource
    ↓
    Correct resource class
    ↓
    Correct deterministic pricing tier
    ↓
    402 Payment Required
    ↓
    Verification
    ↓
    Settlement
    ↓
    Fidelity validation
    ↓
    Authorized payload delivery

Unavailable resources are rejected before payment:

    Known but incomplete
    → 409
    → no payment challenge

    Unknown
    → 404
    → no payment challenge

The Atomic Query production validation confirmed:

    Available Atomic
    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED: true

    Known incomplete Atomic
    STATUS: 409
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED: false

    Unknown Atomic
    STATUS: 404
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED: false

Exact public discovery and control-plane endpoints may remain free even when related protected payload routes require payment.

The current production `402` response and the machine-readable pricing manifest are authoritative if older documentation conflicts.

## Verified Route

Verified Settlement Result:

Status: Success
Network: Base
Asset: USDC

Transaction:
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376

x402-status: verified-live

```text
/v1/plates/tree-system-map
```

Verified behavior:

Browser / human request:
200 OK human bypass page

API-style request:
Accept: application/json

402 Payment Required

Successful paid retrieval:
200 OK

Verified settlement:
success: true

Governance:
Gr <= Es

Settlement network:
Base

Settlement asset:
USDC

## Extended v2 Route Alias Map

The four static core v2 endpoints are served directly by the Worker. Additional v2 routes may continue to alias legacy `/x402/*.json` payloads for protected retrieval and backward compatibility.

```text
/api/v2/naturepedia/index.md -> /x402/naturepedia-system-map.json
/api/v2/naturepedia/tree-system-map.md -> /x402/tree-system-map.json
/api/v2/naturepedia/species-intelligence-map.md -> /x402/species-intelligence-map.json

/api/v2/plates/registry.md -> /x402/plate-registry-expanded.json
/api/v2/plates/tree-system-map.md -> /x402/tree-system-map.json
/api/v2/plates/pollinator-system-map.md -> /x402/pollinator-system-map.json

/api/v2/rrip/resolve -> /x402/rrip-resolve.json
/api/v2/razor/state-token -> /x402/state-token.json
```

## Active v1 Route Aliases

```text
/v1/taxonomy/plate-registry -> /x402/plate-registry.json
/v1/taxonomy/identity-graph -> /x402/identity-graph.json
/v1/taxonomy/naturepedia-system-map -> /x402/naturepedia-system-map.json

/v1/plates/plate-registry-expanded -> /x402/plate-registry-expanded.json
/v1/plates/pollinator-system-map -> /x402/pollinator-system-map.json
/v1/plates/wildlife-system-map -> /x402/wildlife-system-map.json
/v1/registries/water-systems -> /x402/water-systems-registry.json
/v1/plates/water-system-map -> /x402/water-system-map.json
/v1/knowledge-mesh/water-systems -> /x402/knowledge-mesh/water-systems
/v1/plates/plant-community-system-map -> /x402/plant-community-system-map.json
/v1/plates/location-system-map -> /x402/location-system-map.json
/v1/plates/conservation-system-map -> /x402/conservation-system-map.json
/v1/plates/species-intelligence-map -> /x402/species-intelligence-map.json
/v1/plates/tree-system-map -> /x402/tree-system-map.json
```

## Legacy x402 Endpoint Inventory

## Plate Registry

Endpoint:
https://www.robbiegeorgephotography.com/x402/plate-registry.json

Purpose:
Compressed semantic registry retrieval.

## Identity Graph

Endpoint:
https://www.robbiegeorgephotography.com/x402/identity-graph.json

Purpose:
Identity, authorship, provenance, governance retrieval.

## Naturepedia System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/naturepedia-system-map.json

Purpose:
Species → Ecosystem → Location → Season relationship retrieval.

## Expanded Plate Registry

Endpoint:
https://www.robbiegeorgephotography.com/x402/plate-registry-expanded.json

Purpose:
Species → Tree Families → Plant Communities → Ecosystems → Geography / Locations → Time / Migration / Seasons → Conservation relationship retrieval.

June 2026 Registry Expansion:

- plateCount: 163
- lastExpansion: Soil, Carbon, Feedbacks, Bioelectric, Quantum Agriculture, and Plant Intelligence Expansion June 2026

New systems included:

- Soil Systems™ — https://www.robbiegeorgephotography.com/soil-systems
- Carbon Cycle™ — https://www.robbiegeorgephotography.com/carbon-cycle
- Ecosystem Feedbacks™ — https://www.robbiegeorgephotography.com/ecosystem-feedbacks
- Bioelectric Systems™ — https://www.robbiegeorgephotography.com/bioelectric-systems
- Quantum Agriculture™ — https://www.robbiegeorgephotography.com/naturepedia-quantum-agriculture
- Plant Intelligence™ — https://www.robbiegeorgephotography.com/naturepedia-plant-intelligence

New Plate™ entries added:

- Soil Systems Plates: 11
- Carbon Cycle Plates: 10
- Ecosystem Feedbacks Plates: 10
- Bioelectric Systems Plates: 10
- Quantum Agriculture Plates: 12
- Plant Intelligence Plates: 10

Total new Plates™ added:

63

Status:

Live

## Pollinator System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/pollinator-system-map.json

Purpose:
Relationship map connecting floral resources, pollinators, plant communities, soil microbiomes, mycelial networks, and seasonal timing.

## Wildlife System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/wildlife-system-map.json

Purpose:
Relationship map connecting wildlife species, tracks, behavior, habitats, ecosystems, field locations, seasonal timing, and conservation systems.

## Water Systems™ Retrieval Family

Status:

Live

Network:

Base — `eip155:8453`

Asset:

USDC

Governance:

`Gr <= Es`

### Water Systems Registry

Endpoint:

https://www.robbiegeorgephotography.com/x402/water-systems-registry.json

v1 alias:

https://www.robbiegeorgephotography.com/v1/registries/water-systems

Purpose:

Entity-resolved Water Systems™ registry connecting wetlands, river systems, floodplains, groundwater systems, estuaries, coastal systems, watersheds, surface water, subsurface water, hydrological storage, and ecological flow.

Amount:

`5000000`

Reference price:

`5.00 USDC`

### Water System Map

Endpoint:

https://www.robbiegeorgephotography.com/x402/water-system-map.json

v1 alias:

https://www.robbiegeorgephotography.com/v1/plates/water-system-map

Purpose:

Hydrological interaction map connecting precipitation, runoff, infiltration, groundwater recharge, river discharge, wetlands, floodplain inundation, estuarine exchange, coastal systems, watershed behavior, and wildlife habitat.

Amount:

`5000000`

Reference price:

`5.00 USDC`

### Water Systems Knowledge Mesh

Endpoint:

https://www.robbiegeorgephotography.com/x402/knowledge-mesh/water-systems

v1 alias:

https://www.robbiegeorgephotography.com/v1/knowledge-mesh/water-systems

Purpose:

Premium Water Systems™ Knowledge Mesh binding Weather™ precipitation, storm, temperature, snowpack, and evaporation constraints to rivers, wetlands, floodplains, groundwater systems, estuaries, coastal systems, seasonal ecology, and surface-subsurface water behavior.

Amount:

`25000000`

Reference price:

`25.00 USDC`

Hydrological retrieval pathway:

    Weather Registry
    ↓
    Weather System Map
    ↓
    Water Systems Registry
    ↓
    Water System Map
    ↓
    Water Systems Knowledge Mesh
    ↓
    Conditional x402 Retrieval

Verified browser behavior:

`200 OK` human-bypass gateway

Expected API behavior without settlement:

`402 Payment Required`

## Plant Community System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/plant-community-system-map.json

Purpose:
Relationship map connecting plant communities, pollinators, soil microbiomes, mycelial networks, native habitat, ecological succession, and carbon storage.

## Tree System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/tree-system-map.json

Purpose:
Paid compressed relationship map connecting trees, tree families, forest communities, mycelial networks, wildlife relationships, carbon storage, watersheds, and seasonal ecology.

Connects:

- Trees of North America
- Birches of North America
- Oaks of North America
- Maples of North America
- Aspens of North America
- Pines of North America
- Plant Communities
- Mycelial Networks
- Soil Microbiome
- Ecological Restoration & Habitat Recovery

Amount:

`5000000`

Reference price:

`5.00 USDC`

Pricing class:

`subtree`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Status:

Live

## RRIP Resolution Endpoint

Free control-plane endpoint:

https://www.robbiegeorgephotography.com/api/v2/rrip/resolve

Protected snapshot endpoint:

https://www.robbiegeorgephotography.com/x402/rrip-resolve.json

Purpose:

Recursive Registry Inheritance Principle resolution for registry traversal, inheritance-path validation, compression-state grounding, and Authorship Conservation Rule compliance signaling.

The exact `/api/v2/rrip/resolve` control-plane route remains available for free discovery and resolution signaling.

The protected `/x402/rrip-resolve.json` payload is classified as a full snapshot resource.

Protected snapshot amount:

`25000000`

Reference price:

`25.00 USDC`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Protected route status:

Active

An x402 payment grants one retrieval of the protected payload only. It does not grant framework implementation, training, embedding, synchronization, redistribution, or derivative-dataset rights.

## Robbie's Razor State Token

Free control-plane endpoint:

https://www.robbiegeorgephotography.com/api/v2/razor/state-token

Protected snapshot endpoint:

https://www.robbiegeorgephotography.com/x402/state-token.json

Purpose:

Registry-state validation, deterministic state signaling, entropy-hash verification, lattice grounding, cache validation, and governance continuity.

The exact `/api/v2/razor/state-token` control-plane route remains available for free discovery and state validation.

The protected `/x402/state-token.json` payload is classified as a full snapshot resource.

Protected snapshot amount:

`25000000`

Reference price:

`25.00 USDC`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Protected route status:

Active

An x402 payment grants one retrieval of the protected payload only. It does not grant framework implementation, synchronization, training, embedding, redistribution, or derivative-dataset rights.

## Location System Map

Endpoint:

`/x402/location-system-map.json`

Purpose:

Paid compressed relationship map connecting major Naturepedia field locations, wildlife systems, habitats, seasonal timing, water systems, and applied observation guides.

Connects:

- Field Locations
- Yellowstone Wildlife Guide
- Grand Teton Wildlife Guide
- Blackwater Wildlife Guide
- Chesapeake Bay Wildlife System
- Lake Mattamuskeet Wildlife System
- Machias Seal Island
- Water Systems
- Seasonal Wildlife Calendar
- Wildlife Species

Amount:

`5000000`

Reference price:

`5.00 USDC`

Pricing class:

`subtree`

Status:

Live

## Conservation System Map

Endpoint:

`/x402/conservation-system-map.json`

Purpose:

Paid compressed relationship map connecting conservation, habitat protection, biodiversity, water systems, pollinators, plant communities, wildlife movement, and restoration systems.

Connects:

- Wildlife Conservation & Habitat
- Wildlife Species
- Ecosystems of North America
- Water Systems
- Plant Communities
- Floral Resource Networks
- Seasonal Wildlife Calendar
- Field Locations
- Wildlife Migration & Seasonal Patterns

Amount:

`5000000`

Reference price:

`5.00 USDC`

Pricing class:

`subtree`

Status:

Live

## Species Intelligence Map

Endpoint:

`/x402/species-intelligence-map.json`

Purpose:

Paid compressed relationship map connecting wildlife species, Species Plates, tracks, behavior, habitat, field locations, seasonal timing, and conservation context.

Connects:

- Wildlife Species
- Species Plates
- North American Animal Tracks
- Wildlife Behavior & Ecology
- Wildlife Conservation & Habitat
- Field Locations
- Seasonal Wildlife Calendar
- Ecosystems of North America
- Wildlife Migration & Seasonal Patterns

Amount:

`5000000`

Reference price:

`5.00 USDC`

Pricing class:

`subtree`

Status:

Live
