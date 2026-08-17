#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const PROTOCOL_ID = "RR-BRP-0.1.0";
const RESULTS_VERSION = "0.1.0";
const RELEASE_TAG = "benchmarks-v0.2.0";
const MEMORY_GATE_PATH = "benchmarks/benchmark_memory_gate_savings.py";
const MEMORY_GATE_SHA256 = "c584b675c2f0fca692105159d27f2281789859e55f75306940642efc32a1c938";
const EXPECTED_LIVE_CALLS = 72;
const MODELS = ["gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.6-sol"];
const CONDITIONS = ["API-C0", "API-R1"];
const AUTHORIZATION_PATH = "results/v0.1.0/RUN_AUTHORIZATION.json";

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
  if (result.status !== 0) {
    fail(
      `${command} ${args.join(" ")} failed with exit code ${result.status}\n` +
      (result.stderr || result.stdout)
    );
  }

  return result;
}

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch (error) {
    fail(`Unable to read ${filePath}: ${error.message}`);
  }
}

function writeJson(filePath, value) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function parseArgs(argv) {
  const index = argv.indexOf("--run-dir");
  if (index === -1 || !argv[index + 1]) {
    fail("Usage: node finalize_partial_run.mjs --run-dir results/v0.1.0/runs/<run-id>");
  }

  const allowed = new Set(["--run-dir", argv[index + 1]]);
  const unknown = argv.filter(argument => !allowed.has(argument));
  if (unknown.length) fail(`Unknown argument(s): ${unknown.join(", ")}`);

  return { runDirectory: argv[index + 1] };
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

function verifyRunDirectory(runDirectory) {
  const expectedRoot = path.resolve("results/v0.1.0/runs");
  const resolvedRunDirectory = path.resolve(runDirectory);

  if (!resolvedRunDirectory.startsWith(`${expectedRoot}${path.sep}`)) {
    fail("Run directory must be below results/v0.1.0/runs.");
  }
  if (!fs.existsSync(resolvedRunDirectory) || !fs.statSync(resolvedRunDirectory).isDirectory()) {
    fail(`Run directory does not exist: ${runDirectory}`);
  }

  const runId = path.basename(resolvedRunDirectory);
  if (!/^rr-brp-0\.1\.0-[0-9TZ-]+$/.test(runId)) {
    fail(`Unexpected run identifier: ${runId}`);
  }

  return { resolvedRunDirectory, runId };
}

function toRepositoryPath(filePath) {
  const repositoryRoot = path.resolve(process.cwd());
  const resolvedPath = path.resolve(filePath);
  const relativePath = path.relative(repositoryRoot, resolvedPath);

  if (
    relativePath === ".." ||
    relativePath.startsWith(`..${path.sep}`) ||
    path.isAbsolute(relativePath)
  ) {
    fail(`Artifact path is outside the repository: ${filePath}`);
  }

  return relativePath.split(path.sep).join("/");
}

function verifyLiveArtifacts(runDirectory, runId) {
  const preflightPath = path.join(runDirectory, "preflight.json");
  const tracePath = path.join(runDirectory, "raw", "attempts.jsonl");
  const aggregatePath = path.join(runDirectory, "aggregate-summary.json");

  for (const requiredPath of [preflightPath, tracePath, aggregatePath, AUTHORIZATION_PATH]) {
    if (!fs.existsSync(requiredPath)) fail(`Missing required file: ${requiredPath}`);
  }

  const preflight = readJson(preflightPath);
  const authorization = readJson(AUTHORIZATION_PATH);
  const aggregateSummary = readJson(aggregatePath);
  const attempts = fs.readFileSync(tracePath, "utf8")
    .trim()
    .split(/\r?\n/)
    .filter(Boolean)
    .map((line, index) => {
      try {
        return JSON.parse(line);
      } catch (error) {
        fail(`Invalid JSON on trace line ${index + 1}: ${error.message}`);
      }
    });

  if (preflight.protocol !== PROTOCOL_ID || preflight.plannedLiveCalls !== EXPECTED_LIVE_CALLS) {
    fail("Preflight metadata does not match RR-BRP-0.1.0.");
  }
  if (authorization.protocol !== PROTOCOL_ID || authorization.executionAuthorized !== true) {
    fail("Run authorization is missing or invalid.");
  }
  if (aggregateSummary.protocol !== PROTOCOL_ID || aggregateSummary.aggregates?.length !== 6) {
    fail("Aggregate summary is missing the six preregistered model-condition groups.");
  }

  const successfulBySequence = new Map();
  for (const record of attempts) {
    const succeeded =
      Number.isInteger(record.sequence) &&
      record.httpStatus >= 200 &&
      record.httpStatus < 300 &&
      record.error === null;

    if (succeeded) successfulBySequence.set(record.sequence, record);
  }

  const missingSequences = [];
  for (let sequence = 1; sequence <= EXPECTED_LIVE_CALLS; sequence += 1) {
    if (!successfulBySequence.has(sequence)) missingSequences.push(sequence);
  }

  if (missingSequences.length) {
    fail(`Missing successful live sequences: ${missingSequences.join(", ")}`);
  }
  if ([...successfulBySequence.values()].some(record => record.runId !== runId)) {
    fail("One or more successful records reference a different run ID.");
  }

  return {
    preflight,
    authorization,
    aggregateSummary,
    attemptCount: attempts.length,
    completedLiveCalls: successfulBySequence.size
  };
}

function buildEvaluationReports(runDirectory) {
  const reports = [];

  for (const model of MODELS) {
    for (const conditionId of CONDITIONS) {
      for (const repetition of [1, 2, 3]) {
        const stem = `${model.replace(/[^A-Za-z0-9._-]/g, "_")}__${conditionId}__r${repetition}`;
        const outputsPath = path.join(runDirectory, "evaluations", `${stem}.outputs.json`);
        const reportPath = path.join(runDirectory, "evaluations", `${stem}.report.json`);
        const stdoutPath = path.join(runDirectory, "evaluations", `${stem}.stdout.txt`);

        for (const requiredPath of [outputsPath, reportPath, stdoutPath]) {
          if (!fs.existsSync(requiredPath)) fail(`Missing evaluation artifact: ${requiredPath}`);
        }

        reports.push({ model, conditionId, repetition, outputsPath, reportPath, stdoutPath });
      }
    }
  }

  return reports;
}

function executeSyntheticRecovery(runDirectory) {
  const outputDirectory = path.join(runDirectory, "synthetic-memory-gate");
  const stdoutPath = path.join(outputDirectory, "stdout.txt");
  const resultPath = path.join(outputDirectory, "result.json");

  if (fs.existsSync(resultPath) || fs.existsSync(stdoutPath)) {
    fail("Synthetic recovery output already exists; refusing to overwrite it.");
  }

  const taggedContent = run("git", ["show", `${RELEASE_TAG}:${MEMORY_GATE_PATH}`]).stdout;
  const actualHash = sha256(taggedContent);
  if (actualHash !== MEMORY_GATE_SHA256) {
    fail(`Synthetic benchmark hash mismatch: expected ${MEMORY_GATE_SHA256}, received ${actualHash}`);
  }

  const temporaryDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "rr-brp-0.1.0-recovery-"));
  const archivePath = path.join(temporaryDirectory, "benchmark.tar");
  const checkoutPath = path.join(temporaryDirectory, "checkout");
  fs.mkdirSync(checkoutPath, { recursive: true });

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

  try {
    run("git", ["archive", "--format=tar", `--output=${archivePath}`, RELEASE_TAG]);
    run("tar", ["-xf", archivePath, "-C", checkoutPath]);

    const result = run("python3", args, {
      cwd: checkoutPath,
      env: { ...process.env, PYTHONPATH: checkoutPath }
    });

    fs.mkdirSync(outputDirectory, { recursive: true });
    fs.writeFileSync(stdoutPath, result.stdout, "utf8");
    writeJson(resultPath, {
      evidenceClassification: "synthetic-proxy",
      benchmarkRelease: RELEASE_TAG,
      command: ["python3", ...args],
      environmentCorrection: {
        PYTHONPATH: "<temporary-tagged-checkout-root>",
        purpose: "Resolve the tagged repository's src package without changing benchmark inputs or logic."
      },
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

    return { stdoutPath, resultPath, stdoutSha256: sha256(result.stdout) };
  } finally {
    fs.rmSync(temporaryDirectory, { recursive: true, force: true });
  }
}

function main() {
  const { runDirectory: suppliedRunDirectory } = parseArgs(process.argv.slice(2));
  const { resolvedRunDirectory: runDirectory, runId } =
    verifyRunDirectory(suppliedRunDirectory);

  const manifestPath = path.join(runDirectory, "run-manifest.json");
  const deviationLogPath = path.join(runDirectory, "deviations", "deviation-log.json");
  if (fs.existsSync(manifestPath)) {
    fail("Run manifest already exists; refusing to finalize the run twice.");
  }
  if (fs.existsSync(deviationLogPath)) {
    fail("Deviation log already exists; refusing to overwrite it.");
  }

  const verified = verifyLiveArtifacts(runDirectory, runId);
  const evaluationReports = buildEvaluationReports(runDirectory);
  const synthetic = executeSyntheticRecovery(runDirectory);
  const portableEvaluationReports = evaluationReports.map(report => ({
    ...report,
    outputsPath: toRepositoryPath(report.outputsPath),
    reportPath: toRepositoryPath(report.reportPath),
    stdoutPath: toRepositoryPath(report.stdoutPath)
  }));
  const finalizerCommit = run("git", ["rev-parse", "HEAD"]).stdout.trim();
  const completedAt = new Date().toISOString();

  writeJson(deviationLogPath, {
    protocol: PROTOCOL_ID,
    resultsVersion: RESULTS_VERSION,
    runId,
    deviations: [
      {
        deviationId: "RR-BRP-0.1.0-DEV-001",
        date: completedAt.slice(0, 10),
        affectedRunIds: [runId],
        stage: "synthetic-memory-gate",
        description:
          "The initial synthetic-memory-gate invocation stopped after all 72 live API sequences and their evaluations completed.",
        reason:
          "The tagged benchmark imported src.razor.memory_bank, but the temporary tagged checkout root was not present on Python's module search path, producing ModuleNotFoundError: No module named 'src'.",
        expectedEffect:
          "No effect on the 72 completed live API records, model outputs, evaluation reports, or aggregate live-model summary. The synthetic proxy track is separate from live-model evidence.",
        correctiveAction:
          "Executed only the unchanged tagged synthetic benchmark with PYTHONPATH set to the temporary tagged checkout root, then generated the missing synthetic record and run manifest.",
        rerunsPerformed: false,
        liveModelRequestsRepeated: false,
        syntheticTrackRecovered: true,
        affectedObservationsRemainIncluded: true,
        evidenceClassification: "documented-protocol-deviation"
      }
    ]
  });

  writeJson(manifestPath, {
    protocol: PROTOCOL_ID,
    resultsVersion: RESULTS_VERSION,
    evidenceClassification: "first-party-bounded-evaluation",
    runId,
    initialRunStartedAt: verified.preflight.generatedAt,
    completedAt,
    benchmarkRelease: RELEASE_TAG,
    benchmarkDoi: verified.preflight.benchmarkDoi,
    runnerCommit: verified.preflight.repository.checkoutCommit,
    frozenProtocolCommit: verified.authorization.frozenProtocolCommit,
    finalizerCommit,
    plannedLiveCalls: verified.preflight.plannedLiveCalls,
    rawAttemptCount: verified.attemptCount,
    completedLiveCalls: verified.completedLiveCalls,
    liveModelRequestsRepeatedDuringRecovery: false,
    evaluationReports: portableEvaluationReports,
    aggregateSummaryPath: toRepositoryPath(
      path.join(runDirectory, "aggregate-summary.json")
    ),
    aggregateGroupCount: verified.aggregateSummary.aggregates.length,
    syntheticTrack: {
      evidenceClassification: "synthetic-proxy",
      resultPath: toRepositoryPath(synthetic.resultPath),
      stdoutPath: toRepositoryPath(synthetic.stdoutPath),
      stdoutSha256: synthetic.stdoutSha256
    },
    deviationLogPath: toRepositoryPath(deviationLogPath),
    deviationsRecorded: ["RR-BRP-0.1.0-DEV-001"],
    evidenceBoundary:
      "These results apply only to the recorded models, cases, conditions, repetitions, configurations, dates, and environment. They do not establish independent validation, universal validity, model certification, or guaranteed computational savings."
  });

  console.log(JSON.stringify({
    status: "finalized-after-documented-synthetic-stage-recovery",
    runId,
    completedLiveCalls: verified.completedLiveCalls,
    liveModelRequestsRepeated: false,
    syntheticResult: synthetic.resultPath,
    deviationLog: deviationLogPath,
    runManifest: manifestPath
  }, null, 2));
}

try {
  main();
} catch (error) {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
}
