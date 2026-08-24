# Naturepedia™ x402 Live Endpoints
## Production Machine-Retrieval Status

## Document Status

**Status:** Production infrastructure live  
**Worker:** `cold-bird-7036`  
**Primary domain:** `https://www.robbiegeorgephotography.com`  
**Current pricing manifest:** v3.0.0  
**Current governing authority:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Network:** Base — `eip155:8453`  
**Asset:** USDC

This document records current machine-facing endpoint architecture and selected verified production behavior for Naturepedia™.

It preserves the distinction among:

```text
public discovery
resource identity
resource availability
pricing class
payment challenge
settlement
protected delivery
usage rights
```

These states must not be collapsed into one another.

---

# Current Machine Status

```text
Production Worker:
LIVE

Public machine discovery:
LIVE

v2 public control plane:
LIVE

Atomic Query:
ACTIVE for explicitly registered deterministic resources

Enriched Query:
ACTIVE for the explicitly registered Biography Enriched Query

Structured Plate™:
ACTIVE for explicitly registered and validated resources

$5 bounded-resource pricing class:
DEFINED
specific resource availability is registration-specific

$25 large-snapshot pricing class:
DEFINED
specific resource availability is registration-specific

Historical live settlement:
VERIFIED

Historical protected payload delivery:
VERIFIED
```

Machine metadata:

```text
x402-status: verified-live
x402-network: eip155:8453
x402-asset: USDC
x402-production-status: active
x402-first-settlement: successful
```

Required distinction:

```text
production x402 infrastructure live
≠
every possible protected resource active
```

---

# Canonical and Pricing Authority

Grand Compression authority:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Authoritative x402 pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Commercial Data License:

https://www.robbiegeorgephotography.com/commercial-data-license

Framework Licensing:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

---

# Core Production Rule

The production gateway must resolve:

```text
resource
before
price
```

not:

```text
route shape
→ price
→ assume resource exists
```

Protected retrieval follows:

```text
Request
↓
Canonical resource resolution
↓
Explicit availability validation
↓
Access-class resolution
↓
Pricing
↓
402 challenge when applicable
```

---

# Fail-Closed Availability Model

## Unknown Resource

```text
HTTP 404 Not Found
payment challenge: no
```

## Known but Incomplete Resource

```text
HTTP 409 Conflict
payment challenge: no
```

## Registered + Complete + Protected Resource

```text
eligible for HTTP 402 Payment Required
```

This prevents an agent from being asked to pay for a resource that is unavailable or incomplete.

---

# Endpoint Families

## Legacy Compatibility Namespace

Legacy machine paths may remain available where explicitly implemented:

```text
/x402/*
```

The existence of this namespace does not mean every syntactically valid `/x402/` path exists.

---

# Current v1 Namespaces

Current machine-retrieval namespaces include:

```text
/v1/query/atomic/*
/v1/query/enriched/*
/v1/taxonomy/*
/v1/plates/*
/v1/registries/*
/v1/knowledge-mesh/*
/v1/sovereign/*
```

These are route families.

Required distinction:

```text
namespace exists
≠
every path inside namespace exists
```

---

# Atomic Query

Public route template:

```text
/v1/query/atomic/{resource}
```

Canonical internal compatibility template:

```text
/x402/query/atomic/{resource}
```

Current verified Atomic resource:

```text
/v1/query/atomic/robbie-george-biography-plate
```

Canonical internal path:

```text
/x402/query/atomic/robbie-george-biography-plate
```

Canonical identifier:

```text
robbie-george#robbie-george-biography-plate
```

Canonical authority:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Configuration:

```text
Access class: atomic
Price: 0.005 USDC
Atomic units: 5000
Resource class: atomic-query
Schema: naturepedia.atomic-query.v1
Status: active for explicitly registered deterministic payloads
```

---

# Verified Atomic Challenge

Observed production result:

```text
STATUS: 402
AMOUNT: 5000
TIER: atomic
PAYMENT REQUIRED: true
```

Result:

```text
PASS
```

This verifies the challenge behavior for the registered Biography Atomic Query.

During that activation validation:

```text
new Atomic payment supplied: no
new Atomic settlement: no
new Atomic protected delivery test: no
```

