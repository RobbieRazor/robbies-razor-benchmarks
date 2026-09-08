import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { stripTypeScriptTypes } from "node:module";
import { test } from "node:test";
import { runInNewContext } from "node:vm";

// Run from mcp-server with:
// node --test scripts/test-catalog-validation.mjs
// Requires Node.js 22.13 or newer, including the repository's Node 22 CI.
// These are isolated loader tests, not an MCP transport or deployment test.
// All HTTP responses are simulated. No network calls or payments occur.

const source = readFileSync(new URL("../src/index.ts", import.meta.url), "utf8");
const startMarker = "async function loadCatalog(";
const endMarker = "\nfunction normalize(";
const start = source.indexOf(startMarker);
const end = source.indexOf(endMarker, start);

// Test the actual function, not a separately maintained copy of its logic.
// Fail explicitly if a refactor changes these extraction boundaries.
assert.ok(start >= 0, "Cannot locate loadCatalog in src/index.ts");
assert.ok(end > start, "Cannot locate the end of loadCatalog");
assert.equal(source.indexOf(startMarker, start + 1), -1, "Duplicate loadCatalog");
const loaderJavaScript = stripTypeScriptTypes(source.slice(start, end));
const catalogUrl = "https://www.robbiegeorgephotography.com/.well-known/ai-catalog.json";

function harness(body, options = {}) {
  const requests = [];
  let jsonCalls = 0;
  const load = runInNewContext(loaderJavaScript + "\nloadCatalog;", {
    AI_CATALOG_URL: catalogUrl,
    fetch: async (url, init) => {
      assert.equal(url, catalogUrl, "Unexpected upstream URL");
      requests.push({ url, init });
      if (options.networkError) throw new Error("Simulated network failure");
      const status = options.status ?? 200;
      return {
        ok: status >= 200 && status < 300,
        status,
        json: async () => {
          jsonCalls += 1;
          if (options.invalidJson) throw new SyntaxError("Simulated invalid JSON");
          return body;
        },
      };
    },
  }, { timeout: 1000 });
  return { load, requests, get jsonCalls() { return jsonCalls; } };
}

const item = {
  id: "urn:example:naturepedia",
  identifier: "Naturepedia\u2122",
  slug: "naturepedia",
  type: "text/html",
  mediaType: "text/html",
  name: "Naturepedia\u2122",
  description: "Fixture for catalog validation, not a production resource.",
  url: "https://example.com/naturepedia",
  alternateUrl: "https://example.com/naturepedia/",
  requiresPayment: true,
  paymentProtocol: "x402",
  network: "eip155:8453",
  asset: "USDC",
  price: "0.025",
  rightsExcluded: ["training", "bulk ingestion"],
  provenance: { authority: "test-only", sources: ["fixture"] },
};

test("valid empty catalog stays a successful empty result", async () => {
  const fixture = { catalog: { items: [] } };
  assert.strictEqual(await harness(fixture).load(), fixture.catalog.items);
});

test("valid records and all additional metadata are preserved without mutation", async () => {
  const fixture = { catalog: { items: [structuredClone(item)] } };
  const before = structuredClone(fixture);
  const result = await harness(fixture).load();
  assert.strictEqual(result, fixture.catalog.items);
  assert.deepStrictEqual(fixture, before);
  assert.equal(result[0].identifier, "Naturepedia\u2122");
});

test("optional fields remain optional", async () => {
  assert.deepStrictEqual(await harness({ catalog: { items: [{}] } }).load(), [{}]);
});

test("requiresPayment false remains a valid boolean", async () => {
  const result = await harness({ catalog: { items: [{ requiresPayment: false }] } }).load();
  assert.equal(result[0].requiresPayment, false);
});

test("request uses JSON accept header and performs only one fetch", async () => {
  const h = harness({ catalog: { items: [] } });
  await h.load();
  assert.equal(h.requests.length, 1);
  assert.equal(h.requests[0].init.headers.Accept, "application/json");
  assert.equal(h.jsonCalls, 1);
});

const malformedEnvelopes = [
  ["null root", null],
  ["array root", []],
  ["string root", "bad"],
  ["number root", 7],
  ["boolean root", false],
  ["missing catalog", {}],
  ["null catalog", { catalog: null }],
  ["array catalog", { catalog: [] }],
  ["string catalog", { catalog: "bad" }],
  ["number catalog", { catalog: 7 }],
  ["boolean catalog", { catalog: false }],
  ["missing items", { catalog: {} }],
  ["null items", { catalog: { items: null } }],
  ["object items", { catalog: { items: {} } }],
  ["string items", { catalog: { items: "bad" } }],
  ["number items", { catalog: { items: 7 } }],
  ["boolean items", { catalog: { items: false } }],
];
for (const [label, body] of malformedEnvelopes) {
  test("reject malformed envelope: " + label, async () => {
    await assert.rejects(harness(body).load(), /AI catalog validation failed/);
  });
}

for (const value of [null, [], "bad", 7, false]) {
  test("reject non-object record: " + JSON.stringify(value), async () => {
    await assert.rejects(
      harness({ catalog: { items: [value] } }).load(),
      /catalog\.items\[0\] must be an object/,
    );
  });
}

const stringFields = [
  "id", "identifier", "slug", "type", "mediaType", "name", "description",
  "url", "alternateUrl", "paymentProtocol", "network", "asset", "price",
];
for (const field of stringFields) {
  test("reject wrong type for " + field, async () => {
    const h = harness({ catalog: { items: [{ ...item, [field]: 7 }] } });
    await assert.rejects(h.load(), (error) => {
      assert.ok(error.message.includes("catalog.items[0]." + field));
      assert.ok(error.message.includes("must be a string when present"));
      return true;
    });
  });
}

for (const value of ["true", null, 0]) {
  test("reject non-boolean requiresPayment: " + JSON.stringify(value), async () => {
    await assert.rejects(
      harness({ catalog: { items: [{ requiresPayment: value }] } }).load(),
      /requiresPayment must be a boolean/,
    );
  });
}

test("one invalid record rejects the catalog instead of returning partial results", async () => {
  await assert.rejects(
    harness({ catalog: { items: [item, { name: null }] } }).load(),
    /catalog\.items\[1\]\.name must be a string/,
  );
});

test("invalid JSON rejects with an explicit error", async () => {
  await assert.rejects(harness(null, { invalidJson: true }).load(), /invalid JSON/);
});

for (const status of [400, 404, 429, 500, 503]) {
  test("HTTP " + status + " rejects before attempting JSON parsing", async () => {
    const h = harness({ catalog: { items: [] } }, { status });
    await assert.rejects(h.load(), new RegExp("AI catalog returned HTTP " + status));
    assert.equal(h.jsonCalls, 0);
    assert.equal(h.requests.length, 1);
  });
}

test("network failure rejects instead of returning an empty catalog", async () => {
  const h = harness(null, { networkError: true });
  await assert.rejects(h.load(), /Simulated network failure/);
  assert.equal(h.requests.length, 1);
});
