# Repository Specification — Robbie’s Razor™ Benchmarks

**Status:** Repository-Normative / Canonically Subordinate to MRD v2.0  
**Applies to:** `robbies-razor-benchmarks` repository  
**Author and originator:** Robbie George  
**Current governing MRD:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Canonical claim range:** RC-01 through RC-22  
**Repository spec version:** 1.3  
**Last updated:** 2026-08-23

---

# 1. Canonical Authority

The current governing framework authority is:

**The Grand Compression Cosmology — Master Reference Document, MRD v2.0**

Canonical authority:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Robbie’s Razor™:

https://www.robbiegeorgephotography.com/robbies-razor

Robbie’s Razor Compliance Framework:

https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework

Primary repository authority documents:

```text
docs/AUTHORITY.md
docs/doctrine/mrd-v2.0-alignment.md
docs/doctrine/canonical-claim-alignment.md
docs/mrd/mrd-v2.0-manifest.json
AGENTS.md
```

MRD v2.0 governs:

- canonical framework definitions;
- canonical terminology;
- canonical claim identity;
- authorship and attribution;
- evidence requirements;
- reference-implementation boundaries;
- cross-domain interpretation;
- provisional-status rules;
- AI-agent interpretation.

This repository specification governs only the **repository-specific meaning of benchmark execution, evaluator behavior, schemas, implementation contracts, and result interpretation**.

If this file conflicts with MRD v2.0 or the Canonical Claims Register on canonical framework meaning:

```text
MRD v2.0 governs
```

---

# 2. Repository Role

This repository is an:

- implementation surface;
- benchmarking surface;
- evaluation surface;
- diagnostic surface;
- doctrine-alignment layer;
- structured-example layer;
- machine-readable governance layer;
- reproducibility surface.

It is not:

- a replacement MRD;
- an independent validating institution;
- a production certification;
- proof that all canonical claims are empirically supported;
- authorization to redefine Robbie’s Razor™ or Grand Compression terminology.

Naturepedia™ is the primary reference implementation of the broader Grand Compression architecture.

Reference implementation status demonstrates implementation.

It does not independently establish universal theoretical validity.

---

# 3. Historical-Version Boundary

Earlier MRD versions remain part of the framework’s historical provenance.

Historical materials may include:

- preprints;
- archived notes;
- frozen benchmark runs;
- frozen evaluators;
- older result bundles;
- version-specific diagrams.

Do not silently rewrite genuine historical provenance merely to make every artifact say `MRD v2.0`.

Required distinction:

```text
historical authority at publication
≠
current governing authority
```

Current interpretation resolves to MRD v2.0.

Historical artifacts retain their original version identity.

---

# 4. Scope: Normative vs Non-Normative

## Normative within this repository

The following are repository-normative within their declared scope:

- benchmark input and output contracts;
- evaluator behavior;
- schemas;
- scoring implementations;
- deterministic fixture handling;
- benchmark-local definitions;
- test expectations;
- evidence interpretation boundaries;
- implementation classification;
- historical-artifact handling;
- machine-readable fidelity rules.

## Non-Normative unless explicitly promoted

The following remain explanatory or interpretive unless separately governed:

- metaphors;
- diagrams;
- analogies;
- worldview framing;
- infrastructure extrapolations;
- economic extrapolations;
- policy implications;
- cross-domain illustrations;
- speculative physical interpretation.

A non-normative explanation must not silently become a benchmark rule or canonical claim.

---

# 5. What “Robbie’s Razor Compliance” Means Here

Within this repository, **Razor compliance** means conformance to the declared benchmark and implementation contract being evaluated.

Depending on the benchmark, this may include whether:

1. expected task behavior is preserved under declared constraints;
2. redundant recomputation is reduced relative to a declared baseline;
3. supplied memory-confidence rules behave according to the implementation contract;
4. replay-priority behavior follows the configured scoring rule;
5. semantic diffusion or other repository metrics remain within declared benchmark thresholds;
6. required provenance, identity, or structured state is preserved;
7. outputs satisfy the applicable schema and evaluator rules.

The repository MUST preserve the distinction:

