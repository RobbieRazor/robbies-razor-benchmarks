# Robbie's Razor Benchmark Results v0.1.0

## Preregistered Bounded Evaluation Protocol

**Protocol identifier:** RR-BRP-0.1.0
**Results package version:** 0.1.0
**Protocol status:** draft-preregistration
**Execution authorized:** No
**Date created:** 2026-08-16
**Author and evaluator:** Robbie George
**Governing authority:** GC-MRD-v2.0
**Benchmark release:** benchmarks-v0.2.0
**Benchmark software version:** 0.2.0
**Benchmark DOI:** 10.5281/zenodo.21969841
**Benchmark DOI URL:** https://doi.org/10.5281/zenodo.21969841
**Benchmark archive:** https://zenodo.org/records/21969841
**Repository:** https://github.com/RobbieRazor/robbies-razor-benchmarks
**Canonical benchmark page:** https://www.robbiegeorgephotography.com/robbies-razor-benchmarks
**Canonical Publication Manifest:** https://www.robbiegeorgephotography.com/canonical-publication-manifest.json

---

## 1. Purpose

This document preregisters the procedure for producing Robbie's Razor Benchmark Results v0.1.0.

The result package will evaluate named models under explicitly bounded, recorded, and reproducible conditions using Robbie's Razor Benchmarks v0.2.0.

The purpose is to create a transparent first-party empirical record containing:

* frozen benchmark inputs;
* documented model and runtime configurations;
* matched baseline conditions;
* observable execution traces;
* raw and derived metrics;
* failures and exclusions;
* protocol deviations;
* reproducibility metadata;
* evidence-state classifications; and
* bounded interpretations.

No model execution governed by this protocol may begin while the protocol status remains `draft-preregistration`.

---

## 2. Evidence Classification

The initial result package will carry the evidence classification:

```text
first-party-bounded-evaluation
```

This classification means:

* the benchmark author or maintainer conducted or directly supervised the evaluations;
* the tested conditions are explicitly documented;
* the results apply only to the tested benchmark version, models, configurations, inputs, dates, and environments;
* the package is intended to support inspection and reproduction; and
* the package is not independent third-party validation.

The following classifications must not be applied to this package unless supported by separately documented evidence:

```text
independent-validation
universal-validation
model-certification
production-certification
cross-domain-validation
scientific-consensus
```

---

## 3. Governing Evidence Boundary

This protocol and its resulting records may measure bounded performance involving compression, expression, memory, recursion, preserved reusable structure, predictive compression, recursive stability, and total computational cost.

Publication of a result package does not by itself establish:

* independent empirical validation;
* universal validity;
* model certification;
* scientific consensus;
* causal equivalence across domains;
* guaranteed reductions in computational cost;
* guaranteed improvements in model performance;
* production readiness;
* commercial fitness; or
* applicability outside the documented evaluation boundary.

All conclusions must remain limited to the named models, benchmark tasks, baselines, configurations, environments, execution dates, and recorded observations.

---

## 4. Frozen Benchmark Dependency

All evaluations in Result Package v0.1.0 must resolve to:

```text
Benchmark name: Robbie's Razor Benchmarks
Benchmark version: 0.2.0
Release tag: benchmarks-v0.2.0
DOI: 10.5281/zenodo.21969841
```

Before execution begins, the evaluator must record:

* the exact Git commit SHA associated with the tested release;
* the release URL;
* the Zenodo DOI;
* the archive URL;
* the local checkout SHA;
* the dependency-lock state;
* the checksum of the evaluated input package; and
* whether the local checkout contains uncommitted changes.

Evaluations performed against `main`, an untagged branch, or an unrecorded working tree must not be included as canonical v0.1.0 results.

---

## 5. Evaluation Questions

The package is designed to examine the following bounded questions:

1. Under the documented tasks, how consistently does each tested model preserve required structure through recursive operations?
2. How much reusable structure is retained, lost, distorted, or regenerated?
3. How do the tested conditions compare with the declared matched baselines?
4. What observable computational costs are associated with each tested condition?
5. Under what documented conditions do failures, instability, drift, or incomplete preservation occur?
6. Are the reported outcomes reproducible across repeated runs using the same recorded configuration?
7. Which observations are supported directly by execution records, and which interpretations remain provisional?

These questions do not preregister a preferred outcome.

Null, negative, failed, incomplete, and contradictory results must be preserved.

---

## 6. Target Model Matrix

Result Package 0.1 will evaluate one bounded OpenAI model family across three documented capability and cost tiers. Expanding the study to GPT-5.5, GPT-5.4, o3, other providers, or additional model families requires a separately declared protocol amendment or later result package.

