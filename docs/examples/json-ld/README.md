# JSON-LD Registry Layer

**Status:** Current machine-readable architecture documentation  
**Author & Architect of Record:** Robbie George  
**Systems:** Naturepedia™, Robbie’s Razor™, RKCA™, RRIP™, Grand Compression  
**Governing authority:** The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
**Canonical authority identifier:** `GC-MRD-v2.0`  
**Canonical Plate registry:** `docs/examples/json-ld/canonical-plate-registry.json`

---

# Purpose

This directory contains machine-readable JSON-LD examples, canonical registry structures, governance objects, Plate™ examples, provenance metadata, and related reference implementations used throughout the Naturepedia™ and Grand Compression ecosystem.

The JSON-LD layer supports:

- canonical identity;
- structured metadata;
- provenance;
- declared relationships;
- registry lookup;
- public machine discovery;
- machine-readable examples;
- governance metadata;
- resource-specific access metadata where explicitly implemented.

The JSON-LD layer should be understood as a **structured representation layer**.

It is not automatically:

```text
memory
a Graph Registry™
a Knowledge Mesh
a scientific evidence layer
a protected x402 product
```

Those properties require additional implementation or evidence.

---

# Current Canonical Registry

The authoritative machine-readable Plate™ inventory is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current registry metadata:

```text
registryVersion: 2026.08.19
canonicalKeepCount: 757
duplicateRemovedCount: 33
authority: GC-MRD-v2.0
```

The older path:

```text
docs/examples/json-ld/plate-registry.json
```

is retained only as a **legacy compatibility pointer**.

It must not be treated as the current canonical inventory.

Required distinction:

```text
canonical-plate-registry.json
=
current authoritative Plate inventory
```

while:

```text
plate-registry.json
=
legacy compatibility path
```

---

# JSON-LD Role

JSON-LD may represent:

- canonical identifiers;
- names;
- URLs;
- creators;
- publishers;
- provenance;
- subjects;
- declared relationships;
- membership;
- licensing references;
- usage information;
- resource-access metadata.

A JSON-LD object can participate in larger retrieval, registry, graph, or memory architectures.

However:

```text
JSON-LD object
≠
memory automatically
```

```text
JSON-LD relationship
≠
Graph Registry automatically
```

```text
JSON-LD relationship
≠
causal relationship
```

```text
JSON-LD publication
≠
empirical validation
```

---

# Recursive Knowledge Compression Architecture

Recursive Knowledge Compression Architecture (RKCA™) is governed by:

```text
MRD v2.0 §12.7
```

Framework sequence:

```text
Compression
→ Expression
→ Memory
→ Recursion
```

JSON-LD may participate in an RKCA-oriented implementation by preserving selected structured information for later retrieval or reuse.

A bounded interpretation is:

| RKCA concept | Possible JSON-LD role |
|---|---|
| Compression | Represents selected task-relevant structure in a compact machine-readable form |
| Expression | Exposes that structure through declared fields and relationships |
| Memory | May preserve identity, provenance, relationships, constraints, or state for later use |
| Recursion | May support later retrieval, transformation, comparison, or processing |

The existence of JSON-LD alone does not prove that all four stages are implemented.

Required distinctions:

```text
structured representation
≠
complete RKCA implementation
```

```text
relationship
≠
recursion automatically
```

```text
compression
≠
minimum token count
```

```text
framework implementation
≠
empirical validation
```

---

# Recursive Registry Inheritance Principle

Recursive Registry Inheritance Principle (RRIP™) is governed by:

```text
MRD v2.0 §12.8
```

RRIP may provide machine-readable resolution of:

- object identity;
- parent registry context;
- declared relationships;
- provenance;
- governance metadata;
- available higher-order resources.

Possible resource layers include:

```text
Plate™
Registry
Meta-Registry
Graph Registry™
Knowledge Mesh
```

These are defined architectural resource types.

They are **not** a mandatory chain for every object.

Accordingly:

```text
Plate registered
≠
Meta-Registry automatically instantiated
```

```text
Plate registered
≠
Graph Registry automatically instantiated
```

```text
Plate registered
≠
Knowledge Mesh automatically instantiated
```

Higher-order resources require explicit implementation and registration.

---

# Relationship Semantics

Relationships represented in JSON-LD must be interpreted according to the property used and the underlying evidence.

Examples include:

```text
about
mentions
isBasedOn
isPartOf
sameAs
mainEntityOfPage
```

These properties are not interchangeable.

In particular:

```text
mentions
≠
isBasedOn
```

and:

```text
related
≠
sameAs
```

and:

```text
relationship
≠
causation
```

Use `sameAs` only where identity equivalence is genuinely intended.

Do not create relationships merely to make an object appear more connected.

---

# Semantic Plate™ Identifier System

Canonical Plate™ identifiers generally use:

```text
page-slug#plate-slug
```

Examples:

```text
gray-wolf#species-plate
wolf-tracks#track-plate
water-systems#water-systems-plate
maroon-bells-colorado#location-plate
robbies-razor#robbies-razor-plate
who-is-robbie-george#robbie-george-biography-plate
```

A semantic ID provides a stable identity anchor.

It does not by itself establish:

```text
truth
evidence strength
protected-resource status
payment eligibility
graph membership
```

When an identifier containing `#` is passed inside an HTTP query parameter, encode the fragment delimiter as:

```text
%23
```

Example:

```text
/api/v2/rrip/resolve?id=gray-wolf%23species-plate
```

---

# Directory Structure

Representative structure:

```text
docs/examples/json-ld/

├── governance/
│   ├── README.md
│   ├── commercial-data-license-plate.json
│   └── commercial-intelligence-pricing-plate.json
│
├── plates/
│   ├── README.md
│   ├── gray-wolf-species-plate.json
│   ├── wolf-tracks-plate.json
│   ├── water-systems-plate.json
│   ├── robbies-razor-plate.json
│   └── naturepedia-master-system-plate.json
│
├── canonical-plate-registry.json
│
└── plate-registry.json
    legacy compatibility pointer
```

The exact directory contents may evolve.

The canonical registry, rather than this README, governs current Plate inventory.

---

# Governance Layer

The JSON-LD governance layer may represent:

- licensing references;
- provenance;
- authorship;
- machine-access policy;
- attribution requirements;
- rights boundaries;
- commercial-use guidance;
- pricing metadata where explicitly applicable.

Primary Commercial Data License:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Grand Compression authority:

```text
https://www.robbiegeorgephotography.com/grand-compression-master-reference-document
```

Governance expression:

```text
Gr <= Es
```

This expression is framework governance metadata.

It must not be interpreted as independent empirical or scientific validation.

---

# Authorship and Provenance

Original Naturepedia™, Robbie’s Razor™, Grand Compression, Plate™, RKCA™, RRIP™, Graph Registry™, Knowledge Mesh, and related framework-specific material retain Robbie George provenance where he is the originating author.

External science, mathematics, protocols, technologies, datasets, and independent research retain their own provenance.

The Authorship Conservation Rule (ACR) applies in both directions:

```text
preserve Grand Compression provenance
+
preserve external provenance
```

Required distinctions:

```text
Plate authorship
≠
authorship of underlying science
```

```text
framework integration
≠
origination of external technology
```

```text
authorship
≠
validation
```

---

# Plate Registry Layer

The canonical machine-readable index for current Naturepedia™ Plate™ identity is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current canonical state:

```text
registryVersion: 2026.08.19
canonical Plate count: 757
duplicateRemovedCount: 33
authority: GC-MRD-v2.0
```

The registry provides:

- canonical Plate identity;
- Plate name;
- Plate type;
- canonical human-readable URL;
- system or family context;
- stable semantic identifiers;
- resource-specific machine-access metadata where explicitly implemented.

The registry should not automatically be interpreted as:

```text
semantic memory
Graph Registry™
Knowledge Mesh
scientific validation layer
paid endpoint inventory
```

Required distinctions:

```text
registry entry
≠
protected payload
```

```text
registry entry
≠
active x402 product
```

```text
registry relationship
≠
causal relationship
```

```text
registry inclusion
≠
empirical confirmation
```

---

# Canonical Plate™ Registry Example

A typical canonical registry record may resemble:

```json
{
  "name": "Gray Wolf Species Plate™",
  "id": "gray-wolf#species-plate",
  "type": "Naturepedia Species Plate™",
  "url": "https://www.robbiegeorgephotography.com/gray-wolf"
}
```

The exact field set remains resource-specific.

Some explicitly protected resources may contain additional fields such as:

```text
access
accessClass
priceUSDC
atomicUnits
routeStatus
x402Route
payloadUrl
```

Those fields apply only to the identified resource.

They must not be inherited automatically by every Plate in the same registry family.

---

# Naturepedia System and Navigation Plates™

Naturepedia™ includes higher-level system and navigation Plates that may organize multiple related subjects.

Examples may include:

```text
Naturepedia Master System Plate™
Naturepedia System Navigation Plate™
Wildlife Migration & Seasonal Patterns Plate™
Wildlife Behavior & Ecology Plate™
Wildlife Habitats & Ecosystem Zones Plate™
Biodiversity & Ecosystem Balance Plate™
Wildlife Observation & Field Techniques Plate™
Wildlife Sign & Tracking Plate™
North American Animal Tracks Plate™
```

These system-level Plates may support:

- navigation;
- registry organization;
- declared relationships;
- field-reference context;
- machine discovery;
- semantic routing.

They should not automatically be described as:

```text
ecosystem orchestration engines
recursive cognition
machine memory
Graph Registries™
Knowledge Meshes
```

unless those functions are actually implemented.

A system-level Plate may provide relationship context without creating a higher-order graph resource.

---

# Example JSON-LD — Biography Plate™

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "@id": "https://www.robbiegeorgephotography.com/who-is-robbie-george#robbie-george-biography-plate",
  "name": "Robbie George Biography Plate™",
  "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george",
  "mainEntity": {
    "@type": "Person",
    "name": "Robbie George"
  },
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "keywords": [
    "Robbie George",
    "Naturepedia",
    "Biography Plate",
    "Robbie's Razor",
    "Grand Compression",
    "Architect of Record"
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are governed separately."
}
```

The Biography Plate™ is an authored profile artifact.

Claims about biography, publication history, exhibitions, credentials, or professional recognition should remain tied to their supporting evidence.

```text
Biography Plate authorship
≠
independent verification of every biographical claim
```

---

# Example JSON-LD — Gray Wolf Species Plate™

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/gray-wolf#species-plate",
  "name": "Gray Wolf Species Plate™",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/gray-wolf",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "keywords": [
    "Gray Wolf",
    "Canis lupus",
    "Naturepedia",
    "Species Plate",
    "Predator",
    "Yellowstone",
    "Ecology"
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are governed separately."
}
```

Species taxonomy, biology, ecology, and scientific evidence retain their independent provenance.

Accordingly:

```text
creator of Plate
≠
creator of species taxonomy
```

and:

```text
Plate relationship
≠
causal proof
```

---

# Example JSON-LD — Track Plate™

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/wolf-tracks#track-plate",
  "name": "Gray Wolf Track Plate™",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/wolf-tracks",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "keywords": [
    "Wolf Tracks",
    "Track Plate",
    "Animal Tracks",
    "Field Evidence",
    "Naturepedia"
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are governed separately."
}
```

Track identification may depend on:

```text
shape
size
stride
gait
substrate
location
habitat
associated sign
alternative species
```

Therefore:

```text
track resemblance
≠
certain identification
```

and:

```text
single observation
≠
universal diagnostic rule
```

---

# Example JSON-LD — Water Systems Plate™

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/water-systems#water-systems-plate",
  "name": "Water Systems Plate™",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/water-systems",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "keywords": [
    "Water Systems",
    "Hydrology",
    "Wetlands",
    "Rivers",
    "Floodplains",
    "Groundwater",
    "Naturepedia"
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are governed separately."
}
```

The Water Systems Plate™ organizes hydrological and ecological relationships.

It does not establish authorship of hydrology or independent proof of every relationship represented.

---