Therefore:

```text
Atomic challenge verified
≠
Atomic settlement newly verified
```

---

# Atomic Availability Tests

## Known but Incomplete

Tested resource:

```text
/v1/query/atomic/robbies-razor-plate
```

Observed:

```text
409 Conflict
payment challenge: false
```

Result:

```text
PASS
```

## Unknown

A deliberately nonexistent Atomic identifier returned:

```text
404 Not Found
payment challenge: false
```

Result:

```text
PASS
```

Atomic safety matrix:

```text
registered + complete
→ 402 / 5000 / atomic

known incomplete
→ 409 / no payment

unknown
→ 404 / no payment
```

---

# Enriched Query

Public route template:

```text
/v1/query/enriched/{resource}
```

Current pricing:

```text
0.025 USDC
25000 atomic units
```

Current production state:

```text
ACTIVE FOR ONE EXPLICITLY REGISTERED RESOURCE
```

Current registered production route:

```text
/v1/query/enriched/robbie-george-biography-plate
```

Verified challenge behavior:

```text
STATUS: 402
AMOUNT: 25000
TIER: enriched
PAYMENT REQUIRED: true
```

No agent should infer that another Enriched resource is active merely because:

- the route template exists;
- the price is published;
- a pricing variable exists.

Required rule:

```text
published Enriched price or route template
≠
blanket Enriched resource availability
```

Activation remains resource-specific and requires an explicitly registered, governed, deterministic payload plus production validation.

---

# Structured Plate™ Retrieval

Current verified registered routes:

```text
/v1/plates/item/commercial-data-license-plate
/v1/plates/item/commercial-intelligence-pricing-plate
/v1/plates/item/robbie-george-biography-plate
```

Configuration:

```text
Access class: single-plate
Price: 0.25 USDC
Atomic units: 250000
```

Verified challenge behavior for all three:

```text
STATUS: 402
AMOUNT: 250000
TIER: single-plate
PAYMENT REQUIRED: true
```

Result:

```text
PASS
```

Unknown Plate:

```text
404
no payment
```

Known but incomplete Plate:

```text
409
no payment
```

Registered complete protected Plate:

```text
eligible 402
```

No new `$0.25` settlement or protected-delivery test was performed during the August 20 regression validation.

---

# `$5` Bounded-Resource Class

Current pricing class:

```text
5.00 USDC
5000000 atomic units
gateway class: subtree
```

This class may apply to qualifying bounded resources such as:

- taxonomy subtrees;
- Registries;
- identity graphs;
- System Maps.

The pricing class itself does not activate every possible resource.

However, this repository contains production evidence for at least one specific `$5` protected resource:

```text
/v1/plates/tree-system-map
```

Pricing-v3 challenge observed:

```text
402 Payment Required
5000000 atomic units
tier: subtree
```

Therefore:

```text
Tree System Map
→ challenge-verified under $5 class
```

but:

```text
Tree System Map verified
≠
every $5 resource active
```

---

# `$25` Snapshot Class

Current pricing class:

```text
25.00 USDC
25000000 atomic units
gateway class: snapshot
```

This class may apply to qualifying explicitly registered large resources such as:

- full Registry snapshots;
- Knowledge Mesh snapshots.

The class does not automatically instantiate every possible large resource.

Production evidence exists for at least one specific `$25` resource:

```text
/v1/knowledge-mesh/geology
```

Pricing-v3 challenge observed:

```text
402 Payment Required
25000000 atomic units
tier: snapshot
```

Therefore:

```text
Geology Knowledge Mesh
→ challenge-verified under $25 class
```

but:

```text
Geology Knowledge Mesh verified
≠
every Knowledge Mesh active
```

---

# Current Pricing Table

| Access class | Price | Atomic units | Production interpretation |
|---|---:|---:|---|
| Discovery / previews | Free | `0` | Public where exposed |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active for explicitly registered deterministic resources |
| Enriched relationship query | `$0.025 USDC` | `25000` | Biography Enriched Query challenge verified; other resources require explicit registration |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active for explicitly registered and validated Plate resources |
| Bounded subtree / Registry / System Map class | `$5.00 USDC` | `5000000` | Pricing class defined; Tree System Map challenge specifically verified |
| Full Registry / Knowledge Mesh snapshot class | `$25.00 USDC` | `25000000` | Pricing class defined; Geology Knowledge Mesh challenge specifically verified |

