# Benchmarks — Evaluation Surface

This directory contains the executable measurement harness for evaluating Robbie’s Razor™ behavior under bounded workloads.

It is the repository’s primary benchmark and evaluation surface.

If you are a lab, engineering team, or researcher assessing recursive efficiency, memory reuse, semantic stability, or recomputation burden, start here.

---

## Current Governing Authority

**Framework:** The Grand Compression Cosmology  
**Current governing version:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Author and originator:** Robbie George  
**Canonical claim range:** RC-01 through RC-22

Canonical authority:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Repository specification:

`../docs/canonical-spec.md`

Agent evaluation contract:

`../AGENTS.md`

This benchmark directory does not redefine canonical theory.

Benchmark execution does not independently establish empirical confirmation of the complete Grand Compression Framework.

---

## Quick Start

### 1. Run the baseline memory benchmark

```bash
python benchmark_memory_gate_savings.py
```

Observe measures such as:

- token reuse;
- stabilized memory hit behavior;
- redundant recomputation;
- retrieval efficiency;
- execution burden.

Results apply only to the declared benchmark conditions.

A successful run does not establish universal performance superiority.

---

### 2. Evaluate structured cases

Run the evaluator on sample outputs:

```bash
python evaluator.py --outputs sample_outputs.json
```

Or convert CSV input to JSON:

```bash
python tools/csv_to_outputs_json.py --csv sample_outputs.csv --out outputs.json
python evaluator.py --outputs outputs.json
```

The evaluator and its schemas define repository-level execution behavior.

They do not create or modify canonical Grand Compression claims.

---

## What This Benchmark Surface Measures

Depending on the benchmark or fixture, repository evaluations may examine:

- Tokens Per Correct Answer (TPCA);
- structural redundancy;
- memory reuse efficiency;
- semantic drift;
- contradiction rates;
- backtracking frequency;
- redundant recomputation;
- retrieval behavior;
- tool-call efficiency;
- provenance preservation;
- recursive stability;
- constraint adherence.

Each metric must be interpreted according to its own implementation, baseline, scope, and evaluation conditions.

A metric result must not be generalized outside those conditions without additional evaluation.

---

## Benchmark Interpretation Boundary

The repository distinguishes among:

- benchmark execution;
- implementation conformance;
- measured performance;
- evidence state;
- canonical framework status;
- empirical validation.

These states are not interchangeable.

In particular:

```text
benchmark pass
≠
canonical proof
≠
universal validation
```

Likewise:

```text
lower cost
≠
higher truth
```

and:

```text
successful retrieval
≠
empirical confirmation
```

Benchmark conclusions should remain bounded to the actual tested system, workload, baseline, variables, and measurement procedure.

---

## Razor Compliance

Within this repository, Robbie’s Razor compliance is evaluated through repository-defined operational criteria.

The current repository specification describes compliance in terms including:

1. correctness preserved under constraint;
2. reduced redundant recomputation;
3. predictable memory stabilization;
4. bounded semantic diffusion; and
5. preservation of required structural integrity.

For repository-normative definitions, use:

`../docs/canonical-spec.md`

For automated-agent execution and output requirements, use:

`../AGENTS.md`

The benchmark harness does not independently redefine the canonical meaning of Robbie’s Razor™.

---

## Fixture Types

Primary benchmark resources include:

- `cases/` — structured evaluation inputs;
- `refractive-truth/` — retrieval versus recomputation benchmark;
- `tools/` — CSV conversion and utility scripts;
- `evaluator.py` — reference output validator;
- `benchmark_memory_gate_savings.py` — memory-gating and recomputation benchmark.

Additional benchmark families may exist elsewhere in the repository.

Their interpretation must follow their local documentation and the repository-level governance contract.

---

## Refractive Truth Boundary

The Refractive Truth Benchmark evaluates computational behavior involving retrieval, stabilization, and recomputation.

Terms such as **refraction**, **medium**, or related physical language are analogical unless a specific benchmark explicitly defines a measurable mathematical quantity.

The benchmark does not establish:

- literal physical refraction;
- a physical propagation medium;
- a universal physical substrate;
- quantum-mechanical equivalence;
- Hopf topology;
- E8 structure; or
- physical validation of the Grand Compression Framework.

