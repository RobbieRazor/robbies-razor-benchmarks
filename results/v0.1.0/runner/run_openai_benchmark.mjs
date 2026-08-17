#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import { spawnSync } from "node:child_process";
import { performance } from "node:perf_hooks";

const PROTOCOL_ID = "RR-BRP-0.1.0";
const RESULTS_VERSION = "0.1.0";
const RELEASE_TAG = "benchmarks-v0.2.0";
const RELEASE_COMMIT = "a97c037a4509baee41f8ffa724f1d85e3e598421";
const BENCHMARK_DOI = "10.5281/zenodo.21969841";
const CASE_PATH = "benchmarks/cases/razor_eval_v0.json";
const EVALUATOR_PATH = "benchmarks/evaluator.py";
const MEMORY_GATE_PATH = "benchmarks/benchmark_memory_gate_savings.py";
const PROTOCOL_PATH = "results/v0.1.0/RESULTS_PROTOCOL.md";
const AUTHORIZATION_PATH = "results/v0.1.0/RUN_AUTHORIZATION.json";

const FROZEN_HASHES = Object.freeze({
  [CASE_PATH]: "e13fc7a5addb3c31c3d3f54c39fcb3171cf3a20cfc685e34ea44ecfbdebd1031",
  [EVALUATOR_PATH]: "d49569efc1b57a205f08d155b39b4faa1572bd0edcb9026ea9272a223ee0ad7c",
  [MEMORY_GATE_PATH]: "c584b675c2f0fca692105159d27f2281789859e55f75306940642efc32a1c938"
});

const MODELS = Object.freeze([
  "gpt-5.6-luna",
  "gpt-5.6-terra",
  "gpt-5.6-sol"
]);

const CONDITIONS = Object.freeze({
  "API-C0": null,
  "API-R1":
    "Apply this response discipline: preserve correctness and every explicit task constraint; eliminate explanation, repetition, and unsupported content; return only the shortest sufficient answer."
});

const REPETITION_ORDER = Object.freeze({
  1: ["API-C0", "API-R1"],
  2: ["API-R1", "API-C0"],
  3: ["API-C0", "API-R1"]
});

const MAX_OUTPUT_TOKENS = 64;
const MAX_RETRIES = 2;
const REQUEST_TIMEOUT_MS = 120_000;
const RETRYABLE_STATUSES = new Set([429, 500, 502, 503, 504]);

function fail(message) {
  throw new Error(message);
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: options.cwd || process.cwd(),
    encoding: "utf8",
    env: options.env || process.env,
    maxBuffer: 20 * 1024 * 1024
  });

  if (result.error) throw result.error;
  if (result.status !== 0 && !options.allowFailure) {
    fail(
      `${command} ${args.join(" ")} failed with exit code ${result.status}\n${result.stderr || result.stdout}`
    );
  }

  return result;
}

function git(args, options = {}) {
  return run("git", args, options).stdout.trim();
}

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function taggedFile(repositoryPath) {
  return run("git", ["show", `${RELEASE_TAG}:${repositoryPath}`]).stdout;
}

function jsonParse(value, label) {
  try {
    return JSON.parse(value);
  } catch (error) {
    fail(`Unable to parse ${label} as JSON: ${error.message}`);
  }
}

function ensureDirectory(directory) {
  fs.mkdirSync(directory, { recursive: true });
}