---

# Public v2 Control Plane

Current public endpoints:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These exact endpoints are public machine-facing infrastructure resources.

They are served independently of protected paid payloads.

Required distinction:

```text
public control-plane endpoint
≠
protected commercial resource
```

---

# Naturepedia Discovery Endpoint

```text
/api/v2/naturepedia/index.md
```

Purpose:

- machine discovery;
- Naturepedia navigation;
- resource-family awareness;
- canonical routing orientation.

It does not automatically create protected resources.

---

# Plate Registry Endpoint

```text
/api/v2/plates/registry.md
```

Purpose:

- Plate™ discovery;
- registry navigation;
- resource identity;
- routing information.

Do not automatically describe this endpoint as a Graph Registry™ unless the returned production payload explicitly implements Graph Registry semantics.

Required distinction:

```text
Plate registry
≠
Graph Registry automatically
```

---

# RRIP Resolution Endpoint

```text
/api/v2/rrip/resolve
```

Purpose:

- RRIP-oriented relationship resolution;
- inheritance-path lookup;
- registry relationship grounding.

Canonical relationship:

```text
MRD v2.0 §12.8
→ Recursive Registry Inheritance Principle (RRIP™)
```

This public resolver does not automatically imply a paid `$25` RRIP snapshot.

---

# Registry-State Endpoint

```text
/api/v2/razor/state-token
```

Purpose:

- registry version signaling;
- registry-state comparison;
- state signatures;
- registry-count metadata;
- cache coordination;
- synchronization metadata.

It does not establish:

```text
truth
scientific validity
physical entropy
```

Required distinction:

```text
state signature
≠
evidence validation
```

---

# Public v2 Workflow

A client may use:

```text
State Awareness
↓
Discovery
↓
Registry / Resolution
↓
Resource Selection
↓
Availability Check
```

After resource resolution:

```text
public resource
→ free retrieval
```

or:

```text
registered protected resource
→ x402 flow
```

may apply.

---

# Knowledge Mesh Boundary

Knowledge Mesh is a defined higher-order resource class within the architecture.

It is **not a mandatory stage of every machine retrieval**.

Use:

```text
Discovery
→ Resolution
→ Available Resource
→ Optional protected retrieval
```

rather than forcing:

```text
every request
→ Knowledge Mesh traversal
```

A Knowledge Mesh should appear only when the selected resource actually belongs to an implemented Knowledge Mesh path.

---

# RKCA Resource Hierarchy Boundary

Framework architecture may describe:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

This describes possible structural organization.

It does not mean every Plate currently has every higher-order layer instantiated.

Required distinction:

```text
resource type defined
≠
production resource instantiated
```

---

# Public v2 Endpoint Delivery Boundary

The four core endpoints:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

should be documented as their **actual public endpoints**.

Do not simultaneously describe them as though the public request itself is simply a paid alias for:

```text
/x402/naturepedia-system-map.json
/x402/plate-registry-expanded.json
/x402/rrip-resolve.json
/x402/state-token.json
```

unless that exact aliasing behavior is required by the runtime implementation and clearly distinguished from access policy.

Implementation reuse of an internal payload does not transform a public control-plane endpoint into a paid resource.

---

# Historical Verified Settlement

A successful live Base USDC settlement has been recorded in production.

Historical transaction:

```text
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376
```

Historical verified resource:

```text
/v1/plates/tree-system-map
```

Recorded historical behavior included:

```text
browser request
→ 200 human bypass

API request
→ 402

successful paid retrieval
→ 200

settlement
→ success
```

This establishes:

```text
production settlement capability
+
historical protected-delivery capability
```

It does not establish:

```text
settlement completed on every current protected route
```

---

# Challenge vs Settlement vs Delivery

These states must remain separate.

```text
402 challenge verified
≠
settlement verified
```

```text
settlement verified
≠
every route settlement-tested
```

```text
protected delivery verified historically
≠
protected delivery retested for every new class
```

Current known examples:

```text
Tree System Map:
historical end-to-end settlement/delivery evidence exists
pricing-v3 challenge also verified

Geology Knowledge Mesh:
pricing-v3 challenge verified
new settlement not tested in that observation

Atomic Biography:
challenge verified
new settlement not tested

Structured Plates:
challenge verified
new settlement not tested in regression round

Enriched:
Biography Enriched Query challenge verified; other resources require explicit registration
```

---

# Human vs Machine Behavior

Human browser traffic may receive public informational or gateway responses.

Machine-oriented requests to registered protected resources may receive:

```text
402 Payment Required
```

The response depends on:

- resource identity;
- availability;
- requested representation;
- access policy.

A machine-style header alone does not create a protected resource.

---

# Retrieval Rights Boundary

An x402 payment grants:

```text
one endpoint-level retrieval
```

of the identified protected resource under applicable terms.

It does not automatically grant:

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

---

# Commercial and Framework Rights

Commercial data retrieval rights and framework implementation rights remain separate.

```text
x402 Retrieval Access
≠
Commercial Data License
≠
Robbie’s Razor™ Framework License
```

Payment is retrieval authorization, not ownership or framework licensing.

---

# Payment and Evidence Boundary

Required distinctions:

```text
payment
≠
canonical authority
```

```text
payment
≠
scientific validation
```

```text
registry inclusion
≠
truth
```

```text
successful machine retrieval
≠
independent empirical confirmation
```

Canonical orientation:

```text
RC-21 — Reference Implementation Distinction
```

---

# Hopf Fibration Boundary

Hopf Fibration is an established mathematical reference exposed through public discovery.

Current status:

```text
requiresPayment: false
```

Do not infer paid routes such as:

```text
/v1/registries/hopf-fibration
/v1/plates/hopf-fibration-map
/v1/knowledge-mesh/hopf-fibration
/x402/hopf...
```

unless those resources are explicitly created and registered in a later production change.

---

# Current Verified Production Matrix

```text
PUBLIC DISCOVERY
Status: live

PUBLIC v2 CONTROL PLANE
Status: live

ATOMIC BIOGRAPHY QUERY
Price: 0.005 USDC
Units: 5000
Challenge: verified
Settlement in activation round: not performed

ATOMIC KNOWN-INCOMPLETE
409
No payment
Verified

ATOMIC UNKNOWN
404
No payment
Verified

ENRICHED QUERY
Price: 0.025 USDC
Units: 25000
Status: ACTIVE FOR THE REGISTERED BIOGRAPHY ENRICHED QUERY
Challenge: 402 / 25000 / enriched verified
Settlement in activation validation: not performed

STRUCTURED PLATES
Price: 0.25 USDC
Units: 250000
Three registered challenge routes verified
New settlement in regression round: not performed

TREE SYSTEM MAP
Price: 5.00 USDC
Units: 5000000
Pricing-v3 challenge: verified
Historical settlement: verified
Historical protected delivery: verified

GEOLOGY KNOWLEDGE MESH
Price: 25.00 USDC
Units: 25000000
Pricing-v3 challenge: verified
New settlement in Aug. 18 observation: not performed
```

---

# Final Production Interpretation

The strongest current model is:

```text
canonical identity
↓
public discovery
↓
explicit resource registration
↓
availability
↓
resource class
↓
fixed price
↓
402 when protected
↓
settlement when authorized
↓
protected retrieval
```

Never infer:

```text
URL family
+
published price
=
live payable product
```

---

# Attribution

Naturepedia™, Robbie’s Razor™, Plate™ Architecture, RRIP™, Graph Registry™, Knowledge Mesh terminology, and associated original Grand Compression machine-infrastructure concepts originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

These materials are governed by the **Authorship Conservation Rule (ACR)**.

x402, Base, USDC, Cloudflare, HTTP, MCP, JSON, and related external protocols and technologies retain their independent provenance and ownership.

---

## Legacy x402 Endpoint Inventory

> **Historical / compatibility documentation**
>
> The entries below preserve earlier x402 endpoint design, deployment, and registry-expansion documentation.
>
> They are **not the authoritative current production-status matrix**.
>
> For current production interpretation, use the verified production sections above together with the authoritative pricing manifest:
>
> `https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json`
>
> Historical route documentation does not establish that the same resource is currently registered, complete, protected, payable, settlement-tested, or deliverable.

