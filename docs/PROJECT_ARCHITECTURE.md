# Project Architecture

## Purpose

This document explains how the repository’s doctrine, governance, structured resources, benchmarks, and delivery systems align with **The Grand Compression Cosmology — Master Reference Document, MRD v2.0**.

The repository is a public technical and evaluation surface. It does not replace the complete Master Reference Document or independently validate every canonical claim.

---

## Canonical Alignment

**Governing document:** The Grand Compression Cosmology — Master Reference Document  
**Governing version:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Author and originator:** Robbie George  
**Canonical section range:** Sections 1–13  
**Canonical appendix range:** Appendices A–Q  
**Canonical claim range:** RC-01 through RC-22  
**Primary reference implementation:** Naturepedia™  

Canonical authority resolver:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Complete versioned PDF:

https://asf-file-uploads.s3.us-east-1.amazonaws.com/image/upload/production/3790/Grand-Compr_1247ef65e1/1785596435.pdf

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Repository implementation contract:

`docs/doctrine/mrd-v2.0-alignment.md`

Machine-readable MRD manifest:

`docs/mrd/mrd-v2.0-manifest.json`

MRD v1.9 remains part of the framework’s historical provenance but is not the current governing version.

---

## Authority Architecture

The governing authority and implementation architecture is:

```mermaid
flowchart TD
    A[Canonical webpage] --> B[Versioned MRD v2.0 PDF]
    B --> C[GitHub technical repository]
    C --> D[Cloudflare Worker delivery layer]
    D --> E[Naturepedia reference implementation]
```

Each layer has a distinct role.

### Canonical Webpage

The canonical webpage provides:

- authority resolution
- current-version identification
- citation
- canonical claim publication
- human access
- links to complete versioned materials

### Versioned PDF

The versioned PDF provides:

- the complete MRD v2.0 document encoding
- Sections 1–13
- Appendices A–Q
- embedded Appendices E, F, I, P, and Q
- stable versioned reference material

### GitHub Repository

The repository provides:

- public technical doctrine
- implementation-alignment documents
- structured examples
- schemas
- manifests
- indexes
- change logs
- benchmarks
- diagnostics
- governance contracts
- agent instructions
- reproducibility materials

### Cloudflare Worker

The Cold-bird Worker provides the public machine-delivery boundary, including:

- resource discovery
- route validation
- public-resource delivery
- protected-resource routing
- human-browser bypass behavior
- x402 payment challenges
- settlement enforcement
- canonical serialization
- boundary validation
- request binding
- hash generation
- verified delivery
- strict failure behavior

### Naturepedia™

Naturepedia is the primary reference implementation of the architecture.

It demonstrates how the framework can be translated into Plates™, registries, System Maps, Knowledge Meshes, human-readable pages, and machine-readable resources.

Reference-implementation status demonstrates implementation. It does not constitute independent empirical validation or universal confirmation.

---

## Structural Design Principle

The repository organization reflects the canonical recursion cycle:

```text
compression → expression → memory → recursion
```

The architecture separates authority, explanation, preserved structure, evaluation, and delivery so that implementation work cannot silently redefine canonical theory.

---

## Repository Layers

| Layer | Function | Primary locations |
|---|---|---|
| Canonical authority | Resolves governing theory and current version | Canonical webpage and versioned MRD PDF |
| Authority governance | Defines repository authority and alignment rules | `docs/AUTHORITY.md`, `docs/doctrine/` |
| Human-readable expression | Explains architecture and research scope | `README.md`, `docs/index.md`, `docs/RESEARCH_OVERVIEW.md`, `docs/architecture/` |
| Structured memory | Preserves manifests, indexes, examples, registries, and change state | `docs/mrd/`, `docs/examples/` |
| Evaluation recursion | Executes benchmarks and diagnostics | `benchmarks/`, `diagnostics/`, `docs/diagnostics/` |
| Governance | Constrains contributors and automated agents | `AGENTS.md`, `CONTRIBUTING.md`, `governance/`, `docs/examples/skills/SKILL.md` |
| Delivery boundary | Publishes public and protected machine resources | Cold-bird Cloudflare Worker |
| Reference implementation | Demonstrates the architecture in operation | Naturepedia™ |

---

## Canonical Authority Layer

Canonical definitions, claims, qualifications, and status are governed by MRD v2.0.

Repository documents may:

- point to canonical authority
- summarize concepts for implementation
- encode structured metadata
- define tests and schemas
- document operational behavior
- provide bounded examples

Repository documents must not:

- silently redefine canonical terminology
- renumber canonical claims
- promote provisional material to canonical status
- treat implementation status as empirical validation
- treat structural resemblance as cross-domain proof
- replace the complete MRD

