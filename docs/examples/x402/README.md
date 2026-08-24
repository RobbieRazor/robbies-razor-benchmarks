# x402 Production Architecture
## Naturepedia™ Governed Machine Retrieval

## Document Status

**Status:** Production architecture documentation  
**Current governing authority:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Infrastructure:** Robbie George Photography / Naturepedia™  
**Settlement protocol:** x402-compatible retrieval  
**Network:** Base — `eip155:8453`  
**Asset:** USDC  
**Pricing manifest:** v3.0.0  
**Evidence boundary:** Implementation and payment state are distinct from empirical validation

This folder documents the machine-facing discovery, retrieval, availability, pricing, and x402 settlement architecture used by Robbie George Photography and Naturepedia™.

The architecture separates:

```text
canonical authority
public discovery
resource availability
pricing
payment challenge
settlement
payload retrieval
usage rights
```

These states must not be collapsed into one another.

---

# Canonical Authority

Grand Compression Master Reference Document:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Repository authority:

```text
docs/AUTHORITY.md
```

Repository specification:

```text
docs/canonical-spec.md
```

Current governing framework:

```text
MRD v2.0
GC-MRD-v2.0
RC-01 through RC-22
```

Canonical authority is not created by x402 payment, endpoint availability, settlement, or machine retrieval.

---

# Production Architecture

The production system contains several distinct planes.

```text
Authority Plane
↓
Discovery / Control Plane
↓
Resource Resolution
↓
Availability Gate
↓
Pricing Resolution
↓
x402 Challenge
↓
Payment Verification / Settlement
↓
Protected Retrieval
```

Additional machine-facing functions may include:

```text
registry discovery
RRIP resolution
registry-state signaling
cache coordination
provenance
governance metadata
```

---

# Public Discovery and Control Plane

Current public machine-facing v2 endpoints include:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These endpoints are public control-plane or discovery resources.

They are not themselves proof that every referenced higher-order resource exists as a paid retrieval object.

Required distinction:

```text
discovery record
≠
protected resource registration
```

---

# `/api/v2/naturepedia/index.md`

Role:

```text
Naturepedia machine discovery
routing orientation
resource-family awareness
machine-facing entry point
```

It may identify available or governed resource classes.

It does not automatically create protected payloads.

---

# `/api/v2/plates/registry.md`

Role:

```text
Plate™ discovery
registry navigation
resource routing
machine-readable registry orientation
```

A registry entry may identify a resource.

Registry presence alone does not establish:

- payload completeness;
- paid-resource availability;
- empirical validation;
- licensing rights.

---

# `/api/v2/rrip/resolve`

Role:

```text
RRIP-oriented relationship resolution
inheritance-path lookup
contextual relationship grounding
```

Canonical framework relationship:

```text
MRD §12.8
→ Recursive Registry Inheritance Principle (RRIP™)
```

The endpoint is an implementation of a resolution function.

Required distinction:

```text
RRIP endpoint works
≠
RRIP universally validated
```

---

# `/api/v2/razor/state-token`

Role:

```text
registry-state signaling
version awareness
state comparison
cache coordination
synchronization metadata
```

The state token may help a client determine whether previously retrieved state should be refreshed.

It does **not** independently verify:

```text
truth
empirical validity
entropy
scientific correctness
```

Required distinction:

```text
state-token match
≠
content validation
```

and:

```text
registry state
≠
evidence state
```

---

# State-Aware Retrieval Pattern

A machine client may use:

```text
State Check
↓
Discovery
↓
Resource Resolution
↓
Availability Check
↓
Free Retrieval or Protected Retrieval
```

Possible cache-aware behavior:

```text
state unchanged
→ cached resource may remain usable subject to its own validity rules

state changed
→ refresh or revalidation may be appropriate
```

This is an architectural pattern.

A matching state token does not guarantee that externally changing facts remain current.

---

# v1 Protected Retrieval Architecture

The production Worker supports governed v1 retrieval classes.

Representative route families include:

```text
/v1/query/atomic/*
/v1/query/enriched/*
/v1/taxonomy/*
/v1/plates/*
/v1/sovereign/*
/v1/knowledge-mesh/*
```

Legacy `/x402/*` paths may remain available for compatibility where explicitly implemented.

A route family or route template must not be interpreted as proof that every syntactically valid resource identifier is sellable.

---

# Resource Existence Rule

The production gateway separates:

```text
route exists
```

from:

```text
resource exists
```

and:

```text
resource is complete
```

and:

```text
resource is payment-eligible
```

This is a core production rule.

---

# Fail-Closed Availability Model

Protected retrieval uses an availability gate before payment challenge issuance.

