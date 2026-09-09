import { McpServer } from "@modelcontextprotocol/server";
import { z } from "zod";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { stripTypeScriptTypes } from "node:module";
import { test } from "node:test";
import { runInNewContext } from "node:vm";

// Run from mcp-server with:
// node --test scripts/test-catalog-validation.mjs
// Requires Node.js 22.13 or newer, including the repository's Node 22 CI.
// The first section isolates the loader; the second tests MCP SDK tool replies.
// Neither section tests the Cloudflare HTTP wrapper or a deployment.
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

// SDK-level regression tests. The original 51 isolated loader tests above remain.
// These exercise the actual createServer function and the installed MCP SDK over
// an in-process JSON-RPC transport. Catalog HTTP responses are simulated.
// They do not test the Cloudflare HTTP wrapper, a deployed endpoint, or payments.

const serverStart = source.indexOf("const SITE_ORIGIN =");
const serverEnd = source.indexOf("\nconst mcpHandler =", serverStart);
assert.ok(serverStart >= 0, "Cannot locate server constants in src/index.ts");
assert.ok(serverEnd > serverStart, "Cannot locate MCP HTTP-wrapper boundary");
const serverJavaScript = stripTypeScriptTypes(source.slice(serverStart, serverEnd));

async function sdkHarness(t, body, options = {}) {
  let fetchCount = 0;
  const createServer = runInNewContext(serverJavaScript + "\ncreateServer;", {
    McpServer,
    z,
    // Use the host Error classes so SDK instanceof checks match production.
    Error,
    SyntaxError,
    fetch: async (url, init) => {
      assert.equal(url, catalogUrl, "Unexpected upstream URL");
      const headers = new Headers(init?.headers);
      for (const name of ["authorization", "x-payment", "payment-signature"]) {
        assert.equal(headers.has(name), false, "Unexpected credential/payment header");
      }
      fetchCount += 1;
      if (options.networkError) throw new Error("Simulated network failure");
      const status = options.status ?? 200;
      return {
        ok: status >= 200 && status < 300,
        status,
        json: async () => {
          if (options.invalidJson) throw new SyntaxError("Simulated invalid JSON");
          return structuredClone(body);
        },
      };
    },
  }, { timeout: 1000 });

  const server = createServer();
  const pending = new Map();
  let nextId = 0;
  let closed = false;

  // Implement the public MCP Transport contract without opening a socket.
  const transport = {
    async start() {},
    async send(message) {
      const waiter = pending.get(message.id);
      if (!waiter) return; // Ignore server notifications.
      if ("method" in message) {
        throw new Error("This test does not support server-initiated requests");
      }
      pending.delete(message.id);
      clearTimeout(waiter.timer);
      waiter.resolve(JSON.parse(JSON.stringify(message)));
    },
    async close() {
      if (closed) return;
      closed = true;
      for (const waiter of pending.values()) {
        clearTimeout(waiter.timer);
        waiter.reject(new Error("MCP test transport closed before reply"));
      }
      pending.clear();
      transport.onclose?.();
    },
  };
  t.after(async () => { await server.close(); });
  await server.connect(transport);

  function request(method, params) {
    assert.equal(closed, false, "MCP test transport is closed");
    assert.equal(typeof transport.onmessage, "function", "SDK did not attach a receiver");
    return new Promise((resolve, reject) => {
      const id = ++nextId;
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error("Timed out waiting for MCP reply to " + method));
      }, 5000);
      pending.set(id, { resolve, reject, timer });
      try {
        transport.onmessage({ jsonrpc: "2.0", id, method, params });
      } catch (error) {
        pending.delete(id);
        clearTimeout(timer);
        reject(error);
      }
    });
  }

  const initialized = await request("initialize", {
    protocolVersion: "2025-11-25",
    capabilities: {},
    clientInfo: { name: "naturepedia-catalog-ci-test", version: "0.0.0" },
  });
  assert.equal(initialized.error, undefined, "MCP initialization failed");
  assert.ok(initialized.result?.capabilities?.tools, "MCP tools capability missing");
  transport.onmessage({ jsonrpc: "2.0", method: "notifications/initialized" });

  return {
    get fetchCount() { return fetchCount; },
    async call(name, args) {
      const reply = await request("tools/call", { name, arguments: args });
      assert.equal(reply.error, undefined,
        "A catalog failure must be a tool result, not a JSON-RPC protocol error");
      assert.ok(reply.result, "MCP reply has no tool result");
      return reply.result;
    },
  };
}

