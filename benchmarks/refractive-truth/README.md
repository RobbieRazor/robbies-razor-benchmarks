# Refractive Truth Benchmark

## Purpose

The **Refractive Truth Benchmark** evaluates whether Robbie’s Razor behaves like a
*structured medium* rather than a flat statistical surface.

In this benchmark, **semantic refraction** is defined operationally as:

> **Efficiency of retrieval and stabilization versus recomputation**,  
> gated by confidence and locality constraints in the Razor memory substrate.

This benchmark is intentionally engineering-facing. It does **not** assume or require
acceptance of any external physics theory. All claims are testable via observable outputs.

---

## What This Benchmark Tests

The harness measures how the Razor’s **confidence-gated memory system** responds to
prompts with differing physical or logical consistency.

Specifically, it records:

- Whether a prompt results in a **memory hit** or requires recomputation
- The **confidence score** returned by the MemoryBank
- A derived **Lattice Stability Score (LSS)** (currently mapped from confidence)
- Whether a prompt is **rejected** by the stability gate
- Approximate **latency**, as a proxy for retrieval vs recompute cost

This allows evaluators to test the hypothesis:

> Valid, physically consistent continuations propagate more efficiently
> through the system than contradictory or non-local continuations.

---

## Conceptual Mapping (Analogy Only)

| Conceptual Term | Engineering Interpretation |
|----------------|----------------------------|
| Refraction | Memory retrieval efficiency vs recomputation |
| Medium | Confidence-gated memory substrate |
| Stability | Consistency under repeated access |
| Total Internal Reflection | Low-confidence rejection by the gate |
| LSS (Lattice Stability Score) | Normalized stability metric (0–1) |

No literal physical claims are made. These are **analogies used to define testable behavior**.

---

## Files

- **`harness.py`**  
  Runnable benchmark harness wired to `src/razor/memory_bank.py`.

- **Output**  
  JSON report printed to stdout containing:
  - Per-prompt trace results
  - Summary metrics (hit rate, rejection rate, latency)

---

## How to Run

From the repository root:

```bash
PYTHONPATH=. python benchmarks/refractive-truth/harness.py
```

## Notes for Evaluators

This benchmark is contract-first: the output schema is stable even if
internal implementations evolve.

The current LSS mapping is intentionally conservative and may be refined.

Results should be reproducible across paraphrases if the substrate is stable.

## Authorship & Scope

Robbie’s Razor and its benchmark protocols are authored by Robbie George.

This benchmark is a validation harness, not a claim of physical law or
mainstream physics endorsement.