```text
Request
↓
Canonical normalization
↓
Resource-class resolution
↓
Explicit availability lookup
↓
Availability state
```

## Unknown Resource

```text
HTTP 404 Not Found
payment challenge: no
```

Meaning:

```text
the requested resource is not registered as available
```

---

## Known but Incomplete Resource

```text
HTTP 409 Conflict
payment challenge: no
```

Meaning:

```text
the resource is recognized
but its governed payload is not ready for protected sale
```

---

## Registered and Complete Resource

```text
eligible for x402 challenge
```

When protected access applies:

```text
HTTP 402 Payment Required
```

This prevents a syntactically valid route from charging for an unavailable resource.

---

# Pricing Authority

The authoritative production pricing manifest is:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Current manifest version:

```text
3.0.0
```

Payment protocol:

```text
x402
```

Network:

```text
eip155:8453
```

Asset:

```text
USDC
```

Decimals:

```text
6
```

Production pricing uses fixed atomic-unit amounts.

---

# Current Pricing Classes

| Access class | Price | USDC atomic units | Availability interpretation |
|---|---:|---:|---|
| Discovery / previews | Free | `0` | Public where exposed |
| Atomic canonical query | `$0.005` | `5000` | Active only for explicitly registered deterministic payloads |
| Enriched query | `$0.025` | `25000` | Active for the explicitly registered Biography Enriched Query |
| Structured Plate™ payload | `$0.25` | `250000` | Active only for registered and validated Plate payloads |
| Bounded subtree / Registry / System Map class | `$5.00` | `5000000` | Pricing class available; actual resource availability is registration-specific |
| Full Registry / Knowledge Mesh snapshot class | `$25.00` | `25000000` | Pricing class available; actual resource availability is registration-specific |

Important:

```text
price class exists
≠
every possible resource in that class exists
```

The `$5` and `$25` rows describe governed pricing classes.

They must not be interpreted as blanket registration of every:

- subtree;
- Registry;
- System Map;
- full Registry;
- Knowledge Mesh.

---

# Pricing Resolution

Pricing is determined by the resolved governed resource class rather than URL text alone.

Conceptually:

```text
request path
↓
canonical resource
↓
resource availability
↓
access class
↓
fixed price
```

Do not infer pricing solely from a substring in a URL.

---

# Atomic Canonical Query

Public template:

```text
/v1/query/atomic/{resource}
```

Current verified Atomic resource:

```text
/v1/query/atomic/robbie-george-biography-plate
```

Canonical internal compatibility path:

```text
/x402/query/atomic/robbie-george-biography-plate
```

Canonical Plate identifier:

```text
robbie-george#robbie-george-biography-plate
```

Human authority:

https://www.robbiegeorgephotography.com/who-is-robbie-george

Configuration:

```text
Access class: atomic
Price: 0.005 USDC
Atomic units: 5000
Network: eip155:8453
Asset: USDC
Resource class: atomic-query
Schema: naturepedia.atomic-query.v1
```

Verified challenge behavior:

```text
STATUS: 402
AMOUNT: 5000
TIER: atomic
PAYMENT REQUIRED: true
```

This verifies the payment challenge for that registered resource.

It does not mean every Atomic route has been individually settlement-tested.

---

# Enriched Query

Public template:

```text
/v1/query/enriched/{resource}
```

Pricing configuration:

```text
Access class: enriched
Price: 0.025 USDC
Atomic units: 25000
```

Current state:

```text
ACTIVE FOR THE REGISTERED BIOGRAPHY ENRICHED QUERY
```

Enriched resources must not issue payment challenges merely because the route class exists. Only an explicitly registered, governed, deterministic payload is payment-eligible.

Activation requires an explicitly governed resource with:

- deterministic payload;
- registration;
- availability gate;
- fidelity boundary;
- production validation.

---

# Structured Plate™ Retrieval

Current verified Structured Plate™ challenge routes include:

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

Observed challenge behavior:

```text
STATUS: 402
AMOUNT: 250000
TIER: single-plate
PAYMENT REQUIRED: true
```

for the verified registered resources.

Unknown identifiers remain subject to:

```text
404
```

Known but incomplete identifiers remain subject to:

```text
409
```

before any payment challenge.

---

# Bounded Multi-Record Resources

The pricing manifest provides a governed `$5.00` class for bounded multi-record resources such as a qualifying:

- taxonomy subtree;
- Registry;
- System Map.

This is a pricing class.

A particular resource is paid and available only when its production record indicates:

```text
known
+
complete
+
registered
+
payment-eligible
```

Do not infer a resource from taxonomy or architecture terminology.