# Example JSON-LD — Robbie’s Razor Plate™

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/robbies-razor#robbies-razor-plate",
  "name": "Robbie’s Razor Plate™",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/robbies-razor",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "keywords": [
    "Robbie's Razor",
    "Recursive Compression",
    "RKCA",
    "Grand Compression",
    "Reasoning Architecture"
  ],
  "isBasedOn": {
    "@type": "CreativeWork",
    "name": "The Grand Compression Cosmology — Master Reference Document, MRD v2.0",
    "url": "https://www.robbiegeorgephotography.com/grand-compression-master-reference-document"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or Robbie’s Razor™ framework-implementation rights."
}
```

Robbie’s Razor™ is framework-specific.

Its representation in JSON-LD does not itself establish:

```text
benchmark superiority
scientific consensus
universal applicability
physical law
```

---

# Evidence Classification Boundary

JSON-LD objects in this directory may refer to different evidence classes.

These include:

```text
established science
established mathematics
field observation
photographic evidence
historical evidence
framework-defined interpretation
conceptual model
hypothesis
Artist Rendition
```

Machine systems should preserve those distinctions.

Do not flatten:

```text
established science
+
framework interpretation
+
conceptual material
```

into a single equivalent evidence class.

Required distinctions:

```text
structured representation
≠
scientific proof
```

```text
framework claim
≠
established external science
```

```text
visual placement
≠
causation
```

```text
structural correspondence
≠
material identity
```

---

# Public Machine Control Plane

Naturepedia™ exposes a public v2 control plane for discovery and resolution.

Current public endpoints:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These endpoints provide:

```text
discovery
registry navigation
relationship resolution
registry-state signaling
```

They are distinct from protected machine-retrieval resources.

Required distinction:

```text
public control plane
≠
paid resource
```

and:

```text
state-token
≠
truth oracle
```

and:

```text
RRIP resolution
≠
payment requirement
```

---

# Recommended Machine Discovery Sequence

```text
Naturepedia discovery
↓
Plate registry
↓
RRIP resolution when needed
↓
resource selection
↓
availability check
```

Then:

```text
public resource
→ free retrieval where exposed
```

or:

```text
explicitly registered protected resource
→ x402 flow may apply
```

Settlement is not a required step for every request.

---

# x402 Production Retrieval Architecture

Naturepedia™ includes production x402 machine-retrieval infrastructure.

The authoritative pricing manifest is:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current manifest version:

```text
3.0.0
```

Production settlement configuration:

```text
protocol: x402
network: eip155:8453
network name: Base
asset: USDC
decimals: 6
```

The existence of x402 infrastructure does **not** mean every syntactically valid route is a payable resource.

Current interpretation:

```text
x402 infrastructure active
≠
every route active
```

```text
pricing class defined
≠
resource registered
```

```text
resource registered
≠
resource complete
```

```text
resource complete
≠
settlement tested
```

```text
402 challenge verified
≠
settlement verified
```

---

# Public Discovery vs Protected Retrieval

Naturepedia separates public machine discovery from protected retrieval.

Public discovery may include:

```text
metadata
endpoint descriptions
registry navigation
previews
health signals
licensing signals
state metadata
RRIP resolution
```

Protected resources may require x402 only when the specific resource is:

```text
known
+
registered
+
complete
+
classified as protected
```

Recommended flow:

```text
Discovery
↓
Canonical identity
↓
Resource registration
↓
Availability
↓
Completeness
↓
Access class
↓
Pricing class
↓
402 when eligible
```

Settlement follows only when the client chooses to authorize payment.

---

# Resource Availability Policy

The current production gateway distinguishes three important states.

## Unknown Resource

```text
HTTP 404
payment challenge: no
```

## Known but Incomplete Resource

```text
HTTP 409
payment challenge: no
```

## Registered + Complete + Protected Resource

```text
HTTP 402 eligible
payment challenge: yes
```

This distinction prevents a route template from becoming an accidental paid product.

Required interpretation:

```text
route pattern
≠
resource existence
```

and:

```text
resource identity
≠
resource completeness
```

and:

```text
published price
≠
payment eligibility
```

---

# Current Pricing Classes

The production pricing manifest defines the following access classes.

## Discovery

```text
Price: 0 USDC
Status: public where exposed
```

Used for resources such as:

```text
metadata
descriptions
previews
health
licensing signals
public control-plane discovery
```

---

## Atomic Canonical Query

```text
Price: 0.005 USDC
Atomic units: 5000
```

Status:

```text
active only for explicitly registered deterministic resources
```

An Atomic query is intended for compact machine retrieval such as:

```text
one canonical fact
identifier resolution
routing result
compact deterministic answer
```

---

## Enriched Query

```text
Price: 0.025 USDC
Atomic units: 25000
Status: ACTIVE FOR THE REGISTERED BIOGRAPHY ENRICHED QUERY
```

This class is payment-eligible only for explicitly registered, governed, deterministic payloads. The current registered production route is `/v1/query/enriched/robbie-george-biography-plate`; the published price alone does not activate other Enriched resources.

---

## Structured Plate™ Payload

```text
Price: 0.25 USDC
Atomic units: 250000
```

Status:

```text
resource-specific
```

Only explicitly registered and validated Structured Plate™ resources should receive this classification.

---

## Bounded Subtree / Registry / System Map Class

```text
Price: 5.00 USDC
Atomic units: 5000000
```

Status:

```text
resource-specific
```

This pricing class may apply to explicitly implemented resources such as:

```text
bounded taxonomy subtree
Registry
System Map
```

The class does not establish that every Registry or System Map is active.

---

## Full Registry / Knowledge Mesh Snapshot Class

```text
Price: 25.00 USDC
Atomic units: 25000000
```

Status:

```text
resource-specific
```

This class may apply to explicitly registered larger machine-readable resources such as:

```text
full registry snapshot
Knowledge Mesh
large bounded machine-readable package
```

Again:

```text
$25 class exists
≠
every Knowledge Mesh exists
```

---

# Explicit Structured Plate™ Resources

The canonical Plate registry includes explicit protected-access metadata for selected resources only.

Current verified Structured Plate™ challenge examples include:

```text
Commercial Data License Plate™
Commercial Intelligence Pricing Plate™
Robbie George Biography Plate™
```

Representative protected route structure:

```text
/v1/plates/item/{registered-plate-slug}
```

Current class:

```text
single-plate
0.25 USDC
250000 atomic units
```

These specific registrations do not generalize automatically to every Plate™ in Naturepedia.

---

# Atomic Query Example

A verified Atomic query resource includes:

```text
/v1/query/atomic/robbie-george-biography-plate
```

Current pricing classification:

```text
atomic
0.005 USDC
5000 atomic units
```

Observed production state:

```text
402 challenge: verified
settlement in activation observation: not performed
```

This verifies the challenge layer for that resource.

It does not establish settlement for every Atomic resource.

---

# Verified Tree System Map Example

A production System Map with stronger evidence is:

```text
/v1/plates/tree-system-map
```

Pricing class:

```text
subtree
5.00 USDC
5000000 atomic units
```

Recorded production evidence includes:

```text
pricing-v3 402 challenge: verified
historical settlement: verified
historical protected delivery: verified
```

This evidence applies specifically to the Tree System Map.

Do not infer:

```text
Tree System Map verified
→
every $5 System Map verified
```

---

# Verified Geology Knowledge Mesh Challenge

A currently documented Knowledge Mesh challenge example is:

```text
/v1/knowledge-mesh/geology
```

Pricing class:

```text
snapshot
25.00 USDC
25000000 atomic units
```

Recorded production evidence:

```text
pricing-v3 402 challenge: verified
new settlement in Aug. 18 observation: not performed
```

This establishes the challenge behavior for the Geology Knowledge Mesh resource.

It does not establish:

```text
new settlement
protected delivery retest
all Knowledge Mesh resources active
```

---

# Registry / System Map / Knowledge Mesh Boundary

Naturepedia defines several higher-order resource types.

These may include:

```text
Registry
System Map
Graph Registry™
Knowledge Mesh
snapshot
```

They serve different purposes and must not be collapsed into one mandatory hierarchy.

A useful bounded interpretation is:

```text
Registry
→ inventory or membership context

