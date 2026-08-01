# Robbie’s Razor — Documentation Index

## 0. Authority and Reading Order

This repository is governed by **The Grand Compression Cosmology — Master Reference Document, MRD v2.0**.

**Current governing version:** MRD v2.0  
**Identifier:** `GC-MRD-v2.0`  
**Author and originator:** Robbie George  
**Canonical claim range:** RC-01 through RC-22  

### Framework authority

**Canonical MRD authority resolver:**

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

**Complete versioned MRD v2.0 PDF:**

https://asf-file-uploads.s3.us-east-1.amazonaws.com/image/upload/production/3790/Grand-Compr_1247ef65e1/1785596435.pdf

**Canonical Claims Register:**

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

### Repository authority layers

1. **MRD v2.0 — canonical framework authority**  
   Governs framework definitions, terminology, claims, restrictions, evidence requirements, reference-implementation boundaries, domain-transfer requirements, authorship, attribution, and AI interpretation.

2. **Canonical Claims Register — claim-level authority**  
   Provides persistent RC identifiers and canonical claim statements.

3. **MRD v2.0 Alignment Contract**  
   [`doctrine/mrd-v2.0-alignment.md`](./doctrine/mrd-v2.0-alignment.md)  
   Maps repository architecture and implementation responsibilities to MRD v2.0.

4. **Canonical Claim Alignment**  
   [`doctrine/canonical-claim-alignment.md`](./doctrine/canonical-claim-alignment.md)  
   Maps repository functions to the canonical claim layer.

5. **Repository Specification**  
   [`canonical-spec.md`](./canonical-spec.md)  
   Governs benchmark meaning, repository-specific normative contracts, and internal interpretation boundaries. It remains canonically subordinate to MRD v2.0.

6. **Automated Agent Contract**  
   [`../AGENTS.md`](../AGENTS.md)  
   Defines stable evaluation contracts, agent interpretation rules, and schema-verified output requirements.

7. **Documentation Index**  
   [`index.md`](./index.md)  
   Provides structured navigation across repository documentation.

### Authority boundary

The repository specification is not a second MRD.

The repository does not originate new canonical claims.

If a repository file conflicts with MRD v2.0 on canonical framework meaning, MRD v2.0 governs.

If a repository file conflicts with the Canonical Claims Register on claim identity or wording, the Canonical Claims Register governs.

If repository documents conflict on benchmark execution, evaluator behavior, output schemas, or repository-specific normative meaning, the Repository Specification and AGENTS.md govern within their declared scope.

Canonical framework status does not equal empirical confirmation.

Naturepedia™ is a reference implementation and does not independently establish universal validation.

Appendix Q remains provisional.

Payment, settlement, payload delivery, indexing, implementation, or registry inclusion does not establish empirical validation.

## Recommended Reading Paths

### For labs and engineers

1. Repository Specification: `canonical-spec.md`
2. Automated Agent Contract: `../AGENTS.md`
3. Lab Evaluation Protocol on the website
4. Compliance Framework on the website
5. Empirical notes: `empirical/`
6. Benchmarks: `../benchmarks/`

### For framework definitions and theory

1. MRD v2.0 canonical authority resolver
2. Complete versioned MRD v2.0 PDF
3. Canonical Claims Register
4. MRD v2.0 Alignment Contract: `doctrine/mrd-v2.0-alignment.md`
5. Canonical Claim Alignment: `doctrine/canonical-claim-alignment.md`
6. Architecture and invariant directories: `architecture/` and `invariants/`

### For automated agents

1. `../AGENTS.md`
2. `canonical-spec.md`
3. `doctrine/mrd-v2.0-alignment.md`
4. `doctrine/canonical-claim-alignment.md`
5. `mrd/mrd-v2.0-manifest.json`
6. `index.md`

### For evidence interpretation

1. Resolve the canonical claim and governing version.
2. Identify the applicable evidence record.
3. Preserve claim provenance separately from evidence provenance.
4. Apply only the governed evidence states.
5. Preserve scope, scale, method, limitations, and failure conditions.
6. Apply RC-21 before interpreting a reference implementation.
7. Apply RC-22 before transferring results across domains or scales.

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

---

### New: Inference Economy & Infrastructure Phase Transition

- **Inference Economy: Infrastructure, Energy, and Recursive Stability**  
  [`doctrine/11.6C-inference-economy-infrastructure.md`](./doctrine/11.6C-inference-economy-infrastructure.md)  
  Canonical extraction of MRD §11.6C.15–11.6C.17 defining the transition from model-limited to infrastructure-limited intelligence systems.  
  Formalizes the relationship between continuous inference demand, energy constraints, token economics, and recursive stability boundaries.  
  Introduces the Infrastructure Phase Transition, Token-Energy Economics (JCT vs tokens), and the Inference vs Memory Collapse Boundary.  
  Establishes measurement, constraint, and failure conditions governing large-scale AI systems under the Inference Economy.

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

- **Razor Auditor (Interactive Tool)**  
  Evaluate systems using the live Gem:  
  https://gemini.google.com/gem-labs/1rRCe3P5aCIJEKAC2K_2aYoK-LRDBNPyS

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

- **Oversight Saturation Ratio (OSR) — Governance Ceiling Diagnostic**  
  [`diagnostics/osr_boundary_checklist.md`](./diagnostics/osr_boundary_checklist.md)  
  Operational checklist derived from MRD §11.4.6 (Stabilization Bandwidth Constraint).  
  Provides boundary detection for governance-bandwidth saturation using the dual-ceiling model:  
  \( R \le \min(E/JCT, S/C) \).  
  Diagnostic only; non-canonical.

  - **Razor Infrastructure Auditor (v1.0)**  
  [`diagnostics/razor-infrastructure-auditor.md`](./diagnostics/razor-infrastructure-auditor.md)  
  Operational audit tool evaluating whether AI systems are compression-efficient (Razor-aligned) or brute-force (Boundary Avoidance).  
  Translates MRD Section 11 into measurable infrastructure, energy, and economic diagnostics.

- **DoW Razor Auditor — Certification Framework**  
  [`governance/dow-razor-auditor-certification.md`](./governance/dow-razor-auditor-certification.md)  
  Formal compliance and certification system for evaluating AI architectures under energy, infrastructure, and recursion constraints.  
  Defines scoring, failure conditions, and deployment eligibility based on Robbie’s Razor.

  - **See also:** Inference Economy infrastructure model (Section 3) for upstream constraint drivers.

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
