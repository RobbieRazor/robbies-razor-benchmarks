import { McpServer } from "@modelcontextprotocol/server";
import { createMcpHandler } from "agents/mcp/server";
import { z } from "zod";

const SITE_ORIGIN = "https://www.robbiegeorgephotography.com";
const AI_CATALOG_URL = `${SITE_ORIGIN}/.well-known/ai-catalog.json`;
const PRICING_MANIFEST_URL =
  `${SITE_ORIGIN}/.well-known/x402-pricing.json`;

type CatalogItem = {
  id?: string;
  identifier?: string;
  slug?: string;
  type?: string;
  mediaType?: string;
  name?: string;
  description?: string;
  url?: string;
  alternateUrl?: string;
  requiresPayment?: boolean;
  paymentProtocol?: string;
  network?: string;
  asset?: string;
  price?: string;
};

async function loadCatalog(): Promise<CatalogItem[]> {
  const response = await fetch(AI_CATALOG_URL, {
    headers: {
      Accept: "application/json",
      "User-Agent": "Naturepedia-MCP/0.1.2",
    },
  });

  if (!response.ok) {
    throw new Error(`AI catalog returned HTTP ${response.status}`);
  }

  const body = (await response.json()) as {
    catalog?: { items?: CatalogItem[] };
  };

  return Array.isArray(body.catalog?.items) ? body.catalog.items : [];
}

function normalize(value: unknown): string {
  return String(value ?? "").trim().toLowerCase();
}

function createServer() {
  const server = new McpServer({
    name: "Naturepedia Canonical Discovery",
    version: "0.1.2",
  });

  server.registerTool(
    "about_naturepedia",
    {
      description:
        "Describe Naturepedia, its canonical authority structure, and its machine-readable discovery and x402 access layers.",
      inputSchema: {},
    },
    async () => ({
      content: [
        {
          type: "text" as const,
          text: JSON.stringify(
            {
              name: "Naturepedia",
              publisher: "Robbie George Photography",
              creator: "Robbie George",
              homepage: `${SITE_ORIGIN}/naturepedia`,
              discoveryCatalog: AI_CATALOG_URL,
              authority: "GC-MRD-v2.0",
              benchmark: {
                name: "Robbie's Razor Benchmarks",
                version: "0.2.0",
                releaseTag: "benchmarks-v0.2.0",
                canonicalPage:
                  `${SITE_ORIGIN}/robbies-razor-benchmarks`,
                release:
                  "https://github.com/RobbieRazor/robbies-razor-benchmarks/releases/tag/benchmarks-v0.2.0",
                taggedCitation:
                  "https://github.com/RobbieRazor/robbies-razor-benchmarks/blob/benchmarks-v0.2.0/CITATION.cff",
                canonicalPublicationManifest:
                  `${SITE_ORIGIN}/canonical-publication-manifest.json`,
                evidenceBoundary:
                  "MCP availability and benchmark metadata do not establish independent empirical validation, universal validity, or model certification.",
              },
              accessModel:
                "MCP discovery and resolution remain public and read-only. Separate protected machine-readable endpoints may require class-specific x402 payments.",
              pricing: {
                manifest: PRICING_MANIFEST_URL,
                version: "3.0.0",
                paymentProtocol: "x402",
                network: "eip155:8453",
                asset: "USDC",
                paidMcpTools: false,
              },
              governance:
                "An x402 payment grants one endpoint-level retrieval only. It does not grant training, embedding, bulk-ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, or framework-implementation rights.",
              commercialLicense:
                `${SITE_ORIGIN}/commercial-data-license`,
              frameworkLicense:
                `${SITE_ORIGIN}/robbies-razor-framework-licensing`,
            },
            null,
            2,
          ),
        },
      ],
    }),
  );

  server.registerTool(
    "search_naturepedia",
    {
      description:
        "Search the live Naturepedia AI catalog for canonical pages, registries, system maps, knowledge meshes, Robbie's Razor resources, and MRD authority records.",
      inputSchema: {
        query: z.string().min(2).max(200),
        maxResults: z.number().int().min(1).max(20).default(8),
      },
    },
    async ({ query, maxResults }) => {
      const terms = normalize(query).split(/\s+/).filter(Boolean);
      const items = await loadCatalog();

      const matches = items
        .map((item) => {
          const searchable = normalize([
            item.name,
            item.description,
            item.slug,
            item.identifier,
            item.id,
            item.type,
          ].join(" "));
          const score = terms.reduce(
            (total, term) => total + (searchable.includes(term) ? 1 : 0),
            0,
          );
          return { item, score };
        })
        .filter(({ score }) => score > 0)
        .sort((a, b) => b.score - a.score)
        .slice(0, maxResults)
        .map(({ item }) => item);

      return {
        content: [
          {
            type: "text" as const,
            text: JSON.stringify(
              {
                query,
                resultCount: matches.length,
                canonicalSource: AI_CATALOG_URL,
                results: matches,
              },
              null,
              2,
            ),
          },
        ],
      };
    },
  );

  server.registerTool(
    "resolve_naturepedia_resource",
    {
      description:
        "Resolve an exact Naturepedia identifier, slug, URL, or catalog ID to its current canonical record and payment metadata.",
      inputSchema: {
        identifier: z.string().min(2).max(500),
      },
    },
    async ({ identifier }) => {
      const target = normalize(identifier).replace(/\/+$/, "");
      const items = await loadCatalog();

      const match = items.find((item) =>
        [item.id, item.identifier, item.slug, item.url, item.alternateUrl]
          .map((value) => normalize(value).replace(/\/+$/, ""))
          .includes(target),
      );

      return {
        content: [
          {
            type: "text" as const,
            text: JSON.stringify(
              match
                ? {
                    resolved: true,
                    canonicalSource: AI_CATALOG_URL,
                    resource: match,
                    rightsNotice:
                      "An x402 payment grants one endpoint-level retrieval only. It does not grant training, embedding, bulk-ingestion, redistribution, resale, synchronization, private-dataset construction, derivative-dataset creation, commercial implementation, or framework-implementation rights.",
                    pricingManifest: PRICING_MANIFEST_URL,
                    pricingVersion: "3.0.0",
                    commercialLicense:
                      `${SITE_ORIGIN}/commercial-data-license`,
                    frameworkLicense:
                      `${SITE_ORIGIN}/robbies-razor-framework-licensing`,
                  }
                : {
                    resolved: false,
                    identifier,
                    canonicalSource: AI_CATALOG_URL,
                  },
              null,
              2,
            ),
          },
        ],
      };
    },
  );

  return server;
}

const mcpHandler = createMcpHandler(createServer, {
  route: "/mcp",
  responseMode: "json",
  allowedHostnames: [
    "naturepedia-mcp.robbiengs.workers.dev",
    "mcp.robbiegeorgephotography.com",
  ],
  onerror(error) {
    console.error("naturepedia_mcp_error", {
      message: error.message,
      stack: error.stack,
    });
  },
});

export default {
  async fetch(request: Request, env: unknown, ctx: ExecutionContext) {
    const url = new URL(request.url);

    if (url.pathname === "/health") {
      return Response.json({
        ok: true,
        service: "naturepedia-mcp",
        version: "0.1.2",
        mcpEndpoint: `${url.origin}/mcp`,
      });
    }

    return mcpHandler(request, env, ctx);
  },
} satisfies ExportedHandler;