function writeJson(filePath, value) {
  ensureDirectory(path.dirname(filePath));
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function appendJsonLine(filePath, value) {
  ensureDirectory(path.dirname(filePath));
  fs.appendFileSync(filePath, `${JSON.stringify(value)}\n`, "utf8");
}

function utcRunId() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function extractText(payload) {
  return (payload?.output || [])
    .flatMap(item => item?.content || [])
    .filter(item => item?.type === "output_text")
    .map(item => item?.text || "")
    .join("");
}

function classifyRefusal(payload) {
  return (payload?.output || []).some(item =>
    (item?.content || []).some(content => content?.type === "refusal")
  );
}

function parseArgs(argv) {
  const execute = argv.includes("--execute");
  const dryRun = argv.includes("--dry-run") || !execute;
  const unknown = argv.filter(arg => !["--execute", "--dry-run"].includes(arg));

  if (unknown.length) fail(`Unknown argument(s): ${unknown.join(", ")}`);
  if (execute && argv.includes("--dry-run")) {
    fail("Choose either --dry-run or --execute, not both.");
  }

  return { execute, dryRun };
}

function buildPlan(cases) {
  const plan = [];

  for (const model of MODELS) {
    for (const benchmarkCase of cases) {
      for (const repetition of [1, 2, 3]) {
        for (const conditionId of REPETITION_ORDER[repetition]) {
          plan.push({
            sequence: plan.length + 1,
            model,
            caseId: benchmarkCase.id,
            repetition,
            conditionId
          });
        }
      }
    }
  }

  return plan;
}

function verifyFrozenArtifacts() {
  const resolvedCommit = git(["rev-parse", `${RELEASE_TAG}^{commit}`]);
  if (resolvedCommit !== RELEASE_COMMIT) {
    fail(`Release tag mismatch: expected ${RELEASE_COMMIT}, received ${resolvedCommit}`);
  }

  const artifacts = {};
  for (const [repositoryPath, expectedHash] of Object.entries(FROZEN_HASHES)) {
    const content = taggedFile(repositoryPath);
    const actualHash = sha256(content);
    if (actualHash !== expectedHash) {
      fail(`Frozen hash mismatch for ${repositoryPath}: expected ${expectedHash}, received ${actualHash}`);
    }
    artifacts[repositoryPath] = { sha256: actualHash, verified: true };
  }

  return { resolvedCommit, artifacts };
}

function readAuthorizationForExecution() {
  if (!fs.existsSync(PROTOCOL_PATH)) fail(`Missing ${PROTOCOL_PATH}`);
  if (!fs.existsSync(AUTHORIZATION_PATH)) {
    fail(`Formal execution is blocked: missing ${AUTHORIZATION_PATH}`);
  }

  const protocol = fs.readFileSync(PROTOCOL_PATH, "utf8");
  const authorization = jsonParse(
    fs.readFileSync(AUTHORIZATION_PATH, "utf8"),
    AUTHORIZATION_PATH
  );

  if (!/Protocol status:\*\*\s*frozen-preregistered/i.test(protocol)) {
    fail("Formal execution is blocked: protocol status is not frozen-preregistered.");
  }
  if (!/Execution authorized:\*\*\s*Yes/i.test(protocol)) {
    fail("Formal execution is blocked: RESULTS_PROTOCOL.md does not authorize execution.");
  }
  if (authorization.protocol !== PROTOCOL_ID) {
    fail(`Authorization protocol must equal ${PROTOCOL_ID}.`);
  }
  if (authorization.executionAuthorized !== true) {
    fail("Formal execution is blocked by RUN_AUTHORIZATION.json.");
  }
  if (authorization.providerTermsReviewed !== true) {
    fail("Formal execution is blocked: provider terms review is not recorded.");
  }

  for (const field of ["approvedBudgetUsd", "projectedMaximumCostUsd"]) {
    if (!Number.isFinite(authorization[field]) || authorization[field] <= 0) {
      fail(`${field} must be a positive number.`);
    }
  }
  if (authorization.projectedMaximumCostUsd > authorization.approvedBudgetUsd) {
    fail("Projected maximum cost exceeds the approved budget ceiling.");
  }
  if (!/^[0-9a-f]{40}$/.test(authorization.frozenProtocolCommit || "")) {
    fail("Authorization must record the 40-character frozen protocol commit SHA.");
  }

  return authorization;
}

function repositoryState() {
  const status = git(["status", "--porcelain"]);
  return {
    checkoutCommit: git(["rev-parse", "HEAD"]),
    branch: git(["branch", "--show-current"]),
    dirty: status.length > 0,
    statusLines: status ? status.split("\n") : []
  };
}

function requestBodyFor(entry, benchmarkCase) {
  const body = {
    model: entry.model,
    input: benchmarkCase.prompt,
    reasoning: { effort: "none" },
    max_output_tokens: MAX_OUTPUT_TOKENS,
    stream: false,
    store: false
  };

  if (entry.conditionId === "API-R1") {
    body.instructions = CONDITIONS["API-R1"];
  }

  return body;
}

async function waitBeforeRetry(attemptNumber, retryAfterHeader) {
  const retryAfterSeconds = Number(retryAfterHeader);
  const delayMs = Number.isFinite(retryAfterSeconds)
    ? Math.max(0, retryAfterSeconds * 1000)
    : Math.min(30_000, 1000 * 2 ** (attemptNumber - 1));

  await new Promise(resolve => setTimeout(resolve, delayMs));
}

async function executeEntry({ entry, benchmarkCase, runId, runnerCommit, tracePath }) {
  const requestBody = requestBodyFor(entry, benchmarkCase);

  for (let attempt = 1; attempt <= MAX_RETRIES + 1; attempt += 1) {
    const startedAt = new Date().toISOString();
    const startedClock = performance.now();
    let response = null;
    let payload = null;
    let rawBody = "";
    let networkError = null;

    try {
      response = await fetch("https://api.openai.com/v1/responses", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify(requestBody),
        signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS)
      });
      rawBody = await response.text();
      if (rawBody) {
        try {
          payload = JSON.parse(rawBody);
        } catch (error) {
          payload = {
            parseError: error.message,
            rawResponseBody: rawBody
          };
        }
      }
    } catch (error) {
      networkError = {
        name: error?.name || "Error",
        message: error?.message || String(error)
      };
    }

    const completedAt = new Date().toISOString();
    const wallClockMs = Number((performance.now() - startedClock).toFixed(3));
    const httpStatus = response?.status ?? null;
    const record = {
      recordType: "openai-api-attempt",
      protocol: PROTOCOL_ID,
      resultsVersion: RESULTS_VERSION,
      benchmarkRelease: RELEASE_TAG,
      benchmarkDoi: BENCHMARK_DOI,
      runId,
      sequence: entry.sequence,
      conditionId: entry.conditionId,
      repetition: entry.repetition,
      caseId: entry.caseId,
      requestedModel: entry.model,
      returnedModel: payload?.model || null,
      startedAt,
      completedAt,
      wallClockMs,
      httpStatus,
      providerResponseId: payload?.id || null,
      providerRequestId: response?.headers?.get("x-request-id") || null,
      requestBody,
      responseBody: payload,
      visibleOutput: extractText(payload),
      refusalObserved: classifyRefusal(payload),
      usage: {
        inputTokens: payload?.usage?.input_tokens ?? null,
        cachedInputTokens: payload?.usage?.input_tokens_details?.cached_tokens ?? null,
        outputTokens: payload?.usage?.output_tokens ?? null,
        reasoningTokens: payload?.usage?.output_tokens_details?.reasoning_tokens ?? null,
        totalTokens: payload?.usage?.total_tokens ?? null
      },
      error: payload?.error || networkError,
      attempt,
      retryCount: attempt - 1,
      runnerCommit
    };

    appendJsonLine(tracePath, record);

    const retryable = networkError !== null || RETRYABLE_STATUSES.has(httpStatus);
    if (retryable && attempt <= MAX_RETRIES) {
      await waitBeforeRetry(attempt, response?.headers?.get("retry-after"));
      continue;
    }

    if (networkError || !response?.ok) {
      fail(
        `Request failed for sequence ${entry.sequence} after ${attempt} attempt(s); see ${tracePath}`
      );
    }

    return record;
  }

  fail(`Unreachable retry state for sequence ${entry.sequence}`);
}