```text
benchmark correctness
=
agreement with declared benchmark targets
```

not:

```text
benchmark correctness
=
independent universal truth
```

A benchmark may contain reference answers, expected outputs, or acceptable-answer sets.

Those are **benchmark-local evaluation targets** unless independently established otherwise.

Accordingly:

```text
benchmark pass
≠
universal factual proof
```

and:

```text
Razor compliance
≠
empirical validation of the complete framework
```

This repository does not, merely through a compliance result, claim:

- production readiness;
- vendor superiority;
- universal reasoning superiority;
- hardware displacement;
- universal performance dominance;
- scientific confirmation of every Grand Compression claim.

---

# 6. Correctness Boundary

The term **correctness** in executable benchmark contexts refers to satisfaction of the benchmark’s declared evaluation rule.

Examples may include:

- exact match;
- acceptable-answer membership;
- numeric tolerance;
- substring / contains matching;
- schema conformance;
- deterministic expected behavior.

These rules are operational.

They do not independently establish philosophical, scientific, or universal truth.

Required distinction:

```text
passes evaluator
≠
proven true in every external context
```

Any benchmark claiming external factual validity should identify:

- source;
- dataset;
- authority;
- evaluation method;
- uncertainty;
- scope;
- revision conditions.

---

# 7. Core Repository Contracts

## 7.1 Agent and evaluation contract

Automated evaluators and coding agents should follow:

```text
AGENTS.md
```

AGENTS.md defines repository execution and interpretation boundaries.

## 7.2 Reference evaluator

The primary evaluator is:

```text
benchmarks/evaluator.py
```

Its implemented scoring rules define benchmark-local behavior.

Evaluator behavior does not redefine canonical Grand Compression theory.

## 7.3 Repository authority

Authority and attribution are governed by:

```text
docs/AUTHORITY.md
```

## 7.4 MRD alignment

Implementation alignment is governed by:

```text
docs/doctrine/mrd-v2.0-alignment.md
```

---

# 8. Context Rot

Within this repository, **Context Rot** is an operational label for observed or measured degradation associated with increasing context length, iteration count, or recursive processing under a declared evaluation.

Possible manifestations may include:

- drift;
- looping;
- redundancy;
- contradiction;
- loss of task relevance;
- reduced benchmark performance;
- loss of semantic coherence.

Repository references include:

```text
docs/context_rot_explainer.md
docs/context_rot_illustration.json
```

Context Rot is not automatically established merely because a response is long or complex.

A measured claim should identify:

- task;
- model;
- context size;
- baseline;
- metric;
- observed change;
- uncertainty;
- alternative explanations.

---

# 9. Razor Diffusion Metric

Repository materials may use **Razor Diffusion Metric (RDM / RDM*)** as an implementation-specific measurement surface.

Primary references include:

```text
docs/razor-diffusion-metric.md
razor_metrics/rdm.py
razor_metrics/facets.py
razor_metrics/shear.py
razor_metrics/boundary.py
```

RDM values are repository metrics.

They MUST NOT automatically be interpreted as:

- universal intelligence scores;
- universal truth measures;
- universal entropy measures;
- scientific constants.

Any empirical interpretation remains bounded by the implemented metric and evaluation conditions.

---

# 10. Memory Primitive — RazorMemoryBank

The repository reference memory primitive is:

```text
src/razor/memory_bank.py
```

Its implementation may:

- store entries;
- associate supplied confidence values;
- gate retrieval according to a configured confidence threshold;
- short-circuit recomputation when a qualifying stored entry is returned;
- evict entries according to the configured policy.

The implementation does **not** independently verify the truth of a stored result merely because its supplied confidence exceeds a threshold.

Required distinction:

```text
confidence threshold passed
≠
verification
```

```text
retrieved from memory
≠
revalidated
```

```text
stored
≠
correct
```

```text
high supplied confidence
≠
independent evidence
```

Accordingly, the phrase **confidence-gated retrieval** is preferred over language implying that the implementation itself proves or stabilizes truth.

---

# 11. Memory Stabilization

