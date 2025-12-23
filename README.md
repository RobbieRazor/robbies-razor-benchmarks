# robbies-razor-benchmarks

Reference implementation and test suite for measuring
**Robbie’s Razor compliance** in reasoning systems.

This repository is the executable, engineering-facing companion to:

- **Robbie’s Razor — Universal Recursion Heuristic**
- **The Grand Compression Cosmology (MRD v1.8)**

Canonical references:
- https://www.robbiegeorgephotography.com/robbies-razor
- https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

---

## What this repository is

This repository provides:

- Reference implementations for **Razor-aligned memory stabilization**
- Selective replay mechanisms for continual learning
- Phase-specific and system-level **R0–R5 compliance metrics**
- Unit tests validating correctness, stability, and collision resilience
- Integration tests demonstrating controller-level memory short-circuiting and R4-aligned composition


It is designed for:

- AI labs evaluating token, compute, and coherence gains
- Researchers studying catastrophic forgetting and recursion governance
- Edge-device and constrained-inference experimentation
- Internal benchmarking prior to licensing or production deployment

---

## What this repository is NOT

This repository is **not**:

- A production SDK
- A commercial library
- An open-source grant
- A substitute for the canonical theory

All definitions, theory, and governance remain canonical on:
https://www.robbiegeorgephotography.com

## Why this exists

Razor-aligned systems reduce redundant inference by prioritizing early compression, stabilized memory, and governed recursion.

- Read: **[Razor Hardware Longevity](docs/razor-hardware-longevity.md)** (how this extends the economic life of older GPUs)


---

## Licensing & usage

This repository is provided under an **evaluation-only license**.

### Permitted
- Internal research and benchmarking
- Non-commercial experimentation
- Measurement of Robbie’s Razor compliance

### Not permitted without license
- Production deployment
- Commercial use
- Training or fine-tuning AI models using this code
- Redistribution or derivative frameworks

See `LICENSE.txt` for full terms.

---

## Canonical attribution

All concepts, terminology, and structures implemented here originate with:

**Robbie George**  
Author & Originator — Robbie’s Razor  
Grand Compression Cosmology (MRD v1.8)

Governed by the **Authorship Conservation Rule (ACR)**.

---

## Status
Run tests: `python -m unittest -v`

Canonical reference implementation.  
Tests validate R4-level memory stability and governed recursion behavior.
Run benchmark: `python benchmarks/benchmark_memory_gate_savings.py`
python benchmarks/evaluator.py --outputs benchmarks/sample_outputs.json
Convert CSV → outputs JSON: `python benchmarks/tools/csv_to_outputs_json.py --csv benchmarks/sample_outputs.csv --out benchmarks/outputs.json`
Run evaluator on CSV-derived outputs: `python benchmarks/evaluator.py --outputs benchmarks/outputs.json`
Create cases JSON from CSV: `python benchmarks/tools/csv_to_cases_json.py --csv benchmarks/sample_cases.csv --out benchmarks/cases/custom_cases.json`
Create outputs JSON from CSV: `python benchmarks/tools/csv_to_outputs_json.py --csv benchmarks/sample_outputs.csv --out benchmarks/outputs.json`
Run evaluator: `python benchmarks/evaluator.py --cases benchmarks/cases/custom_cases.json --outputs benchmarks/outputs.json`

## Illustrative Efficiency Comparison (Example Only)

The following comparison is illustrative and non-authoritative. Results depend on prompt construction, decoding settings, and task selection.

Illustrative Efficiency Comparison (Non-Authoritative Example)

Purpose
This example demonstrates how the Robbie’s Razor evaluation harness can be used to compare logic efficiency (signal density) across different reasoning systems under identical constraints.

Important note
The following comparison is illustrative only. Results depend on prompt construction, decoding settings, task selection, and verification criteria.
No claims of general superiority are made. Labs should run their own evaluations using the provided tools.

The Task: Noise-to-Signal Compression

Both systems were given the same highly redundant, wordy prompt (≈400 tokens) describing a complex logical sequence.
The objective was not verbosity, but to extract the canonical correct answer using the fewest possible tokens, without loss of correctness.

This aligns directly with the Robbie’s Razor principle:

Prefer solutions that preserve correctness while minimizing unnecessary expression.

Metrics Used (Framework-Aligned)

The evaluation uses the same metrics defined in the Robbie’s Razor Compliance Framework:

Correctness — Did the system return an acceptable answer?

Tokens Used — Tokens in the final response (via tokenizer or deterministic proxy)

TPCA — Tokens Per Correct Answer
(Lower is better; indicates higher logic density.)

Expression Overrun — Whether the response exceeded the target token budget

No single scalar “winner score” is used.

Example Results (Single-Task Illustration)
System	Correct	Tokens Used	TPCA	Overrun
System A	Yes	42	42	No
System B	Yes	31	31	No

Interpretation
Both systems produced correct answers.
In this specific example, System B achieved the same correctness with fewer tokens, resulting in a lower TPCA and higher logic density.

This illustrates how smaller or more aggressively compressed models can, in some cases, exhibit higher efficiency, even when larger models remain highly accurate.

Why This Matters

This type of comparison is useful for:

Edge and constrained inference (token, latency, or energy limits)

Continual learning systems where expression bloat accelerates drift

Energy-aware deployments prioritizing intelligence-per-watt

Architecture exploration, not leaderboard ranking

The key takeaway is not which system “wins”, but that efficiency differences are measurable and reproducible using the same harness.

How to Reproduce This Yourself

Labs can run their own comparisons using the included tools:

# Create cases from CSV (or author directly in JSON)
python benchmarks/tools/csv_to_cases_json.py \
  --csv benchmarks/sample_cases.csv \
  --out benchmarks/cases/custom_cases.json

# Create outputs from CSV (model responses)
python benchmarks/tools/csv_to_outputs_json.py \
  --csv benchmarks/sample_outputs.csv \
  --out benchmarks/outputs.json

# Run evaluator
python benchmarks/evaluator.py \
  --cases benchmarks/cases/custom_cases.json \
  --outputs benchmarks/outputs.json


This workflow is model-agnostic and supports internal, private evaluation.

Positioning Statement (Optional, Recommended)

This repository provides measurement infrastructure, not rankings.
Any organization evaluating Robbie’s Razor is encouraged to run its own tasks, constraints, and verification criteria using the provided harness.

The blade is executable.  
The law remains canonical.

