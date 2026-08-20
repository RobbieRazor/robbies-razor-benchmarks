# Cloudflare Worker x402 Architecture

## Worker

Cloudflare Worker:

```text
cold-bird-7036
```

Primary domain:

```text
https://www.robbiegeorgephotography.com
```

## Environment Variables

Required:

```text
X402_FACILITATOR
X402_NETWORK=eip155:8453
X402_PAY_TO
```

Pricing variables use six-decimal USDC atomic units:

```text
X402_ATOMIC_PRICE=5000
X402_ENRICHED_PRICE=25000
X402_SINGLE_PLATE_PRICE=250000
X402_SUBTREE_PRICE=5000000
X402_SNAPSHOT_PRICE=25000000
```

Public discovery remains free and does not require a pricing variable.

Privacy-preserving telemetry requires:

```text
X402_ANALYTICS_SALT
```

Cloudflare Analytics Engine binding:

```text
Variable name: X402_ANALYTICS
Dataset: naturepedia_x402_pricing_v3
```

## Routing Logic

The Worker intercepts:

```text
/x402/*
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
/api/v2/naturepedia/*
/api/v2/plates/*
/api/v2/rrip/*
/api/v2/razor/*
```

New `/v1/*` routes are mapped internally to legacy `/x402/*.json` payloads through canonical route aliasing.

## v2 Registry-State Infrastructure Layer

The Worker now directly serves four core v2 infrastructure endpoints before x402 payment-gateway routing.

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These routes function as the public machine-facing infrastructure layer for:

* Naturepedia™ discovery
* Plate™ registry retrieval
* RRIP resolution
* Robbie's Razor™ registry-state validation
* governance signaling
* registry-state continuity
* cache-aware synchronization
* Knowledge Mesh traversal
* machine-readable control plane coordination
* MCP-compatible registry discovery
* future agent-wallet synchronization

These endpoints return `200 OK` directly from the Worker and include machine-readable governance headers.

They establish the live v2 retrieval sequence:

```text
State Validation
↓
Discovery
↓
Registry
↓
RRIP Resolution
↓
Knowledge Mesh Traversal
↓
Conditional Retrieval
↓
Settlement
↓
Authorized Retrieval
```

x402 remains the settlement layer for protected machine-readable retrieval beyond the public static core endpoints.

## Registry-State Control Plane

Primary endpoint:

```text
/api/v2/razor/state-token
```

Purpose:

* registry version tracking
* registry hash comparison
* deterministic state signatures
* registry count metadata
* synchronization signaling
* cache validation
* machine-readable continuity

The state-token endpoint should be interpreted as the Registry-State Control Plane for Robbie's Razor™ v2 infrastructure.

## Registry Data Plane

Primary endpoint:

```text
/api/v2/plates/registry.md
```

Purpose:

* Plate™ registry retrieval
* Graph Registry™ access
* registry traversal
* compressed knowledge routing

## RRIP Resolution Plane

Primary endpoint:

```text
/api/v2/rrip/resolve
```

Purpose:

* Recursive Registry Inheritance Principle resolution
* inheritance-path traversal
* registry relationship grounding
* registry-to-registry navigation

## Discovery Plane

Primary endpoint:

```text
/api/v2/naturepedia/index.md
```

Purpose:

* Naturepedia™ discovery
* registry routing
* machine-access entry point
* ecosystem traversal

## v2 Route Alias Map

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

Additional protected v2 route roles:

```text
/api/v2/naturepedia/* -> registry discovery and Naturepedia system-map retrieval
/api/v2/plates/* -> Plate™ registry and Graph Registry™ retrieval
/api/v2/rrip/* -> RRIP runtime resolution and registry traversal
/api/v2/razor/* -> Robbie's Razor™ state-token validation and registry-state signaling
```

## Pricing Class Logic

Pricing is assigned by the delivered resource class rather than solely by its URL prefix.

Authoritative pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered and validated payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

### Active Atomic Query Architecture

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

Production Atomic configuration:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Network: eip155:8453
    Asset: USDC
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active

Atomic `/v1` requests normalize to their canonical internal `/x402/query/atomic/` path before pricing, resource availability, payment verification, settlement, and payload-fidelity validation.

