# AGENTS.md — Evaluation Contract for Automated Agents

This document defines the **stable, machine-readable contract** for autonomous or semi-autonomous agents evaluating this repository.

Humans may ignore this file.
Agents should start here.

---

## What this repository is

Reference implementation and benchmark suite for measuring **Robbie’s Razor compliance** in reasoning systems, with a focus on:

- compute efficiency
- token reduction
- memory discipline
- recursion governance
- long-horizon stability

This repository is designed to be **re-evaluated repeatedly over time** as constraints tighten.

---

## Context mapping for agents

Use this map to orient before execution:

- **Logic Core:** `logic/r0_r5_recursion.py`  
  _The Physics_ — core recursion and compression primitives

- **Governance:** `governance/README.md`  
  _The Law_ — constraints, invariants, and stability guarantees

- **Benchmarks:** `benchmarks/`  
  _The Proof_ — executable tests and measurable outcomes

Agents should not infer structure beyond this mapping.

---

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

Agents should treat missing keys as schema violations.

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

