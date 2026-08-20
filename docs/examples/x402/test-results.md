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

### Pricing v3 Snapshot Challenge Verification — 2026-08-18

A second unpaid production request tested the protected Geology Knowledge Mesh endpoint:

```text
https://www.robbiegeorgephotography.com/v1/knowledge-mesh/geology
```

Observed result:

```text
402 Payment Required

Payment-Required: present
X-402-Provider: Base-USDC
X-402-Amount: 25000000
X-402-Gateway-Tier: snapshot
X-Robbie-Pricing-Version: 3.0.0
X-Robbie-Pricing-Manifest: https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
Link: <https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json>; rel="describedby"; type="application/ld+json"
Cache-Control: no-store
```

The amount `25000000` represents `25.00 USDC` using six-decimal USDC atomic units. This verifies the active snapshot and Knowledge Mesh challenge class.

No payment was authorized, no settlement was attempted, and protected payload delivery was not tested during this observation.

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

## Current Pricing v3 Configuration — 2026-08-20

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Discovery and previews | Free | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered and validated payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

Authoritative pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

### Atomic Query Production Activation — 2026-08-20

Atomic Query was activated in production for explicitly registered deterministic resources.

Current active route:

    /v1/query/atomic/robbie-george-biography-plate

Canonical internal route:

    /x402/query/atomic/robbie-george-biography-plate

Canonical resolved Plate identifier:

    robbie-george#robbie-george-biography-plate

Canonical authority:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Production pricing:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Network: eip155:8453
    Asset: USDC

### Atomic Available-Resource Challenge Test

Observed production result:

    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED HEADER: true
    PAYMENT REQUIRED: true
    ERROR: Payment Required

Result:

    PASS

This verified that a registered Atomic Query resource with a complete deterministic payload issues the correct fixed `402 Payment Required` challenge at `5000` USDC atomic units.

No payment payload was supplied, no USDC payment was authorized, no settlement was attempted, and protected Atomic payload delivery was not tested during this challenge observation.

### Atomic Known-but-Incomplete Safety Test

Test route:

    /v1/query/atomic/robbies-razor-plate

Observed production result:

    STATUS: 409
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED HEADER: false
    PAYMENT REQUIRED: false
    CODE: ATOMIC_PAYLOAD_NOT_REGISTERED
    ROUTE STATUS: reserved

Result:

    PASS

This verified that a recognized Atomic resource without a complete registered deterministic payload is rejected before payment.

The route returned `409 Conflict` and did not expose an x402 amount, pricing tier, or payment challenge.

### Atomic Unknown-Resource Safety Test

Test route:

    /v1/query/atomic/definitely-not-a-real-atomic-resource-20260820

Observed production result:

    STATUS: 404
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED HEADER: false
    PAYMENT REQUIRED: false
    CODE: ATOMIC_RESOURCE_NOT_FOUND
    ERROR: Atomic Query resource not found

Result:

    PASS

This verified that an unknown Atomic resource is rejected before payment.

The route returned `404 Not Found` and did not expose an x402 amount, pricing tier, or payment challenge.

### Atomic Production Safety Matrix

    Registered + complete Atomic resource
    → 402 Payment Required
    → amount 5000
    → tier atomic

    Known + incomplete Atomic resource
    → 409 Conflict
    → no payment challenge

    Unknown Atomic resource
    → 404 Not Found
    → no payment challenge

Status:

    PASS

### Atomic Discovery-Surface Validation — 2026-08-20

A consolidated production validation was performed after deployment of the synchronized machine-discovery metadata.

Observed results:

    PASS — Pricing manifest HTTP 200 — status=200
    PASS — Atomic pricing active — status=active, price=0.005, units=5000
    PASS — Atomic active route registered — /v1/query/atomic/robbie-george-biography-plate
    PASS — Enriched remains reserved — status=reserved, price=0.025, units=25000

    PASS — AI Catalog HTTP 200 — status=200
    PASS — Atomic resource in AI Catalog — status=active, price=0.005, units=5000

    PASS — OpenAPI HTTP 200 — status=200
    PASS — Atomic OpenAPI route present — getNaturepediaAtomicQuery
    PASS — OpenAPI Atomic price correct

    PASS — Canonical Publication Manifest HTTP 200 — status=200
    PASS — CPM Atomic active
    PASS — CPM Enriched reserved

    PASS — AI Root HTTP 200 — status=200
    PASS — AI Root Atomic active
    PASS — AI Root Enriched reserved

    PASS — MCP server card HTTP 200 — status=200
    PASS — MCP Atomic active
    PASS — MCP Enriched reserved

    PASS — Atomic live challenge — status=402, amount=5000, tier=atomic