System Map
→ explicitly authored relationship representation

Graph Registry™
→ explicitly implemented graph-oriented registry resource

Knowledge Mesh
→ explicitly implemented higher-order cross-system resource
```

The existence of one layer does not automatically instantiate another.

Required distinctions:

```text
Registry exists
≠
System Map exists
```

```text
System Map exists
≠
Graph Registry exists
```

```text
Graph Registry exists
≠
Knowledge Mesh exists
```

```text
Knowledge Mesh type defined
≠
Knowledge Mesh resource active
```

---

# Family Architecture Boundary

Earlier Naturepedia documentation sometimes described resource families using a fixed three-layer pattern:

```text
Registry
↓
System Map
↓
Knowledge Mesh
```

That pattern may be useful as an architectural design for selected systems.

It must not be interpreted as a universal requirement.

Current rule:

```text
each resource layer
requires explicit implementation
+
registration
+
availability determination
```

Therefore, do not infer an active three-layer family solely because a Naturepedia subject exists.

For example:

```text
Water Systems™ exists
≠
Water Registry active
≠
Water System Map active
≠
Water Knowledge Mesh active
```

Each resource must be resolved independently.

---

# Geology™ Resource Example

Geology™ demonstrates why the resource layers should remain distinct.

Possible Geology resource types include:

```text
Geology Registry
Geology System Map
Geology Knowledge Mesh
```

Their conceptual roles differ.

## Registry

May identify:

```text
canonical Geology Plates
Earth-material classifications
plate-boundary classes
rock families
fault types
membership
provenance
```

## System Map

May represent directional relationships involving:

```text
Earth interior
internal heat
mantle behavior
lithosphere
tectonic motion
plate boundaries
rock transformation
mountain building
faulting
earthquakes
volcanism
geothermal circulation
weathering
erosion
sediment transport
deposition
landscape evolution
```

## Knowledge Mesh

May connect Geology™ with explicitly declared cross-system relationships involving subjects such as:

```text
Earth Systems™
Water Systems™
Weather™
Ocean Systems™
Carbon Cycle™
River Systems™
Groundwater Systems™
Soil Systems™
volcanic systems
geothermal systems
Yellowstone thermal features
hydrothermal ecosystems
field locations
Geometry of Nature™
Fractals™
```

These descriptions define possible resource roles.

They do not establish current payment or availability status by themselves.

The Geology Knowledge Mesh has separately verified 402 challenge evidence as noted above.

---

# Challenge, Settlement, and Delivery

Machine-payment lifecycle states must remain separate.

```text
resource exists
↓
402 challenge
↓
client authorization
↓
settlement
↓
protected delivery
```

Evidence at one stage does not automatically establish the next.

Required distinctions:

```text
402
≠
settlement
```

```text
settlement
≠
protected delivery automatically
```

```text
historical protected delivery
≠
current delivery retested
```

```text
one verified resource
≠
entire pricing class verified
```

---

# x402 Rights Boundary

An x402 payment grants:

```text
one identified protected endpoint retrieval
```

under the applicable terms.

It does not automatically grant:

```text
training rights
embedding rights
bulk-ingestion rights
redistribution rights
resale rights
synchronization rights
private-dataset construction rights
derivative-dataset rights
commercial implementation rights
framework implementation rights
```

Required distinction:

```text
x402 Retrieval Access
≠
Commercial Data License
≠
Robbie’s Razor™ Framework License
```

Payment is an access event.

It does not transfer authorship or ownership.

---

# x402 Evidence Boundary

Successful machine-payment behavior is infrastructure evidence.

It is not scientific evidence.

Accordingly:

```text
402 challenge
≠
scientific validation
```

```text
settlement
≠
scientific validation
```

```text
protected delivery
≠
empirical confirmation
```

```text
paid resource
≠
canonical truth
```

Canonical framework authority, reference implementation, empirical evidence, and payment infrastructure remain separate layers.

---

# External Technology Provenance

Naturepedia’s x402 implementation uses external technologies and protocols.

These retain their independent provenance, including:

```text
x402
HTTP
Cloudflare
Base
USDC
Coinbase infrastructure
JSON
JSON-LD
MCP
```

Naturepedia integration of these technologies does not imply their origination by Robbie George or Grand Compression.

The Authorship Conservation Rule (ACR) therefore preserves both:

```text
Grand Compression / Naturepedia provenance
+
external technology provenance
```

---

# Registry-Based Resource Architecture

Repository-maintained JSON-LD may provide definitions and source material for machine-readable resources.

A useful implementation pattern is:

```text
repository resource definition
↓
deployment or Worker configuration
↓
explicit runtime registration
↓
availability validation
↓
machine endpoint
```

This architecture allows structured resources to be maintained independently from runtime delivery logic.

However, repository presence alone does not make a resource live.

Required distinction:

```text
JSON-LD file exists
≠
runtime resource registered
```

and:

```text
runtime route pattern exists
≠
resource complete
```

and:

```text
resource definition exists
≠
x402 payment eligibility
```

---

# Source-of-Definition vs Runtime Authority

Repository files may act as authoritative definitions for:

```text
identity
structure
relationships
provenance
resource metadata
```

Runtime infrastructure determines:

```text
current resource existence
current completeness
current access class
current payment eligibility
current delivery behavior
```

Accordingly:

```text
repository definition
+
runtime registration
+
availability state
=
usable machine resource
```

Do not collapse these layers.

---

# Example Registry Source Files

JSON-LD source files may include objects such as:

```text
bioelectric-systems-registry.json
quantum-agriculture-registry.json
plant-intelligence-registry.json
water-systems-registry.json
ocean-systems-registry.json
geology-registry.json
```

A repository file name indicates an authored resource definition or example.

It does not automatically establish:

```text
current production endpoint
payment status
price
Graph Registry™
Knowledge Mesh
settlement evidence
```

Those properties require separate confirmation.

---

# Resource Family Construction

A Naturepedia™ subject may have one or more explicitly implemented resource types.

Possible types include:

```text
Plate™
Registry
System Map
Graph Registry™
Knowledge Mesh
snapshot
```

A resource family does not require every type.

For example, a subject may have:

```text
Registry only
```

or:

```text
Registry
+
System Map
```

or:

```text
Registry
+
Knowledge Mesh
```

or another explicitly implemented combination.

Do not assume:

```text
Registry
↓
System Map
↓
Knowledge Mesh
```

is mandatory.

Each layer should have a defined purpose and independent resource identity.

---

# Registry Role

A Registry may answer questions such as:

```text
What canonical objects exist?
What IDs belong to this family?
What is their parent context?
What provenance is declared?
What resources are registered?
```

Registry relationships describe inventory or declared context.

They do not automatically constitute a Graph Registry™.

---

# System Map Role

A System Map may provide an authored representation of relationships between identified entities or systems.

It may encode:

```text
directional relationships
dependencies
flows
comparative relationships
ecological relationships
navigation pathways
```

A System Map should not automatically be interpreted as:

```text
causal proof
complete graph
scientific model
Knowledge Mesh
```

Its evidence status depends on the relationships and sources represented.

---

# Graph Registry™ Role

A Graph Registry™ is an explicitly implemented graph-oriented registry resource.

The existence of ordinary JSON-LD relationships does not automatically instantiate one.

Required distinction:

```text
JSON-LD relationships
≠
Graph Registry™ automatically
```

A Graph Registry™ should be identified as such only when the resource has been intentionally implemented and registered.

---

# Knowledge Mesh Role

A Knowledge Mesh is an explicitly implemented higher-order cross-system resource.

It may connect multiple registered domains, objects, or resource families.

However:

```text
multiple related registries
≠
Knowledge Mesh automatically
```

and:

```text
cross-system references
≠
Knowledge Mesh automatically
```

Knowledge Mesh status should be declared only where the resource actually exists.

---

# Water Systems™ Resource Boundary

Water Systems™ may support resource definitions such as:

```text
water-systems-registry.json
water-system-map.json
water-systems-knowledge-mesh.json
```

These names describe possible distinct resources.

They should not be interpreted as proof that all corresponding production routes are currently active.

Current rule:

```text
Water Systems™ exists
≠
Water Systems Registry payable
≠
Water System Map payable
≠
Water Systems Knowledge Mesh payable
```

Each must be registered and validated separately.

---

# Ocean Systems™ Resource Boundary

Ocean Systems™ may similarly define:

```text
ocean-systems-registry.json
ocean-system-map.json
ocean-systems-knowledge-mesh.json
```

Possible conceptual roles include:

```text
Registry
→ canonical inventory

