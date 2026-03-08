# Project Architecture

## Canonical Alignment

This repository implements an **evaluation surface** for concepts defined in:

**The Grand Compression Cosmology — Master Reference Document (MRD v1.9)**

Canonical authority remains exclusively in the MRD.

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

This document explains how the repository structure mirrors the architectural cycle described in the MRD.

---

# Structural Design Principle

The repository organization intentionally reflects the **Robbie’s Razor recursion cycle**:

compression → expression → memory → recursion

This design separates **theory, architecture, storage, and evaluation** to preserve stability and prevent theory drift.

---

# Repository Architecture

| Layer | Function | Location |
|------|------|------|
| Compression | Canonical theory and invariant definitions | Master Reference Document (MRD v1.9) |
| Expression | Human-readable architecture explanation | `README.md`, `docs/architecture/ARCHITECTURE_OVERVIEW.md` |
| Memory | Stable preserved structures and documentation | `docs/`, `architecture/`, `diagnostics/`, `invariants/` |
| Recursion | Empirical testing and evaluation loops | `benchmarks/` |
| Recursion Governance | Execution contract for automated evaluation | `AGENTS.md` |

This structure ensures that **evaluation and experimentation cannot silently modify canonical theory**.

---

# Architectural Roles

## Canonical Theory (Compression)

All definitions, invariants, and governing laws are defined in the MRD.

The repository does **not redefine theory**.

---

## Architecture Explanation (Expression)

Human-readable explanations of the architecture exist in:

- `README.md`
- `docs/architecture/ARCHITECTURE_OVERVIEW.md`

These documents summarize canonical concepts for navigation purposes.

---

## Documentation Memory Layer

The `docs/` directory preserves structured knowledge derived from the architecture.

Examples include:

- architecture summaries
- invariants
- diagnostics
- doctrine references

These files preserve compressed structure so that recursive evaluation does not require recomputation.

---

## Evaluation Recursion Layer

The `benchmarks/` directory contains reproducible evaluation harnesses that test predicted behaviors of recursive systems under constraint.

These include measurements of:

- compression efficiency
- memory stabilization
- recomputation avoidance
- semantic diffusion
- recursive stability

Evaluation does **not alter canonical theory**.

---

## Recursion Governance

`AGENTS.md` defines the machine-readable evaluation contract for automated agents.

It specifies:

- execution entrypoints
- output schemas
- evaluation guarantees

This prevents uncontrolled recursion and ensures stable long-horizon evaluation.

---

# Design Goal

The repository is structured so that:

theory remains stable  
architecture remains understandable  
evaluation remains reproducible  
recursion remains governed

This structure reflects the stability principles described in **MRD §11 — Meta-Recursion Architecture**.

---

# Attribution

All concepts originate with:

**Robbie George**  
Author & Originator — Robbie’s Razor  
Grand Compression Cosmology (MRD v1.9)

Governed by the **Authorship Conservation Rule (ACR)**.