| Provider | Model ID | Evaluation Role | API Discovery State | Inference Verification |
|---|---|---|---|---|
| OpenAI | `gpt-5.6-luna` | Cost-sensitive GPT-5.6 tier | Listed by the project’s `/v1/models` response on 2026-08-16 | Verified by Responses API diagnostic on 2026-08-16 (`HTTP 200`; returned model matched; output `OK`) |
| OpenAI | `gpt-5.6-terra` | Balanced GPT-5.6 tier | Listed by the project’s `/v1/models` response on 2026-08-16 | Verified by Responses API diagnostic on 2026-08-16 (`HTTP 200`; returned model matched; output `OK`) |
| OpenAI | `gpt-5.6-sol` | Frontier GPT-5.6 tier | Listed by the project’s `/v1/models` response on 2026-08-16 | Verified by Responses API diagnostic on 2026-08-16 (`HTTP 200`; returned model matched; output `OK`) |

### Model Resolution Rule

The exact model identifier submitted with every request MUST be preserved in the raw execution record. The execution timestamp, API endpoint, returned model identifier, reasoning configuration, token usage, request identifier when available, and provider-reported usage fields MUST also be recorded.

Availability through `/v1/models` confirms project-level discovery only. It does not by itself confirm successful inference, stable future availability, identical behavior across dates, or empirical performance.

### Initial Execution Order

The preregistered execution order is:

1. `gpt-5.6-luna`
2. `gpt-5.6-terra`
3. `gpt-5.6-sol`

A minimal access-verification request MUST succeed for each model before formal benchmark execution begins. Access-verification responses are diagnostics and MUST NOT be counted as benchmark results.

---

## 7. Baseline and Treatment Matrix

Result Package 0.1 contains two explicitly separated evidence tracks:

1. A live-model matched-pair evaluation using the versioned cases in `benchmarks/cases/razor_eval_v0.json`.
2. A deterministic synthetic memory-gate evaluation using `benchmarks/benchmark_memory_gate_savings.py`.

Synthetic proxy results MUST NOT be represented as observed model-performance results.

### 7.1 Live-Model Matched-Pair Conditions

| Condition ID | Condition | Definition | Purpose |
|---|---|---|---|
| `API-C0` | Direct-response control | Submit the original versioned case prompt without any Robbie’s Razor instruction wrapper. | Establish each model’s unmodified response behavior, correctness, expression length, and reported token usage. |
| `API-R1` | Razor-constrained treatment | Submit the identical case with the fixed response-discipline instruction defined below. | Measure whether bounded expression discipline changes correctness, output length, overrun rate, token use, or latency. |

The fixed `API-R1` instruction is:

> Apply this response discipline: preserve correctness and every explicit task constraint; eliminate explanation, repetition, and unsupported content; return only the shortest sufficient answer.

No other Robbie’s Razor explanatory material, examples, scoring criteria, acceptable answers, or expected outputs may be shown to the model.

### 7.2 Matched-Control Requirements

For every model and case, `API-C0` and `API-R1` MUST use:

- the same versioned case input;
- the same model identifier;
- the same API endpoint;
- `reasoning.effort: none`;
- the same maximum-output-token allowance;
- no tools, retrieval, web search, files, MCP calls, or external memory;
- no conversation history;
- `store: false`;
- independent requests;
- the same repetition count;
- the same evaluator and scoring rules; and
- the same execution environment wherever technically possible.

The treatment instruction is the only intentionally varied input.

The execution order within each model MUST alternate by repetition:

1. Repetition 1: `API-C0`, then `API-R1`
2. Repetition 2: `API-R1`, then `API-C0`
3. Repetition 3: `API-C0`, then `API-R1`

This alternation reduces—but does not eliminate—order and transient service effects.

### 7.3 Synthetic Memory-Gate Conditions

| Condition ID | Condition | Repository Definition | Evidence Classification |
|---|---|---|---|
| `SYN-C0` | Always-compute baseline | Every generated query incurs the configured assumed inference cost. | Synthetic proxy |
| `SYN-R1` | Razor memory-gate treatment | A qualifying memory hit bypasses the configured assumed inference cost. | Synthetic proxy |

The synthetic comparison MUST use the tagged `benchmarks-v0.2.0` implementation and record every command-line parameter, including:

- total queries;
- unique queries;
- memory capacity;
- stability threshold;
- assumed tokens per inference;
- assumed milliseconds per inference; and
- random seed.

Its token and latency values are configured assumptions, not provider-observed usage or elapsed inference measurements.

### 7.4 Excluded Adversarial Diagnostic