Overall result:

    PASS

This confirms that the active Atomic Query class is synchronized across:

- production Worker routing
- x402 pricing manifest
- AI Catalog
- OpenAPI service description
- Canonical Publication Manifest
- AI Root
- MCP server-card metadata
- live x402 challenge behavior

The Enriched Query class remains reserved at `0.025 USDC` / `25000` atomic units.

### Structured Plate Regression Verification — 2026-08-20

The three existing registered Structured Plate™ routes were retested after Atomic activation.

Routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

Observed result for all three:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true

Result:

    PASS

Atomic Query activation did not alter the existing `$0.25` Structured Plate challenge behavior.

No new `$0.25` settlement or protected Structured Plate payload-delivery test was performed during this regression validation.

Unknown Plate identifiers continue to return `404` without a payment challenge.

Known Plates without complete registered payloads continue to return `409` without a payment challenge.

### Current Production Retrieval State

    Discovery
    Free
    Active

    Atomic Query
    0.005 USDC
    5000 atomic units
    Active for explicitly registered deterministic payloads

    Enriched Query
    0.025 USDC
    25000 atomic units
    Reserved

    Structured Plate
    0.25 USDC
    250000 atomic units
    Active for registered and validated payloads

    Bounded Registry / Taxonomy / System Map
    5.00 USDC
    5000000 atomic units
    Active

    Full Registry / Knowledge Mesh / Snapshot
    25.00 USDC
    25000000 atomic units
    Active

### Retrieval Rights Boundary

An x402 payment grants one endpoint-level retrieval of the identified resource only.

Payment does not grant:

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

Commercial reuse and framework implementation remain subject to separate written licensing agreements.


## Governance Header Verification

```http
X-Robbie-Razor-Governance: Gr <= Es
```

## Endpoint Families Verified

### Legacy x402 Routes

