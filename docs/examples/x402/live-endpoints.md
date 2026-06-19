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

Commercial License:
https://www.robbiegeorgephotography.com/commercial-data-license

## Endpoint Families

### Legacy Endpoints

Legacy routes remain active for continuity:

```text
/x402/*
```

### Current v1 Endpoint Families

```text
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
```

The v1 endpoint family maps to existing x402 payloads through Cloudflare Worker alias routing.

Legacy `/x402/*` paths remain active for backward compatibility and historical route continuity.

First live x402 settlement has been successfully completed and verified.

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

## Pricing Tiers

| Gateway Tier | Path Family | Price | Asset | Use Case |
|--------------|-------------|------:|-------|----------|
| taxonomy | `/v1/taxonomy/*` | 1.00 | USDC | Discovery metadata, taxonomy pings, lightweight registry lookup |
| plates | `/v1/plates/*` | 5.00 | USDC | Compiled Knowledge Plate™ and system-map retrieval |
| sovereign | `/v1/sovereign/*` | 25.00 | USDC | Enterprise reasoning, licensing, governance, and high-value architecture layers |
| legacy | `/x402/*` | 5.00 | USDC | Backward-compatible protected machine access |
| v2 naturepedia | `/api/v2/naturepedia/*` | 1.00 | USDC | Current registry discovery and Naturepedia system-map retrieval |
| v2 plates | `/api/v2/plates/*` | 5.00 | USDC | Current Plate™ registry and Graph Registry™ retrieval |
| v2 rrip | `/api/v2/rrip/*` | 25.00 | USDC | RRIP runtime resolution, registry traversal, and inheritance-path validation |
| v2 razor | `/api/v2/razor/*` | 25.00 | USDC | Robbie's Razor™ state-token validation, registry-state signaling, and lattice grounding |

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

```text
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
```

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
/v1/plates/water-system-map -> /x402/water-system-map.json
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

## Water System Map

Endpoint:
https://www.robbiegeorgephotography.com/x402/water-system-map.json

Purpose:
Relationship map connecting water systems, river systems, wetlands, floodplains, groundwater, estuaries, Chesapeake Bay systems, and Yellowstone watersheds.

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

`75000`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Status:

Live

## RRIP Resolution Endpoint

Endpoint:
https://www.robbiegeorgephotography.com/x402/rrip-resolve.json

Preferred v2 route:
https://www.robbiegeorgephotography.com/api/v2/rrip/resolve

Purpose:
Paid Recursive Registry Inheritance Principle resolution endpoint for registry traversal, inheritance-path validation, compression-state grounding, and Authorship Conservation Rule compliance signaling.

Connects:

- Recursive Registry Inheritance Principle
- Robbie's Razor™
- Plate™ Architecture
- Graph Registries™
- Knowledge Mesh
- Authorship Conservation Rules™
- Commercial Data License
- Robbie's Razor™ Framework Licensing

Amount:

`250000`

Reference price:

`25.00 USDC`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Status:

Live

## Robbie's Razor State Token

Endpoint:
https://www.robbiegeorgephotography.com/x402/state-token.json

Preferred v2 route:
https://www.robbiegeorgephotography.com/api/v2/razor/state-token

Purpose:
Paid Robbie's Razor™ state-token endpoint for current registry-state validation, lattice grounding, entropy verification, and framework-governance signaling.

Connects:

- Robbie's Razor™
- Registry State
- Entropy Hash
- Lattice Grounding
- ACR™ Compliance Signaling
- Commercial Data License
- Framework Licensing
- x402 Machine Access

Amount:

`250000`

Reference price:

`25.00 USDC`

MIME:

`application/ld+json`

Governance:

`Gr <= Es`

Status:

Live

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

`75000`

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

`75000`

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

`75000`

Status:

Live