Atomic route classification occurs before broader `/x402/` fallback routing so an Atomic resource cannot fall through into subtree or snapshot pricing.

### Atomic Resource Availability Boundary

Atomic resources use an explicit registration model.

A route pattern alone is not proof that a sellable resource exists.

Required behavior:

    Registered + complete deterministic Atomic payload
    → eligible for payment challenge
    → HTTP 402
    → amount 5000
    → gateway tier atomic

    Known but incomplete Atomic resource
    → HTTP 409
    → no payment challenge

    Unknown Atomic resource
    → HTTP 404
    → no payment challenge

This fail-closed boundary ensures the Worker does not request payment for an unavailable or unregistered Atomic deliverable.

### Verified Atomic Production Challenge

Verified active route:

    /v1/query/atomic/robbie-george-biography-plate

Observed production result:

    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED HEADER: true
    PAYMENT REQUIRED: true
    ERROR: Payment Required

Result:

    PASS

This verifies the deterministic `$0.005 USDC` Atomic Query challenge class.

No payment payload was supplied during this validation. No new Atomic USDC settlement or protected Atomic payload-delivery test was performed.

### Verified Atomic Known-Incomplete Boundary

Verified route:

    /v1/query/atomic/robbies-razor-plate

Observed result:

    STATUS: 409
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED HEADER: false
    PAYMENT REQUIRED: false
    CODE: ATOMIC_PAYLOAD_NOT_REGISTERED
    ROUTE STATUS: reserved

Result:

    PASS

The recognized resource is not charged because a complete deterministic Atomic payload is not registered.

### Verified Atomic Unknown-Resource Boundary

Verified route:

    /v1/query/atomic/definitely-not-a-real-atomic-resource-20260820

Observed result:

    STATUS: 404
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED HEADER: false
    PAYMENT REQUIRED: false
    CODE: ATOMIC_RESOURCE_NOT_FOUND
    ERROR: Atomic Query resource not found

Result:

    PASS

Unknown Atomic resources are rejected before payment.

### Enriched Query Architecture

Public route template:

    /v1/query/enriched/{resource}

Production configuration:

    Access class: enriched
    Price: 0.025 USDC
    Atomic units: 25000
    Route status: reserved

The Enriched Query class remains reserved.

Enriched resources must not issue payment challenges until their governed deterministic payloads are explicitly registered, availability-gated, fidelity-bound, and production validated.

### Verified Single-Plate Challenge Routes

Current active Structured Plate™ routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

Verified no-payment challenge behavior for all three:

    HTTP status: 402 Payment Required
    Access class: single-plate
    Price: 0.25 USDC
    Atomic units: 250000
    Network: Base / eip155:8453
    Asset: USDC
    Rights conveyed: one endpoint-level retrieval only

Observed regression result:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true

Result:

    PASS

Atomic activation did not alter the existing Structured Plate challenge class.

Verified Structured Plate safety behavior:

- Unknown Plate identifiers return `404` without a payment challenge.
- Known Plates without registered complete payloads return `409` without a payment challenge.
- Structured Plate challenges are issued only when a complete registered payload passes availability and payload-source preflight validation.
- No new `$0.25 USDC` settlement was executed during the Atomic production validation round.

### Other Active Pricing Classes

Bounded Registry, Taxonomy Subtree, and System Map retrieval:

    Access class: subtree
    Price: 5.00 USDC
    Atomic units: 5000000
    Route status: active

Full Registry, Knowledge Mesh, RRIP protected resource, state-token protected resource, and premium snapshot retrieval:

    Access class: snapshot
    Price: 25.00 USDC
    Atomic units: 25000000
    Route status: active

The exact public control-plane endpoints:

    /api/v2/rrip/resolve
    /api/v2/razor/state-token

remain free discovery and validation surfaces.

Related protected snapshot payloads may require the `$25.00 USDC` snapshot price.

### Protected Retrieval Safety Sequence