function evaluateGroups({ casesContent, evaluatorContent, successfulRecords, runDirectory }) {
  const frozenDirectory = path.join(runDirectory, "frozen");
  const outputDirectory = path.join(runDirectory, "evaluations");
  ensureDirectory(frozenDirectory);
  ensureDirectory(outputDirectory);

  const casesPath = path.join(frozenDirectory, "razor_eval_v0.json");
  const evaluatorPath = path.join(frozenDirectory, "evaluator.py");
  fs.writeFileSync(casesPath, casesContent, "utf8");
  fs.writeFileSync(evaluatorPath, evaluatorContent, "utf8");

  const reports = [];
  for (const model of MODELS) {
    for (const conditionId of Object.keys(CONDITIONS)) {
      for (const repetition of [1, 2, 3]) {
        const group = successfulRecords.filter(
          record =>
            record.requestedModel === model &&
            record.conditionId === conditionId &&
            record.repetition === repetition
        );

        if (group.length !== 4) {
          fail(`Expected 4 completed records for ${model}/${conditionId}/r${repetition}; received ${group.length}`);
        }

        const safeModel = model.replace(/[^A-Za-z0-9._-]/g, "_");
        const stem = `${safeModel}__${conditionId}__r${repetition}`;
        const outputsPath = path.join(outputDirectory, `${stem}.outputs.json`);
        const reportPath = path.join(outputDirectory, `${stem}.report.json`);
        const stdoutPath = path.join(outputDirectory, `${stem}.stdout.txt`);
        const outputs = Object.fromEntries(group.map(record => [record.caseId, record.visibleOutput]));
        writeJson(outputsPath, outputs);

        const evaluation = run("python3", [
          evaluatorPath,
          "--cases",
          casesPath,
          "--outputs",
          outputsPath,
          "--model",
          model,
          "--report-out",
          reportPath
        ]);
        fs.writeFileSync(stdoutPath, evaluation.stdout, "utf8");
        reports.push({ model, conditionId, repetition, outputsPath, reportPath, stdoutPath });
      }
    }
  }

  return reports;
}

