/**
 * sample-worker.ts
 *
 * Reference-only Cloudflare Worker pattern aligned with the Naturepedia™
 * x402 Retrieval Pricing Manifest, version 3.0.0.
 *
 * IMPORTANT
 * ---------
 * This file is NOT production code.
 *
 * It intentionally does NOT implement:
 * - facilitator payment verification
 * - settlement
 * - wallet authorization
 * - replay protection
 * - protected payload delivery
 * - canonical payload hashing
 * - request-binding hashes
 * - production telemetry
 * - production licensing enforcement
 * - payload fidelity enforcement
 *
 * Its purpose is to demonstrate one important production principle:
 *
 *   route syntax
 *   ≠
 *   resource existence
 *
 *   pricing class
 *   ≠
 *   resource registration
 *
 *   only an explicitly registered + complete + protected resource
 *   may become eligible for an x402 payment challenge
 *
 * Authoritative production pricing:
 * https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
 *
 * Production Worker:
 * cold-bird-7036
 *
 * Current governing framework authority:
 * GC-MRD-v2.0
 */

type AccessClass =
  | "discovery"
  | "atomic"
  | "enriched"
  | "single-plate"
  | "subtree"
  | "snapshot";

type PricingClassStatus =
  | "active"
  | "pricing-class-defined";

type ResourceState =
  | "registered-complete"
  | "known-incomplete";

type PricingTier = {
  accessClass: AccessClass;
  priceUSDC: string;
  atomicUnits: string;
  currency: "USDC";
  classStatus: PricingClassStatus;
  availabilityMode:
    | "public"
    | "explicit-registration-required";
  description: string;
};

type ResourceRecord = {
  id: string;
  canonicalAuthority: string;
  accessClass: AccessClass;
  state: ResourceState;
  paths: string[];
  schemaVersion?: string;
  productionChallengeValidation?: {
    date: string;
    status: 402;
    amountAtomicUnits: string;
    gatewayTier: AccessClass;
    paymentRequired: true;
    settlementTestedInThisValidation: boolean;
    protectedPayloadDeliveryTestedInThisValidation: boolean;
    result: "PASS";
  };
};

const PRICING_MANIFEST =
  "https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json";

const GOVERNING_AUTHORITY = "GC-MRD-v2.0";

const NETWORK = "eip155:8453";

const ASSET = "USDC";

/**
 * Pricing-class configuration.
 *
 * NOTE:
 * "pricing-class-defined" does NOT mean that every resource that could
 * theoretically belong to that class exists or is payment-eligible.
 */
const PRICING: Record<AccessClass, PricingTier> = {
  discovery: {
    accessClass: "discovery",
    priceUSDC: "0.00",
    atomicUnits: "0",
    currency: "USDC",
    classStatus: "active",
    availabilityMode: "public",
    description:
      "Public metadata, discovery, previews, health information, licensing signals, and control-plane resources where exposed."
  },

  atomic: {
    accessClass: "atomic",
    priceUSDC: "0.005",
    atomicUnits: "5000",
    currency: "USDC",
    classStatus: "active",
    availabilityMode: "explicit-registration-required",
    description:
      "One narrowly bounded canonical fact, identifier resolution, routing result, or compact canonical answer. Only explicitly registered deterministic payloads are payment-eligible."
  },

  enriched: {
    accessClass: "enriched",
    priceUSDC: "0.025",
    atomicUnits: "25000",
    currency: "USDC",
    classStatus: "active",
    availabilityMode: "explicit-registration-required",
    description:
      "Multiple relationships, citations, provenance, or modest enrichment. Only explicitly registered, governed, deterministic payloads are payment-eligible."
  },

  "single-plate": {
    accessClass: "single-plate",
    priceUSDC: "0.25",
    atomicUnits: "250000",
    currency: "USDC",
    classStatus: "active",
    availabilityMode: "explicit-registration-required",
    description:
      "One complete Structured Plate™ payload. Only explicitly registered, validated, complete Plate payloads are payment-eligible."
  },

  subtree: {
    accessClass: "subtree",
    priceUSDC: "5.00",
    atomicUnits: "5000000",
    currency: "USDC",
    classStatus: "pricing-class-defined",
    availabilityMode: "explicit-registration-required",
    description:
      "Pricing class for qualifying bounded multi-record resources such as a taxonomy subtree, Registry, identity graph, or System Map. Individual resource availability is registration-specific."
  },

  snapshot: {
    accessClass: "snapshot",
    priceUSDC: "25.00",
    atomicUnits: "25000000",
    currency: "USDC",
    classStatus: "pricing-class-defined",
    availabilityMode: "explicit-registration-required",
    description:
      "Pricing class for qualifying explicitly registered large resources such as a full Registry or Knowledge Mesh snapshot. The class does not imply that every possible snapshot resource exists."
  }
};

/**
 * Explicit protected-resource registry.
 *
 * This is the key safety pattern demonstrated by this example.
 *
 * Do NOT derive sellable resources from:
 * - path prefixes
 * - taxonomy names
 * - framework terminology
 * - pricing tiers
 * - architectural diagrams
 *
 * Every protected resource must have an explicit record.
 */