The Worker uses a fail-closed retrieval sequence:

    Request
    ↓
    Canonical route normalization
    ↓
    Gateway-tier classification
    ↓
    Explicit resource availability check
    ↓
    Unknown → 404 / no payment
    Known but incomplete → 409 / no payment
    Registered + complete → continue
    ↓
    Deterministic x402 challenge
    ↓
    Payment verification
    ↓
    Settlement
    ↓
    Exact protected payload construction
    ↓
    Tollbooth boundary fidelity validation
    ↓
    Canonical payload hash
    ↓
    Request-binding hash
    ↓
    Authorized response

For Atomic Query delivery, fidelity validation requires:

    Resource class: atomic-query
    Gateway tier: atomic
    Schema version: naturepedia.atomic-query.v1
    Canonical /x402/ path
    Registered Canonical Publication Manifest record

This prevents an Atomic payload from being delivered under the wrong price class or resource class.

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
- derivative-dataset rights
- commercial implementation rights
- Robbie's Razor™ framework implementation rights

Commercial data reuse requires a separate written agreement.

Framework and strategic-infrastructure implementation requires a separate enterprise agreement.

## Human Bypass

Human browser traffic may receive a gateway information page instead of a payment challenge.

Browser traffic is intentionally separated from machine-readable retrieval flows.

## API Challenge Behavior

Requests using headers such as:

```http
Accept: application/json
```

may receive:

```http
402 Payment Required
```

when accessing protected machine-readable resources.

## Governance and State Headers

Primary governance header:

```http
X-Robbie-Razor-Governance: Gr <= Es
```

Current paid responses may also include:

```http
X-Robbie-Registry-State: RGP-{tier}-{timestamp}
X-Robbie-Razor-State-Entropy: {entropy-hash}
X-Robbie-License-Scope: x402 endpoint retrieval only; no training, resale, embeddings, bulk ingestion, or framework implementation rights
X-Robbie-Commercial-License: https://www.robbiegeorgephotography.com/commercial-data-license
X-Robbie-Framework-License: https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing
```

## Payment Flow

Current verified status:

```text
Production infrastructure live.
Production x402 challenge verified.
Human browser bypass verified.
v2 control plane active.
Coinbase CDP facilitator verified.
Base USDC settlement verified.
Protected payload delivery verified.
First live x402 settlement successful.

Machine Status:

x402-status: verified-live
x402-network: eip155:8453
x402-asset: USDC
```

Expected flow:

1. Agent requests protected route.
2. Worker returns HTTP 402 challenge.
3. Agent submits payment payload.
4. Facilitator verifies payment.
5. Facilitator settles payment.
6. Worker returns protected JSON-LD payload.
7. Verified successful settlement recorded.
8. Protected payload delivered with HTTP 200.

## Verified Routes
Verified Settlement Route:

/v1/plates/tree-system-map

Settlement Status:
Success

Network:
Base

Asset:
USDC

Transaction:
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376

x402-status: verified-live

```text
/v1/plates/tree-system-map
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```
## Verified v2 Infrastructure Behavior

Verified static v2 endpoint behavior:

```text
/api/v2/naturepedia/index.md -> 200 OK markdown discovery index
/api/v2/plates/registry.md -> 200 OK markdown Plate registry index
/api/v2/rrip/resolve -> 200 OK JSON RRIP resolution payload
/api/v2/razor/state-token -> 200 OK JSON Robbie's Razor state-token payload
```

Verified protected resource behavior:

```text
Human/browser request:
200 OK human bypass page

API-style request:
Accept: application/json

402 Payment Required

X-402-Provider: Base-USDC
X-402-Amount: <USDC atomic units>
X-402-Gateway-Tier: atomic | enriched | single-plate | subtree | snapshot
X-Robbie-Pricing-Version: 3.0.0
X-Robbie-Pricing-Manifest: https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current status:

```text
Production 402 challenge verified.
Human browser bypass verified.
v2 static core endpoints verified.
v2 route aliasing verified.
RRIP endpoint routing verified.
State-token endpoint routing verified.
Coinbase CDP facilitator verified.
Base USDC settlement verified.
Protected payload delivery verified.
First live x402 settlement successful.

Machine Status:

x402-status: verified-live
x402-production-status: active

Machine Status:

x402-status: verified-live
x402-network: eip155:8453
x402-asset: USDC
x402-production-status: active
x402-first-settlement: successful
```