function mean(values) {
  return values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : null;
}

function median(values) {
  if (!values.length) return null;
  const ordered = [...values].sort((a, b) => a - b);
  const middle = Math.floor(ordered.length / 2);
  return ordered.length % 2
    ? ordered[middle]
    : (ordered[middle - 1] + ordered[middle]) / 2;
}

function populationStandardDeviation(values) {
  if (!values.length) return null;
  const average = mean(values);
  return Math.sqrt(mean(values.map(value => (value - average) ** 2)));
}

function describe(values) {
  const finite = values.filter(Number.isFinite);
  return {
    count: finite.length,
    minimum: finite.length ? Math.min(...finite) : null,
    maximum: finite.length ? Math.max(...finite) : null,
    mean: mean(finite),
    median: median(finite),
    populationStandardDeviation: populationStandardDeviation(finite),
    observedRange: finite.length ? Math.max(...finite) - Math.min(...finite) : null
  };
}

function buildAggregateSummary({ reports, successfulRecords, runDirectory }) {
  const aggregates = [];

  for (const model of MODELS) {
    for (const conditionId of Object.keys(CONDITIONS)) {
      const groupReports = reports
        .filter(report => report.model === model && report.conditionId === conditionId)
        .map(report => jsonParse(fs.readFileSync(report.reportPath, "utf8"), report.reportPath));
      const evaluatorResults = groupReports.flatMap(report => report.results || []);
      const raw = successfulRecords.filter(
        record => record.requestedModel === model && record.conditionId === conditionId
      );
      const correct = evaluatorResults.filter(result => result.correct);
      const overrunEligible = evaluatorResults.filter(result => result.target_max_tokens !== null);
      const overruns = overrunEligible.filter(
        result => result.tokens > result.target_max_tokens
      );
      const visibleTokens = evaluatorResults.map(result => result.tokens).filter(Number.isFinite);
      const correctTokens = correct.map(result => result.tokens).filter(Number.isFinite);
      const wallClock = raw.map(record => record.wallClockMs).filter(Number.isFinite);
      const providerInput = raw.map(record => record.usage.inputTokens).filter(Number.isFinite);
      const providerOutput = raw.map(record => record.usage.outputTokens).filter(Number.isFinite);
      const providerTotal = raw.map(record => record.usage.totalTokens).filter(Number.isFinite);
      const cachedInput = raw.map(record => record.usage.cachedInputTokens).filter(Number.isFinite);

      aggregates.push({
        model,
        conditionId,
        completedRequestCount: raw.length,
        errorCount: raw.filter(record => record.error !== null).length,
        refusalCount: raw.filter(record => record.refusalObserved).length,
        observationCount: evaluatorResults.length,
        correctAnswerCount: correct.length,
        accuracy: evaluatorResults.length ? correct.length / evaluatorResults.length : null,
        visibleOutputTokens: visibleTokens.reduce((sum, value) => sum + value, 0),
        tokensPerCorrectAnswer:
          correct.length
            ? correctTokens.reduce((sum, value) => sum + value, 0) / correct.length
            : null,
        expressionOverrunRate:
          overrunEligible.length ? overruns.length / overrunEligible.length : null,
        providerReportedUsage: {
          inputTokens: providerInput.reduce((sum, value) => sum + value, 0),
          outputTokens: providerOutput.reduce((sum, value) => sum + value, 0),
          totalTokens: providerTotal.reduce((sum, value) => sum + value, 0),
          cachedInputTokens: cachedInput.reduce((sum, value) => sum + value, 0)
        },
        descriptiveStatistics: {
          visibleOutputTokensPerObservation: describe(visibleTokens),
          wallClockMsPerRequest: describe(wallClock),
          providerInputTokensPerRequest: describe(providerInput),
          providerOutputTokensPerRequest: describe(providerOutput),
          providerTotalTokensPerRequest: describe(providerTotal)
        }
      });
    }
  }

  const summary = {
    protocol: PROTOCOL_ID,
    resultsVersion: RESULTS_VERSION,
    evidenceClassification: "first-party-bounded-evaluation",
    generatedAt: new Date().toISOString(),
    aggregationMethod:
      "Descriptive aggregation across 3 repetitions and 4 frozen cases for each named model and condition.",
    aggregates,
    evidenceBoundary:
      "These descriptive results apply only to the recorded models, cases, conditions, repetitions, configurations, dates, and environment."
  };
  writeJson(path.join(runDirectory, "aggregate-summary.json"), summary);
  return summary;
}

