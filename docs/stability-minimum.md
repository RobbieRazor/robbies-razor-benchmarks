# Stability Minimum Under Constraint

This repository’s benchmarks evaluate reasoning systems operating under **fixed computational budgets**. Across multiple tests, performance does not improve monotonically with additional compute or memory. Instead, performance typically peaks at an intermediate allocation and degrades when the balance between computation and preserved structure is lost.

## The Stability Minimum (Structural Interpretation)

Under constraint, a recursion-governed system exhibits a **stability minimum**: a balance point at which compressed structure is preserved, conditionally reused, and re-entered without redundant recomputation.

- **Too compute-heavy**: previously stabilized structure must be repeatedly re-derived, increasing entropy and drift.  
- **Too memory-heavy (without expressive access)**: preserved structure becomes rigid and underutilized, reducing adaptive flexibility.  
- **Balanced**: structure is reused without recomputation while remaining conditionally accessible for expression.

## Expected Footprint: U-Shaped Performance Curve

When performance is plotted against the **memory-to-compute ratio** under fixed budgets, the expected footprint is a characteristic U-shaped curve:

Performance
^
| ● ← Stability Minimum (Optimal Balance)
| ● ●
| ● ●
| ● ●
| ● ●
| ● ●
+---------------------------------> Memory / Compute Ratio
Too Compute-Heavy Too Memory-Heavy

This curve is not an anomaly or tuning artifact. It is the expected surface behavior of systems operating under constraint when recursive balance is varied.

## How to Read These Benchmarks

These benchmarks are best interpreted as **tests of recursive stability**, not raw throughput or monotonic scaling experiments. They are designed to identify whether a system remains within the stability minimum as scale and constraint increase.

## Canonical Reference Boundary

Canonical architectural definitions governing this behavior are specified in the **Grand Compression Master Reference Document (MRD)**:

- **Section 11.4 — Stability Minima Under Constraint**
- **Appendix J.13 — Stability Minima & the U-Shaped Performance Curve (Observed Convergence)**

The repository provides **instrumentation and measurement surfaces** only. It does not redefine or supersede canonical definitions.