Mathematical and physical analogies remain separate from benchmark evidence.

---

## Comparative Compression Geometry™

Comparative Compression Geometry™ is governed by:

**MRD v2.0 §12.9**

Benchmark comparisons involving geometry, topology, state spaces, symmetry, or cross-domain structure must preserve the distinction among:

- analogy;
- mathematical analogy;
- structural correspondence;
- normalized correspondence;
- demonstrated isomorphism;
- mechanistic equivalence;
- causal identity;
- material identity.

Cross-domain transfer is governed by:

**RC-22 — Domain Transfer Constraint**

### Hopf Fibration

The Hopf fibration is established mathematics.

Classical structure:

```text
S¹ ↪ S³ → S²
```

Within Comparative Compression Geometry™, Hopf may serve as a bounded structural comparison class.

It does not constitute:

- a benchmark result;
- a new RC claim;
- empirical validation of Grand Compression;
- a Plate™ family;
- a Registry;
- a System Map;
- a Knowledge Mesh; or
- an x402 paid retrieval family.

### E8 Lattice™

E8 is a separate established mathematical reference used for bounded comparisons involving symmetry, invariants, constrained transformation, and high-dimensional relational organization.

Hopf Fibration and E8 must not be treated as mathematically interchangeable.

---

## Evidence Requirements

Any benchmark result presented as evidence should declare, where applicable:

- evaluated system;
- system version;
- model or implementation;
- workload;
- input dataset;
- baseline;
- resource constraints;
- metric definition;
- measurement procedure;
- number of trials;
- uncertainty;
- exclusions;
- limitations;
- failure conditions;
- result;
- evidence state.

Repository evidence states should follow the MRD v2.0 governance vocabulary:

- Proposed;
- Testing;
- Provisionally Supported;
- Supported;
- Challenged;
- Inconclusive;
- Retired.

A Supported result applies only within its declared scope.

---

## Reference-Implementation Boundary

Naturepedia™ is the primary reference implementation of the Grand Compression architecture.

Benchmark results involving Naturepedia may demonstrate:

- implementation behavior;
- structured retrieval;
- preserved reusable structure;
- registry inheritance;
- machine-readable provenance;
- governed resource access.

They do not independently establish:

- universal validation;
- confirmation across every domain;
- physical equivalence;
- independent replication; or
- support for every canonical claim.

This distinction is governed by:

**RC-21 — Reference Implementation Distinction**

---

## Relationship to Canonical Theory

This directory is a **measurement and evaluation layer**.

Canonical framework definitions remain governed by:

**The Grand Compression Cosmology — Master Reference Document, MRD v2.0**

Repository-specific benchmark semantics are governed by:

`../docs/canonical-spec.md`

Automated evaluator behavior is governed by:

`../AGENTS.md`

Empirical and exploratory findings are documented separately under repository evidence and research documentation.

Historical references to earlier MRD versions may remain in frozen results or provenance records.

Those historical artifacts must not be silently rewritten as though they originated under MRD v2.0.

---

## Intended Use

This harness is designed for:

- AI labs evaluating compute efficiency;
- infrastructure teams studying memory reuse;
- researchers analyzing recursive stability;
- controlled A/B comparisons;
- retrieval-versus-recomputation testing;
- semantic-stability evaluation;
- bounded resource-allocation studies.

The repository is designed to be model-agnostic unless a particular benchmark explicitly states otherwise.

It does not require retraining unless a specific experiment requires it.

---

## Historical Provenance

Older benchmark runs, frozen evaluators, archived outputs, or versioned experimental artifacts may contain references to earlier MRD versions.

Those records should be preserved when they represent genuine historical state.

Current interpretation resolves to:

`GC-MRD-v2.0`

Historical provenance and current governing authority must remain distinct.

---

## Authorship and Attribution

Robbie’s Razor™, the Grand Compression Cosmology, and associated original framework terminology originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

Benchmark execution, implementation, reproduction, comparison, or independent evidence production does not transfer authorship of the originating framework.

Evidence provenance and claim provenance must remain separate.