const PROTECTED_RESOURCES: ResourceRecord[] = [
  {
    id: "robbie-george-biography-atomic-query",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/who-is-robbie-george",
    accessClass: "atomic",
    state: "registered-complete",
    schemaVersion: "naturepedia.atomic-query.v1",
    paths: [
      "/v1/query/atomic/robbie-george-biography-plate",
      "/x402/query/atomic/robbie-george-biography-plate"
    ],
    productionChallengeValidation: {
      date: "2026-08-20",
      status: 402,
      amountAtomicUnits: "5000",
      gatewayTier: "atomic",
      paymentRequired: true,
      settlementTestedInThisValidation: false,
      protectedPayloadDeliveryTestedInThisValidation: false,
      result: "PASS"
    }
  },

  {
    id: "robbie-george-biography-enriched-query",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/who-is-robbie-george",
    accessClass: "enriched",
    state: "registered-complete",
    schemaVersion: "naturepedia.enriched-query.v1",
    paths: [
      "/v1/query/enriched/robbie-george-biography-plate",
      "/x402/query/enriched/robbie-george-biography-plate"
    ],
    productionChallengeValidation: {
      date: "2026-08-24",
      status: 402,
      amountAtomicUnits: "25000",
      gatewayTier: "enriched",
      paymentRequired: true,
      settlementTestedInThisValidation: false,
      protectedPayloadDeliveryTestedInThisValidation: false,
      result: "PASS"
    }
  },

  {
    id: "robbies-razor-atomic-query",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/robbies-razor",
    accessClass: "atomic",
    state: "known-incomplete",
    schemaVersion: "naturepedia.atomic-query.v1",
    paths: [
      "/v1/query/atomic/robbies-razor-plate",
      "/x402/query/atomic/robbies-razor-plate"
    ]
  },

  {
    id: "commercial-data-license-plate",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/commercial-data-license",
    accessClass: "single-plate",
    state: "registered-complete",
    paths: [
      "/v1/plates/item/commercial-data-license-plate"
    ],
    productionChallengeValidation: {
      date: "2026-08-20",
      status: 402,
      amountAtomicUnits: "250000",
      gatewayTier: "single-plate",
      paymentRequired: true,
      settlementTestedInThisValidation: false,
      protectedPayloadDeliveryTestedInThisValidation: false,
      result: "PASS"
    }
  },

  {
    id: "commercial-intelligence-pricing-plate",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/commercial-data-license",
    accessClass: "single-plate",
    state: "registered-complete",
    paths: [
      "/v1/plates/item/commercial-intelligence-pricing-plate"
    ],
    productionChallengeValidation: {
      date: "2026-08-20",
      status: 402,
      amountAtomicUnits: "250000",
      gatewayTier: "single-plate",
      paymentRequired: true,
      settlementTestedInThisValidation: false,
      protectedPayloadDeliveryTestedInThisValidation: false,
      result: "PASS"
    }
  },

  {
    id: "robbie-george-biography-plate",
    canonicalAuthority:
      "https://www.robbiegeorgephotography.com/who-is-robbie-george",
    accessClass: "single-plate",
    state: "registered-complete",
    paths: [
      "/v1/plates/item/robbie-george-biography-plate"
    ],
    productionChallengeValidation: {
      date: "2026-08-20",
      status: 402,
      amountAtomicUnits: "250000",
      gatewayTier: "single-plate",
      paymentRequired: true,
      settlementTestedInThisValidation: false,
      protectedPayloadDeliveryTestedInThisValidation: false,
      result: "PASS"
    }
  }
];

/**
 * Public control-plane endpoints.
 *
 * These are intentionally modeled separately from protected resources.
 *
 * In particular:
 *
 * /api/v2/rrip/resolve
 * and
 * /api/v2/razor/state-token
 *
 * must NOT become $25 products merely because a snapshot pricing class exists.
 */
const PUBLIC_CONTROL_PLANE = new Set([
  "/api/v2/naturepedia/index.md",
  "/api/v2/plates/registry.md",
  "/api/v2/rrip/resolve",
  "/api/v2/razor/state-token"
]);

/**
 * Protected route families.
 *
 * A published route family and published price do not make every resource
 * in that family active.
 */
function isEnrichedFamily(pathname: string): boolean {
  return (
    pathname.startsWith("/v1/query/enriched/") ||
    pathname.startsWith("/x402/query/enriched/")
  );
}

function isAtomicFamily(pathname: string): boolean {
  return (
    pathname.startsWith("/v1/query/atomic/") ||
    pathname.startsWith("/x402/query/atomic/")
  );
}

function isSinglePlateFamily(pathname: string): boolean {
  return pathname.startsWith("/v1/plates/item/");
}

function findProtectedResource(
  pathname: string
): ResourceRecord | undefined {
  return PROTECTED_RESOURCES.find((resource) =>
    resource.paths.includes(pathname)
  );
}

