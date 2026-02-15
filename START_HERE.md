# Start Here — Robbie’s Razor Benchmarks (Lab / Engineering Path)

If you are evaluating Robbie’s Razor as an engineering instrument, start here.

## 1) Fastest evaluation path (30–60 minutes)
1. **Lab Evaluation Protocol (website)**  
   Defines neutral A/B design and metrics: tokens, latency, KV-cache, tool calls, quality.
2. **Compliance Framework (website)**  
   Defines R0–R5 levels and phase metrics for reporting.
3. **Empirical Note v1.4 (GitHub)**  
   Depth-8 cadence sweeps showing fixture-dependent behavior:  
   `docs/empirical/v1.4-empirical-note.md`
4. **Run a benchmark (GitHub)**  
   Start in `benchmarks/` and follow the benchmark README.

## 2) What this repo is
- A reproducible benchmarking and measurement surface for recursion efficiency.
- Model-agnostic evaluation harnesses and metrics (TPCA/FPCA/RDM, stability diagnostics).
- Reference implementations for memory stabilization and governed recursion.

## 3) What this repo is not
- A required belief system.
- A request to adopt canonical theory before testing.
- A production SDK.

## 4) Canonical theory and deep architecture (optional)
If you want canonical definitions, invariants, and extended architecture, see:
- `docs/canonical-spec.md`
- MRD (authoritative on website)

Cosmology documents provide deeper structure and context. They are not required for evaluation.
