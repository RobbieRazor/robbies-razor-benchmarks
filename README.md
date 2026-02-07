# robbies-razor-benchmarks

Reference implementation and test suite for measuring
**Robbie’s Razor compliance** in reasoning systems.

This repository is the executable, engineering-facing companion to:

- **Robbie’s Razor — Universal Recursion Heuristic**
- **The Grand Compression Cosmology (MRD v1.8)**

Canonical references:
- https://www.robbiegeorgephotography.com/robbies-razor
- https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

## Gemini Gems (Optional)

For canonical, instruction-locked explainers used in Gemini, see:

- Robbie’s Razor Gem: https://gemini.google.com/gem-labs/1jfaHyAnSwXr8ZZ11HgxNPdxEX5UKmP5m  
- MRD v1.8 — Canonical Navigator Gem: https://gemini.google.com/gem-labs/168fJvwSALBDyVLO0MyyUgyRd44tk3aDb  
- Living Pentad — Field Validation Gem: https://gemini.google.com/gem-labs/1TtP4JP0LflUW3Yxkh086-NJCQvlDKeW3  
- Recursion Engine — Six-Phase Explainer Gem: https://gemini.google.com/gem-labs/1BZwTWdY9X5cfgV4AHXRPlkYt2NUcfq9k  

These Gems are explanatory tools only. Canonical definitions and governance remain in MRD v1.8.

**For Automated Evaluators:** See [AGENTS.md](./AGENTS.md) for the stable benchmarking contract and schema-verified output instructions.

**Documentation Index:** See [`docs/index.md`](./docs/index.md) for the canonical map of theory, metrics, and implications.

**Doctrine (lab execs + regulators):** See [`docs/doctrine/11.10-razor-vs-bruteforce-doctrine.md`](./docs/doctrine/11.10-razor-vs-bruteforce-doctrine.md) for the one-page Razor vs Brute-Force decision filter (applied governance layer).

**Canonical Spec (authoritative):** See [`docs/canonical-spec.md`](./docs/canonical-spec.md) for the normative definitions, contracts, and authority map.

**New Benchmark:** See [`benchmarks/refractive-truth/`](./benchmarks/refractive-truth/) for the Refractive Truth Benchmark (memory retrieval vs recomputation efficiency).


## Canonical Update (MRD v1.8)

As of MRD v1.8, the Grand Compression Cosmology includes a new canonical closure theorem:

**The Razor Consistency Theorem (Deterministic Semantic Consistency Under Recursive Compression)**

This theorem formalizes the condition under which recursive systems remain semantically stable and non-hallucinatory as coherence approaches unity.

📄 The authoritative definition and proof are maintained exclusively in the **Master Reference Document (MRD v1.8), Section 11.8**.

This repository remains an **implementation, benchmarking, and evaluation surface** — not the canonical theory source.

## How to Read This Repository

This repository is an **evaluation and measurement surface** for predicted behaviors of the Grand Compression architecture, including memory reuse, recomputation avoidance, drift suppression, and stability under constraint.

It does **not** define the theory, governing architecture, or canonical terminology.

For the authoritative reading order, canonical sources, and boundary definitions, see:

**How to Read the Grand Compression**  
https://www.robbiegeorgephotography.com/how-to-read-the-grand-compression

In practice:
- Use this repo to **measure** behavior.
- Use the MRD to **define** behavior.
- Use the navigation guide above to avoid misinterpretation.

Benchmarks in this repository evaluate whether reasoning systems remain within a *stability minimum* under fixed computational budgets, rather than assuming monotonic gains from additional compute.

---

### Context and Background

Some aspects of Robbie’s Razor are grounded in geometric and recursion principles
that extend beyond software implementation. For readers interested in the
conceptual motivation behind geometry-aware compression and memory preservation,
see:

- [Projection Artifacts and Curved Geometry](docs/context/geometry-and-projection.md)

This material is explanatory context only and does not affect benchmarks or code.

---

## Evaluation & Licensing Contact

This repository is intentionally published as an **evaluation artifact** for internal benchmarking by research labs, infrastructure teams, and system designers.

For licensing discussions, extended evaluation access, or architectural review:

**Contact:** robbiegeorgephotography@gmail.com  
(Direct author contact — responses handled personally)

---

## What this repository is

