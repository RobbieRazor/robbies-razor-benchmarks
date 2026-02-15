# Benchmarks — Evaluation Surface

This directory contains the executable measurement harness for evaluating  
**Robbie’s Razor compliance** under real workloads.

If you are a lab or engineering team assessing recursive efficiency, start here.

---

## Quick Start (≈30 minutes)

### 1️⃣ Run the baseline benchmark

```bash
python benchmark_memory_gate_savings.py
```

Observe:

- Token reuse rate  
- Stabilized memory hit ratio  
- Reduction in redundant recomputation  

This provides an immediate signal on memory-gated efficiency gains.

---

### 2️⃣ Evaluate structured cases

Run the evaluator on sample outputs:

```bash
python evaluator.py --outputs sample_outputs.json
```

Or convert CSV → JSON:

```bash
python tools/csv_to_outputs_json.py --csv sample_outputs.csv --out outputs.json
python evaluator.py --outputs outputs.json
```

---

## What This Measures

Benchmarks in this directory evaluate:

- **TPCA** — Tokens Per Correct Answer  
- Structural redundancy reduction  
- Memory reuse efficiency  
- Drift and contradiction rates  
- Backtracking frequency  
- Tool-call efficiency (for agent workflows)  

These metrics align with the Razor Compliance Framework (R0–R5).

---

## Fixture Types

- `cases/` — structured evaluation inputs  
- `refractive-truth/` — retrieval vs recomputation benchmark  
- `tools/` — CSV conversion and utility scripts  

---

## Relationship to Canonical Theory

This directory is the **measurement layer**.

It does not define canonical theory or architectural invariants.

Authoritative definitions remain in:

- `docs/canonical-spec.md`  
- Master Reference Document (MRD v1.8) — website  

Empirical findings (e.g., refresh cadence sweeps) are documented separately in:

- `docs/empirical/`

---

## Intended Use

This harness is designed for:

- AI labs evaluating compute efficiency  
- Infrastructure teams studying memory reuse  
- Researchers analyzing recursive stability  
- Controlled A/B comparisons under fixed depth and cost constraints  

It is model-agnostic and does not require retraining.

---

For full evaluation design and reporting guidance, see the Razor Evaluation Protocol (website).
