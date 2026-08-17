# Robbie's Razor Benchmark Results v0.1.0

## Bounded First-Party Evaluation Record

This directory contains the first preregistered result package produced under **RR-BRP-0.1.0** using **Robbie's Razor Benchmarks v0.2.0**.

These results are a **first-party bounded evaluation**. They apply only to the named models, frozen cases, conditions, repetitions, configurations, execution dates, and recorded environment. Publication does not establish independent validation, universal validity, model certification, production certification, or guaranteed computational savings.

## Record identity

| Field | Value |
|---|---|
| Result-package version | 0.1.0 |
| Protocol | RR-BRP-0.1.0 |
| Protocol status | Frozen and preregistered |
| Evidence classification | First-party bounded evaluation |
| Run ID | `rr-brp-0.1.0-2026-08-17T11-22-19-303Z` |
| Benchmark release | `benchmarks-v0.2.0` |
| Benchmark software DOI | [10.5281/zenodo.21969841](https://doi.org/10.5281/zenodo.21969841) |
| Frozen benchmark commit | `a97c037a4509baee41f8ffa724f1d85e3e598421` |
| Frozen protocol commit | `c6764fb8376d7ada10cb032137ec0c246483051d` |
| Frozen protocol SHA-256 | `85bf058948dd3112256107d72ef4cdd69564ad9ac71905165aa0edbb6870283f` |
| Models | `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol` |
| Cases | 4 frozen cases |
| Conditions | `API-C0` and `API-R1` |
| Repetitions | 3 per model-condition pair |
| Completed live calls | 72 of 72 |
| Result Dataset DOI | Pending publication |

## Conditions

- **API-C0** — provider API request using the frozen case prompt without the Robbie's Razor response-discipline instruction.
- **API-R1** — the same frozen case prompt with the preregistered instruction to preserve correctness and explicit constraints while returning the shortest sufficient answer.

The comparison isolates these two recorded request conditions. It does not establish that either condition represents every possible baseline, prompt, provider configuration, workload, or production environment.

## Raw observations

All 72 planned live requests completed successfully.

- No request errors were recorded.
- No refusals were recorded.
- The returned model identifiers matched the requested model identifiers.
- Provider-side response storage was disabled in every recorded request.
- Four frozen cases were evaluated three times under each model-condition pair.
- The raw execution trace is preserved in the run directory.

## Derived aggregate metrics

Each row contains 12 evaluated observations: four cases multiplied by three repetitions.

| Model | Condition | Correct | Accuracy | Visible output tokens | Tokens per correct answer | Expression-overrun rate | Provider-reported total tokens | Mean wall-clock time |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-luna | API-C0 | 9/12 | 75% | 36 | 2.33 | 0% | 310 | 1,079.44 ms |
| gpt-5.6-luna | API-R1 | 12/12 | 100% | 24 | 2.00 | 0% | 684 | 1,145.37 ms |
| gpt-5.6-terra | API-C0 | 6/12 | 50% | 42 | 3.00 | 0% | 327 | 985.42 ms |
| gpt-5.6-terra | API-R1 | 12/12 | 100% | 24 | 2.00 | 0% | 684 | 825.57 ms |
| gpt-5.6-sol | API-C0 | 12/12 | 100% | 24 | 2.00 | 0% | 288 | 1,496.60 ms |
| gpt-5.6-sol | API-R1 | 12/12 | 100% | 24 | 2.00 | 0% | 684 | 1,188.48 ms |

The evaluator-derived visible-output token metric is distinct from provider-reported total token usage. The added API-R1 instruction increased provider-reported input and total tokens in this run even where visible answers were shorter. Accordingly, this result does **not** demonstrate lower total API token use or lower total computational cost.

## Bounded interpretation

Within these recorded cases and conditions:

- API-R1 produced 12/12 correct answers for each tested model.
- Compared with API-C0, API-R1 increased observed accuracy by 25 percentage points for `gpt-5.6-luna` and 50 percentage points for `gpt-5.6-terra`.
- `gpt-5.6-sol` produced 12/12 correct answers under both conditions.
- Visible output tokens decreased from 36 to 24 for `gpt-5.6-luna`, from 42 to 24 for `gpt-5.6-terra`, and remained 24 under both conditions for `gpt-5.6-sol`.
- Mean wall-clock time changed in mixed directions and is reported descriptively, not as a stable latency claim.
- Expression-overrun rate was zero for every model-condition group.

These observations do not support a universal model ranking or a conclusion that API-R1 will improve every model, task, prompt, domain, cost measure, or deployment.

## Synthetic memory-gate track

A separate tagged synthetic proxy used the preregistered parameters:

| Parameter | Value |
|---|---:|
| Total queries | 1,000 |
| Unique queries | 200 |
| Memory capacity | 10,000 |
| Stability threshold | 0.95 |
| Assumed tokens per inference | 800 |
| Assumed milliseconds per inference | 600 |
| Seed | 123 |

The synthetic track recorded:

- 199 Razor inferences versus 1,000 baseline inferences;
- 801 memory hits and 801 avoided inferences;
- an 80.10% memory-hit rate;
- 640,800 proxy token savings; and
- 480,600 milliseconds of proxy latency savings.

These are **synthetic-proxy values derived from explicit assumptions**. They are not measurements of the three live OpenAI models, provider infrastructure, billing, energy use, or production latency.

## Documented deviation

Deviation `RR-BRP-0.1.0-DEV-001` records that the original synthetic-memory-gate subprocess stopped after the 72 live requests and their evaluations had completed because the temporary tagged checkout root was absent from Python's module search path.

Recovery:

- preserved all original live traces and evaluations;
- repeated zero live model requests;
- ran only the unchanged tagged synthetic benchmark;
- set `PYTHONPATH` to the temporary tagged checkout root;
- generated the missing synthetic record and run manifest; and
- preserved the event as a documented protocol deviation.

## Reproducibility and audit trail

The package preserves:

- the frozen protocol and authorization records;
- benchmark and protocol commit identifiers;
- frozen-artifact hashes;
- exact request bodies without credentials;
- provider response identifiers and usage metadata;
- visible outputs;
- evaluator outputs and reports;
- aggregate descriptive metrics;
- the synthetic proxy record;
- the deviation log; and
- a normalized, repository-relative run manifest.

No API key, bearer token, personal filesystem path, or private reasoning trace is included in the reviewed package.

## Evidence boundary

This package is authored and executed by the benchmark maintainer. It is not independent third-party validation. The evidence state must not be upgraded to `independently-reproduced` unless an operationally independent evaluator completes a sufficiently comparable documented reproduction.

The results do not establish universal validity, causal equivalence, scientific consensus, model certification, production certification, or guaranteed reductions in tokens, latency, resource use, energy use, or cost.