Within repository benchmark language, **memory stabilization** may describe predictable behavior of the declared storage, retrieval, threshold, and eviction mechanism.

It does not mean:

- factual verification;
- epistemic certainty;
- universal semantic stability;
- immunity from stale or incorrect memory.

A stored incorrect result may remain consistently retrievable.

Therefore:

```text
stable retrieval
≠
correct retrieval
```

External validation or revalidation must be specified separately when required.

---

# 12. Selective Replay

The repository selective-replay implementation is:

```text
src/razor/selective_replay.py
```

Replay priority may use caller-supplied inputs such as:

- loss;
- confidence;
- rarity.

These values influence an implementation-specific composite priority score.

Required distinctions:

```text
high replay score
≠
proven incorrect example
```

```text
high replay score
≠
objective instability
```

```text
loss input
≠
automatically information-theoretic entropy
```

The implementation tests priority and sampling behavior.

It does not independently prove a universal theory of replay or learning.

---

# 13. Refractive Truth Benchmark

The Refractive Truth Benchmark is an engineering evaluation harness.

Primary reference:

```text
benchmarks/refractive-truth/README.md
```

Runner:

```text
benchmarks/refractive-truth/harness.py
```

It may compare retrieval/reuse behavior against recomputation under declared constraints.

Terms such as **refraction** are analogical unless a specific mathematical or physical definition is explicitly supplied.

The benchmark makes no automatic claim of literal optical or physical refraction.

Required distinction:

```text
engineering analogy
≠
literal physics
```

---

# 14. Efficiency Interpretation

Repository evaluations may measure cost dimensions such as:

- tokens;
- model calls;
- recomputation events;
- latency;
- memory use;
- retrieval count;
- task-level accuracy;
- benchmark-local utility.

A measured reduction in one cost dimension does not automatically establish total-system efficiency.

For example:

```text
fewer model calls
≠
lower total production energy
```

unless total-system energy has actually been measured.

Likewise:

```text
fewer tokens
≠
lower total cost in every deployment
```

Efficiency claims should identify:

- baseline;
- system;
- task;
- measured cost dimension;
- omitted costs;
- uncertainty.

---

# 15. Causal Attribution Boundary

The repository SHOULD avoid statements such as:

```text
efficiency gains are caused by governed recursion
```

unless the evaluation isolates causation.

A safer benchmark interpretation is:

```text
the evaluated implementation
produced a measured difference
under the declared configuration
```

Possible causal contributors may include:

- memory reuse;
- caching;
- threshold behavior;
- implementation details;
- prompt differences;
- model behavior;
- retrieval architecture;
- dataset effects;
- random variation.

Causal claims require an appropriate experimental design.

---

# 16. Inference Parity

Inference parity means comparable declared task-level outcomes within specified tolerances and conditions.

It does not imply:

- identical hardware;
- identical model architecture;
- identical latency;
- identical throughput;
- identical energy consumption;
- identical internal reasoning;
- identical error distribution;
- universal equivalence.

An inference-parity result should identify:

- task;
- dataset;
- target metric;
- tolerance;
- model/version;
- runtime;
- hardware where relevant;
- sample size;
- uncertainty.

---

# 17. Logic Density

Repository materials may use **logic density** as an orientation concept for useful or preserved task-relevant structure relative to a declared burden.

A quantitative logic-density claim must define:

- numerator;
- denominator;
- task;
- baseline;
- fidelity requirement;
- measurement method.

Logic density is not automatically interchangeable with:

- FLOPs;
- energy;
- throughput;
- intelligence;
- factual accuracy.

---

# 18. Canonical vs Repository Definitions

Canonical Grand Compression concepts remain governed by MRD v2.0.

Repository-specific operational definitions exist only for benchmark execution.

Required distinction:

```text
repository operational definition
≠
new canonical definition
```

Repository code must not silently redefine a canonical framework term.

---

# 19. Authority Map

## Canonical / repository-normative

```text
docs/canonical-spec.md
AGENTS.md
docs/AUTHORITY.md
docs/doctrine/mrd-v2.0-alignment.md
docs/doctrine/canonical-claim-alignment.md
CITATION.cff
LICENSE.txt
governance/README.md
```

