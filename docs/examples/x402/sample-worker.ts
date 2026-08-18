/**
 * sample-worker.ts
 *
 * Reference-only Cloudflare Worker pattern aligned with the Naturepedia™
 * x402 Retrieval Pricing Manifest, version 3.0.0.
 *
 * This file is NOT production code and does not verify or settle payments.
 * Do not deploy it without implementing current facilitator verification,
 * settlement, wallet, payload-delivery, and failure-handling requirements.
 *
 * Authoritative pricing:
 * https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
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
    routeStatus: "reserved",
    description:
      "One fact, identifier resolution, routing result, or compact canonical answer."
  },

  enriched: {
    accessClass: "enriched",
    priceUSDC: "0.025",
    atomicUnits: "25000",
    currency: "USDC",
    routeStatus: "reserved",
    description:
      "Multiple relationships, citations, provenance, or modest enrichment."
  },

  "single-plate": {
    accessClass: "single-plate",
    priceUSDC: "0.25",
    atomicUnits: "250000",
    currency: "USDC",
    routeStatus: "reserved",
    description:
      "One complete structured Plate payload with registered relationships, citations, provenance, and governance fields."
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

const PROTECTED_ROUTE_EXAMPLES: Array<{
  prefix: string;
  accessClass: AccessClass;
}> = [
  {
    prefix: "/x402/knowledge-mesh/",
    accessClass: "snapshot"
  },
  {
    prefix: "/x402/plate-registry-expanded.json",
    accessClass: "snapshot"
  },
  {
    prefix: "/x402/rrip-resolve.json",
    accessClass: "snapshot"
  },
  {
    prefix: "/x402/state-token.json",
    accessClass: "snapshot"
  },
  {
    prefix: "/v1/plates/tree-system-map",
    accessClass: "subtree"
  },
  {
    prefix: "/x402/tree-system-map.json",
    accessClass: "subtree"
  }
];

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

    const route = PROTECTED_ROUTE_EXAMPLES.find(({ prefix }) =>
      url.pathname.startsWith(prefix)
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
            "This sample documents pricing classification only. Payment verification and settlement are intentionally not implemented.",
          pricingVersion: "3.0.0",
          pricingManifest: PRICING_MANIFEST,
          network: "eip155:8453",
          asset: "USDC",
          route: url.pathname,
          tier,
          rightsScope:
            "One endpoint-level retrieval only; no training, embedding, bulk ingestion, redistribution, resale, synchronization, private-dataset, derivative-dataset, commercial-implementation, or framework-implementation rights."
        },
        null,
        2
      ),
      {
        status: 501,
        headers: {
          "content-type": "application/json; charset=utf-8",
          "cache-control": "no-store",
          "X-Robbie-Pricing-Version": "3.0.0",
          "X-Robbie-Pricing-Manifest": PRICING_MANIFEST
        }
      }
    );
  }
};