`baselines/cheating_agent.py` is an adversarial non-progress diagnostic. It is excluded from the primary aggregate comparison for Result Package 0.1 because it is not a matched live-model control.

If executed, its output MUST be stored under diagnostics and labeled:

`adversarial-synthetic-diagnostic`

It MUST NOT be counted as empirical support for efficiency, correctness, progress, or model performance.

---

## 8. Preregistered Run Configuration

### 8.1 Live API Evaluation

| Field | Preregistered Value |
|---|---|
| Provider | OpenAI |
| Endpoint | `POST https://api.openai.com/v1/responses` |
| Protocol | HTTPS JSON |
| Model order | `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol` |
| Case source | `benchmarks/cases/razor_eval_v0.json` from `benchmarks-v0.2.0` |
| Conditions | `API-C0` and `API-R1` |
| Repetitions | 3 independent requests per model, case, and condition |
| Reasoning effort | `none` |
| Maximum output tokens | `64` |
| Streaming | Disabled |
| Tools | None |
| External retrieval | None |
| Conversation history | None |
| Stored by provider | `store: false` |
| Temperature | Omitted; provider/model default |
| Top-p | Omitted; provider/model default |
| API request format | Responses API |
| Evaluator | Tagged `benchmarks/evaluator.py` |
| Live-model calls | 72 planned requests: 3 models × 4 cases × 2 conditions × 3 repetitions |

The control request MUST use the original case prompt as `input` and MUST omit the `instructions` field.

The treatment request MUST use the same original case prompt as `input` and the fixed `API-R1` text as `instructions`.

No acceptable answer, scoring mode, target answer, target token count, evaluator output, previous model response, or earlier repetition may be included in any model request.

### 8.2 Request Recording

For every API attempt, record:

- protocol identifier;
- benchmark release and DOI;
- condition identifier;
- repetition number;
- case identifier;
- requested model;
- returned model;
- UTC start and completion timestamps;
- measured wall-clock duration;
- HTTP status;
- provider response identifier;
- complete permitted request body with secrets removed;
- complete observable response body;
- visible output text;
- provider-reported input tokens;
- provider-reported cached input tokens;
- provider-reported output tokens;
- provider-reported reasoning tokens;
- provider-reported total tokens;
- error object when present;
- retry count; and
- runner commit SHA.

API keys, authorization headers, credentials, private account information, and hidden provider reasoning MUST NOT be recorded.

### 8.3 Retry Policy

A request may be retried only for:

- HTTP `429`;
- HTTP `500`, `502`, `503`, or `504`;
- connection failure; or
- client-side timeout.

A maximum of two retries is permitted after the initial attempt.

Every failed attempt MUST remain in the raw trace. A retry MUST retain the same model, condition, case, repetition number, request body, and configuration.

Incorrect answers, excessive output, formatting failures, refusals, or other completed model responses MUST NOT be retried.

### 8.4 Evaluation Rules

Correctness and visible-output token measures MUST be calculated using the tagged evaluator without manually editing model responses.

Provider-reported API usage MUST be preserved separately from evaluator-calculated visible-output tokens.

The following primary measures will be reported by model and condition:

- accuracy;
- correct-answer count;
- visible-output tokens;
- tokens per correct answer;
- expression-overrun rate;
- provider-reported input tokens;
- provider-reported output tokens;
- provider-reported total tokens;
- cached input tokens;
- wall-clock duration;
- completed-request count;
- error count; and
- refusal count when observable.

No metric may be removed solely because it is unfavorable, null, zero, or inconsistent with the expected direction.

### 8.5 Synthetic Memory-Gate Run

The synthetic memory-gate benchmark MUST be executed once with its tagged default configuration:

```text
total_queries=1000
unique_queries=200
memory_capacity=10000
stability_threshold=0.95
assumed_tokens_per_inference=800
assumed_ms_per_inference=600
seed=123
```
The exact command, stdout, environment information, and structured result MUST be archived.

These outputs MUST be labeled synthetic-proxy and reported separately from live OpenAI API measurements.

### 8.6 Abort Conditions

Formal execution MUST stop before additional requests are issued if:

the checked-out repository is not the frozen protocol commit;
the benchmark release cannot be resolved to benchmarks-v0.2.0;
the case file differs from its frozen checksum;
the API request configuration differs from this section;
a target model is unavailable;
output recording fails;
credential redaction cannot be assured; or
the projected account spend would exceed the declared package budget.

An aborted run may be resumed only after documenting the cause, corrective action, affected requests, and whether the correction changes the preregistered design.

### 8.7 Frozen Artifact Manifest

