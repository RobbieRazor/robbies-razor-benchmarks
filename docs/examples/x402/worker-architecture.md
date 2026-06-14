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

Pricing:

```text
X402_DISCOVERY_PRICE=1.00
X402_PLATE_PRICE=5.00
X402_SOVEREIGN_PRICE=25.00
X402_LEGACY_PRICE=5.00
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

## v2 Static Core Infrastructure Endpoints

The Worker now directly serves four core v2 infrastructure endpoints before x402 payment-gateway routing.

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These routes function as the public machine-facing infrastructure layer for:

- Naturepedia™ discovery
- Plate™ registry discovery
- RRIP resolution
- Robbie's Razor™ state validation
- governance signaling
- registry-state continuity

These endpoints return `200 OK` directly from the Worker and include machine-readable governance headers.

They establish the live v2 retrieval sequence:

```text
Discovery
↓
Registry
↓
Resolution
↓
Validation
↓
Settlement
```

x402 remains the settlement layer for protected machine-readable retrieval beyond the public static core endpoints.

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

## Tier Logic

```text
taxonomy -> 1.00 USDC
plates -> 5.00 USDC
sovereign -> 25.00 USDC
legacy -> 5.00 USDC

v2 naturepedia -> taxonomy tier -> 1.00 USDC
v2 plates -> plates tier -> 5.00 USDC
v2 rrip -> sovereign tier -> 25.00 USDC
v2 razor -> sovereign tier -> 25.00 USDC
```

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
Production x402 challenge verified.
Payment settlement pending first live transaction.
```

Expected flow:

1. Agent requests protected route.
2. Worker returns HTTP 402 challenge.
3. Agent submits payment payload.
4. Facilitator verifies payment.
5. Facilitator settles payment.
6. Worker returns protected JSON-LD payload.

## Verified Routes

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
X-402-Gateway-Tier: taxonomy | plates | sovereign | legacy
```

Current status:

```text
Production 402 challenge verified.
Human browser bypass verified.
v2 static core endpoints verified.
v2 route aliasing verified.
RRIP endpoint routing verified.
State-token endpoint routing verified.
Payment settlement pending first live transaction.
```