---

# Full Registry and Knowledge Mesh Class

The pricing manifest provides a `$25.00` class for qualifying large machine-readable resources such as:

- full Registry snapshots;
- Knowledge Mesh snapshots.

Again:

```text
pricing class
≠
resource existence
```

The resource must be explicitly registered and production-ready.

---

# Structured Resource Hierarchy Boundary

Grand Compression / RKCA may describe resource types such as:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

This is an architectural relationship.

It does not mean every Plate currently has:

```text
Registry
Meta-Registry
Graph Registry
Knowledge Mesh
```

counterparts.

Required distinction:

```text
architectural layer defined
≠
production resource instantiated
```

---

# Hopf Fibration Boundary

Hopf Fibration is publicly discoverable as an established mathematical reference.

Current production interpretation:

```text
requiresPayment: false
```

Do not infer paid resources such as:

```text
/v1/registries/hopf-fibration
/v1/plates/hopf-fibration-map
/v1/knowledge-mesh/hopf-fibration
/x402/hopf...
```

unless a later governed production record explicitly creates them.

---

# Human and Machine Access

Human browser requests may receive ordinary public informational responses.

Machine-oriented requests to registered protected resources may receive:

```text
HTTP 402 Payment Required
```

depending on:

- route;
- requested representation;
- availability state;
- access class.

A header such as:

```text
Accept: application/json
```

may participate in machine-response routing.

It does not by itself create a paid resource.

---

# Settlement Boundary

The production environment has verified x402 settlement infrastructure on:

```text
Base
eip155:8453
USDC
```

The system has recorded at least one successful live settlement.

Historical verified transaction:

```text
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376
```

This establishes that live settlement has occurred.

It does **not** establish that every currently documented protected endpoint has completed an independent end-to-end settlement test.

Required distinction:

```text
settlement infrastructure verified
≠
every route settlement-tested
```

---

# Challenge vs Settlement vs Delivery

Keep these states separate.

```text
402 challenge verified
```

means:

```text
the gateway issued the expected payment requirement
```

```text
settlement verified
```

means:

```text
a valid payment was successfully processed under the tested conditions
```

```text
payload delivery verified
```

means:

```text
protected content was delivered after the applicable verification flow
```

One state must not automatically be used as evidence for another route.

---

# MCP Compatibility

The machine-retrieval architecture can complement the Naturepedia MCP server.

MCP may support:

- discovery;
- canonical resolution;
- tool invocation;
- structured resource access.

x402 may govern protected retrieval where applicable.

Required distinction:

```text
MCP
≠
x402
```

and:

```text
MCP resource discoverable
≠
paid resource
```

and:

```text
MCP tool available
≠
wallet settlement required
```

The two systems may interoperate without being the same protocol layer.

---

# Agent Retrieval Pattern

A governed agent flow may be:

```text
Discover
↓
Resolve canonical resource
↓
Check resource state
↓
Check availability
↓
Determine access class
↓
Free retrieval OR 402 challenge
↓
Payment verification if required
↓
Protected retrieval
↓
Validate returned identity / provenance / version
```

The exact ordering may vary by client.

---

# State Validation Boundary

A state token can help detect changes to registry state.

It does not prove that the content represented by the registry is:

- scientifically correct;
- complete;
- externally current;
- independently validated.

Required distinction:

```text
state consistency
≠
truth
```

---

# Fidelity Validation

A retrieved payload should preserve its governed:

- identifier;
- canonical source;
- resource class;
- version;
- provenance;
- constraints;
- evidence status where applicable.

Successful payload delivery alone does not establish that every encoded statement is empirically correct.

---

# Retrieval Rights Boundary

One successful x402 payment authorizes the identified endpoint retrieval under the applicable access conditions.

It does **not** grant:

- training rights;
- embedding rights;
- bulk ingestion rights;
- redistribution rights;
- resale rights;
- synchronization rights;
- private-dataset construction rights;
- derivative-dataset rights;
- commercial implementation rights;
- Robbie’s Razor™ framework implementation rights.

Public discovery likewise does not grant those rights.

---

# Commercial Data Rights

Commercial data reuse is governed separately.

Commercial licensing:

https://www.robbiegeorgephotography.com/commercial-data-license

A retrieval payment and a commercial data license are different grants.

Required distinction:

```text
x402 retrieval
≠
commercial data rights
```

---

# Framework Rights

Framework licensing is governed separately.

Framework licensing:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

Required distinction:

```text
x402 retrieval
≠
Robbie’s Razor implementation license
```

---

# Three-Layer Rights Model

The system should preserve:

```text
Public discovery
↓
Protected retrieval
↓
Separate commercial / framework rights where applicable
```

These layers are complementary.

They are not interchangeable.

---

# Payment Is Not Evidence

x402 state must remain separate from framework evidence status.

Required distinctions:

```text
payment
≠
scientific support
```

```text
settlement
≠
canonical authority
```

```text
payload delivery
≠
empirical validation
```

```text
registry inclusion
≠
truth
```

---

# Canonical vs Machine Infrastructure

The governing sequence is:

```text
Canonical human authority
↓
Machine-readable representation
↓
Discovery
↓
Optional protected retrieval
```

Machine infrastructure serves the canonical material.

It does not replace the canonical human authority.

---

# Resource Registration Rule

Before adding a new paid resource, verify:

```text
canonical identity
resource class
payload
provenance
version
availability state
price class
rights boundary
failure behavior
```

Then validate:

```text
unknown → 404
known incomplete → 409
registered complete → eligible 402
```

This rule should remain fail-closed.

---

# New Resource Activation Checklist

A new protected resource SHOULD have:

```text
[ ] canonical identifier
[ ] canonical authority URL
[ ] explicit resource record
[ ] deterministic or governed payload
[ ] resource-class assignment
[ ] fixed pricing assignment
[ ] availability state
[ ] 404 test
[ ] 409 test where applicable
[ ] 402 challenge test
[ ] payload fidelity test
[ ] rights notice
[ ] provenance
[ ] version
```

Payment testing may be recorded separately from challenge testing.

---

# Pricing Change Rule

The authoritative source for current retrieval pricing is:

```text
/.well-known/x402-pricing.json
```

Repository examples should defer to that manifest when a conflict arises.

Do not create a second independent price authority inside documentation.

---

# Fixed-Price Rule

Current production pricing uses:

```text
fixedPriceResponses: true
priceRangesAllowedIn402Responses: false
```

A production `402` response should use the fixed price assigned to the resolved access class.

---

# Current Production Summary

```text
Network:
Base / eip155:8453

Asset:
USDC

Pricing manifest:
v3.0.0

Discovery:
Free where exposed

Atomic:
0.005 USDC
5000 units
active only for registered deterministic payloads

Enriched:
0.025 USDC
25000 units
active for the registered Biography Enriched Query

Structured Plate:
0.25 USDC
250000 units
active only for registered validated resources

Bounded multi-record class:
5.00 USDC
5000000 units
resource-specific availability

Large snapshot class:
25.00 USDC
25000000 units
resource-specific availability

Availability:
unknown → 404
known incomplete → 409
registered complete protected resource → eligible 402

Settlement:
live infrastructure verified

Rights:
retrieval only unless separately licensed
```

---

# Evidence and Governance Boundary

Production architecture demonstrates:

- implemented routing;
- resource availability gating;
- deterministic pricing;
- payment challenge behavior;
- live settlement capability;
- machine-readable delivery.

It does not independently demonstrate:

- scientific validation;
- universal Grand Compression validity;
- economic superiority;
- external adoption;
- market demand;
- framework correctness.

Canonical orientation:

```text
RC-21 — Reference Implementation Distinction
```

---

# Final Interpretation Rules

This documentation must preserve:

```text
route template
≠
resource existence
```

```text
pricing class
≠
resource availability
```

```text
discovery
≠
payment requirement
```

```text
state token
≠
truth verification
```

```text
state validation
≠
evidence validation
```

```text
402 challenge
≠
settlement
```

```text
settlement
≠
payload delivery on every route
```

```text
payment
≠
commercial rights
```

```text
payment
≠
framework rights
```

```text
payment
≠
empirical evidence
```

```text
architectural resource class
≠
instantiated production resource
```

---

# Related Files

```text
docs/examples/x402/live-endpoints.md
docs/examples/x402/worker-architecture.md
docs/examples/x402/mcp-compatibility.md
docs/examples/x402/pricing-map-example.json
docs/examples/x402/sample-worker.ts
docs/examples/x402/test-results.md
```

These files may provide implementation examples or historical test records.

Where a repository example conflicts with live production pricing or governed availability, the current production manifest and production resource registry govern.

---

# Attribution

Naturepedia™, Robbie’s Razor™, Plate™ Architecture, Recursive Registry Inheritance Principle (RRIP™), Graph Registry™, Knowledge Mesh terminology, and associated original Grand Compression infrastructure concepts originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

These materials are governed by the **Authorship Conservation Rule (ACR)**.

x402, Base, USDC, MCP, Cloudflare, HTTP, JSON, JSON-LD, and other external protocols, technologies, standards, and platforms retain their independent provenance and ownership.