This repository provides:

- Reference implementations for **Razor-aligned memory stabilization**
- Selective replay mechanisms for continual learning
- Phase-specific and system-level **R0–R5 compliance metrics**
- Unit tests validating correctness, stability, and collision resilience
- Integration tests demonstrating controller-level memory short-circuiting and R4-aligned composition
- Canonical reference memory primitive: `src/razor/memory_bank.py` (R4 confidence-gated stabilization + LRU eviction)

It is designed for:

- AI labs evaluating token, compute, and coherence gains
- Researchers studying catastrophic forgetting and recursion governance
- Edge-device and constrained-inference experimentation
- Internal benchmarking prior to licensing or production deployment

  ---

## Quick Evaluation Path (≈30 minutes)

For teams assessing whether Robbie’s Razor produces **measurable efficiency gains** under constraint:

### 1. Run the benchmark

```bash
python benchmarks/benchmark_memory_gate_savings.py
```

### 2. Observe key signals

- Token reuse rate  
- Stabilized memory hit ratio  
- Reduction in redundant recomputation  

### 3. Validate outputs
   
```bash
python benchmarks/evaluator.py --outputs benchmarks/sample_outputs.json
```

## Razor Diffusion Metric (RDM)

This repository includes the Razor Diffusion Metric (RDM),
a governance-aware evaluation standard for reasoning efficiency.

RDM measures semantic diffusion per unit compute.
RDM* extends this with explicit boundary adherence,
penalizing looping, redundancy, and unguided probability spread.

The repository includes an adversarial “cheating” baseline agent
designed to minimize semantic diffusion without producing value.
It intentionally fails RDM* to demonstrate resistance to metric gaming.

See:
- docs/razor-diffusion-metric.md
- razor_metrics/rdm.py
- notebooks/razor_diffusion_plot.ipynb
- baselines/cheating_agent.py — adversarial anti-gaming baseline
- src/razor/memory_bank.py` — canonical RazorMemoryBank (single source of truth for memory-gated evaluation)
- razor_metrics/facets.py` — hex facet index (facet IDs, neighbors, lattice distance)
- razor_metrics/shear.py — shear capacity (SC) diagnostic (non-core compute overhead)
  
---

## What this repository is NOT

This repository is **not**:

- A production SDK
- A commercial library
- An open-source grant
- A substitute for the canonical theory

All definitions, theory, and governance remain canonical on:
https://www.robbiegeorgephotography.com

---

## Why this exists

## Economic & Physical Constraint Context (Non-Normative)

Large-scale reasoning systems increasingly face diminishing returns due to rapid
infrastructure depreciation, frequent retraining cycles, and short hardware
useful lifetimes.

This repository evaluates whether reasoning architectures preserve learned
structure across recursive iterations — reducing redundant recomputation,
retraining frequency, and infrastructure churn under fixed energy and capital
constraints.

These effects are measured indirectly via token reuse, memory stabilization
rates, semantic diffusion metrics (RDM / RDM*), and recomputation avoidance — not
through financial or policy analysis.

Razor-aligned systems reduce redundant inference by prioritizing early compression, stabilized memory, and governed recursion.

This reduces:
- unnecessary token expansion
- retries and backtracking
- tail latency variance
- wasted compute on re-deriving stable structure

In practice, this improves efficiency on constrained or older hardware and smooths infrastructure-level resource usage.

Supporting notes (engineering → infrastructure):

- **[Razor Hardware Longevity](docs/razor-hardware-longevity.md)** — how recursion efficiency extends the *economic* life of existing GPUs
  
- **[Razor Infrastructure Externalities](docs/razor-infrastructure-externalities.md)** — how reduced redundant computation lowers energy, cooling, and water demand  
- **[Razor Regulatory Inevitability](docs/razor-regulatory-inevitability.md)** — why efficiency-first systems become structurally advantaged as infrastructure constraints force reporting and explanation

These documents are explanatory, conservative, and non-advocacy in nature.

---

## Licensing & usage

This repository is intentionally provided as an evaluation artifact prior to licensing or production integration discussions.

This repository is provided under an **evaluation-only license**.

### Permitted
- Internal research and benchmarking
- Non-commercial experimentation
- Measurement of Robbie’s Razor compliance