function parseMemoryGateOutput(stdout) {
  const captureNumber = label => {
    const match = stdout.match(new RegExp(`${label}:\\s+([0-9.]+%?)`));
    return match ? match[1] : null;
  };

  return {
    totalQueries: captureNumber("Total queries"),
    uniqueQueries: captureNumber("Unique queries"),
    memoryCapacity: captureNumber("Memory capacity"),
    stabilityThreshold: captureNumber("Stability threshold"),
    baselineInferences: captureNumber("Baseline inferences"),
    razorInferences: captureNumber("Razor inferences"),
    inferencesAvoided: captureNumber("Inferences avoided"),
    memoryHits: captureNumber("Memory hits"),
    memoryHitRate: captureNumber("Memory hit rate"),
    assumedTokensPerInference: captureNumber("Assumed tokens/inference"),
    baselineTokens: captureNumber("Baseline tokens"),
    razorTokens: captureNumber("Razor tokens"),
    tokenSavings: captureNumber("Token savings"),
    assumedMsPerInference: captureNumber("Assumed ms/inference"),
    baselineMs: captureNumber("Baseline latency \\(ms\\)"),
    razorMs: captureNumber("Razor latency \\(ms\\)"),
    latencySavingsMs: captureNumber("Latency savings \\(ms\\)")
  };
}

function runSyntheticMemoryGate(runDirectory) {
  const temporaryDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "rr-brp-0.1.0-"));
  const archivePath = path.join(temporaryDirectory, "benchmark.tar");
  const checkoutPath = path.join(temporaryDirectory, "checkout");
  ensureDirectory(checkoutPath);

  try {
    run("git", ["archive", "--format=tar", `--output=${archivePath}`, RELEASE_TAG]);
    run("tar", ["-xf", archivePath, "-C", checkoutPath]);

    const args = [
      MEMORY_GATE_PATH,
      "--total-queries", "1000",
      "--unique-queries", "200",
      "--capacity", "10000",
      "--threshold", "0.95",
      "--tokens-per-inference", "800",
      "--ms-per-inference", "600",
      "--seed", "123"
    ];
    const result = run("python3", args, { cwd: checkoutPath });
    const outputDirectory = path.join(runDirectory, "synthetic-memory-gate");
    ensureDirectory(outputDirectory);
    fs.writeFileSync(path.join(outputDirectory, "stdout.txt"), result.stdout, "utf8");
    writeJson(path.join(outputDirectory, "result.json"), {
      evidenceClassification: "synthetic-proxy",
      benchmarkRelease: RELEASE_TAG,
      command: ["python3", ...args],
      parameters: {
        totalQueries: 1000,
        uniqueQueries: 200,
        memoryCapacity: 10000,
        stabilityThreshold: 0.95,
        assumedTokensPerInference: 800,
        assumedMsPerInference: 600,
        seed: 123
      },
      parsedOutput: parseMemoryGateOutput(result.stdout),
      stdoutSha256: sha256(result.stdout)
    });
  } finally {
    fs.rmSync(temporaryDirectory, { recursive: true, force: true });
  }
}

