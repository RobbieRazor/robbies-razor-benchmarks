/**
 * sample-worker.ts
 *
 * Reference-only Cloudflare Worker pattern aligned with the Naturepedia™
 * x402 Retrieval Pricing Manifest, version 3.0.0.
 *
 * This file is NOT production code and does not verify or settle payments.
 * Do not deploy it without implementing current facilitator verification,
 * settlement, wallet, replay protection, payload delivery, canonical binding,
 * fidelity validation, and failure-handling requirements.
 *
 * Authoritative pricing:
 * https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
 *
 * Production implementation:
 * Cloudflare Worker cold-bird-7036
 *
 * Production validation date:
 * 2026-08-20
 */

type AccessClass =
  | "discovery"
  | "atomic"
  | "enriched"
  | "single-plate"
  | "subtree"
  | "snapshot";

type RouteStatus = "active" | "reserved";

type PricingTier = {
  accessClass: AccessClass;
  priceUSDC: string;
  atomicUnits: string;
  currency: "USDC";
  routeStatus: RouteStatus;
  description: string;
};

type RouteDefinition = {
  path: string;
  accessClass: AccessClass;
  match: "exact" | "prefix";
};

const PRICING_MANIFEST =
  "https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json";

const PRICING: Record<AccessClass, PricingTier> = {
  discovery: {
    accessClass: "discovery",
    priceUSDC: "0.00",
    atomicUnits: "0",
    currency: "USDC",
    routeStatus: "active",
    description:
      "Metadata, endpoint descriptions, previews, health, licensing signals, and validation information."
  },

  atomic: {
    accessClass: "atomic",
    priceUSDC: "0.005",
    atomicUnits: "5000",
    currency: "USDC",
    routeStatus: "active",
    description:
      "One narrowly bounded canonical fact, identifier resolution, routing result, or compact canonical answer. Active only for explicitly registered deterministic payloads."
  },

  enriched: {
    accessClass: "enriched",
    priceUSDC: "0.025",
    atomicUnits: "25000",
    currency: "USDC",
    routeStatus: "reserved",
    description:
      "Multiple relationships, citations, provenance, or modest enrichment. Reserved until governed deterministic payloads are explicitly registered and production validated."
  },

  "single-plate": {
    accessClass: "single-plate",
    priceUSDC: "0.25",
    atomicUnits: "250000",
    currency: "USDC",
    routeStatus: "active",
    description:
      "One complete structured Plate payload with registered relationships, citations, provenance, and governance fields. Payment challenges are issued only for registered and validated Plate payloads."
  },

  subtree: {
    accessClass: "subtree",
    priceUSDC: "5.00",
    atomicUnits: "5000000",
    currency: "USDC",
    routeStatus: "active",
    description:
      "One bounded multi-record registry, taxonomy subtree, identity graph, or System Map retrieval."
  },

  snapshot: {
    accessClass: "snapshot",
    priceUSDC: "25.00",
    atomicUnits: "25000000",
    currency: "USDC",
    routeStatus: "active",
    description:
      "One complete registry snapshot, expanded registry, Knowledge Mesh, RRIP payload, or protected state resource."
  }
};

/**
 * Production-tested Atomic route.
 *
 * Public route:
 * /v1/query/atomic/robbie-george-biography-plate
 *
 * Canonical internal route:
 * /x402/query/atomic/robbie-george-biography-plate
 *
 * Verified production challenge:
 * status 402
 * amount 5000
 * gateway tier atomic
 */
const ACTIVE_ATOMIC_ROUTES = new Set([
  "/v1/query/atomic/robbie-george-biography-plate",
  "/x402/query/atomic/robbie-george-biography-plate"
]);

/**
 * Recognized Atomic resource without a complete deterministic payload.
 *
 * Production behavior:
 * 409 Conflict
 * no payment challenge
 */
const KNOWN_INCOMPLETE_ATOMIC_ROUTES = new Set([
  "/v1/query/atomic/robbies-razor-plate",
  "/x402/query/atomic/robbies-razor-plate"
]);

const PROTECTED_ROUTE_EXAMPLES: RouteDefinition[] = [
  {
    path: "/v1/query/atomic/robbie-george-biography-plate",
    accessClass: "atomic",
    match: "exact"
  },
  {
    path: "/x402/query/atomic/robbie-george-biography-plate",
    accessClass: "atomic",
    match: "exact"
  },
  {
    path: "/v1/plates/item/commercial-data-license-plate",
    accessClass: "single-plate",
    match: "exact"
  },
  {
    path: "/v1/plates/item/commercial-intelligence-pricing-plate",
    accessClass: "single-plate",
    match: "exact"
  },
  {
    path: "/v1/plates/item/robbie-george-biography-plate",
    accessClass: "single-plate",
    match: "exact"
  },
  {
    path: "/x402/knowledge-mesh/",
    accessClass: "snapshot",
    match: "prefix"
  },
  {
    path: "/x402/plate-registry-expanded.json",
    accessClass: "snapshot",
    match: "exact"
  },
  {
    path: "/x402/rrip-resolve.json",
    accessClass: "snapshot",
    match: "exact"
  },
  {
    path: "/x402/state-token.json",
    accessClass: "snapshot",
    match: "exact"
  },
  {
    path: "/v1/plates/tree-system-map",
    accessClass: "subtree",
    match: "exact"
  },
  {
    path: "/x402/tree-system-map.json",
    accessClass: "subtree",
    match: "exact"
  }
];