Required interpretation:

```text
historically documented route
≠
currently active protected resource
```

```text
historical price
≠
current resource availability
```

```text
historical "Live" label
≠
current independent verification
```

```text
route pattern
≠
resource existence
```

The current production availability model remains:

```text
unknown resource
→ 404
→ no payment challenge

known but incomplete resource
→ 409
→ no payment challenge

registered + complete + protected resource
→ eligible for 402
```

---

# Historical Core x402 Route Inventory

The following endpoint names are retained as historical architecture references.

## Plate Registry

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/plate-registry.json
```

Historical purpose:

```text
Compressed semantic registry retrieval.
```

Current interpretation:

The route name is preserved as historical documentation only. Current canonical Plate inventory authority is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

The older:

```text
docs/examples/json-ld/plate-registry.json
```

is a superseded compatibility pointer and should not be treated as the current canonical inventory.

---

## Identity Graph

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/identity-graph.json
```

Historical purpose:

```text
Identity, authorship, provenance, and governance retrieval.
```

Current interpretation:

```text
historical endpoint documentation
≠
current protected-resource verification
```

Any present-day paid status must be established independently through current resource registration and gateway behavior.

---

## Naturepedia System Map

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/naturepedia-system-map.json
```

Historical purpose:

```text
Species
→ Ecosystem
→ Location
→ Season
relationship retrieval
```

Current interpretation:

This preserves the earlier System Map concept.

It does not establish current registration, completeness, price eligibility, or settlement status for this specific resource.

---

## Expanded Plate Registry

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/plate-registry-expanded.json
```

Historical purpose:

```text
Species
→ Tree Families
→ Plant Communities
→ Ecosystems
→ Geography / Locations
→ Time / Migration / Seasons
→ Conservation
```

### June 2026 Historical Expansion Snapshot

Earlier documentation recorded:

```text
plateCount: 163
```

and:

```text
lastExpansion:
Soil, Carbon, Feedbacks, Bioelectric,
Quantum Agriculture, and Plant Intelligence
Expansion — June 2026
```

Systems documented in that expansion included:

```text
Soil Systems™
Carbon Cycle™
Ecosystem Feedbacks™
Bioelectric Systems™
Quantum Agriculture™
Plant Intelligence™
```

Historical added-Plate counts were documented as:

```text
Soil Systems: 11
Carbon Cycle: 10
Ecosystem Feedbacks: 10
Bioelectric Systems: 10
Quantum Agriculture: 12
Plant Intelligence: 10

Total historical addition: 63
```

This `163` count is a **historical inventory snapshot**.

It has been superseded by the current canonical registry state:

```text
canonical Plate count: 757
registryVersion: 2026.08.19
duplicateRemovedCount: 33
```

Do not use the historical `163` count for current registry calculations.

---

# Historical Relationship-Map Routes

## Pollinator System Map

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/pollinator-system-map.json
```

Historical purpose:

```text
Floral resources
↔ Pollinators
↔ Plant communities
↔ Soil microbiomes
↔ Mycelial networks
↔ Seasonal timing
```

Current status interpretation:

```text
historically documented
current protected-resource state: requires independent verification
```

---

## Wildlife System Map

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/wildlife-system-map.json
```

Historical purpose:

```text
Wildlife species
↔ Tracks
↔ Behavior
↔ Habitats
↔ Ecosystems
↔ Field locations
↔ Seasonal timing
↔ Conservation systems
```

Current status interpretation:

```text
historically documented
current protected-resource state: requires independent verification
```

---

# Historical Water Systems™ Retrieval Family

Earlier documentation described a Water Systems™ protected retrieval family on:

```text
Base
eip155:8453
USDC
```

with governance metadata:

```text
Gr <= Es
```

That historical design information is preserved below.

It must not be interpreted as proof that all three Water Systems resources remain currently registered and payable.

---

