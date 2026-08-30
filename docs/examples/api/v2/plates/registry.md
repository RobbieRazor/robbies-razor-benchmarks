# Naturepedia v2 Plate Registry

## Status

**Endpoint class:** Public control plane  
**Endpoint:** `/api/v2/plates/registry.md`  
**Requires payment:** No  
**Architect of Record:** Robbie George  
**Current governing authority:** The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Registry principle:** Recursive Registry Inheritance Principle (RRIP™)

---

# Purpose

This endpoint provides public machine-facing discovery and navigation for registered Naturepedia™ Plate™ assets.

It is intended to help:

- AI agents;
- MCP-compatible systems;
- retrieval engines;
- registry crawlers;
- semantic search systems;
- x402-capable clients;

identify:

- registered Plate™ families;
- canonical Plate identifiers;
- parent registry context;
- public discovery paths;
- RRIP resolution paths;
- resource-availability boundaries;
- protected-retrieval signals where explicitly implemented.

This endpoint is a **discovery and navigation surface**.

It is not itself the complete canonical Plate registry.

---

# Canonical Registry Authority

The authoritative machine-readable Plate inventory is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current canonical registry metadata:

```text
registryVersion: 2026.08.30
canonicalKeepCount: 758
duplicateRemovedCount: 33
registryReferenceCount: 762
canonicalSystemCount: 111
intentionalCrossReferenceCount: 4
```

Expanded AI-readable discovery resources:

```text
https://www.robbiegeorgephotography.com/llms.txt
https://www.robbiegeorgephotography.com/llms-full.txt
```

Required distinction:

```text
/api/v2/plates/registry.md
=
public discovery / navigation
```

while:

```text
docs/examples/json-ld/canonical-plate-registry.json
=
canonical machine-readable Plate inventory
```

---

# Plate Identifier Format

Naturepedia™ Plate identifiers use the pattern:

```text
page-slug#plate-slug
```

Examples:

```text
willows-of-north-america#willow-biodiversity-plate
cedars-of-north-america#cedar-identification-plate
firs-of-north-america#fir-carbon-storage-plate
```

When a Plate identifier is supplied inside an HTTP query parameter, the `#` character should be URL-encoded as:

```text
%23
```

Example RRIP request:

```text
/api/v2/rrip/resolve?id=willows-of-north-america%23willow-biodiversity-plate
```

---

# Registry Architecture

Naturepedia™ defines multiple possible machine-resource layers.

These include:

```text
Plate™
Registry
Meta-Registry
Graph Registry™
Knowledge Mesh
```

These are **defined resource types**, not a mandatory production sequence for every Plate.

A Plate may exist without an instantiated:

```text
Meta-Registry
Graph Registry™
Knowledge Mesh
```

Required distinction:

```text
resource type defined
≠
resource instantiated
```

and:

```text
Plate registered
≠
Graph Registry automatically exists
```

and:

```text
Plate registered
≠
Knowledge Mesh automatically exists
```

Higher-order resources should be described as active only when explicitly implemented and registered.

---

# RRIP Relationship

Recursive Registry Inheritance Principle (RRIP™) is governed by:

```text
MRD v2.0 §12.8
```

RRIP may resolve:

- Plate identity;
- parent registry context;
- declared relationships;
- provenance;
- governance metadata;
- available machine-resource context.

Public RRIP resolver:

```text
/api/v2/rrip/resolve
```

RRIP resolution does not require that every Plate resolve through every higher-order resource layer.

Use:

```text
Plate
→ directly registered parent context
→ declared relationships
→ available higher-order resources when implemented
```

rather than assuming:

```text
every Plate
→ Registry
→ Meta-Registry
→ Graph Registry
→ Knowledge Mesh
```

---

# Public Discovery Workflow

Recommended public machine workflow:

```text
Discovery
↓
Plate Registry
↓
RRIP Resolution when needed
↓
Resource Selection
↓
Availability Check
```

After availability is determined:

```text
public resource
→ free retrieval
```

or:

```text
explicitly registered protected resource
→ x402 flow may apply
```

The public registry endpoint itself does not imply payment.

---

# Resource Availability Policy

Naturepedia™ separates:

```text
route family
resource identity
resource existence
resource completeness
payment eligibility
```

