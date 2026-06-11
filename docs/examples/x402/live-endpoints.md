# Naturepedia x402 Live Endpoints

# x402 Live Endpoint Architecture

Status: Production 402 challenge verified  
Settlement status: Pending first live paid transaction  
Network: Base  
Network ID: eip155:8453  
Asset: USDC  
Governance Header: X-Robbie-Razor-Governance: Gr <= Es  

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

Legacy `/x402/*` paths should not be removed until at least one real x402 payment settlement has been completed and verified.

## Pricing Tiers

| Gateway Tier | Path Family | Price | Asset | Use Case |
|--------------|-------------|------:|-------|----------|
| taxonomy | `/v1/taxonomy/*` | 1.00 | USDC | Discovery metadata, taxonomy pings, lightweight registry lookup |
| plates | `/v1/plates/*` | 5.00 | USDC | Compiled Knowledge Plate™ and system-map retrieval |
| sovereign | `/v1/sovereign/*` | 25.00 | USDC | Enterprise reasoning, licensing, governance, and high-value architecture layers |
| legacy | `/x402/*` | 5.00 | USDC | Backward-compatible protected machine access |

## Verified Route

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

X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
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
