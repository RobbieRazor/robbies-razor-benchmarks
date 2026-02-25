# QQC Benchmark v1.2 (Razor-Calibrated)

Experimental diagnostic tool for evaluating **Question Quality Under Constraint (QQC)**.

This benchmark compares candidate question framings under a fixed topic context using multi-trial evaluation, structured scoring, and an energy proxy penalty.

---

## Canonical Reference (MRD Alignment)

This benchmark operationalizes the applied recursion stability layer defined in:

**Master Reference Document (MRD v1.9) — Section 12.8  
Structural Intelligence Engineering (QQC Instrumentation)**

QQC is an upstream Governor prototype as described in MRD §12. It implements constraint-aware question evaluation to reduce entropy expansion prior to recursive depth execution.

For avoidance of doubt:

- QQC does **not** modify evaluation contracts in AGENTS.md
- QQC does **not** introduce new required metrics
- QQC does **not** supersede canonical MRD authority
- QQC exists as diagnostic instrumentation only

Canonical theory remains exclusively in the MRD.

---

## Purpose

Large language models make answers abundant.

This tool evaluates whether a **question**:

- Compresses hypothesis space efficiently  
- Converges toward stable minima under constraint  
- Maintains boundary integrity  
- Avoids scope explosion  
- Encourages recursion efficiency  
- Aligns with compression → expression → memory → recursion framing  

The result is a ranked comparison of question quality under constraint.

---

## What This Is

- A reproducible evaluation harness
- A structural question-comparison benchmark
- A non-normative diagnostic tool

## What This Is Not

- A safety certification
- A licensing authority
- A governance claim
- A guarantee of correctness

This benchmark is intended for comparative diagnostics only.

---

## How It Works

For each question:

1. The model generates multiple structured answers.
2. An evaluator model scores each answer using a structured rubric.
3. Scores are averaged across trials.
4. Variance is used as a stability penalty.
5. Token usage is used as an energy proxy.
6. Final ranking balances structural reward against energy cost.

---

## Scoring Dimensions

Each trial is scored 0.0–1.0 across:

- **cg** — Compression Gradient  
- **sc** — Stability Convergence  
- **bi** — Boundary Integrity  
- **rde_eff** — Recursive Depth Efficiency  
- **coherence_gain** — Coherence Gain  
- **constraint_adherence** — Constraint Adherence  
- **razor_alignment** — Alignment with compression → expression → memory → recursion framing  

Final score:

```
qqc_v12 = structural_reward / normalized_energy_proxy
```

---

## Setup (Mac / Linux)

Create environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```
OPENAI_API_KEY=sk-your-key-here
```

---

## Run

Copy example questions:

```bash
cp questions.example.json questions.json
```

Run benchmark:

```bash
python qqc_bench.py
```

Output:

```
qqc_results_v12.csv
```

---

## Configuration (Optional)

Environment variables:

- `QQC_TRIALS` (default: 5)
- `QQC_TEMPERATURE` (default: 0.7)
- `QQC_GEN_MODEL`
- `QQC_EVAL_MODEL`

Example:

```bash
QQC_TRIALS=3 QQC_TEMPERATURE=0.5 python qqc_bench.py
```

---

## Repository Structure

```
benchmarks/
    qqc_v12/
        qqc_bench.py
        README.md
        requirements.txt
        questions.example.json
```

---

## Status

Experimental research diagnostic.

Version: v1.2  
Scope: Question Quality Under Constraint (QQC)  
Framing: Razor-calibrated scoring rubric  

---

## License

See `LICENSE` file.