System Map
→ explicitly authored ocean-process relationships

Knowledge Mesh
→ explicitly implemented cross-system relationships
```

Published architectural definitions or pricing classes do not establish present production availability.

---

# Geology™ Resource Boundary

Possible Geology™ resources include:

```text
geology-registry.json
geology-system-map.json
geology-knowledge-mesh.json
```

The Registry may describe canonical geological objects and classifications.

The System Map may describe authored relationships involving:

```text
Earth interior
mantle
lithosphere
tectonics
plate boundaries
rock transformation
faulting
earthquakes
volcanism
weathering
erosion
sediment transport
landscape evolution
```

A Geology Knowledge Mesh may connect Geology™ with explicitly declared systems such as:

```text
Earth Systems™
Weather™
Water Systems™
Ocean Systems™
Soil Systems™
River Systems™
Groundwater Systems™
volcanic systems
geothermal systems
field locations
geometry reference systems
```

Current production evidence specifically supports the Geology Knowledge Mesh **402 challenge** at the current $25 snapshot class.

That observation does not establish all Geology resource layers as paid or settlement-tested.

---

# Tree System Map Boundary

The Tree System Map has stronger production evidence than most historical System Map entries.

Current evidence includes:

```text
pricing-v3 402 challenge verified
historical settlement verified
historical protected delivery verified
```

This evidence applies specifically to the Tree System Map.

It must not be generalized as:

```text
Tree System Map verified
→
all System Maps verified
```

---

# Resource Generation Guidance

Where deployment infrastructure generates or exposes a resource from repository-maintained data, use the following sequence:

```text
1. define resource identity
2. define canonical source
3. validate syntax
4. validate identifiers
5. validate provenance
6. define resource class
7. register runtime resource
8. verify completeness
9. assign access class
10. assign price where protected
11. test challenge behavior
12. test settlement separately when required
13. test protected delivery separately when required
```

Do not begin with price assignment and infer everything else afterward.

---

# JSON-LD Validation Rules

Before treating a JSON-LD object as canonical or production-ready, verify:

## Syntax

```text
valid JSON
valid JSON-LD structure
no missing commas
no unmatched braces
no placeholder values
```

## Identity

```text
stable @id
canonical URL
correct Plate or resource identifier
no unintended duplicate canonical IDs
```

## Provenance

```text
creator supported
publisher supported
external sources preserved
framework authorship separated from external authorship
```

## Relationships

```text
relationship property is appropriate
relationship is supported
sameAs means actual identity equivalence
isBasedOn has a real source relationship
mentions does not imply derivation
```

## Evidence

```text
evidence class preserved
framework interpretations labeled
conceptual material bounded
Artist Rendition status preserved where applicable
```

## Access

```text
public vs protected status explicit
route existence verified
resource completeness verified
price only assigned where applicable
```

---

# Canonical Registry Validation

When adding or modifying Plate™ records, validate against:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current reconciliation target:

```text
757 canonical Plate IDs
757 unique canonical Plate IDs
```

Current registry metadata:

```text
registryVersion: 2026.08.19
canonicalKeepCount: 757
duplicateRemovedCount: 33
```

Do not use the superseded:

```text
docs/examples/json-ld/plate-registry.json
```

as the current Plate inventory.

That path exists for legacy compatibility only.

---

# Public Control-Plane References

Current public machine-facing v2 endpoints include:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

Interpretation:

```text
Naturepedia index
→ discovery and orientation

