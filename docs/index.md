# Robbie’s Razor — Documentation Index

This directory contains the formal documentation, analysis, and contextual framing for **Robbie’s Razor**, an inference-efficiency and memory-coherence framework designed to reduce compute, energy, and regulatory externalities in large-scale AI systems.

The documents below are organized to guide readers from **core metric definitions**, through **hardware and infrastructure implications**, and finally to **regulatory and systemic outcomes**.

---

## 1. Core Metrics & Theory

These documents define the primary metrics and conceptual foundations used throughout the benchmark and evaluation pipeline.

- **Razor Diffusion Metric**  
  [`razor-diffusion-metric.md`](./razor-diffusion-metric.md)  
  Defines the diffusion-based efficiency metric used to evaluate inference stability, memory reuse, and entropy suppression.

---

## 2. Hardware & System Implications

These documents explore how Razor-aligned architectures impact hardware lifespan, memory pressure, and system-level efficiency.

- **GPU Longevity**  
  [`razor-gpu-longevity.md`](./razor-gpu-longevity.md)  
  Analysis of how reduced inference diffusion extends effective GPU service life.

- **Hardware Longevity (Generalized)**  
  [`razor-hardware-longevity.md`](./razor-hardware-longevity.md)  
  Broader implications across accelerators, memory, and interconnects.

---

## 3. Infrastructure & Externalities

These documents connect inference efficiency to real-world infrastructure constraints.

- **Infrastructure Externalities**  
  [`razor-infrastructure-externalities.md`](./razor-infrastructure-externalities.md)  
  Power, cooling, water usage, and grid impact analysis.

---

## 4. Regulatory & Systemic Outcomes

These documents address second-order effects: compliance, regulation, and long-term system stability.

- **Regulatory Inevitability**  
  [`razor-regulatory-inevitability.md`](./razor-regulatory-inevitability.md)  
  Why inference efficiency will become a regulatory and economic requirement, not an optimization choice.

---

## 5. Relationship to Benchmarks & Code

- Benchmarks, evaluators, and reproducible cases are located in the top-level `benchmarks/` directory.
- Metric implementations are located in `razor_metrics/`.
- Governance and intent framing can be found in `governance/`.

This documentation is intended to be read **in sequence**, but each document is designed to stand alone for targeted review.

---

## Status

- Documentation reflects **v1 preprint state**
- Claims are benchmark-backed where applicable
- All authorship and attribution are preserved per repository policy

  ---

## Canonical Status

This document serves as the **canonical documentation map for v1** of Robbie’s Razor.
All future documentation additions are intended to **extend** this structure, not reorder or reinterpret it.