function toolText(result) {
  assert.ok(Array.isArray(result.content), "Tool result content must be an array");
  const text = result.content.filter((entry) => entry.type === "text")
    .map((entry) => entry.text).join("\n");
  assert.ok(text.length > 0, "Tool result must contain useful text");
  return text;
}

const sdkTools = [
  { name: "search_naturepedia", args: { query: "Naturepedia", maxResults: 8 },
    miss: { query: "ci-723-no-such-catalog-resource", maxResults: 8 }, search: true },
  { name: "resolve_naturepedia_resource", args: { identifier: "naturepedia" },
    miss: { identifier: "ci-723-no-such-catalog-resource" }, search: false },
];

for (const tool of sdkTools) {
  test("SDK " + tool.name + ": successful match preserves metadata", async (t) => {
    const h = await sdkHarness(t, { catalog: { items: [item] } });
    const result = await h.call(tool.name, tool.args);
    assert.notEqual(result.isError, true);
    const data = JSON.parse(toolText(result));
    assert.equal(data.canonicalSource, catalogUrl);
    if (tool.search) {
      assert.equal(data.resultCount, 1);
      assert.deepStrictEqual(data.results, [item]);
    } else {
      assert.equal(data.resolved, true);
      assert.deepStrictEqual(data.resource, item);
      assert.ok(data.rightsNotice.length > 0);
    }
    assert.equal(h.fetchCount, 1);
  });

  for (const empty of [false, true]) {
    test("SDK " + tool.name + ": " + (empty ? "valid empty catalog" : "valid no-match") +
      " is not an error", async (t) => {
      const h = await sdkHarness(t, { catalog: { items: empty ? [] : [item] } });
      const result = await h.call(tool.name, tool.miss);
      assert.notEqual(result.isError, true);
      const data = JSON.parse(toolText(result));
      if (tool.search) {
        assert.equal(data.resultCount, 0);
        assert.deepStrictEqual(data.results, []);
      } else {
        assert.equal(data.resolved, false);
        assert.equal("resource" in data, false);
      }
      assert.equal(h.fetchCount, 1);
    });
  }

  const failures = [
    { label: "missing catalog", body: {}, pattern: /AI catalog validation failed/ },
    { label: "invalid field", body: { catalog: { items: [{ name: 7 }] } },
      pattern: /name must be a string/ },
    { label: "invalid JSON", body: null, options: { invalidJson: true }, pattern: /invalid JSON/ },
    { label: "HTTP 503", body: null, options: { status: 503 }, pattern: /AI catalog returned HTTP 503/ },
    { label: "network failure", body: null, options: { networkError: true },
      pattern: /Simulated network failure/ },
  ];
  for (const failure of failures) {
    test("SDK " + tool.name + ": " + failure.label + " returns isError true", async (t) => {
      const h = await sdkHarness(t, failure.body, failure.options);
      const result = await h.call(tool.name, tool.args);
      assert.equal(result.isError, true, "Catalog failure was not marked as a tool error");
      assert.match(toolText(result), failure.pattern);
      assert.equal(h.fetchCount, 1);
    });
  }
}

test("SDK about_naturepedia remains independent of catalog availability", async (t) => {
  const h = await sdkHarness(t, null, { networkError: true });
  const result = await h.call("about_naturepedia", {});
  assert.notEqual(result.isError, true);
  const data = JSON.parse(toolText(result));
  assert.equal(data.authority, "GC-MRD-v2.0");
  assert.equal(data.pricing.paidMcpTools, false);
  assert.equal(h.fetchCount, 0);
});