These states must not be collapsed.

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
eligible for HTTP 402
```

Required distinction:

```text
syntactically valid route
≠
existing resource
```

and:

```text
registered Plate
≠
protected payload
```

and:

```text
published pricing class
≠
active payable resource
```

---

# Current Registry Coverage

The canonical registry contains:

```text
758 canonical Plate records
```

organized across multiple Naturepedia™ systems and families.

Representative registry coverage includes:

## Earth and Environmental Systems

```text
Earth Systems™
Weather™
Water Systems™
Ocean Systems™
Geology™
River Systems™
Wetland Ecosystems™
Forest Ecosystems™
Grassland Ecosystems™
Mountain & Alpine Ecosystems™
Floodplains™
Groundwater Systems™
Estuaries & Coastal Systems™
Climate Carbon Feedbacks™
Soil Systems™
Soil Carbon Systems™
Carbon & Microbial Life™
Forest Carbon Systems™
Volcanic Landscapes™
Geothermal Ecosystems™
Hydrothermal Ecosystems™
Microbial Life Systems™
```

## Plant and Ecological Systems

```text
Plant Intelligence™
Plant Communication™
Plant Electrophysiology™
Mycorrhizal Networks™
Electrical Ecology™
Plant Communities / Native Habitat Systems™
Biodiversity & Ecosystem Balance™
Ecological Restoration & Habitat Recovery™
Pollinator Systems™
```

## Geometry and Mathematical Reference Systems

```text
Geometry of Nature™
Hopf Fibration
E8 Lattice™
Fractals™
Fibonacci™
```

These registry entries do not imply that framework interpretations constitute independent proof of external mathematics, physical mechanisms, or cross-domain causality.

Established mathematics retains its independent historical provenance.

### Hopf Fibration Public Discovery Boundary

```text
Canonical page: https://www.robbiegeorgephotography.com/hopf-fibration
Parent system: Geometry of Nature™
Domain: Mathematics / Topology / Fiber Bundles / State-Space Geometry
Evidence class: established mathematics
CCG relationship: bounded structural comparison class
Governing relationship: MRD v2.0 §12.9 — Comparative Compression Geometry™
```

Current machine-access status:

```text
public canonical page: active
Plate family: not registered
Registry: not registered
System Map: not registered
Knowledge Mesh: not registered
x402 protected route: not registered
```

Registry discovery of the Hopf Fibration does not imply that a Hopf Plate family, Registry, System Map, Knowledge Mesh, or paid x402 resource currently exists. Its Grand Compression relationship remains comparative only.

---

### Fibonacci™ / Pisano Periods Registry Boundary

Canonical Fibonacci page:

https://www.robbiegeorgephotography.com/fibonacci

Parent system:

Geometry of Nature™

Fibonacci canonical Plate count:

11

Featured mathematical Plate:

Pisano Periods & Constraint Bifurcation Plate™

Canonical Plate ID:

fibonacci#pisano-periods-constraint-bifurcation-plate

Classification:

Mathematics / Number Theory / Modular Arithmetic / Fibonacci Periodicity

Evidence class:

first-party-published-mathematical-result

Comparative Compression Geometry™ relationship:

constraint-geometry-case-study

Current registry state:

canonical Plate: registered
structured payload: not registered
individual Structured Plate route: reserved
current individual response: HTTP 409 PLATE_PAYLOAD_NOT_REGISTERED
payment challenge issued: no
planned Structured Plate price if activated: 0.25 USDC

Fibonacci Registry state:

active x402 protected resource
access class: bounded subtree
price: 5.00 USDC

Mathematical summary:

π(m) = 2m
→ m = 12 × 5^k for k >= 0

π(m²) = 2m
→ unique solution m = 12
→ modulus 144
→ π(144) = 24

Required distinction:

registered canonical Plate
≠
registered structured payload

and:

planned price
≠
active payable Plate

and:

mathematical structural comparison
≠
shared physical, biological, causal, material, or universal mechanism

# Tree Family Coverage

Representative Tree family registries include:

```text
Birches of North America™
Oaks of North America™
Maples of North America™
Aspens of North America™
Pines of North America™
Spruces of North America™
Firs of North America™
Hemlocks of North America™
Cedars of North America™
Cypress Trees of North America™
Willows of North America™
Cottonwoods of North America™
Hickories of North America™
Trees of North America™
```

Registry inclusion means that the Plate identities are represented in the canonical inventory.

It does not automatically mean that each family has:

- a protected registry snapshot;
- a System Map;
- a Graph Registry™;
- a Knowledge Mesh;
- or an active x402 product.

---

# Wildlife and Field Coverage

Representative wildlife and field families include:

```text
Wildlife Species™
Wildlife Systems & Ecology™
Wildlife Conservation & Habitat™
Wildlife Migration & Seasonal Patterns™
Wildlife Behavior & Ecology™
Wildlife Observation & Field Techniques™
Wildlife Sign & Tracking™
Animal Scat Identification™
Keystone Species & Trophic Cascades™
Food Webs & Ecological Relationships™
Wildlife Adaptation & Survival™
Birds of Prey™
Waterfowl & Wetland Birds™
Songbirds, Seabirds & Other Birds™
Mammals of North America™
North American Animal Tracks™
```

Field-location and photography-guide coverage includes locations such as:

```text
Acadia
Grand Teton
Yellowstone
Blackwater
Bosque del Apache
Lake Mattamuskeet
Chincoteague
Aransas
Machias Seal Island
```

Exact Plate identity should always be resolved against the canonical registry rather than inferred from this summary.

---

# Plate Categories

The registry contains multiple Plate types, including:

```text
System Plates™
Species Plates™
Identification Plates™
Track Plates™
Comparison Track Plates™
Field Location Plates™
Photography Guide Plates™
Habitat Plates™
Biodiversity Plates™
Ecological Relationship Plates™
Water System Plates™
Earth System Plates™
Plant System Plates™
Governance Plates™
Framework Architecture Plates™
Artist Rendition Plates™
```

A Plate type describes the declared role of the asset.

It does not independently establish:

```text
scientific validity
causal proof
universal applicability
material identity across domains
```

---

# Protected Retrieval Boundary

Public discovery remains separate from protected machine retrieval.

The authoritative production pricing manifest is:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current pricing manifest version:

```text
3.0.0
```

Current pricing classes include:

```text
Discovery
0 USDC

