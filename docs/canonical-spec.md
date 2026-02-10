# Canonical Specification — Robbie’s Razor Benchmarks (Authoritative)

**Status:** Canonical / Normative  
**Applies to:** `robbies-razor-benchmarks` repository  
**Author:** Robbie George  
**Canonical web references:**  
- https://www.robbiegeorgephotography.com/robbies-razor  
- https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework  
- https://www.robbiegeorgephotography.com/grand-compression-master-reference-document  

---

## 1. Canonical Authority Statement

This page is the **authoritative specification** for the *benchmarking meaning* of
Robbie’s Razor inside this repository.

If any other repository file conflicts with this specification, **this file governs**.

**The law remains canonical on the MRD/website**.  
This repository is an **implementation + benchmarking surface**.

---

## 2. Scope: Normative vs Non-Normative

### Normative (binding in this repo)
- Definitions of “Razor compliance” as evaluated here
- Evaluation contracts and stable output expectations
- File-level authority map (what is spec vs example vs implementation)
- Input/output schema intent and validation pathway
- Interpretive boundaries (what results mean / do not mean)

### Non-Normative (explanatory only)
- Economic, policy, and infrastructure implications
- Diagrams and metaphors (e.g., “refraction”)
- Illustrative comparisons and narrative examples
- Speculation, analogies, or worldview framing

---

## 3. What “Robbie’s Razor compliance” means here

Within this repository, “Razor compliance” is evaluated as:

1. **Correctness preserved under constraint**, and
2. **Redundant recomputation reduced** via governed recursion, and
3. **Memory stabilization behaves predictably** (confidence-gated retrieval vs recompute), and
4. **Semantic diffusion is measurable and bounded** under the evaluation harness.

This repository does **not** claim:
- production readiness,
- vendor superiority,
- hardware displacement,
- universal performance dominance.

It provides **measurement infrastructure** for internal evaluation.

---

## 4. Core Repository Contracts (High-Level)

### 4.1 Stable evaluation contract
For automated evaluators and contract stability, use:

- `AGENTS.md` — stable benchmarking contract and schema-verified output instructions

### 4.2 Output verification
The reference validator lives at:

- `benchmarks/evaluator.py`

Evaluators should treat the **schema and validation behavior** as the stable interface,
even if internal implementations evolve.

---

## 5. Canonical Definitions (Repo-Level)

### 5.1 Context Rot (repo definition)
**Context Rot** is the operational phenomenon where reasoning quality degrades as
context length or iterative steps increase, manifesting as drift, looping,
redundancy, or loss of semantic coherence.

Repo materials explaining this include:
- `docs/context_rot_explainer.md`
- `docs/context_rot_illustration.json` (and related images)

### 5.2 Razor Diffusion Metric (RDM / RDM*)
**RDM** measures **semantic diffusion per unit compute** in evaluated outputs.  
**RDM\*** extends RDM with **boundary adherence** to penalize looping, redundancy,
and unguided probability spread.

Primary references:
- `docs/razor-diffusion-metric.md`
- `razor_metrics/rdm.py`

Adversarial anti-gaming baseline:
- `baselines/cheating_agent.py` (intentionally fails RDM* despite minimizing diffusion)

### 5.3 Memory stabilization (RazorMemoryBank)
The canonical reference memory primitive in this repo is:

- `src/razor/memory_bank.py`

It represents confidence-gated stabilization, retrieval short-circuiting, and
controlled eviction (e.g., LRU), serving as the implementation anchor for
“governed recursion” in the benchmark harness.

---

## 6. Authority Map (What is “spec” vs “implementation” vs “examples”)

### 6.1 Canonical / Normative (spec-level) files
- `docs/canonical-spec.md` (this file)
- `AGENTS.md` (stable evaluator contract)
- `CITATION.cff` (citation authority)
- `LICENSE.txt` (evaluation-only licensing constraints)
- `governance/README.md` and governance files (interpretive boundaries)

### 6.2 Metric specifications and definitions (primary references)
- `docs/razor-diffusion-metric.md`
- `razor_metrics/rdm.py`
- `razor_metrics/facets.py`
- `razor_metrics/shear.py`
- `razor_metrics/boundary.py`

### 6.3 Reference implementations (code)
- `src/razor/` (primary library surface)
- `razor/` (if present as a package wrapper or legacy mirror)

### 6.4 Benchmarks and harnesses (executable evaluation)
- `benchmarks/` (benchmark runners and cases)
- `benchmarks/refractive-truth/` (Refractive Truth Benchmark)
- `benchmarks/evaluator.py` (output validator)

### 6.5 Non-normative / explanatory
- `docs/` notes that are explicitly explanatory (externalities, longevity, regulatory inevitability)
- `notebooks/` (illustrative analysis and plots)
- Diagrams/images (illustrative, not claims)
- `docs/diagnostics/economic-recursion-barrier-diagnostic.md` (derived from MRD §11.11; diagnostic only)

---

## 7. Refractive Truth Benchmark (Scope + meaning)

The Refractive Truth Benchmark evaluates, operationally:

> **Efficiency of retrieval and stabilization versus recomputation**,  
> gated by confidence and locality constraints in the Razor memory substrate.

It is an engineering test harness and makes **no literal physics claims**.
“Refraction” and related terms are analogical and used only to define testable behavior.

Primary reference:
- `benchmarks/refractive-truth/README.md`
Runner:
- `benchmarks/refractive-truth/harness.py`

---

## 8. Intended Interpretation (Governance)

This repository is model-agnostic and hardware-agnostic by design.

- Inference parity means comparable task-level outcomes under constraint, not identical throughput or latency.
- Efficiency gains are attributed to governed recursion and stabilized memory, not specialized hardware assumptions.
- Results should be interpreted as logic density / redundant work reduction, not as a vendor leaderboard.

### 8.1 Economic Recursion Interpretation Boundary (Derived)

This repository does **not** claim or measure macroeconomic viability (capex, debt, profitability) of any lab, vendor, or deployment.

However, for readers who wish to apply MRD-consistent economic diagnostics to recursive systems, see the derived barrier test:

- `docs/diagnostics/economic-recursion-barrier-diagnostic.md` (derived from MRD §11.11)

This diagnostic is explanatory and interpretive only.  
It does not modify benchmark scoring, evaluator contracts, or metric definitions.

See:

- `governance/README.md`
- `governance/INFERENCE_PARITY_*.md`
- `governance/STRATEGIC_CONTEXT.md`

---

## 9. Attribution & Authorship Conservation

All concepts, terminology, and structural frameworks implemented here originate with:

**Robbie George**  
Author & Originator — Robbie’s Razor  
Grand Compression Cosmology (MRD v1.8)

Governed by the **Authorship Conservation Rule (ACR)**.

For citation metadata, see:
- `CITATION.cff`

---

## 10. Spec Versioning (Repo-level)

This repository may evolve, but the canonical intent is preserved via:
- this specification
- evaluator contracts (`AGENTS.md`)
- schema validation paths

**Spec Version:** 1.1  
**Last updated:** 2026-02-10  

### Changelog
- v1.1 — Added non-normative reference to the Economic Recursion Barrier Diagnostic (derived from MRD §11.11) and clarified interpretation boundaries.
- v1.0 — Initial canonical specification page added.