Each file governs only within its declared role.

## Metric specifications

```text
docs/razor-diffusion-metric.md
razor_metrics/rdm.py
razor_metrics/facets.py
razor_metrics/shear.py
razor_metrics/boundary.py
```

## Reference implementations

```text
src/razor/
```

A legacy or wrapper package, if present, must not silently override the primary implementation contract.

## Benchmarks

```text
benchmarks/
```

including benchmark-specific harnesses and fixtures.

## Diagnostics

```text
diagnostics/
docs/diagnostics/
```

Diagnostics are not automatically canonical claims.

## Non-normative material

May include:

- explanatory notes;
- strategic implications;
- infrastructure narratives;
- economic interpretation;
- diagrams;
- metaphors;
- notebooks.

---

# 20. Comparative Compression Geometry™

Comparative Compression Geometry™ is governed by:

```text
MRD v2.0 §12.9
```

Repository comparison work must distinguish:

```text
visual resemblance
≠
structural correspondence
≠
mathematical equivalence
≠
mechanistic equivalence
≠
material identity
```

Cross-domain use is additionally governed by:

**RC-22 — Domain Transfer Constraint**

---

# 21. Established Mathematics Boundary

Established external mathematics retains independent provenance.

The repository MUST NOT imply that Robbie George or Grand Compression originated pre-existing mathematics merely because it is used as a framework reference.

Examples include:

- Hopf fibration;
- E8;
- topology;
- fiber bundles;
- Lie theory;
- Fibonacci mathematics;
- fractals;
- quantum-state geometry.

Required distinction:

```text
bounded mathematical reference
≠
Grand Compression discovery
```

and:

```text
established mathematics
≠
Grand Compression validation
```

---

# 22. Hopf Fibration Boundary

The classical Hopf fibration is:

```text
S¹ ↪ S³ → S²
```

It is established mathematics.

Within Naturepedia™, it is treated as:

```text
Parent:
Geometry of Nature™

Evidence class:
Established mathematics

Framework role:
Comparative only

CCG relationship:
Bounded structural comparison class
```

Public reference:

https://www.robbiegeorgephotography.com/hopf-fibration

Its inclusion does not automatically create:

- a Plate™ family;
- a Registry;
- a System Map;
- a Knowledge Mesh;
- an x402 resource family.

Repository code and documentation MUST NOT invent such resources merely from the existence of the Hopf reference page.

---

# 23. E8 Boundary

E8 is a separate established mathematical reference.

Public reference:

https://www.robbiegeorgephotography.com/e8-lattice

Hopf and E8 are distinct.

```text
Hopf
≠
E8
```

Their inclusion within Comparative Compression Geometry™ does not establish a causal progression, shared physical mechanism, or material identity.

---

# 24. Reference-Implementation Boundary

Naturepedia™ and repository code are reference implementations.

Under:

**RC-21 — Reference Implementation Distinction**

the repository MUST preserve:

```text
reference implementation
≠
independent validation
```

This applies equally to:

- code;
- schemas;
- Workers;
- MCP;
- Plates;
- registries;
- System Maps;
- Knowledge Meshes;
- payment infrastructure.

---

# 25. Domain-Transfer Boundary

Cross-domain transfer is governed by:

**RC-22 — Domain Transfer Constraint**

A transfer should identify:

- source objects;
- target objects;
- source domain;
- target domain;
- scale;
- normalization;
- preserved relationships;
- exclusions;
- constraints;
- evidence;
- competing explanations;
- limitations;
- failure conditions.

Structural similarity alone is insufficient.

---

# 26. Payment and Retrieval Boundary

Payment and empirical status are independent.

Required distinctions:

```text
HTTP 402 challenge
≠
settlement
```

```text
settlement
≠
claim validation
```

```text
payload delivery
≠
scientific support
```

```text
price
≠
evidence quality
```

---

# 27. Resource Existence Boundary

A route pattern does not establish resource existence.

Required behavior for protected resources is:

```text
Unknown
→ 404
→ no payment challenge
```