When a repository statement conflicts with the current canonical authority, the canonical authority controls unless an explicit versioned implementation exception has been documented.

---

## Doctrine and Governance Layer

The primary repository authority documents are:

- `docs/AUTHORITY.md`
- `docs/doctrine/mrd-v2.0-alignment.md`
- `docs/doctrine/canonical-claim-alignment.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `docs/examples/skills/SKILL.md`

These files establish:

- current authority
- canonical boundaries
- authorship requirements
- evidence-status requirements
- agent constraints
- contribution rules
- machine-readable fidelity requirements
- implementation boundaries
- historical-version treatment

They prevent benchmark, documentation, schema, or agent changes from silently altering canonical theory.

---

## Human-Readable Expression Layer

Human-readable architecture and research explanations are located primarily in:

- `README.md`
- `docs/index.md`
- `docs/RESEARCH_OVERVIEW.md`
- `docs/PROJECT_ARCHITECTURE.md`
- `docs/architecture/`
- `docs/glossary.md`

These documents provide orientation and navigation.

They are subordinate to the current canonical MRD authority and must preserve the distinction between:

- canonical statements
- implementation descriptions
- hypotheses
- provisional constructs
- benchmark observations
- independently reproduced evidence

---

## Structured Memory Layer

Machine-readable resources preserve the state needed for reliable retrieval and reuse.

Examples include:

- MRD manifests
- AI-root metadata
- indexes
- change logs
- JSON resources
- JSON-LD resources
- schemas
- Plate registries
- System Maps
- Knowledge Meshes
- agent capability records

Structured resources should preserve:

- stable identity
- relationships
- provenance
- constraints
- version state
- canonical paths
- retrieval paths
- evidence status
- known exclusions
- schema compatibility

This follows the MRD v2.0 requirement that compressed information becomes durable recursive infrastructure only when the structure required for later use remains preserved.

---

## Plate-to-Mesh Architecture

The primary implementation sequence is:

```mermaid
flowchart LR
    A[Plate] --> B[Registry]
    B --> C[System Map]
    C --> D[Knowledge Mesh]