Atomic canonical query
0.005 USDC
5000 atomic units

Enriched relationship query
0.025 USDC
25000 atomic units
active for the registered Biography Enriched Query

Structured Plate™
0.25 USDC
250000 atomic units
resource-specific

Bounded subtree / Registry / System Map class
5.00 USDC
5000000 atomic units
resource-specific

Full Registry / Knowledge Mesh snapshot class
25.00 USDC
25000000 atomic units
resource-specific
```

A pricing class does not activate every possible resource in that class.

---

# Explicit Structured Plate Examples

The canonical registry may include explicit machine-access metadata for protected Plate resources that have been independently registered and validated.

Examples include:

```text
Commercial Data License Plate™
Commercial Intelligence Pricing Plate™
Robbie George Biography Plate™
```

Such records may include fields such as:

```text
access
accessClass
priceUSDC
atomicUnits
routeStatus
x402Route
payloadUrl
```

These fields apply to the identified resource only.

They must not be generalized automatically to every Plate in the same family.

---

# Rights Boundary

Public discovery and registry inclusion do not grant:

- training rights;
- embedding rights;
- bulk-ingestion rights;
- redistribution rights;
- resale rights;
- synchronization rights;
- private-dataset construction rights;
- derivative-dataset rights;
- commercial implementation rights;
- Robbie’s Razor™ framework implementation rights.

An x402 payment grants one identified endpoint-level retrieval under applicable terms.

Required distinction:

```text
x402 Retrieval Access
≠
Commercial Data License
≠
Robbie’s Razor™ Framework License
```

Payment does not transfer authorship or ownership.

---

# Governance

Current framework authority:

```text
The Grand Compression Cosmology
Master Reference Document
MRD v2.0
```

Canonical identifier:

```text
GC-MRD-v2.0
```

Governance expression:

```text
Gr <= Es
```

This expression is framework governance metadata.

It must not be interpreted as independent empirical validation of a scientific or physical claim.

---

# Authorship and Provenance

Original Grand Compression, Robbie’s Razor™, Naturepedia™, RRIP™, Plate™ architecture, Graph Registry™, Knowledge Mesh, and related framework-specific concepts retain Robbie George provenance where they originate within the framework.

External mathematics, science, technologies, and protocols retain their independent provenance.

Accordingly:

```text
framework authorship
≠
authorship of external mathematics or science
```

and:

```text
registry inclusion
≠
empirical confirmation
```

and:

```text
use within Naturepedia
≠
origination by Naturepedia
```

---

# Related Public Endpoints

Naturepedia discovery:

```text
/api/v2/naturepedia/index.md
```

Plate registry discovery:

```text
/api/v2/plates/registry.md
```

RRIP resolution:

```text
/api/v2/rrip/resolve
```

Registry-state signaling:

```text
/api/v2/razor/state-token
```

These are public control-plane resources.

They should not automatically be interpreted as paid aliases for protected resources.

---

# Machine Interpretation Guidance

Agents should use this endpoint to discover registered Plate families and identify appropriate next-resolution steps.

For exact current Plate identity:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

For relationship resolution:

```text
/api/v2/rrip/resolve
```

For state awareness:

```text
/api/v2/razor/state-token
```

For protected retrieval:

```text
resolve resource
↓
verify existence
↓
verify completeness
↓
verify protected status
↓
apply pricing class
↓
402 only when eligible
```

Never infer:

```text
route family
+
published price
=
active payable product
```

---

# Version

```json
{
  "version": "2.0.1",
  "registryType": "plate-discovery",
  "endpointClass": "public-control-plane",
  "canonicalRegistry": "docs/examples/json-ld/canonical-plate-registry.json",
  "canonicalPlateCount": 758,
  "registryVersion": "2026.08.30",
  "authority": "GC-MRD-v2.0",
  "protectedRetrieval": "resource-specific",
  "dateModified": "2026-08-30",
  "architectOfRecord": "Robbie George"
}
```
