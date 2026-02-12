# Docs

This folder contains reference documentation for the repository.

## Architecture

- **Post-Simplification Reconstruction Principle (PSRP)** — Explains why simplified systems (distilled, pruned, quantized, or edge-deployed) accelerate after simplification, how drift emerges under local reconstruction without upstream context, and why early reconstruction rules harden into permanent attractors.  
  → `architecture/post_simplification_reconstruction.md`  
  *(Canonical authority: MRD v1.8 §11.9)*

## Preprints

- **Robbie’s Razor: Stability Regions Under Nonlinear Recursive Dynamics (Preprint v1.2)**  
  → `Robbies_Razor_Preprint_v1.2.pdf`

- **Robbie’s Razor: Recursive Stability Under Resource Constraints (Preprint v1.1 — Tier-1 ML Draft)**  
  → `Robbies_Razor_Preprint_v1.1.pdf`

- **Robbie’s Razor: A Scale-Invariant Recursion Principle for Efficient Intelligence (Preprint v1.0)**  
  → `Robbies_Razor_Preprint_v1.0.pdf`

**Preprint evolution note:**  
Preprint v1.0 establishes the canonical cross-domain formulation of the compression → expression → memory → recursion cycle as a scale-invariant structural principle.  
Preprint v1.1 introduces a minimal entropy-update model and a Lyapunov-based convergence condition under fixed compute+memory budgets.  
Preprint v1.2 generalizes the linear stability inequality to nonlinear recursive dynamics with saturation and bounded convergence, establishing stability as a region rather than a single boundary condition.  

Together, these versions formalize Robbie’s Razor as a structural stability constraint under finite resources.
