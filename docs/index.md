# Robbie’s Razor — Documentation Index

## 0. Canonical Specification (Authoritative)

- **Canonical Spec (authoritative)**  
  [`canonical-spec.md`](./canonical-spec.md)  
  The single source of truth for definitions, normative contracts, and repository authority.

  ### Canonical Provenance & Attribution

- **Appendix P — Provenance, Priority & Convergent Rediscovery Clarifier**  
  [`appendices/appendix-p-provenance-priority-convergence.md`](./appendices/appendix-p-provenance-priority-convergence.md)  
  Formal clarification of authorship, priority of conception, and structural scope for Robbie’s Razor and the Grand Compression Cosmology.  
  Establishes canonical attribution boundaries and distinguishes formal framework elements from convergent external rediscoveries.

This directory contains the formal documentation, analysis, and contextual framing for **Robbie’s Razor**, an inference-efficiency and memory-coherence framework designed to reduce compute, energy, and regulatory externalities in large-scale AI systems.

The documents below are organized to guide readers from **core metric definitions**, through **hardware and infrastructure implications**, and finally to **regulatory and systemic outcomes**.

---

## 1. Core Metrics & Theory

These documents define the primary metrics and conceptual foundations used throughout the benchmark and evaluation pipeline.

- **Razor Diffusion Metric**  
  [`razor-diffusion-metric.md`](./razor-diffusion-metric.md)  
  Defines the diffusion-based efficiency metric used to evaluate inference stability, memory reuse, and entropy suppression.

- **Physics Unification — Research Note**  
  [`physics_unification.md`](./physics_unification.md)  
  Contextual mapping between Razor’s locality- and stability-based inference substrate and broader medium-first interpretations of intelligence.  
  (Explanatory; not a claim of experimental physics validation.)

  - **Context Rot — Explanatory Note**  
  [`context_rot_explainer.md`](./context_rot_explainer.md)  
  Illustrative discussion of long-context failure as failed recursive closure.

Additional non-canonical research notes exploring geometric constraints on recursive stability are available in `geometric_stability_notes.tex` (explanatory; not a formal proof).

Optional utilities for hex-lattice experiments are documented in `lattice_geometry_util.md`.

---

## 2. Hardware & System Implications

These documents explore how Razor-aligned architectures impact hardware lifespan, memory pressure, and system-level efficiency.

- **GPU Longevity**  
  [`razor-gpu-longevity.md`](./razor-gpu-longevity.md)  
  Analysis of how reduced inference diffusion extends effective GPU service life.

- **Hardware Longevity (Generalized)**  
  [`razor-hardware-longevity.md`](./razor-hardware-longevity.md)  
  Broader implications across accelerators, memory, and interconnects.

  ### Empirical Context (Non-Canonical)

- **Memory–Compute Allocation Minima**  
  [`empirical/memory_compute_allocation_minima.md`](./empirical/memory_compute_allocation_minima.md)  
  External empirical pattern showing a stability minimum under fixed resource budgets, consistent with Razor-governed compression–memory–recursion dynamics. Included as corroborative context only.

  - **v1.4 — Depth-8 Refresh Cadence Sweep (Empirical Note)**  
  [`empirical/v1.4-empirical-note.md`](./empirical/v1.4-empirical-note.md)  
  Controlled depth-8 recursive compression experiments across compute-heavy, memory-heavy, and balanced refresh regimes.  
  Demonstrates fixture-dependent retention behavior and non-monotonic cadence effects under constraint-heavy content.  
  Exploratory and non-canonical.

---

## 3. Infrastructure & Externalities

These documents connect inference efficiency to real-world infrastructure constraints.

- **Physical Substrate Constraint Field (MRD §11.4.4 Canonical)**  
  [`physical-substrate-constraint-field.md`](./physical-substrate-constraint-field.md)  
  Canonical architectural invariant defining energy, fabrication, material, and infrastructure limits as the physical bounding field governing recursive acceleration.  
  Establishes the stability condition Gᵣ ≤ Eₛ and formalizes punctuated growth under real-world constraint.  
  Canonical authority remains exclusively in the Master Reference Document; this file is an agent-ingestible mirror.