function jsonResponse(
  body: unknown,
  status: number,
  extraHeaders: Record<string, string> = {}
): Response {
  return new Response(
    JSON.stringify(body, null, 2),
    {
      status,
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "X-Reference-Only": "true",
        "X-Robbie-Governing-Authority": GOVERNING_AUTHORITY,
        "X-Robbie-Pricing-Version": "3.0.0",
        "X-Robbie-Pricing-Manifest": PRICING_MANIFEST,
        ...extraHeaders
      }
    }
  );
}

function unknownResourceResponse(
  pathname: string,
  accessClass?: AccessClass
): Response {
  return jsonResponse(
    {
      status: "reference-only",
      enforcement: false,
      error: "Protected resource not registered",
      code: "RESOURCE_NOT_FOUND",
      route: pathname,
      accessClass: accessClass ?? null,
      paymentRequired: false,

      productionRule:
        "Unknown protected resources return HTTP 404 without a payment challenge.",

      interpretation:
        "A route template, URL prefix, pricing tier, or architecture label does not establish that a sellable resource exists."
    },
    404
  );
}

function incompleteResourceResponse(
  resource: ResourceRecord,
  pathname: string
): Response {
  return jsonResponse(
    {
      status: "reference-only",
      enforcement: false,
      error: "Protected payload not registered as complete",
      code: "PAYLOAD_NOT_REGISTERED",
      route: pathname,
      resourceId: resource.id,
      canonicalAuthority: resource.canonicalAuthority,
      accessClass: resource.accessClass,
      resourceState: resource.state,
      paymentRequired: false,

      productionRule:
        "Known but incomplete protected resources return HTTP 409 without a payment challenge."
    },
    409
  );
}

function registeredReferenceResponse(
  resource: ResourceRecord,
  pathname: string
): Response {
  const tier = PRICING[resource.accessClass];

  /**
   * 501 is intentional.
   *
   * This file does not implement a real x402 challenge, payment verification,
   * settlement, or protected payload delivery.
   */
  return jsonResponse(
    {
      status: "reference-only",
      enforcement: false,

      message:
        "This sample found an explicitly registered and complete protected resource. The production Worker may proceed to the real x402 challenge flow. This reference file intentionally stops before payment enforcement.",

      route: pathname,
      resourceId: resource.id,
      canonicalAuthority: resource.canonicalAuthority,
      resourceState: resource.state,

      pricingVersion: "3.0.0",
      pricingManifest: PRICING_MANIFEST,
      network: NETWORK,
      asset: ASSET,

      tier,

      schemaVersion:
        resource.schemaVersion ?? null,

      productionChallengeValidation:
        resource.productionChallengeValidation ?? null,

      referenceBehavior:
        "registered-complete resource → production system may become eligible for 402",

      rightsScope:
        "One endpoint-level retrieval only; no training, embedding, bulk ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, or framework implementation rights.",

      evidenceBoundary: [
        "resource registration does not establish empirical validation",
        "402 challenge does not equal settlement",
        "settlement does not transfer authorship",
        "payment does not grant broader commercial or framework rights"
      ]
    },
    501
  );
}

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    if (request.method !== "GET") {
      return jsonResponse(
        {
          error: "method_not_allowed",
          allowedMethods: ["GET"]
        },
        405,
        {
          allow: "GET"
        }
      );
    }

    /**
     * Public control plane.
     *
     * A real production implementation would return the actual public
     * resource here.
     *
     * This example simply passes the request through.
     */
    if (PUBLIC_CONTROL_PLANE.has(url.pathname)) {
      return fetch(request);
    }

    /**
     * Explicit resource lookup occurs BEFORE pricing.
     */
    const resource = findProtectedResource(url.pathname);

    if (resource) {
      if (resource.state === "known-incomplete") {
        return incompleteResourceResponse(
          resource,
          url.pathname
        );
      }

      if (resource.state === "registered-complete") {
        return registeredReferenceResponse(
          resource,
          url.pathname
        );
      }
    }

    /**
     * If the request clearly targets a protected route family but no
     * explicit resource record exists, fail closed with 404.
     */
    if (isAtomicFamily(url.pathname)) {
      return unknownResourceResponse(
        url.pathname,
        "atomic"
      );
    }

    if (isEnrichedFamily(url.pathname)) {
      return unknownResourceResponse(
        url.pathname,
        "enriched"
      );
    }

    if (isSinglePlateFamily(url.pathname)) {
      return unknownResourceResponse(
        url.pathname,
        "single-plate"
      );
    }

    /**
     * IMPORTANT:
     *
     * We intentionally DO NOT use rules such as:
     *
     *   /x402/knowledge-mesh/* → snapshot
     *   /v1/taxonomy/*        → subtree
     *   /api/v2/rrip/*        → snapshot
     *
     * because a URL prefix does not prove that a protected product exists.
     *
     * $5 and $25 remain pricing classes whose individual resources must be
     * explicitly registered.
     */

    return fetch(request);
  }
};
