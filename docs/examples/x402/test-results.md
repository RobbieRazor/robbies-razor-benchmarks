# x402 Test Results

## Test Record Status

Historical verification date: `2026-06-11`

Pricing manifest v3 production deployment: `2026-08-17`

The original payment challenge, settlement, and payload-delivery test remains part of the historical verification record.

The pricing v3 manifest is live in production. Post-deployment challenge-header and settlement testing for pricing version `3.0.0` must be recorded separately rather than rewriting the historical results as though they were newly observed.

## Worker

```text
cold-bird-7036
```

## Verified Human Browser Test

URL:

```text
https://www.robbiegeorgephotography.com/v1/plates/tree-system-map
```

Result:

```text
200 OK

Naturepedia x402 Gateway

Human visitors bypass payment gating.

Protected Resource:
Naturepedia Tree System Map
```

## Historical Verified API / Agent Challenge Test — 2026-06-11

Historical request:

```javascript
fetch("https://www.robbiegeorgephotography.com/v1/plates/tree-system-map", {
  headers: {
    "Accept": "application/json"
  }
})
```

Historical observed result:

```text
402 Payment Required

X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
```

These headers are preserved as part of the original production test and do not describe the current gateway classification.

## Pricing v3 Verified Challenge Headers — 2026-08-18

A new unpaid production request was made to the protected Tree System Map route using an API-oriented Accept header and a non-browser audit user agent.

Observed result:

```text
402 Payment Required

Payment-Required: present
X-402-Provider: Base-USDC
X-402-Amount: 5000000
X-402-Gateway-Tier: subtree
X-Robbie-Pricing-Version: 3.0.0
X-Robbie-Pricing-Manifest: https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
Link: <https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json>; rel="describedby"; type="application/ld+json"
Cache-Control: no-store
```

## Cloudflare Log Confirmation

Observed log messages:

```text
x402 route triggered
x402 detection result
x402 human/search bypass
x402 returning payment challenge
```

## Historical Pricing Verification — 2026-06-11

The original production test verified the prior gateway architecture:

```text
taxonomy  = $1.00
plates    = $5.00
sovereign = $25.00
legacy    = $5.00
```

These historical tier names and values are retained only as part of the original test record and are no longer the production pricing authority.

## Current Pricing v3 Configuration — 2026-08-17

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Reserved |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Reserved |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

Authoritative pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Status: Pricing manifest version `3.0.0` is live. Post-deployment challenge-header and settlement re-verification must be recorded as a new observation.

## Governance Header Verification

```http
X-Robbie-Razor-Governance: Gr <= Es
```

## Endpoint Families Verified

### Legacy x402 Routes

```text
/x402/*
```

Verified endpoint count:

```text
14
```

### v1 Compatibility Routes

```text
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
```

Verified endpoint count:

```text
12
```

### v2 Infrastructure and Retrieval Routes

```text
/api/v2/naturepedia/*
/api/v2/plates/*
/api/v2/rrip/*
/api/v2/razor/*
```

Verified endpoint count:

```text
8
```

### Core v2 Infrastructure Endpoints Verified

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

Verified behavior:

```text
200 OK
Worker-served
Machine-readable
Governance-enabled
```

### Machine-Facing Architecture Inventory

```text
x402 Routes: 14
v1 Routes:   12
v2 Routes:    8
----------------
Total:       34
```

### Architecture Layers Verified

```text
Discovery
Registry
Resolution
Validation
Settlement
```

### Registry-State Synchronization Verified

```text
State-token endpoint deployed
RRIP endpoint deployed
Registry endpoint deployed
Discovery endpoint deployed
Worker routing verified
v2 alias routing verified
```

## Current Status

```text
Production infrastructure live.

Historical x402 challenge verified.

Historical Base USDC settlement verified.

Historical protected payload delivery verified.

Human browser bypass verified.

Discovery Plane live.

Registry Plane live.

RRIP Resolution Plane live.

State Validation Plane live.

v1 compatibility architecture active.

v2 machine retrieval architecture active.

Pricing manifest version 3.0.0 live.

New deterministic pricing variables configured.

Analytics Engine binding configured.

Privacy-preserving analytics salt configured.

Pricing-v3 challenge-header verification completed on 2026-08-18.

Pricing-v3 paid settlement and payload-delivery re-verification pending.
```

## Validation Checklist

* Historical human-browser bypass verified
* Historical API payment challenge verified
* Historical Base USDC settlement verified
* Historical protected payload delivery verified
* Base network configured as `eip155:8453`
* USDC settlement infrastructure configured
* Governance headers enabled
* Pricing manifest version `3.0.0` live
* Atomic price configured as `5000`
* Enriched price configured as `25000`
* Structured Plate™ price configured as `250000`
* Subtree price configured as `5000000`
* Snapshot price configured as `25000000`
* Analytics Engine binding configured
* Privacy-preserving analytics salt configured
* Pricing-v3 challenge-header verification completed on 2026-08-18
* Pricing-v3 settlement verification pending
* Pricing-v3 payload-delivery verification pending
