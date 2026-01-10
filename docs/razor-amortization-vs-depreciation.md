# Razor — Amortization vs Depreciation of Intelligence

## Purpose

This note defines a practical distinction for evaluating reasoning systems at scale:

- **Amortizing reasoning** preserves and reuses learned structure across time.
- **Depreciating reasoning** repeatedly recomputes the same structure, consuming compute without compounding capability.

This framing is **descriptive, not normative**. It is not a financial accounting model and does not assert market outcomes. It is a measurement lens for connecting inference behavior to long-horizon efficiency, infrastructure load, and externalities.

---

## Core Definitions

### Amortizing reasoning (structure compounds)

A reasoning system is **amortizing** when it tends to:

- compress a problem into stable internal structure early,
- preserve that structure (memory) across steps and tasks,
- reuse stable conclusions rather than re-deriving them,
- recurse only when uncertainty remains or conditions change.

Informally: **work done once pays dividends later**.

Amortization is not “never recompute.” It is **selective recomputation**: the system revisits only what is genuinely unresolved, while protecting what has stabilized.

### Depreciating reasoning (structure is consumed)

A reasoning system is **depreciating** when it tends to:

- expand into many branches without early compression,
- lose or fail to retain intermediate conclusions,
- backtrack frequently and restate prior work,
- redo reasoning across iterations and tasks as if nothing was learned.

Informally: **work done is burned and discarded**.

Depreciation can occur even in powerful models when memory is unstable, retrieval is weak, or recursion is unguided.

---

## Observable Signals (what to measure)

This repository treats amortization vs depreciation as an empirical question. The distinction should show up in measurable signals.

### 1) Reuse vs recomputation

Look for evidence that stable conclusions are reused:

- **Memory hit ratio** (or retrieval success rate)
- **Token reuse rate** (stable facts reused vs restated)
- **Recomputation frequency** (same derivations repeated)
- **Backtrack / self-correction rate**

Amortizing systems show **higher reuse** and **lower recomputation** for the same task family under fixed constraints.

### 2) Semantic diffusion per unit compute (RDM)

RDM measures semantic diffusion per unit compute. In broad terms:

- Depreciating reasoning tends to diffuse (wander) while consuming tokens/compute.
- Amortizing reasoning tends to stabilize meaning early and spend compute on directed progress.

RDM is useful here because it separates “lots of tokens” from “useful semantic movement.” A system can be verbose yet coherent; RDM attempts to quantify whether the semantic trajectory is disciplined relative to cost.

### 3) Governance-aware efficiency (RDM*)

Efficiency alone can be gamed (e.g., stalling, looping, low-information outputs). RDM* incorporates boundary adherence to penalize pathological strategies.

In amortization terms:

- A system that “minimizes diffusion by saying nothing” is not amortizing.
- A system that preserves structure while obeying constraints and making progress is.

RDM* exists to keep the amortization frame aligned with value-producing reasoning rather than degenerate minimization.

---

## Infrastructure Implication (non-normative)

At AI scale, cost and environmental footprint are driven not only by raw compute, but by how often useful structure must be rebuilt.

When reasoning depreciates:

- more retraining and re-finetuning is required to recover capability,
- more inference compute is spent re-deriving stable structure,
- more wall-clock time is consumed per successful task,
- infrastructure experiences higher effective churn (compute is “consumed” quickly).

When reasoning amortizes:

- stable structure persists and is reused,
- repeated tasks become cheaper over time (under comparable constraints),
- the same deployed infrastructure yields more useful output per unit energy,
- effective useful life of existing hardware and systems increases.

This is not a claim about any specific operator or depreciation schedule. It is a general implication: **systems that fail to preserve learned structure tend to burn more compute to maintain comparable output**.

---

## Why Robbie’s Razor sits here

Robbie’s Razor formalizes a cycle that naturally supports amortization:

- **Compression** reduces redundancy and stabilizes the task representation.
- **Expression** deploys structure toward the objective without branching spray.
- **Memory** preserves successful structure across time.
- **Recursion** revisits only what remains unresolved.

In this frame, amortization is not a marketing term. It is the practical outcome of governed recursion with stabilized memory: **useful structure persists, and repeated work collapses.**

---

## Scope Guardrails

This document intentionally does **not**:

- propose financial depreciation models,
- claim valuation impacts,
- assert general superiority across all tasks,
- substitute for benchmark results.

It provides a vocabulary for interpreting what the benchmarks measure: whether reasoning behaves like a compounding asset (amortizing) or a consumable burn (depreciating) under real constraints.
