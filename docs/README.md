# Docs

This folder contains reference documentation for the repository.

## Architecture

- **Post-Simplification Reconstruction Principle (PSRP)** — Explains why simplified systems (distilled, pruned, quantized, or edge-deployed) accelerate after simplification, how drift emerges under local reconstruction without upstream context, and why early reconstruction rules harden into permanent attractors.  
  → `architecture/post_simplification_reconstruction.md`  
  *(Canonical authority: MRD v1.8 §11.9)*

## Preprints

- **Robbie’s Razor: A Scale-Invariant Recursion Principle for Efficient Intelligence (Preprint v1.0)**  
  → `Robbies_Razor_Preprint_v1.0.pdf`

- **Robbie’s Razor: Recursive Stability Under Resource Constraints (Preprint v1.1 — Tier-1 ML Draft)**  
  → `Robbies_Razor_Preprint_v1.1.pdf`

**Preprint evolution note:**  
Preprint v1.0 establishes the canonical cross-domain formulation of the compression → expression → memory → recursion cycle as a scale-invariant structural principle.  
Preprint v1.1 extends this formulation with a minimal entropy-update model, a stability-minimum footprint under fixed compute+memory budgets, and a Lyapunov-based convergence condition.  
v1.1 provides an analytical backbone while preserving the structural ordering defined in v1.0.