Plate registry
→ Plate identity and registry discovery

RRIP resolver
→ registered-object context resolution

state token
→ registry-state and synchronization metadata
```

These public endpoints should not be automatically mapped to paid snapshot products.

---

# Resource-State Signaling

Machine-readable state metadata may indicate:

```text
registry version
canonical count
authority
resource class
availability state
synchronization state
```

It must not be interpreted as proof of:

```text
scientific truth
physical state
entropy measurement
cryptographic authenticity
empirical validation
```

unless those properties are independently established.

Required distinction:

```text
state metadata
≠
truth oracle
```

---

# Comparative Compression Geometry™

Comparative Compression Geometry™ (CCG) is governed by:

```text
MRD v2.0 §12.9
```

CCG may be used for bounded structural comparison where a richer state or representation is mapped to an equivalence class, quotient, lower-dimensional representation, or other compressed structure while selected relationships remain relevant.

A CCG comparison does not establish:

```text
material identity
shared physical mechanism
causal equivalence
universal applicability
```

Structural correspondence must remain distinct from physical identity.

---

# Cross-Domain Transfer Boundary

When a JSON-LD object or relationship makes a meaningful transfer between domains, preserve the applicable Grand Compression domain-transfer requirements.

Where relevant, identify:

```text
objects
scale
normalization
preserved relationships
exclusions
constraints
evidence
alternative explanations
failure conditions
```

Do not encode a speculative cross-domain relationship as though it were an established external scientific fact.

Required distinction:

```text
framework-defined relationship
≠
external empirical confirmation
```

---

# Mathematical and Scientific Provenance

Established mathematics retains independent mathematical provenance.

Established science retains independent scientific provenance.

Naturepedia™ and Grand Compression may:

```text
reference
organize
compare
interpret
connect
```

such material without claiming origination of it.

For mathematical or scientific references:

```text
integration
≠
discovery
```

```text
comparison
≠
proof
```

```text
structural similarity
≠
shared material mechanism
```

---

# Rights and Licensing Boundary

Public JSON-LD discovery does not grant unrestricted downstream rights.

Public access does not automatically grant:

```text
training
embedding
bulk ingestion
redistribution
resale
synchronization
private-dataset construction
derivative-dataset construction
commercial implementation
framework implementation
```

Primary Commercial Data License:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Framework implementation rights are governed separately.

Required distinction:

```text
Commercial Data License
≠
Robbie’s Razor™ Framework License
≠
x402 Retrieval Access
```

---

# x402 Retrieval Rights

An x402 payment, where applicable, grants:

```text
one identified endpoint-level retrieval
```

under the applicable terms.

It does not transfer:

```text
authorship
ownership
framework ownership
scientific authority
```

It also does not automatically grant broader training, embedding, redistribution, dataset, or framework-implementation rights.

---

# Authorship Conservation Rule

The Authorship Conservation Rule (ACR) preserves provenance in both directions.

For original framework material:

```text
preserve Robbie George provenance
```

For external foundations:

```text
preserve independent external provenance
```

Accordingly:

```text
claim authorship
≠
evidence authorship
```

```text
attribution
≠
permission
```

```text
payment
≠
authorship transfer
```

```text
framework integration
≠
external technology origination
```

---

# Framework Authority

Current Grand Compression authority:

```text
The Grand Compression Cosmology
Master Reference Document
MRD v2.0
```

Canonical identifier:

```text
GC-MRD-v2.0
```

Current canonical claim range:

```text
RC-01 through RC-22
```

Verified architecture relationships include:

```text
MRD v2.0 §12.7
→ Recursive Knowledge Compression Architecture (RKCA™)