The following identifiers were resolved directly from the tagged Git repository before formal execution:

| Artifact | Frozen Identifier |
|---|---|
| Benchmark release tag | `benchmarks-v0.2.0` |
| Release commit | `a97c037a4509baee41f8ffa724f1d85e3e598421` |
| Release DOI | `10.5281/zenodo.21969841` |
| `benchmarks/cases/razor_eval_v0.json` | `sha256:e13fc7a5addb3c31c3d3f54c39fcb3171cf3a20cfc685e34ea44ecfbdebd1031` |
| `benchmarks/evaluator.py` | `sha256:d49569efc1b57a205f08d155b39b4faa1572bd0edcb9026ea9272a223ee0ad7c` |
| `benchmarks/benchmark_memory_gate_savings.py` | `sha256:c584b675c2f0fca692105159d27f2281789859e55f75306940642efc32a1c938` |

Before formal execution, the runner MUST independently recalculate these SHA-256 values from the tagged Git objects.

Any mismatch requires an immediate abort. Substituting a file from `main`, another branch, the working tree, or another release is prohibited unless documented through a new protocol version or preregistered amendment.

---

## 9. Repetition Requirements

Unless a condition is demonstrably deterministic, each model-task configuration must be executed a minimum of three times.

Each repeated run must receive a unique run identifier.

If only one execution is completed, the result must be classified as:

```text
single-observation
```

A single observation must not be described as demonstrating stability or reproducibility.

Deterministic status may be claimed only when:

* deterministic settings are documented;
* the provider or runtime supports deterministic execution;
* identical inputs and settings are used; and
* repeated verification produces identical observable outputs or hashes.

---

## 10. Observable Execution Record

Each canonical run should preserve, where permitted:

* the complete submitted request;
* all visible prompts and inputs;
* the complete visible response;
* structured output;
* visible tool calls;
* tool results;
* retrieval references;
* timestamps;
* HTTP or SDK status;
* token counts;
* latency;
* reported cost;
* warnings;
* errors;
* retries; and
* termination reason.

The package must not publish:

* API keys;
* authentication tokens;
* private credentials;
* personal information not required by the protocol;
* provider-private data;
* hidden chain-of-thought;
* private model reasoning;
* confidential prompts;
* copyrighted material that cannot be redistributed; or
* information prohibited from publication by applicable provider terms.

When content must be removed, the record must disclose that redaction occurred and state the reason.

A cryptographic hash may be retained for a nonpublic artifact when legally and operationally appropriate.

---

## 11. Metrics

All reported metrics must be traceable to raw observations.

The evaluation may report:

* task completion;
* output validity;
* structural preservation;
* reusable-structure preservation;
* recursive stability;
* transformation drift;
* compression-related measurements;
* predictive-compression measurements;
* baseline deltas;
* input tokens;
* output tokens;
* total tokens;
* execution latency;
* reported API cost;
* retry count;
* error count; and
* failure classification.

For every metric, the result package must identify:

* metric name;
* definition;
* unit;
* calculation method;
* source fields;
* missing-data treatment;
* aggregation method;
* direction of interpretation;
* limitations; and
* applicable benchmark cases.

No metric may be silently redefined after execution begins.

---

## 12. Statistical and Descriptive Reporting

Result Package v0.1.0 will prioritize descriptive reporting.

Where repeated runs exist, the package should report:

* number of valid runs;
* number of failed runs;
* minimum;
* maximum;
* mean;
* median;
* standard deviation, when meaningful; and
* observed range.

Inferential statistical claims must not be made unless their hypotheses, sample sizes, assumptions, and analysis procedures are preregistered before execution.

Small sample sizes must be disclosed.

The absence of a statistically significant difference must not be interpreted automatically as equivalence.

---

## 13. Failure and Missing-Data Policy

Failures are part of the empirical record and must not be silently removed.

Each failed or incomplete run must receive a classification such as:

```text
provider-error
timeout
rate-limit
invalid-output
schema-failure
tool-failure
retrieval-failure
context-limit
configuration-error
evaluator-error
unknown-failure
```

Missing data must be labeled explicitly.

A run may be excluded from an aggregate only when:

* the exclusion rule was preregistered; or
* a documented protocol deviation makes the run incomparable.

The original run record must remain preserved even when excluded from an aggregate.

---

## 14. Protocol Deviations

Any departure from this protocol must be recorded in a deviation log containing:

* deviation identifier;
* affected run IDs;
* date;
* description;
* reason;
* expected effect;
* corrective action;
* whether reruns were performed; and
* whether the affected observations remain included.