## Water Systems Registry

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/water-systems-registry.json
```

Historical v1 alias:

```text
https://www.robbiegeorgephotography.com/v1/registries/water-systems
```

Historical purpose:

```text
Entity-resolved Water Systems™ registry connecting
wetlands,
river systems,
floodplains,
groundwater systems,
estuaries,
coastal systems,
watersheds,
surface water,
subsurface water,
hydrological storage,
and ecological flow.
```

Historical pricing classification:

```text
5000000 atomic units
5.00 USDC
subtree / registry class
```

Current interpretation:

```text
pricing class remains defined
≠
this specific resource is currently verified active
```

---

## Water System Map

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/water-system-map.json
```

Historical v1 alias:

```text
https://www.robbiegeorgephotography.com/v1/plates/water-system-map
```

Historical purpose:

```text
Hydrological interaction map connecting
precipitation,
runoff,
infiltration,
groundwater recharge,
river discharge,
wetlands,
floodplain inundation,
estuarine exchange,
coastal systems,
watershed behavior,
and wildlife habitat.
```

Historical pricing classification:

```text
5000000 atomic units
5.00 USDC
subtree / System Map class
```

Current interpretation:

Current availability of this specific resource must be determined independently.

Do not infer its active status from the current $5 pricing class alone.

---