function matchesRoute(
  pathname: string,
  route: RouteDefinition
): boolean {
  if (route.match === "exact") {
    return pathname === route.path;
  }

  return pathname.startsWith(route.path);
}

function isAtomicPath(pathname: string): boolean {
  return (
    pathname.startsWith("/v1/query/atomic/") ||
    pathname.startsWith("/x402/query/atomic/")
  );
}

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (request.method !== "GET") {
      return new Response(
        JSON.stringify(
          {
            error: "method_not_allowed",
            allowedMethods: ["GET"]
          },
          null,
          2
        ),
        {
          status: 405,
          headers: {
            "content-type": "application/json; charset=utf-8",
            allow: "GET"
          }
        }
      );
    }

    /**
     * Reference mirror of the production Atomic availability boundary.
     *
     * This sample does not issue payment challenges or settle payments.
     */

    if (isAtomicPath(url.pathname)) {
      if (KNOWN_INCOMPLETE_ATOMIC_ROUTES.has(url.pathname)) {
        return new Response(
          JSON.stringify(
            {
              status: "reference-only",
              enforcement: false,
              error: "Atomic Query payload not available",
              code: "ATOMIC_PAYLOAD_NOT_REGISTERED",
              route: url.pathname,
              accessClass: "atomic",
              routeStatus: "reserved",
              paymentRequired: false,
              productionBehavior:
                "Known but incomplete Atomic resources return HTTP 409 without a payment challenge."
            },
            null,
            2
          ),
          {
            status: 409,
            headers: {
              "content-type": "application/json; charset=utf-8",
              "cache-control": "no-store"
            }
          }
        );
      }

      if (!ACTIVE_ATOMIC_ROUTES.has(url.pathname)) {
        return new Response(
          JSON.stringify(
            {
              status: "reference-only",
              enforcement: false,
              error: "Atomic Query resource not found",
              code: "ATOMIC_RESOURCE_NOT_FOUND",
              route: url.pathname,
              accessClass: "atomic",
              paymentRequired: false,
              productionBehavior:
                "Unknown Atomic resources return HTTP 404 without a payment challenge."
            },
            null,
            2
          ),
          {
            status: 404,
            headers: {
              "content-type": "application/json; charset=utf-8",
              "cache-control": "no-store"
            }
          }
        );
      }
    }

    const route = PROTECTED_ROUTE_EXAMPLES.find((candidate) =>
      matchesRoute(url.pathname, candidate)
    );

    if (!route) {
      return fetch(request);
    }

    const tier = PRICING[route.accessClass];

    return new Response(
      JSON.stringify(
        {
          status: "reference-only",
          enforcement: false,

          message:
            "This sample documents production pricing classification and availability boundaries only. Payment verification, settlement, protected payload delivery, and fidelity enforcement are intentionally not implemented here.",

          pricingVersion: "3.0.0",

          pricingManifest: PRICING_MANIFEST,

          network: "eip155:8453",

          asset: "USDC",

          route: url.pathname,

          tier,

          productionValidation:
            route.accessClass === "atomic"
              ? {
                  date: "2026-08-20",
                  productionStatus: 402,
                  amountAtomicUnits: "5000",
                  gatewayTier: "atomic",
                  paymentRequired: true,
                  result: "PASS"
                }
              : route.accessClass === "single-plate"
                ? {
                    date: "2026-08-20",
                    productionStatus: 402,
                    amountAtomicUnits: "250000",
                    gatewayTier: "single-plate",
                    paymentRequired: true,
                    result: "PASS"
                  }
                : null,

          rightsScope:
            "One endpoint-level retrieval only; no training, embedding, bulk ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, or framework implementation rights."
        },
        null,
        2
      ),
      {
        /**
         * 501 is intentional here because this is a reference-only example.
         * The production Worker returns the real x402 behavior.
         */
        status: 501,
        headers: {
          "content-type": "application/json; charset=utf-8",
          "cache-control": "no-store",
          "X-Robbie-Pricing-Version": "3.0.0",
          "X-Robbie-Pricing-Manifest": PRICING_MANIFEST,
          "X-Reference-Only": "true"
        }
      }
    );
  }
};