### Not permitted without license
- Production deployment
- Commercial use
- Training or fine-tuning AI models using this code
- Redistribution or derivative frameworks

See `LICENSE.txt` for full terms.

---

## Canonical attribution

All concepts, terminology, and structures implemented here originate with:

**Robbie George**  
Author & Originator — Robbie’s Razor  
Grand Compression Cosmology (MRD v1.8)

Governed by the **Authorship Conservation Rule (ACR)**.

---

## Status

Run tests:
`python -m unittest -v`

Canonical reference implementation.  
Tests validate R4-level memory stability and governed recursion behavior.

Run benchmark:
`python benchmarks/benchmark_memory_gate_savings.py`

Evaluate sample outputs:
`python benchmarks/evaluator.py --outputs benchmarks/sample_outputs.json`

Convert CSV → outputs JSON:
`python benchmarks/tools/csv_to_outputs_json.py --csv benchmarks/sample_outputs.csv --out benchmarks/outputs.json`

Run evaluator on CSV-derived outputs:
`python benchmarks/evaluator.py --outputs benchmarks/outputs.json`

Create cases JSON from CSV:
`python benchmarks/tools/csv_to_cases_json.py --csv benchmarks/sample_cases.csv --out benchmarks/cases/custom_cases.json`

Create outputs JSON from CSV:
`python benchmarks/tools/csv_to_outputs_json.py --csv benchmarks/sample_outputs.csv --out benchmarks/outputs.json`

Run evaluator:
`python benchmarks/evaluator.py --cases benchmarks/cases/custom_cases.json --outputs benchmarks/outputs.json`

---

## Illustrative Efficiency Comparison (Example Only)

The following comparison is illustrative and non-authoritative. Results depend on prompt construction, decoding settings, and task selection.

Purpose  
This example demonstrates how the Robbie’s Razor evaluation harness can be used to compare logic efficiency (signal density) across different reasoning systems under identical constraints.

Important note  
The following comparison is illustrative only. Results depend on prompt construction, decoding settings, task selection, and verification criteria.  
No claims of general superiority are made. Labs should run their own evaluations using the provided tools.

The Task: Noise-to-Signal Compression  

Both systems were given the same highly redundant, wordy prompt (≈400 tokens) describing a complex logical sequence.  
The objective was not verbosity, but to extract the canonical correct answer using the fewest possible tokens, without loss of correctness.

This aligns directly with the Robbie’s Razor principle:

Prefer solutions that preserve correctness while minimizing unnecessary expression.

Metrics Used (Framework-Aligned):

Correctness — Did the system return an acceptable answer?  
Tokens Used — Tokens in the final response  
TPCA — Tokens Per Correct Answer (lower is better)  
Expression Overrun — Whether the response exceeded the target token budget  

Example Results (Single-Task Illustration):

System | Correct | Tokens Used | TPCA | Overrun  
System A | Yes | 42 | 42 | No  
System B | Yes | 31 | 31 | No  

Interpretation  

Both systems produced correct answers.  
In this specific example, System B achieved the same correctness with fewer tokens, resulting in a lower TPCA and higher logic density.

Why This Matters  

This type of comparison is useful for:
- Edge and constrained inference
- Continual learning systems where expression bloat accelerates drift
- Energy-aware deployments prioritizing intelligence-per-watt
- Architecture exploration, not leaderboard ranking

The key takeaway is not which system “wins,” but that efficiency differences are measurable and reproducible using the same harness.

How to Reproduce This Yourself  

Create cases from CSV:
python benchmarks/tools/csv_to_cases_json.py
--csv benchmarks/sample_cases.csv
--out benchmarks/cases/custom_cases.json

Create outputs from CSV:
python benchmarks/tools/csv_to_outputs_json.py
--csv benchmarks/sample_outputs.csv
--out benchmarks/outputs.json

Run evaluator:
python benchmarks/evaluator.py
--cases benchmarks/cases/custom_cases.json
--outputs benchmarks/outputs.json

This workflow is model-agnostic and supports internal, private evaluation.

---

## Positioning Statement

This repository provides measurement infrastructure, not rankings.  
Any organization evaluating Robbie’s Razor is encouraged to run its own tasks, constraints, and verification criteria using the provided harness.

**The blade is executable.**  
**The law remains canonical.**