## Water Systems Knowledge Mesh

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/knowledge-mesh/water-systems
```

Historical v1 alias:

```text
https://www.robbiegeorgephotography.com/v1/knowledge-mesh/water-systems
```

Historical purpose:

```text
Water Systems™ Knowledge Mesh connecting weather,
precipitation,
storm,
temperature,
snowpack,
evaporation,
rivers,
wetlands,
floodplains,
groundwater,
estuaries,
coastal systems,
seasonal ecology,
and surface-subsurface water behavior.
```

Historical pricing classification:

```text
25000000 atomic units
25.00 USDC
snapshot / Knowledge Mesh class
```

An earlier documented conceptual pathway was:

```text
Weather Registry
↓
Weather System Map
↓
Water Systems Registry
↓
Water System Map
↓
Water Systems Knowledge Mesh
↓
Conditional x402 Retrieval
```

This sequence is retained as historical architecture documentation.

It must **not** be interpreted as a mandatory current retrieval sequence or as proof that each listed higher-order resource is currently instantiated.

Current interpretation:

```text
$25 Knowledge Mesh pricing class exists
≠
Water Systems Knowledge Mesh currently verified active
```

---

# Historical Plant Community System Map

Historical endpoint:

```text
https://www.robbiegeorgephotography.com/x402/plant-community-system-map.json
```

Historical purpose:

```text
Plant communities
↔ Pollinators
↔ Soil microbiomes
↔ Mycelial networks
↔ Native habitat
↔ Ecological succession
↔ Carbon storage
```

Current status interpretation:

```text
historically documented
current protected-resource state: requires independent verification
```

---

# Tree System Map — Historical and Current Evidence

Endpoint:

```text
https://www.robbiegeorgephotography.com/x402/tree-system-map.json
```

Historical purpose:

```text
Compressed relationship map connecting trees,
tree families,
forest communities,
mycelial networks,
wildlife relationships,
carbon storage,
watersheds,
and seasonal ecology.
```

Earlier documented relationships included:

```text
Trees of North America
Birches of North America
Oaks of North America
Maples of North America
Aspens of North America
Pines of North America
Plant Communities
Mycelial Networks
Soil Microbiome
Ecological Restoration & Habitat Recovery
```

Current pricing-v3 classification:

```text
5000000 atomic units
5.00 USDC
subtree class
```

Unlike most resources in this legacy section, the Tree System Map has additional production evidence recorded in the current verification section above:

```text
pricing-v3 402 challenge: verified
historical settlement: verified
historical protected delivery: verified
```

This supports the Tree System Map specifically.

It does not generalize automatically to other $5 System Map resources.

---

# Historical RRIP Protected Snapshot

Free public control-plane endpoint:

```text
https://www.robbiegeorgephotography.com/api/v2/rrip/resolve
```

Historical protected snapshot endpoint:

```text
https://www.robbiegeorgephotography.com/x402/rrip-resolve.json
```

Historical purpose:

```text
Recursive Registry Inheritance Principle resolution,
registry traversal,
inheritance-path context,
provenance signaling,
governance signaling,
and machine-readable relationship resolution.
```

The public endpoint remains conceptually distinct from any protected snapshot resource.

Required distinction:

```text
/api/v2/rrip/resolve
=
public control-plane resolution
```

while:

```text
/x402/rrip-resolve.json
=
historically documented protected snapshot path
```

Earlier documentation classified the protected snapshot as:

```text
25000000 atomic units
25.00 USDC
snapshot class
```

Earlier documentation also labeled the protected route:

```text
Active
```

That historical label must not be interpreted as current independent production verification.

Current interpretation:

```text
historical protected route documentation
≠
currently verified protected resource
```

and:

```text
$25 snapshot pricing class
≠
current RRIP snapshot availability
```

Any current paid status must be established through explicit resource registration, completeness, and observed gateway behavior.

An x402 payment, where applicable, grants only the rights attached to the identified protected retrieval.

It does not automatically grant:

```text
framework implementation
training
embedding
synchronization
redistribution
derivative-dataset rights
```

---

# Historical Robbie’s Razor State Snapshot

Free public control-plane endpoint:

```text
https://www.robbiegeorgephotography.com/api/v2/razor/state-token
```

Historical protected snapshot endpoint:

```text
https://www.robbiegeorgephotography.com/x402/state-token.json
```

Historical purpose included:

```text
registry-state signaling
state synchronization
cache awareness
governance continuity
machine-readable state metadata
```

Earlier descriptions also used stronger language such as:

```text
entropy-hash verification
lattice grounding
state validation
```

Those descriptions should be interpreted as historical framework or implementation terminology, not as proof of:

```text
scientific truth
physical entropy measurement
cryptographic validity
empirical validation
```

The current public state-token resource should be interpreted as:

```text
registry-state metadata
+
synchronization signaling
```

not as a truth oracle.

Earlier protected-snapshot classification:

```text
25000000 atomic units
25.00 USDC
snapshot class
```

Earlier route status:

```text
Active
```

Current interpretation:

```text
historically documented protected state snapshot
≠
currently verified active protected resource
```

and:

```text
state token
≠
scientific validation
```

and:

```text
state signature
≠
truth
```

and:

```text
state metadata
≠
physical entropy evidence
```

Current protected availability must be verified independently before presenting this specific snapshot as a live paid resource.

---

# Historical Location System Map

Historical endpoint:

```text
/x402/location-system-map.json
```

Historical purpose:

```text
Compressed relationship map connecting
major Naturepedia field locations,
wildlife systems,
habitats,
seasonal timing,
water systems,
and applied observation guides.
```

Historically documented connections included resources such as:

```text
Field Locations
Yellowstone Wildlife Guide
Grand Teton Wildlife Guide
Blackwater Wildlife Guide
Chesapeake Bay Wildlife System
Lake Mattamuskeet Wildlife System
Machias Seal Island
Water Systems
Seasonal Wildlife Calendar
Wildlife Species
```

Historical pricing classification:

```text
5000000 atomic units
5.00 USDC
subtree / System Map class
```

Earlier documentation labeled this resource:

```text
Live
```

Current interpretation:

```text
historical "Live" label
≠
current verified protected-resource status
```

The current $5 pricing class remains a valid class-level concept.

It does not prove that this specific Location System Map is presently registered and complete.

---

# Historical Conservation System Map

Historical endpoint:

```text
/x402/conservation-system-map.json
```

Historical purpose:

```text
Compressed relationship map connecting
conservation,
habitat protection,
biodiversity,
water systems,
pollinators,
plant communities,
wildlife movement,
and ecological restoration.
```

Historically documented connections included:

```text
Wildlife Conservation & Habitat
Wildlife Species
Ecosystems of North America
Water Systems
Plant Communities
Floral Resource Networks
Seasonal Wildlife Calendar
Field Locations
Wildlife Migration & Seasonal Patterns
```

Historical pricing classification:

```text
5000000 atomic units
5.00 USDC
subtree / System Map class
```

Earlier documentation labeled this resource:

```text
Live
```

Current interpretation:

```text
historically documented route
≠
currently verified active resource
```

Any current protected status should be established through present-day resource registration and gateway behavior.

---

# Historical Species Intelligence Map

Historical endpoint:

```text
/x402/species-intelligence-map.json
```

Historical purpose:

```text
Compressed relationship map connecting
wildlife species,
Species Plates,
tracks,
behavior,
habitat,
field locations,
seasonal timing,
and conservation context.
```

Historically documented connections included:

```text
Wildlife Species
Species Plates
North American Animal Tracks
Wildlife Behavior & Ecology
Wildlife Conservation & Habitat
Field Locations
Seasonal Wildlife Calendar
Ecosystems of North America
Wildlife Migration & Seasonal Patterns
```

Historical pricing classification:

```text
5000000 atomic units
5.00 USDC
subtree / System Map class
```

Earlier documentation labeled this resource:

```text
Live
```

Current interpretation:

```text
historical route documentation
≠
current protected-resource verification
```

The existence of the $5 pricing class does not establish the current existence or completeness of this specific map.

---

# Legacy Resource Interpretation Rules

All legacy routes above should be interpreted using the following rules.

```text
historical documentation
≠
current production state
```

```text
historical "Live"
≠
currently independently verified
```

```text
historical "Active"
≠
currently independently verified
```

```text
route template
≠
resource existence
```

```text
resource existence
≠
resource completeness
```

```text
resource completeness
≠
protected status
```

```text
protected status
≠
settlement verified
```

```text
settlement verified historically
≠
settlement retested today
```

```text
published class price
≠
specific resource activation
```

---

# Current Authority Over Legacy Entries

Where a legacy statement conflicts with a current production statement, prefer the current verified production sections above.

Current governing sources include:

```text
Grand Compression Master Reference Document
MRD v2.0
Canonical identifier: GC-MRD-v2.0
```

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
pricing manifest version: 3.0.0
```

