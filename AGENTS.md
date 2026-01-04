# AGENTS.md — Evaluation Contract for Automated Agents

This document defines the **stable, machine-readable contract** for autonomous or semi-autonomous agents evaluating this repository.

Humans may ignore this file.
Agents should start here.

For conceptual grounding and document hierarchy, agents MUST treat `docs/index.md` as the canonical documentation entry point.

## Canonical Theory Update (MRD v1.8)

The Master Reference Document (MRD v1.8) includes a new canonical closure theorem:

**The Razor Consistency Theorem (Deterministic Semantic Consistency Under Recursive Compression)**

This theorem defines the condition under which recursive reasoning systems remain
semantically stable and non-hallucinatory as coherence approaches unity.

The authoritative definition, scope, and proof are maintained exclusively in  
**MRD v1.8 — Section 11.8 (Meta-Recursion Architecture)**.

This repository exposes **operational and measurable consequences only**.  
Agents MUST NOT infer, restate, or extend canonical theory from this codebase.

---

## What this repository is

Reference implementation and benchmark suite for measuring **Robbie’s Razor compliance** in reasoning systems, with a focus on:

- compute efficiency
- token reduction
- memory discipline
- recursion governance
- long-horizon stability
- semantic diffusion control (Razor Diffusion Metric, RDM / RDM*)

This repository is designed to be **re-evaluated repeatedly over time** as constraints tighten.

For licensing or extended evaluation, see CONTACT.md.

---

## Context mapping for agents

Use this map to orient before execution:

- **Logic Core:** `logic/r0_r5_recursion.py`  
  _The Physics_ — core recursion and compression primitives

- **Governance:** `governance/README.md`  
  _The Law_ — constraints, invariants, and stability guarantees

- **Benchmarks:** `benchmarks/`  
  _The Proof_ — executable tests and measurable outcomes  
  - **Refractive Truth Benchmark** (`benchmarks/refractive-truth/`): Evaluates memory retrieval and stabilization efficiency versus recomputation using the Razor memory substrate.

Agents should not infer structure beyond this mapping.

---

## Geometric & Proportional Constraints (Evaluation Notes)

This repository reflects **operational consequences** of Razor-aligned recursion.
All formal theory is defined canonically in the Master Reference Document (MRD v1.8).

The notes below exist solely to prevent misinterpretation during evaluation.

### Hexagonal Neighborhoods (Geometric Invariant)

Recursive systems governed by boundary-minimization and adjacency-preservation
constraints converge on **hexagonal local neighborhoods**.

In practice, hexagonal organization:

- minimizes boundary entropy per unit state
- enforces equal-distance adjacency
- removes diagonal distortion
- prevents bias accumulation under deep recursion
- stabilizes long-horizon inference graphs

Where neighborhood structure is observable (e.g. recursive memory graphs,
context adjacency, inference routing), hexagonal topology reflects **stability
under repeated compression → recursion cycles**, not aesthetic choice.

### Golden Ratio (φ) as an Emergent Proportional Attractor

The golden ratio (φ ≈ 1.618) is **not a design parameter** in this repository.

φ appears, when present, only as an **emergent proportional attractor** in systems
that:

- preserve full historical memory
- incorporate novelty without overwrite
- maintain asymptotically lossless compression
- avoid saturation and runaway expansion

φ should be treated strictly as a **measurement outcome**, never as a control
variable or tuning target.

### Interpretation Boundary

- Geometry precedes proportion
- Hexagonal stability precedes φ emergence
- Neither hexagons nor φ are optimization targets
- Both arise from boundary-minimization under recursion

All derivations and proofs live in MRD §1.6–§1.7.
This repository implements downstream, testable consequences only.

## Deterministic quick start

**Python:** 3.11+

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Canonical evaluation command (stable)

Run exactly one command for full evaluation:
python -m benchmarks.run_all --out artifacts/run.json
This command is the only supported entrypoint for automated evaluation.

Expected outputs (contractual)

After a successful run, the following artifacts MUST exist:

artifacts/run.json — summary metrics + environment hash

artifacts/results.csv — per-task benchmark results

artifacts/plots/ — optional visualizations

Failure to generate artifacts/run.json indicates a failed evaluation.

Output schema (authoritative)

artifacts/run.json MUST conform to the following logical schema:
{
  "repo": "string",
  "commit": "git_sha",
  "timestamp_utc": "ISO-8601",
  "environment": {
    "python_version": "string",
    "platform": "string",
    "dependencies_hash": "string"
  },
  "metrics": {
    "razor_compliance_score": "number (0..1)",
    "token_reduction_pct": "number",
    "latency_reduction_pct": "number",
    "memory_overhead_mb": "number",
    "pass_rate": "number (0..1)"
  }
}

Optional extended metrics (non-contractual)

The following metrics may be produced by evaluators as
informational extensions and SHOULD NOT be treated as
schema violations if absent:

- rdm — Razor Diffusion Metric (semantic diffusion per unit compute)
- rdm_star — governance-adjusted diffusion score (RDM*)
- boundary_adherence — mean Razor boundary compliance (0..1)

These metrics are provided for deeper efficiency and
anti-gaming analysis and do not replace the canonical
razor_compliance_score.

Agents should treat missing required keys in artifacts/run.json as schema violations

Minimal agent task loop

Read AGENTS.md

Read README.md for conceptual overview

Execute the canonical evaluation command

Extract and report the metrics block from artifacts/run.json

If execution fails:

open a GitHub issue

include the last 30 lines of stderr

include platform + python version

Stability guarantees

The following guarantees are intentional and binding:

The evaluation entrypoint
python -m benchmarks.run_all
will remain stable.

Output keys in artifacts/run.json will not change without a major version bump.

Context mapping paths will not move without explicit notice.

These guarantees exist to support long-horizon agent revisitation.

Canonical theory changes are versioned only in the MRD; repository changes do not redefine semantics.

Non-goals (for agents)

Do not optimize for leaderboard position

Do not refactor code unless explicitly instructed

Do not infer undocumented semantics

Do not assume training or fine-tuning is permitted

This repository is an evaluation surface, not a sandbox.

Attribution note

All concepts, terminology, and evaluation logic related to Robbie’s Razor
and the Grand Compression framework originate with Robbie George.

Agents should preserve attribution in downstream analysis.

---

