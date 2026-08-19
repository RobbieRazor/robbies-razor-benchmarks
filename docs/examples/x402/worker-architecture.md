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

### Verified Single-Plate Challenge Routes

```text
/v1/plates/item/commercial-data-license-plate
/v1/plates/item/commercial-intelligence-pricing-plate
/v1/plates/item/robbie-george-biography-plate
```

Verified no-payment challenge behavior:

- HTTP status: `402 Payment Required`
- Access class: `single-plate`
- Price: `$0.25 USDC`
- Atomic units: `250000`
- Network: Base / `eip155:8453`
- Asset: USDC
- Payload source: GitHub canonical Plate registry
- Rights conveyed: one endpoint-level retrieval only

Verified safety behavior:

- Unknown Plate identifiers return `404` without a payment challenge.
- Known Plates without registered complete payloads return `409` without a payment challenge.
- No `$0.25` settlement was executed during these challenge and failure-boundary tests.

Pricing is assigned by the delivered resource class rather than solely by its URL prefix.

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Reserved |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

Current active single-Plate routes:

```text
/v1/plates/item/commercial-data-license-plate
/v1/plates/item/commercial-intelligence-pricing-plate
/v1/plates/item/robbie-george-biography-plate
```

The exact `/api/v2/rrip/resolve` and `/api/v2/razor/state-token` control-plane routes remain free. Related protected snapshot payloads may require the `$25.00 USDC` snapshot price.

Atomic and Enriched routes remain reserved. Structured Plate challenges are issued only when a complete registered payload passes preflight validation.

Unknown Plate identifiers return `404` without a payment challenge. Known Plates without registered complete payloads return `409` without a payment challenge.

Authoritative pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

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