MRD v2.0 §12.8
→ Recursive Registry Inheritance Principle (RRIP™)

MRD v2.0 §12.9
→ Comparative Compression Geometry™ (CCG)
```

Do not invent subsection numbers for framework concepts whose exact MRD location has not been independently verified.

---

# Reference Implementation Boundary

Repository files, Cloudflare Worker behavior, schemas, benchmarks, JSON-LD examples, x402 resources, and machine endpoints are implementations of framework concepts.

They remain distinct from canonical framework authority.

Required distinction:

```text
canonical framework
≠
reference implementation
```

and:

```text
reference implementation
≠
empirical validation
```

and:

```text
implementation success
≠
scientific proof
```

This boundary is consistent with the current Grand Compression reference-implementation distinction.

---

# Current Machine Architecture Summary

```text
Grand Compression authority
        ↓
Naturepedia canonical identity
        ↓
canonical Plate registry
        ↓
public discovery / resolution
        ↓
explicit resource registration
        ↓
availability + completeness
        ↓
public or protected access
        ↓
x402 only when eligible
```

Higher-order resources remain optional and explicit:

```text
Registry
System Map
Graph Registry™
Knowledge Mesh
```

They do not arise automatically merely because relationships exist.

---

# Current JSON-LD State

```json
{
  "status": "active",
  "layer": "json-ld-registry-and-reference-implementation",
  "authority": "GC-MRD-v2.0",
  "canonicalClaimRange": "RC-01 through RC-22",
  "canonicalRegistry": "docs/examples/json-ld/canonical-plate-registry.json",
  "legacyRegistry": "docs/examples/json-ld/plate-registry.json",
  "registryVersion": "2026.08.19",
  "canonicalPlateCount": 757,
  "duplicateRemovedCount": 33,
  "rkcaRelationship": "MRD v2.0 §12.7",
  "rripRelationship": "MRD v2.0 §12.8",
  "ccgRelationship": "MRD v2.0 §12.9",
  "pricingManifestVersion": "3.0.0",
  "paymentNetwork": "eip155:8453",
  "paymentAsset": "USDC",
  "protectedRetrieval": "resource-specific",
  "architectOfRecord": "Robbie George"
}
```