```text
Known but incomplete
→ 409
→ no payment challenge
```

```text
Registered and complete
→ eligible for 402 challenge
```

Configured pricing does not imply specific resource availability.

---

# 28. Current Retrieval Pricing

Production pricing authority:

```text
/.well-known/x402-pricing.json
```

Current manifest version:

```text
3.0.0
```

Current classes:

| Access class | Price | Atomic units | Status |
|---|---:|---:|---|
| Public discovery / previews | Free | `0` | Public |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic resources |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for registered and validated resources |
| Bounded subtree / registry / System Map | `$5.00 USDC` | `5000000` | Governed protected class |
| Full registry / Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Governed protected class |

The existence of a class does not establish availability of every possible resource in that class.

---

# 29. Frozen Artifact Boundary

Versioned frozen benchmark outputs are provenance artifacts.

Example:

```text
results/.../frozen/
```

They SHOULD NOT be silently rewritten to:

- update MRD references;
- modernize wording;
- change comments;
- align newer doctrine.

Current interpretation should be documented outside the frozen artifact.

---

# 30. Authorship Conservation

The Grand Compression Cosmology, Robbie’s Razor™, Comparative Compression Geometry™, RKCA™, RRIP™, Plates™, and associated original framework terminology originate with:

**Robbie George**

Repository implementation does not transfer authorship.

Benchmarking does not transfer authorship.

Independent evidence does not transfer claim authorship.

Established external mathematics retains independent historical authorship and provenance.

---

# 31. Evidence Interpretation

The repository SHOULD use governed evidence states:

- Proposed;
- Testing;
- Provisionally Supported;
- Supported;
- Challenged;
- Inconclusive;
- Retired.

A Supported result means supported only within its declared conditions.

It does not mean universally proven.

---

# 32. Required Interpretation Rules

The repository MUST preserve:

```text
confidence
≠
verification
```

```text
retrieval
≠
revalidation
```

```text
stable memory behavior
≠
truth
```

```text
benchmark target
≠
universal ground truth
```

```text
benchmark pass
≠
framework validation
```

```text
implementation
≠
independent confirmation
```

```text
canonical publication
≠
empirical confirmation
```

```text
structural correspondence
≠
material identity
```

```text
established mathematics
≠
Grand Compression validation
```

```text
payment
≠
evidence
```

---

# 33. Spec Versioning

This repository specification may evolve without altering canonical Grand Compression theory.

**Spec Version:** 1.3  
**Last updated:** 2026-08-23

## Changelog

### v1.3

- clarified benchmark-local meaning of correctness;
- separated confidence from verification;
- separated retrieval from revalidation;
- clarified RazorMemoryBank semantics;
- clarified Selective Replay semantics;
- bounded causal efficiency claims;
- added RC-21 and RC-22 implementation guidance;
- added Comparative Compression Geometry boundaries;
- added established-mathematics provenance;
- added Hopf and E8 interpretation boundaries;
- added protected-resource existence semantics;
- aligned current x402 retrieval classes;
- added frozen-artifact preservation rule.

### v1.2

Aligned repository authority, attribution, evidence boundaries, reference-implementation status, and canonical subordination with MRD v2.0 and RC-01 through RC-22.

### v1.1

Added non-normative Economic Recursion Barrier interpretation and clarified repository boundaries.

### v1.0

Initial repository specification.

---

# 34. Final Status

```text
Current governing authority:
MRD v2.0

Canonical identifier:
GC-MRD-v2.0

Canonical claim range:
RC-01 through RC-22

Repository spec:
1.3

Reference-implementation boundary:
RC-21

Domain-transfer boundary:
RC-22

Comparative Compression Geometry:
MRD v2.0 §12.9

Confidence:
Not verification

Memory retrieval:
Not revalidation

Benchmark correctness:
Agreement with declared benchmark targets

Hopf:
Established mathematics / comparative-only

E8:
Established mathematics / separate comparative reference

Enriched Query:
Reserved

Pricing authority:
/.well-known/x402-pricing.json
version 3.0.0
```

Canonical framework definitions remain governed by MRD v2.0 and the Canonical Claims Register.
