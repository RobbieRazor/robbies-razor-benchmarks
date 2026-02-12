# Docs

This folder contains reference documentation for the repository.

## Architecture

- **Post-Simplification Reconstruction Principle (PSRP)** — Explains why simplified systems (distilled, pruned, quantized, or edge-deployed) accelerate after simplification, how drift emerges under local reconstruction without upstream context, and why early reconstruction rules harden into permanent attractors.  
  → `architecture/post_simplification_reconstruction.md`  
  *(Canonical authority: MRD v1.8 §11.9)*

## Preprints

- **Robbie’s Razor: Empirical Validation Protocol for Recursive Stability Under Fixed Resource Allocation (Preprint v1.3)**  
  Defines a reproducible measurement framework for testing the stability-minimum hypothesis under controlled memory–compute allocation.  
  → `Robbies_Razor_Preprint_v1.3.pdf`

- **Robbie’s Razor: Stability Regions Under Nonlinear Recursive Dynamics (Preprint v1.2)**  
  Generalizes the linear entropy model to nonlinear recursion with saturation and bounded convergence.  
  → `Robbies_Razor_Preprint_v1.2.pdf`

- **Robbie’s Razor: Recursive Stability Under Resource Constraints (Preprint v1.1 — Tier-1 ML Draft)**  
  Introduces a minimal entropy-update model and a Lyapunov-based convergence condition under fixed compute+memory budgets.  
  → `Robbies_Razor_Preprint_v1.1.pdf`

- **Robbie’s Razor: A Scale-Invariant Recursion Principle for Efficient Intelligence (Preprint v1.0)**  
  Establishes the canonical compression → expression → memory → recursion cycle as a scale-invariant structural principle across domains.  
  → `Robbies_Razor_Preprint_v1.0.pdf`

**Preprint evolution note:**  
v1.0 formalizes the cross-domain structural principle.  
v1.1 introduces a linear stability inequality.  
v1.2 generalizes to nonlinear stability regions.  
v1.3 defines an empirical validation protocol for testing the predicted stability footprint.