No deviation may be concealed by editing or overwriting the original execution record.

Material changes made after the first run require either:

* a new protocol version;
* a separately identified evaluation phase; or
* explicit classification as exploratory rather than preregistered.

---

## 15. Evidence States

Individual records and aggregate findings may use the following states:

```text
planned
executed
execution-failed
excluded-with-reason
first-party-observed
first-party-reproduced
submitted-unreviewed
under-review
partially-reproduced
maintainer-reproduced
not-reproduced
invalid-protocol-deviation
independently-reproduced
superseded
```

Evidence states must describe the record's review and reproduction status, not the importance of the result.

`Independently-reproduced` may be used only when an evaluator who is operationally independent of the original run reproduces the result under sufficiently comparable documented conditions.

---

## 16. Interpretation Rules

The final report must:

* distinguish raw observations from derived metrics;
* distinguish metrics from interpretations;
* distinguish first-party results from third-party reports;
* disclose material uncertainty;
* preserve failed and contrary results;
* identify model and provider limitations;
* avoid extrapolation beyond tested conditions;
* avoid universal rankings from bounded tasks;
* avoid claims of causal equivalence based only on structural similarity;
* avoid treating publication as validation; and
* preserve the governing evidence boundary.

A model may perform better under a named metric and tested condition without being described as universally superior.

---

## 17. Reproducibility Requirements

A reproduction attempt must identify:

* benchmark version;
* benchmark commit SHA;
* protocol version;
* result-package version;
* model provider;
* exact model identifier;
* runtime environment;
* configuration;
* inputs;
* run count;
* metric implementation;
* deviations;
* output hashes; and
* evaluator identity or declared anonymity status.

Reproduction requires sufficiently comparable conditions. Similarity of conclusions without comparable execution conditions is not sufficient.

---

## 18. Planned Package Structure

The published result package should use the following structure:

```text
results/v0.1.0/
├── RESULTS_PROTOCOL.md
├── README.md
├── results-manifest.json
├── model-matrix.json
├── baseline-matrix.json
├── environment.json
├── runs/
│   ├── requests/
│   ├── responses/
│   ├── traces/
│   └── errors/
├── metrics/
│   ├── raw/
│   └── derived/
├── summaries/
├── deviations/
│   └── deviation-log.json
└── checksums.sha256
```

Only files that contain no restricted credentials, private reasoning, prohibited content, or disallowed personal information may be published.

---

## 19. Publication Plan

After execution and review, the result package should be:

1. committed to a dedicated Git branch;
2. reviewed for completeness and disclosure;
3. merged through a pull request;
4. assigned the release tag `benchmark-results-v0.1.0`;
5. published as a distinct GitHub release;
6. archived as a separate Zenodo Dataset record;
7. assigned its own version-specific DOI;
8. related to benchmark software DOI `10.5281/zenodo.21969841`;
9. added to the Canonical Publication Manifest;
10. added to the MRD benchmark-evaluation record;
11. added to the AI Catalog;
12. added to `llms.txt` and `llms-full.txt`; and
13. exposed through the applicable MCP discovery metadata.

The results Dataset DOI must remain distinct from the benchmark Software DOI.

---

## 20. Change Control

Before the first run, this protocol may be amended while its status remains:

```text
draft-preregistration
```

Before execution begins, the final protocol must be committed and its status changed to:

```text
frozen-preregistered
```

The frozen protocol commit SHA must be recorded in the result manifest.

After the first run:

* material protocol changes require a new protocol version;
* minor clarifications must be logged;
* original records must not be overwritten;
* deviations must be disclosed; and
* exploratory analyses must be labeled separately.

---

## 21. Authorization Gates

Execution remains prohibited until all of the following are complete:

* [ ] Target model matrix completed
* [ ] Baseline matrix completed
* [ ] Benchmark commit SHA recorded
* [ ] Evaluation cases selected
* [ ] Run parameters frozen
* [ ] Repetition count confirmed
* [ ] Metrics and calculation methods confirmed
* [ ] Exclusion rules confirmed
* [ ] Trace-redaction policy confirmed
* [ ] Cost ceiling approved
* [ ] Provider terms reviewed
* [ ] Protocol status changed to `frozen-preregistered`
* [ ] Frozen protocol commit SHA recorded

---

## 22. Current Status

```text
Protocol status: draft-preregistration
Execution authorized: No
Canonical results published: No
Independent reproduction completed: No
Results DOI assigned: No
```

This document establishes the initial governance structure for Robbie's Razor Benchmark Results v0.1.0. It does not contain benchmark results and does not authorize execution until the required preregistration gates are completed.