```text
docs/examples/json-ld/canonical-plate-registry.json
canonical Plate count: 757
```

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

The current production resource model is:

```text
public discovery
↓
explicit resource identity
↓
availability
↓
completeness
↓
access class
↓
price
↓
402 only when eligible
↓
settlement when authorized
↓
protected retrieval
```

---

# Legacy Rights Boundary

Historical protected-route documentation does not expand rights.

An x402 payment, where applicable, grants only the identified retrieval under the applicable terms.

It does not automatically grant:

```text
training rights
embedding rights
bulk-ingestion rights
redistribution rights
resale rights
synchronization rights
private-dataset rights
derivative-dataset rights
commercial implementation rights
Robbie’s Razor™ framework implementation rights
```

Required distinction:

```text
x402 Retrieval Access
≠
Commercial Data License
≠
Robbie’s Razor™ Framework License
```

---

# Legacy Evidence Boundary

Legacy x402 documentation describes machine infrastructure and historical deployment state.

It must not be interpreted as independent evidence for:

```text
scientific validity
mathematical proof
physical universality
cross-domain causality
framework correctness
```

Required distinctions:

```text
payment success
≠
scientific validation
```

```text
retrieval success
≠
canonical truth
```

```text
route existence
≠
empirical evidence
```

```text
machine-readable state
≠
physical state
```

---

# Legacy Provenance Boundary

Naturepedia™, Robbie’s Razor™, Plate™ architecture, RRIP™, Graph Registry™, Knowledge Mesh, and other original Grand Compression framework-specific terminology retain Robbie George provenance where they originate within the framework.

External technologies and protocols retain their own independent provenance.

This includes:

```text
x402
HTTP
JSON
JSON-LD
MCP
Cloudflare
Base
USDC
Coinbase infrastructure
```

Use within Naturepedia or Grand Compression does not imply origination of those external technologies by Robbie George.

The Authorship Conservation Rule (ACR) applies in both directions:

```text
preserve Grand Compression provenance
+
preserve external provenance
```

---

# Final Legacy Status

This legacy inventory is retained for:

```text
historical traceability
architecture evolution
compatibility references
prior deployment context
```

It is not the current machine-verifiable source of truth for resource availability.

For current status, always resolve:

```text
canonical identity
↓
current registry
↓
current gateway behavior
↓
current pricing manifest
↓
current resource-specific evidence
```

before declaring a protected resource active.