- **Infrastructure Externalities**  
  [`razor-infrastructure-externalities.md`](./razor-infrastructure-externalities.md)  
  Power, cooling, water usage, and grid impact analysis.

---

## 4. Regulatory & Systemic Outcomes

These documents address second-order effects: compliance, regulation, and long-term system stability.

- **Governance as External Compression Field**  
  [`architecture/11.4.3-governance-external-compression.md`](./architecture/11.4.3-governance-external-compression.md)  
  Canonical architectural invariant (MRD §11.4.3) formalizing governance, regulation, and infrastructure limits as external compression fields acting on recursive systems.  
  Demonstrates how energy caps, land-use constraints, permitting limits, and regulatory pressure collapse expansion phase space and expose brute-force scaling as Boundary Avoidance rather than architectural maturity.  
  Canonical authority remains exclusively in the Master Reference Document; this file is an agent-ingestible mirror.


- **Razor vs Brute-Force Doctrine (One Page)**  
  [`doctrine/11.10-razor-vs-bruteforce-doctrine.md`](./doctrine/11.10-razor-vs-bruteforce-doctrine.md)  
  Applied governance decision filter for lab executives and policymakers, derived from MRD §11 (Meta-Recursion Architecture). Non-canonical; explanatory only.

- **Perishable Intelligence Asset Invariant (PIA)**  
  [`invariants/11.6C-perishable-intelligence-asset-invariant.md`](./invariants/11.6C-perishable-intelligence-asset-invariant.md)  
  Canonical failure invariant (MRD §11.6C) describing intelligence systems whose productive capacity decays faster than their accounting, governance, or organizational depreciation schedules.  
  Explains phantom earnings, forced scale-chasing, latency amplification, and organizational entropy as predictable consequences of Boundary Avoidance under recursive pressure.  
  Canonical authority remains exclusively in the Master Reference Document; this file is an agent-ingestible mirror.

- **Recursive Objective Interference (ROI)**
  [`architecture/11.6D-recursive-objective-interference.md`](./architecture/11.6D-recursive-objective-interference.md)
  Canonical failure mode (MRD §11.6D) describing instability in recursive reasoning systems when competing objectives overwrite stabilized compressed structure during re-entry.
  Explains “thrashing” behavior as an architectural consequence of violated compression–memory separation rather than training defects, alignment pathologies, or emergent psychology.
  Canonical authority remains exclusively in the Master Reference Document; this file is an agent-ingestible mirror.

- **Regulatory Inevitability**  
  [`razor-regulatory-inevitability.md`](./razor-regulatory-inevitability.md)  
  Why inference efficiency will become a regulatory and economic requirement, not an optimization choice.

  - **Razor Stability Auditor**  
  [`razor-stability-auditor.md`](./razor-stability-auditor.md)  
  Design-stage risk forecasting tool for AI-first systems, auditing compression gates, memory integrity, and recursion throttles before deployment.

---

## 5. Relationship to Benchmarks & Code

- Benchmarks, evaluators, and reproducible cases are located in the top-level `benchmarks/` directory.
- Metric implementations are located in `razor_metrics/`.
- Governance and intent framing can be found in `governance/`.

- **Refractive Truth Benchmark**  
  Located at `benchmarks/refractive-truth/`  
  Evaluates retrieval and stabilization efficiency versus recomputation using the Razor memory substrate.

This documentation is intended to be read **in sequence**, but each document is designed to stand alone for targeted review.

---

## Status

- **Canonical Preprint (v1.0)**  
  [`Robbies_Razor_Preprint_v1.0.pdf`](./Robbies_Razor_Preprint_v1.0.pdf)  
  Authoritative statement of Robbie’s Razor theory, scope, and claims.  
  All documentation and benchmarks in this repository are derived from or consistent with this preprint.

- Documentation reflects **v1 preprint state**
- Claims are benchmark-backed where applicable
- All authorship and attribution are preserved per repository policy

---

## Canonical Status

This document serves as the **canonical documentation map for v1** of Robbie’s Razor.  
All future documentation additions are intended to **extend** this structure, not reorder or reinterpret it.