```

### Plate™

A bounded visual and conceptual knowledge interface with stable identity and links to deeper structured resources.

### Registry

A structured collection preserving identifiers, metadata, provenance, relationships, version state, and retrieval paths.

### System Map

A structured representation of relationships within a declared system boundary.

### Knowledge Mesh

A higher-order network connecting Plates, registries, System Maps, constraints, provenance, and retrieval paths.

Progression through these layers does not automatically increase empirical certainty. Evidence status must remain explicit at every level.

---

## Evaluation Recursion Layer

The benchmark and diagnostic layers test declared behaviors under bounded conditions.

These may include:

- compression efficiency
- preserved reusable structure
- memory stabilization
- recomputation avoidance
- semantic diffusion
- recursive stability
- schema conformance
- provenance retention
- relationship preservation
- retrieval fidelity
- constraint compliance
- deterministic serialization
- Question Quality Under Constraint

Evaluation does not alter canonical theory.

A benchmark result is bounded by its dataset, task, model, runtime, version, configuration, resource budget, measurement method, sample size, and uncertainty.

---

## Agent Governance Layer

`AGENTS.md` and `docs/examples/skills/SKILL.md` provide execution and interpretation constraints for automated agents.

They define requirements concerning:

- authority resolution
- canonical terminology
- version handling
- evidence labeling
- attribution
- protected-resource access
- output behavior
- structured-resource fidelity
- failure behavior
- implementation boundaries

Agents must not infer that:

- payment means validation
- serialization means empirical truth
- implementation means independent confirmation
- resemblance means cross-domain equivalence
- historical documentation overrides the current authority

---

## Delivery and Settlement Layer

The Cold-bird Worker separates public discovery from protected machine-resource delivery.

The production delivery sequence is:

    Request
    ↓
    Canonical route normalization
    ↓
    Gateway-tier classification
    ↓
    Explicit resource availability validation
    ↓
    Resource state
    ↓

    Unknown
    → 404
    → no payment challenge

    Known but incomplete
    → 409
    → no payment challenge

    Registered and complete
    → deterministic x402 challenge
    ↓
    Payment verification
    ↓
    Settlement
    ↓
    Exact protected payload construction
    ↓
    Boundary fidelity validation
    ↓
    Canonical serialization
    ↓
    Payload hash and request binding
    ↓
    Verified delivery

Protected-resource pricing is governed by the canonical Naturepedia™ x402 Pricing Manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Current pricing version:

    3.0.0

Current production pricing:

| Access class | Price | Atomic units | Route status |
|---|---:|---:|---|
| Free discovery and previews | `$0.00 USDC` | `0` | Active |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ retrieval | `$0.25 USDC` | `250000` | Active for registered and validated payloads |
| Bounded subtree, registry, or System Map | `$5.00 USDC` | `5000000` | Active |
| Full registry or Knowledge Mesh snapshot | `$25.00 USDC` | `25000000` | Active |

### Atomic Query Production Class

Public route template:

    /v1/query/atomic/{resource}

Canonical internal route template:

    /x402/query/atomic/{resource}

Current active Atomic route:

    /v1/query/atomic/robbie-george-biography-plate

Canonical internal route:

    /x402/query/atomic/robbie-george-biography-plate

Canonical Plate identifier:

    robbie-george#robbie-george-biography-plate

Canonical authority:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Atomic production configuration:

    Access class: atomic
    Price: 0.005 USDC
    Atomic units: 5000
    Network: eip155:8453
    Asset: USDC
    Resource class: atomic-query
    Schema version: naturepedia.atomic-query.v1
    Route status: active for explicitly registered deterministic payloads

Verified production behavior:

    Registered + complete Atomic resource
    → HTTP 402 Payment Required
    → amount 5000
    → gateway tier atomic

    Known + incomplete Atomic resource
    → HTTP 409 Conflict
    → no payment challenge

    Unknown Atomic resource
    → HTTP 404 Not Found
    → no payment challenge

Verified active Atomic challenge:

    STATUS: 402
    AMOUNT: 5000
    TIER: atomic
    PAYMENT REQUIRED: true

Result:

    PASS

Verified known-but-incomplete Atomic route:

    /v1/query/atomic/robbies-razor-plate

Observed result:

    STATUS: 409
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED: false
    CODE: ATOMIC_PAYLOAD_NOT_REGISTERED

Result:

    PASS

Verified unknown Atomic resource:

    STATUS: 404
    AMOUNT: null
    TIER: null
    PAYMENT REQUIRED: false
    CODE: ATOMIC_RESOURCE_NOT_FOUND

Result:

    PASS

No Atomic payment payload was supplied during this production activation validation.

No new Atomic USDC settlement or protected Atomic payload-delivery test was performed.

### Enriched Query Status

Public route template:

    /v1/query/enriched/{resource}

Production configuration:

    Access class: enriched
    Price: 0.025 USDC
    Atomic units: 25000
    Route status: reserved

The Enriched Query class remains reserved.

Enriched resources must not issue payment challenges until their governed deterministic payloads are explicitly registered, availability-gated, fidelity-bound, and production validated.

### Structured Plate Production Class

Current active Structured Plate™ routes:

    /v1/plates/item/commercial-data-license-plate
    /v1/plates/item/commercial-intelligence-pricing-plate
    /v1/plates/item/robbie-george-biography-plate

Structured Plate production configuration:

    Access class: single-plate
    Price: 0.25 USDC
    Atomic units: 250000
    Route status: active for registered and validated payloads

All three active Structured Plate routes were regression tested after Atomic activation.

Observed result for all three:

    STATUS: 402
    AMOUNT: 250000
    TIER: single-plate
    PAYMENT REQUIRED: true

Result:

    PASS

Atomic activation did not alter the existing Structured Plate challenge behavior.

Unknown Plate identifiers return `404` without a payment challenge.

Known Plates without registered complete payloads return `409` without a payment challenge.

### Deterministic Pricing Requirements

Production `402` responses must declare one fixed price in six-decimal USDC atomic units.

Price ranges, silent substitutions, reuse of another endpoint’s price, and route-family fallthrough into an incorrect pricing class are not permitted.

The resolved resource class and registered route determine the applicable pricing tier.

Atomic resources must use:

    Resource class: atomic-query
    Gateway tier: atomic
    Price: 5000 atomic units

Structured Plate resources must use:

    Resource class: structured-plate
    Gateway tier: single-plate
    Price: 250000 atomic units

System Maps and bounded registries use the subtree class.

Knowledge Meshes and full snapshots use the snapshot class.

### Fail-Closed Availability Boundary

A valid route pattern does not establish that a protected resource exists or is sellable.

The Worker must determine availability before issuing a payment challenge.

Required behavior:

    Unknown resource
    → 404
    → no payment challenge

    Known but incomplete resource
    → 409
    → no payment challenge

    Registered + complete resource
    → eligible for deterministic x402 challenge

This availability boundary applies before payment verification and settlement.

### Fidelity Boundary

After successful settlement, protected payloads must pass the Tollbooth Boundary Fidelity Validation before delivery.

Validation includes:

- canonical `/x402/` path binding
- expected resource class
- expected schema version
- Canonical Publication Manifest alignment
- payload `@id` alignment
- gateway-tier compatibility
- exact serialized payload validation
- canonical payload hashing
- request-binding hashing

For Atomic Query delivery, the required boundary is:

    Resource class: atomic-query
    Gateway tier: atomic
    Schema version: naturepedia.atomic-query.v1
    Canonical internal path: /x402/query/atomic/{resource}

A payload that fails the boundary must not be delivered as a successful protected response.

### Retrieval Rights Boundary

An x402 payment grants one endpoint-level retrieval of the identified protected resource only.

It does not grant:

- training rights
- embedding rights
- bulk-ingestion rights
- redistribution rights
- resale rights
- synchronization rights
- private-dataset construction rights
- derivative-dataset rights
- commercial implementation rights
- Robbie's Razor™ framework implementation rights

Commercial data reuse rights require a separate written agreement.

Framework implementation and strategic-infrastructure rights require a separate enterprise agreement.

These retrieval, commercial-data, and framework-rights layers must remain distinct.

### Governance Header

The Worker’s primary governance response header remains:

    X-Robbie-Razor-Governance: Gr <= Es

The implementation must preserve:

- valid human-browser bypass behavior
- public-document accessibility
- protected-resource enforcement
- deterministic pricing
- explicit resource availability validation
- settlement requirements
- canonical serialization
- payload fidelity validation
- request binding
- governed pricing
- strict `404` behavior for nonexistent protected resources
- strict `409` behavior for known but incomplete protected resources
- deterministic failure behavior
- separation of retrieval rights from commercial reuse and framework implementation rights

---

## GitHub-to-Worker Publication Boundary

Some Worker resources are retrieved from the GitHub `main` branch at request time. Other resources are embedded directly in Worker code.

This creates two distinct publication paths.

### GitHub-Backed Resources

Examples may include:

- `SKILL.md`
- AI-root metadata
- change-log resources
- repository indexes

For GitHub-backed resources, the publication sequence is:

```text
feature branch update
→ review
→ merge into main
→ Worker retrieves updated main-branch resource
→ public delivery
```

Changes made only on `docs/mrd-v2-propagation` are not yet live through Worker routes that retrieve files from `main`.

### Worker-Embedded Resources

Resources embedded directly in Worker code require:

```text
Worker source update
→ validation
→ deployment
→ endpoint testing
```

Merging GitHub changes does not automatically update inline Worker resources.

The AI Catalog and any other embedded control-plane metadata must be updated separately in the Worker when repository propagation is complete.

---

## Version and Change Control

Version changes should be reflected across the applicable:

- authority documents
- manifests
- indexes
- change logs
- structured examples
- schemas
- agent instructions
- citations
- Worker metadata
- public machine resources

Historical versions should remain identifiable as historical provenance.

A historical filename may retain its original version identifier when changing it would destroy provenance or break stable references. Its contents should clearly identify the current authority where appropriate.

---

## Evidence and Validation Boundary

The architecture distinguishes among:

- canonical status
- implementation status
- schema-validation status
- serialization status
- settlement status
- benchmark status
- empirical-validation status

These states are not interchangeable.

A resource may be canonically serialized, successfully settled, and correctly delivered while still containing a hypothesis, provisional construct, implementation example, or unvalidated claim.

Every layer must preserve the evidence status of the information it carries.

---

## Cross-Domain Boundary

No concept, metric, relationship, or model should be transferred across domains or scales solely because of visual or structural similarity.

Cross-domain transfer requires explicit declaration of:

- objects
- scale
- normalization
- relationships
- exclusions
- constraints
- evidence
- alternatives
- failure conditions

This boundary applies to documents, diagrams, Plates, registries, System Maps, Knowledge Meshes, benchmarks, and agent-generated interpretations.

---

## Architectural Goal

The repository is structured so that:

- canonical authority remains stable
- architecture remains understandable
- authorship and provenance remain preserved
- machine-readable resources remain retrievable
- evaluation remains reproducible
- evidence status remains explicit
- recursive execution remains governed
- protected delivery remains deterministic
- implementation cannot silently become theory

This architecture implements the repository-facing contract of MRD v2.0 while preserving the canonical authority of the complete Master Reference Document.

---

## Attribution

The Grand Compression Cosmology, Robbie’s Razor™, the Recursive Knowledge Compression Architecture, RRIP, Plates™, and associated canonical concepts and terminology originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

The repository is governed by the **Authorship Conservation Rule (ACR)**.

Implementation, summarization, benchmarking, serialization, machine transformation, or contribution does not transfer authorship of the originating framework.