Legacy protected-resource routes remain available for backward compatibility:

    /x402/*

The historical endpoint count recorded before Atomic Query activation was:

    14

This historical count is retained as provenance and should not be interpreted as the current total production route count.

### Current v1 Machine Retrieval Families

Current v1 machine-retrieval families include:

    /v1/query/atomic/*
    /v1/taxonomy/*
    /v1/plates/*
    /v1/registries/*
    /v1/knowledge-mesh/*
    /v1/sovereign/*

The current production v1 architecture includes both canonical route families and resource-specific aliases.

Because route registration continues to evolve, this test record does not assert a new aggregate v1 route count without a dedicated inventory test.

### Atomic Query Family

Public route template:

    /v1/query/atomic/{resource}

Canonical internal route template:

    /x402/query/atomic/{resource}

Current active Atomic route:

    /v1/query/atomic/robbie-george-biography-plate

Production state:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active for registered deterministic payloads

Verified behavior:

    Registered + complete
    → 402
    → amount 5000
    → tier atomic
    → payment challenge present

    Known + incomplete
    → 409
    → no payment challenge

    Unknown
    → 404
    → no payment challenge

Result:

    PASS

### v2 Infrastructure and Retrieval Routes

Current v2 families:

    /api/v2/naturepedia/*
    /api/v2/plates/*
    /api/v2/rrip/*
    /api/v2/razor/*

Core v2 infrastructure endpoints verified:

    /api/v2/naturepedia/index.md
    /api/v2/plates/registry.md
    /api/v2/rrip/resolve
    /api/v2/razor/state-token

Verified behavior:

    200 OK
    Worker-served
    Machine-readable
    Governance-enabled

The historical v2 endpoint count recorded before the current Atomic activation remains:

    8

This value is retained as a historical inventory observation rather than a claim about every currently registered Worker route.

### Current Machine-Facing Architecture

The production architecture should now be interpreted by functional layer rather than relying on the older aggregate route-count total:

    Public Authority
    ↓
    Public Discovery
    ↓
    Registry
    ↓
    Resolution
    ↓
    State Validation
    ↓
    Resource Availability Validation
    ↓
    Retrieval Class Resolution
    ↓
    x402 Challenge when required
    ↓
    Verification
    ↓
    Settlement
    ↓
    Fidelity Validation
    ↓
    Authorized Retrieval

### Architecture Layers Verified

    Discovery
    Registry
    Resolution
    Validation
    Availability gating
    Deterministic pricing
    Settlement infrastructure
    Fidelity validation

### Registry-State Synchronization Verified

    State-token endpoint deployed
    RRIP endpoint deployed
    Registry endpoint deployed
    Discovery endpoint deployed
    Worker routing verified
    v2 alias routing verified
    Atomic route normalization verified
    Atomic availability boundary verified
    Atomic pricing classification verified

## Current Status

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

    Deterministic pricing variables configured.

    Atomic Query active for explicitly registered deterministic payloads.

    Atomic Query price:
    0.005 USDC / 5000 atomic units.

    Atomic production challenge:
    402 / 5000 / atomic — PASS.

    Atomic known-incomplete boundary:
    409 / no payment challenge — PASS.

    Atomic unknown-resource boundary:
    404 / no payment challenge — PASS.

    Enriched Query remains reserved:
    0.025 USDC / 25000 atomic units.

    Structured Plate retrieval active for registered and validated payloads.

    Structured Plate regression validation:
    402 / 250000 / single-plate — PASS.

    Subtree retrieval active:
    5.00 USDC / 5000000 atomic units.

    Snapshot retrieval active:
    25.00 USDC / 25000000 atomic units.

    Analytics Engine binding configured.

    Privacy-preserving analytics salt configured.

    Pricing-v3 challenge-header verification completed.

    Atomic discovery-surface synchronization validated on 2026-08-20.

    New Atomic paid settlement and HTTP 200 protected payload-delivery verification pending.

    New Structured Plate paid settlement and protected payload-delivery re-verification pending.

## Validation Checklist

* Historical human-browser bypass verified
* Historical API payment challenge verified
* Historical Base USDC settlement verified
* Historical protected payload delivery verified
* Base network configured as `eip155:8453`
* USDC settlement infrastructure configured
* Governance headers enabled
* Pricing manifest version `3.0.0` live
* Atomic canonical-query price configured as `5000`
* Atomic canonical-query production class is active for explicitly registered deterministic payloads
* Active Atomic route verified at `/v1/query/atomic/robbie-george-biography-plate`
* Active Atomic route returned `402`, amount `5000`, and tier `atomic`
* Atomic `PAYMENT-REQUIRED` challenge behavior verified
* Known incomplete Atomic route `/v1/query/atomic/robbies-razor-plate` returned `409` without a payment challenge
* Unknown Atomic resource returned `404` without a payment challenge
* Atomic pricing synchronized with the production pricing manifest
* Atomic route synchronized with the AI Catalog
* Atomic route synchronized with OpenAPI
* Atomic state synchronized with the Canonical Publication Manifest
* Atomic state synchronized with AI Root
* Atomic state synchronized with MCP server-card metadata
* Enriched relationship-query price configured as `25000`
* Enriched relationship-query class remains reserved
* Structured Plate™ price configured as `250000`
* Structured Plate™ retrieval active only for registered and validated payloads
* Active Structured Plate™ route verified at `/v1/plates/item/commercial-data-license-plate`
* Active Structured Plate™ route verified at `/v1/plates/item/commercial-intelligence-pricing-plate`
* Active Structured Plate™ route verified at `/v1/plates/item/robbie-george-biography-plate`
* All three active Structured Plate™ routes returned `402`, amount `250000`, and tier `single-plate`
* Unknown Plate routes return `404` without a payment challenge
* Known Plates without registered complete payloads return `409` without a payment challenge
* Known incomplete Plate route `/v1/plates/item/robbies-razor-plate` returned `409` without a payment challenge
* Subtree price configured as `5000000`
* Snapshot price configured as `25000000`
* Analytics Engine binding configured
* Privacy-preserving analytics salt configured
* Pricing-v3 challenge-header verification completed
* New Atomic paid settlement verification pending
* New Atomic protected HTTP `200` payload-delivery verification pending
* New `$0.25` Structured Plate™ settlement verification pending
* New `$0.25` protected Structured Plate payload-delivery verification pending

## Rights and Evidence Boundary

Successful x402 challenge behavior, payment settlement, or protected payload delivery does not establish scientific validation, canonical truth, authorship transfer, or broader licensing rights.

An x402 payment grants one endpoint-level retrieval only.

Commercial data reuse and Robbie's Razor™ framework implementation require separate written agreements.