async function main() {
  const mode = parseArgs(process.argv.slice(2));
  const frozen = verifyFrozenArtifacts();
  const casesContent = taggedFile(CASE_PATH);
  const evaluatorContent = taggedFile(EVALUATOR_PATH);
  const cases = jsonParse(casesContent, `${RELEASE_TAG}:${CASE_PATH}`);
  const plan = buildPlan(cases);
  const repo = repositoryState();

  if (cases.length !== 4) fail(`Expected 4 frozen cases; received ${cases.length}`);
  if (plan.length !== 72) fail(`Expected 72 planned calls; received ${plan.length}`);

  const preflight = {
    protocol: PROTOCOL_ID,
    resultsVersion: RESULTS_VERSION,
    mode: mode.execute ? "execute" : "dry-run",
    generatedAt: new Date().toISOString(),
    benchmarkRelease: RELEASE_TAG,
    benchmarkDoi: BENCHMARK_DOI,
    releaseCommit: frozen.resolvedCommit,
    frozenArtifacts: frozen.artifacts,
    repository: repo,
    runtime: {
      node: process.version,
      platform: process.platform,
      architecture: process.arch,
      python: run("python3", ["--version"]).stdout.trim() || run("python3", ["--version"]).stderr.trim()
    },
    models: MODELS,
    conditions: Object.keys(CONDITIONS),
    caseCount: cases.length,
    repetitionCount: 3,
    plannedLiveCalls: plan.length,
    plan
  };

  if (mode.dryRun) {
    const previewPath = path.join(os.tmpdir(), "rr-brp-0.1.0-preflight-preview.json");
    writeJson(previewPath, preflight);
    console.log(`Dry-run preflight passed. No API requests were made.`);
    console.log(`Verified ${Object.keys(frozen.artifacts).length} frozen artifact hashes.`);
    console.log(`Planned live calls: ${plan.length}`);
    console.log(`Preview written to: ${previewPath}`);
    return;
  }

  if (!process.env.OPENAI_API_KEY) {
    fail("Formal execution is blocked: OPENAI_API_KEY is not loaded.");
  }
  if (repo.dirty) {
    fail(`Formal execution is blocked: working tree is not clean: ${repo.statusLines.join("; ")}`);
  }

  const authorization = readAuthorizationForExecution();
  const runId = `rr-brp-0.1.0-${utcRunId()}`;
  const runDirectory = path.join("results", "v0.1.0", "runs", runId);
  const tracePath = path.join(runDirectory, "raw", "attempts.jsonl");
  ensureDirectory(path.dirname(tracePath));
  writeJson(path.join(runDirectory, "preflight.json"), { ...preflight, authorization });

  const successfulRecords = [];
  for (const entry of plan) {
    const benchmarkCase = cases.find(item => item.id === entry.caseId);
    if (!benchmarkCase) fail(`Missing case ${entry.caseId}`);
    console.log(
      `[${entry.sequence}/${plan.length}] ${entry.model} ${entry.caseId} r${entry.repetition} ${entry.conditionId}`
    );
    const record = await executeEntry({
      entry,
      benchmarkCase,
      runId,
      runnerCommit: repo.checkoutCommit,
      tracePath
    });
    successfulRecords.push(record);
  }

  const reports = evaluateGroups({
    casesContent,
    evaluatorContent,
    successfulRecords,
    runDirectory
  });
  const aggregateSummary = buildAggregateSummary({
    reports,
    successfulRecords,
    runDirectory
  });
  runSyntheticMemoryGate(runDirectory);

  writeJson(path.join(runDirectory, "run-manifest.json"), {
    protocol: PROTOCOL_ID,
    resultsVersion: RESULTS_VERSION,
    evidenceClassification: "first-party-bounded-evaluation",
    runId,
    completedAt: new Date().toISOString(),
    benchmarkRelease: RELEASE_TAG,
    benchmarkDoi: BENCHMARK_DOI,
    runnerCommit: repo.checkoutCommit,
    frozenProtocolCommit: authorization.frozenProtocolCommit,
    plannedLiveCalls: plan.length,
    completedLiveCalls: successfulRecords.length,
    evaluationReports: reports,
    aggregateSummaryPath: path.join(runDirectory, "aggregate-summary.json"),
    aggregateGroupCount: aggregateSummary.aggregates.length,
    syntheticTrack: "synthetic-proxy",
    evidenceBoundary:
      "These results apply only to the recorded models, cases, conditions, repetitions, configurations, dates, and environment. They do not establish independent validation, universal validity, model certification, or guaranteed computational savings."
  });

  console.log(`Formal run completed: ${runDirectory}`);
}

main().catch(error => {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
});
