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
```

New `/v1/*` routes are mapped internally to legacy `/x402/*.json` payloads through canonical route aliasing.

## Tier Logic

```text
taxonomy -> 1.00 USDC
plates -> 5.00 USDC
sovereign -> 25.00 USDC
legacy -> 5.00 USDC
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

## Governance Header

```http
X-Robbie-Razor-Governance: Gr <= Es
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

## Verified Route

```text
/v1/plates/tree-system-map
```

## Verified Challenge Result

```text
STATUS: 402
X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
```
