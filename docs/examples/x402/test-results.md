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

```text
/x402/*
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
```

## Current Status

```text
Production x402 challenge verified.

Payment settlement pending first live transaction.
```

## Validation Checklist

- Human browser bypass verified
- API challenge verified
- Base network configured
- USDC settlement configured
- Governance header verified
- Legacy endpoint family active
- v1 endpoint families active
- Settlement verification pending
