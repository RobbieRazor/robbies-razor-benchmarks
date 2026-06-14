# x402 Test Results

## Deployment Date

2026-06-11

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

## Verified API / Agent Challenge Test

Request:

```javascript
fetch("https://www.robbiegeorgephotography.com/v1/plates/tree-system-map", {
  headers: {
    "Accept": "application/json"
  }
})
```

Result:

```text
402 Payment Required

X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
```

## Cloudflare Log Confirmation

Observed log messages:

```text
x402 route triggered
x402 detection result
x402 human/search bypass
x402 returning payment challenge
```

## Pricing Verification

```text
taxonomy  = $1.00
plates    = $5.00
sovereign = $25.00
legacy    = $5.00
```

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
Production x402 challenge verified.

Human browser bypass verified.

RRIP endpoint verified.

State-token endpoint verified.

Registry-state synchronization architecture documented.

Payment settlement pending first live transaction.
```

## Validation Checklist

* Human browser bypass verified
* API challenge verified
* Base network configured
* USDC settlement configured
* Governance header verified
* Legacy endpoint family active
* v1 endpoint families active
* v2 endpoint families active
* RRIP endpoint verified
* State-token endpoint verified
* Registry-state architecture documented
* Settlement verification pending
