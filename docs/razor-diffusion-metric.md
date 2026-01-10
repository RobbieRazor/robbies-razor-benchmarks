# Razor Diffusion Metric (RDM)

## Purpose
The Razor Diffusion Metric (RDM) measures **semantic diffusion per unit compute**
during AI inference. It distinguishes efficient, disciplined reasoning from
token-heavy or unguided probability radiation.

## Baseline Definition

Let:
- e_t be the embedding at reasoning step t
- c_t be the compute cost at step t (tokens or proxy)

Semantic step distance (bounded):
Δ_t = 1 − ⟨ê_{t−1}, ê_t⟩

where ê_t denotes the ℓ₂-normalized embedding at step t, ensuring Δ_t ∈ [0,2].

Cumulative diffusion:
D_T = Σ Δ_t

Total cost:
C_T = Σ c_t

Baseline RDM:
RDM = D_T / C_T

Lower is better.

## Governance Extension (RDM*)

Efficiency alone is insufficient. To prevent pathological cases
(e.g. looping, stalling), RDM incorporates **boundary adherence**.

Let b_t ∈ [0,1] be the Razor compliance score at step t.

Mean adherence:
A = mean(b_t)

Composite metric:
RDM* = RDM × (1 − A)

Only reasoning that is both efficient and governed achieves a strong score.

## Boundary Rules (v1.0)

b_t is computed as the mean of binary rule checks:

1. Memory Reuse
2. Non-Redundancy
3. Constraint Respect
4. Directional Progress

Each rule returns 0 or 1.
