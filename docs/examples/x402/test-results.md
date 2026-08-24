# x402 Test Results
## Production Verification Record and Evidence Boundaries

## Document Status

**Status:** Production test and historical verification record  
**Worker:** `cold-bird-7036`  
**Primary domain:** `https://www.robbiegeorgephotography.com`  
**Current pricing manifest:** v3.0.0  
**Current governing authority:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Network:** Base — `eip155:8453`  
**Asset:** USDC

This document records observed production behavior from several x402 validation rounds.

It intentionally separates:

```text
historical observation
current challenge verification
settlement verification
payload-delivery verification
resource availability
pricing-class definition
```

These states must not be collapsed into one another.

---

# 1. Evidence Hierarchy

This record contains observations from different dates and scopes.

The governing interpretation is:

```text
test performed on resource A
≠
same test performed on every resource in its class
```

and:

```text
pricing class configured
≠
all possible resources in that class active
```

Historical results remain preserved as provenance.

Current production status should be inferred only from explicitly documented tests and current production resource registration.

---

# 2. Important Dates

Historical x402 verification:

```text
2026-06-11
```

Pricing Manifest v3 production deployment:

```text
2026-08-17
```

Pricing-v3 challenge validation:

```text
2026-08-18
```

Atomic Query activation and synchronized production validation:

```text
2026-08-20
```

These are separate validation rounds.

---

# 3. Authoritative Pricing Source

Current production pricing authority:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current manifest version:

```text
3.0.0
```

Repository test documentation does not create a second pricing authority.

---

# 4. Worker

Production Worker:

```text
cold-bird-7036
```

---

# 5. Historical Human-Browser Test
## 2026-06-11

Test URL:

```text
https://www.robbiegeorgephotography.com/v1/plates/tree-system-map
```

Observed browser-facing result:

```text
200 OK

Naturepedia x402 Gateway

Human visitors bypass payment gating.

Protected Resource:
Naturepedia Tree System Map
```

This establishes the historical human-browser bypass behavior for the tested resource.

It does not establish browser behavior for every possible route.

---

# 6. Historical API / Agent Challenge
## 2026-06-11

Historical request:

```javascript
fetch(
  "https://www.robbiegeorgephotography.com/v1/plates/tree-system-map",
  {
    headers: {
      Accept: "application/json"
    }
  }
);
```

Historical observed result:

```text
402 Payment Required

X-402-Provider: Base-USDC
X-402-Amount: 5.00
X-402-Gateway-Tier: plates
```

These header names and gateway classifications belong to the earlier production architecture.

They should not be rewritten to look like pricing-v3 observations.

---

# 7. Historical Settlement and Protected Delivery

The June 2026 production verification included:

```text
live x402 challenge
Base USDC settlement
protected payload delivery
```

That historical test demonstrates that end-to-end settlement and protected payload delivery have occurred in production.

Required distinction:

```text
historical settlement capability verified
≠
every later route settlement-tested
```

---

# 8. Historical Pricing Architecture

The June 11 production test used the earlier pricing structure:

```text
taxonomy  = $1.00
plates    = $5.00
sovereign = $25.00
legacy    = $5.00
```

These values are preserved solely as historical provenance.

They are not the current pricing authority.

---

# 9. Pricing v3 Tree System Map Challenge
## 2026-08-18

A new unpaid production request was made to:

```text
https://www.robbiegeorgephotography.com/v1/plates/tree-system-map
```

using an API-oriented request.

Observed result:

```text
402 Payment Required

Payment-Required: present
X-402-Provider: Base-USDC
X-402-Amount: 5000000
X-402-Gateway-Tier: subtree
X-Robbie-Pricing-Version: 3.0.0
X-Robbie-Pricing-Manifest:
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Cache-Control: no-store
```

Interpretation:

```text
5000000 atomic units
=
5.00 USDC
```

This verifies that the specific Tree System Map resource was challenge-active under the `$5.00` subtree class at the time of the test.

Required distinction:

```text
Tree System Map challenge verified
≠
every possible $5 resource active
```

---

# 10. Pricing v3 Geology Knowledge Mesh Challenge
## 2026-08-18

Tested protected resource:

```text
https://www.robbiegeorgephotography.com/v1/knowledge-mesh/geology
```

Observed result:

```text
402 Payment Required

Payment-Required: present
X-402-Provider: Base-USDC
X-402-Amount: 25000000
X-402-Gateway-Tier: snapshot
X-Robbie-Pricing-Version: 3.0.0
X-Robbie-Pricing-Manifest:
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Cache-Control: no-store
```

Interpretation:

```text
25000000 atomic units
=
25.00 USDC
```

This verifies that the specific Geology Knowledge Mesh resource was challenge-active under the `$25.00` snapshot class at the time of the test.

Required distinction:

```text
Geology Knowledge Mesh challenge verified
≠
every Knowledge Mesh or snapshot active
```

---

# 11. August 18 Settlement Boundary

For the pricing-v3 Tree System Map and Geology Knowledge Mesh observations:

```text
payment authorized: no
settlement attempted: no
protected post-settlement delivery tested: no
```

Therefore those tests establish:

```text
challenge behavior
```

not:

```text
new pricing-v3 settlement behavior
```

---

# 12. Current Pricing Classes

Current pricing authority:

```text
/.well-known/x402-pricing.json
```

| Access class | Price | Atomic units | Current interpretation |
|---|---:|---:|---|
| Discovery / previews | Free | `0` | Public where exposed |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active only for explicitly registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Biography Enriched Query challenge verified; other resources require explicit registration |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active only for registered and validated payloads |
| Bounded subtree / Registry / System Map class | `$5.00 USDC` | `5000000` | Pricing class defined; specific resources require explicit availability |
| Full Registry / Knowledge Mesh snapshot class | `$25.00 USDC` | `25000000` | Pricing class defined; specific resources require explicit availability |

Known test evidence includes:

```text
Tree System Map
→ $5 challenge verified

Geology Knowledge Mesh
→ $25 challenge verified
```

Those observations establish specific active resources, not blanket activation of every resource in those classes.

---

# 13. Availability Model

Current production retrieval follows a fail-closed resource-state model.

```text
Request
↓
Canonical resource resolution
↓
Explicit availability check
```

### Unknown

```text
404
no payment challenge
```

### Known but incomplete

```text
409
no payment challenge
```

### Registered + complete + protected

```text
eligible for 402
```

Required distinction:

```text
route pattern
≠
payable product
```

---

# 14. Atomic Query Activation
## 2026-08-20

Current verified Atomic resource:

```text
/v1/query/atomic/robbie-george-biography-plate
```

Canonical internal route:

```text
/x402/query/atomic/robbie-george-biography-plate
```

Canonical Plate identifier:

```text
robbie-george#robbie-george-biography-plate
```

Canonical authority:

```text
https://www.robbiegeorgephotography.com/who-is-robbie-george
```

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

---

# 15. Atomic Available-Resource Challenge

Observed result:

```text
STATUS: 402
AMOUNT: 5000
TIER: atomic
PAYMENT REQUIRED HEADER: true
PAYMENT REQUIRED: true
ERROR: Payment Required
```

Result:

```text
PASS
```

This verifies the challenge behavior of the registered Atomic Biography resource.

During this validation:

```text
payment supplied: no
settlement attempted: no
protected Atomic payload delivery tested: no
```

---

# 16. Atomic Known-Incomplete Test

Test route:

```text
/v1/query/atomic/robbies-razor-plate
```

Observed result:

```text
STATUS: 409
AMOUNT: null
TIER: null
PAYMENT REQUIRED HEADER: false
PAYMENT REQUIRED: false
CODE: ATOMIC_PAYLOAD_NOT_REGISTERED
ROUTE STATUS: reserved
```

Result:

```text
PASS
```

Interpretation:

```text
known canonical resource
+
incomplete/unregistered protected payload
→ no payment challenge
```

---

# 17. Atomic Unknown-Resource Test

Test route:

```text
/v1/query/atomic/definitely-not-a-real-atomic-resource-20260820
```

Observed result:

```text
STATUS: 404
AMOUNT: null
TIER: null
PAYMENT REQUIRED HEADER: false
PAYMENT REQUIRED: false
CODE: ATOMIC_RESOURCE_NOT_FOUND
ERROR: Atomic Query resource not found
```

Result:

```text
PASS
```

---

# 18. Atomic Safety Matrix

Verified behavior:

```text
Registered + complete Atomic resource
→ 402
→ 5000
→ atomic
```

```text
Known + incomplete Atomic resource
→ 409
→ no payment
```

```text
Unknown Atomic resource
→ 404
→ no payment
```

Overall result:

```text
PASS
```

This is one of the strongest current production safety validations in the x402 architecture.

---

# 19. Historical Enriched Query State
## 2026-08-20

Current price class:

```text
0.025 USDC
25000 atomic units
```

State observed during the August 20 validation:

```text
RESERVED
```

At that time, the Enriched Query class could not be treated as active merely because:

- a route template exists;
- a pricing variable exists;
- the price appears in the manifest.

Required distinction:

```text
Enriched price published
≠
Enriched payload active
```

---

# 20. Atomic Discovery-Surface Synchronization
## 2026-08-20

The August 20 validation reported:

```text
PASS — Pricing manifest HTTP 200
PASS — Atomic pricing active
PASS — Atomic active route registered
PASS — Enriched remains reserved

PASS — AI Catalog HTTP 200
PASS — Atomic resource represented

PASS — OpenAPI HTTP 200
PASS — Atomic OpenAPI route present
PASS — Atomic price correct

PASS — Canonical Publication Manifest HTTP 200
PASS — CPM Atomic active
PASS — CPM Enriched reserved

PASS — AI Root HTTP 200
PASS — AI Root Atomic active
PASS — AI Root Enriched reserved

PASS — MCP server-card HTTP 200
PASS — MCP Atomic metadata active
PASS — MCP Enriched metadata reserved

PASS — Atomic live challenge
```

Overall result:

```text
PASS
```

This establishes metadata and challenge synchronization for the tested Atomic resource.

It does not independently establish settlement or protected delivery for Atomic Query.

---

# 21. MCP Metadata Boundary

The synchronization test included MCP server-card metadata.

That means relevant Atomic and Enriched status information was present in the tested MCP metadata surface.

It does not imply that an HTTP Atomic route is itself an MCP-native tool.

Required distinction:

```text
MCP metadata synchronized
≠
HTTP route becomes MCP tool
```

---

# 22. Structured Plate Regression
## 2026-08-20

Tested routes:

```text
/v1/plates/item/commercial-data-license-plate
/v1/plates/item/commercial-intelligence-pricing-plate
/v1/plates/item/robbie-george-biography-plate
```

Observed result for each:

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

This verifies the `$0.25` challenge behavior for those three explicitly registered Plates.

---

# 23. Structured Plate Settlement Boundary

During that regression round:

```text
new $0.25 settlement performed: no
protected post-settlement Plate delivery retested: no
```

Therefore:

```text
Structured Plate challenge verified
≠
new Structured Plate settlement verified
```

---

# 24. Structured Plate Availability

Current expected safety behavior:

```text
unknown Plate
→ 404
→ no payment challenge
```

```text
known but incomplete Plate
→ 409
→ no payment challenge
```

```text
registered + complete protected Plate
→ eligible 402
```

---

# 25. Specific `$5` Evidence

Current repository evidence supports at least the following specific `$5` protected challenge:

```text
/v1/plates/tree-system-map
→ 402
→ 5000000 atomic units
→ subtree
```

That resource may therefore be described as challenge-verified under the `$5` class as of the recorded test.

Do not generalize this observation to every:

- taxonomy subtree;
- Registry;
- System Map.

---

# 26. Specific `$25` Evidence

Current repository evidence supports at least the following specific `$25` protected challenge:

```text
/v1/knowledge-mesh/geology
→ 402
→ 25000000 atomic units
→ snapshot
```

That resource may therefore be described as challenge-verified under the `$25` class as of the recorded test.

Do not generalize this observation to every:

- full Registry;
- Knowledge Mesh;
- RRIP-related asset;
- state-related asset;
- premium snapshot.

---

# 27. Public v2 Control Plane

Core public endpoints:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

Recorded behavior:

```text
200 OK
Worker-served
machine-readable
governance metadata present
```

These are public control-plane resources.

They must not be conflated with `$5` or `$25` protected products.

---

# 28. State-Token Boundary

The state-token endpoint may communicate:

- registry version;
- registry hash;
- synchronization metadata;
- state signatures.

It does not establish:

```text
scientific truth
empirical validation
physical entropy
```

A successful state-token response verifies only its documented state-comparison function.

---

# 29. Historical Endpoint Counts

Historical legacy endpoint count:

```text
14
```

Historical v2 endpoint inventory observation:

```text
8
```

These counts are preserved as historical observations.

They are not current total-route claims.

Required distinction:

```text
historical count
≠
current inventory
```

---

# 30. Current Route Families

Current machine-facing families may include:

```text
/v1/query/atomic/*
/v1/query/enriched/*
/v1/taxonomy/*
/v1/plates/*
/v1/registries/*
/v1/knowledge-mesh/*
/v1/sovereign/*
```

and:

```text
/api/v2/naturepedia/*
/api/v2/plates/*
/api/v2/rrip/*
/api/v2/razor/*
```

A namespace does not establish that every possible path inside it exists.

---

# 31. Resource-Class Resolution

The current gateway should resolve:

```text
resource identity
before
payment eligibility
```

and:

```text
resource class
before
price
```

Avoid:

```text
URL prefix
→ price
→ assume resource exists
```

---

# 32. Challenge / Settlement / Delivery Matrix

The following states must remain distinct.

| Test | Challenge verified | Settlement verified | Protected delivery verified |
|---|---|---|---|
| Historical June 11 route | Yes | Yes | Yes |
| Tree System Map pricing-v3 observation | Yes | No new settlement | No new delivery test |
| Geology Knowledge Mesh pricing-v3 observation | Yes | No new settlement | No new delivery test |
| Atomic Biography activation | Yes | No | No |
| Structured Plate Aug. 20 regression | Yes | No new settlement | No new delivery test |

This table prevents historical end-to-end success from being projected onto every newer route.

---

# 33. Historical Settlement Transaction

Historical live settlement:

```text
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376
```

This demonstrates production settlement capability.

It should not be cited as the settlement transaction for later Atomic, Enriched, Plate, Tree Map, or Knowledge Mesh tests unless the underlying transaction actually corresponds to them.

---

# 34. Current Production Evidence Summary

Supported production statements include:

```text
Cloudflare Worker is live.
```

```text
Human browser bypass has been observed.
```

```text
Machine/API payment challenges have been observed.
```

```text
Base USDC settlement has historically completed successfully.
```

```text
Protected payload delivery has historically completed successfully.
```

```text
Atomic Biography challenge:
402 / 5000 / atomic — verified.
```

```text
Atomic known-incomplete boundary:
409 / no payment — verified.
```

```text
Atomic unknown boundary:
404 / no payment — verified.
```

```text
Three Structured Plate challenges:
402 / 250000 / single-plate — verified.
```

```text
Tree System Map:
402 / 5000000 / subtree — verified.
```

```text
Geology Knowledge Mesh:
402 / 25000000 / snapshot — verified.
```

```text
Enriched Biography Query:
402 / 25000 / enriched — verified on 2026-08-24.
```

---

# 35. Statements Not Supported by This Record

Do not infer:

```text
all $5 resources are active
```

```text
all $25 resources are active
```

```text
all Knowledge Meshes have been tested
```

```text
all registries have been tested
```

```text
all protected routes have settled
```

```text
all protected routes have delivered payloads after settlement
```

```text
Enriched Query is active
```

```text
public RRIP resolver is a $25 product
```

```text
public state-token endpoint is a $25 product
```

---

# 36. Pricing-Class Interpretation

The safest interpretation is:

```text
Atomic class
→ active with explicitly registered resources
```

```text
Enriched class
→ active for the explicitly registered Biography Enriched Query
```

```text
Structured Plate class
→ active with explicitly registered resources
```

```text
$5 class
→ pricing class defined
→ at least one specific tested resource challenge verified
→ other resources remain resource-specific
```

```text
$25 class
→ pricing class defined
→ at least one specific tested resource challenge verified
→ other resources remain resource-specific
```

---

# 37. Retrieval Rights

An x402 payment grants:

```text
one endpoint-level retrieval
```

of the identified protected resource under applicable access terms.

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

# 38. Payment Is Not Licensing

Required distinction:

```text
x402 payment
≠
Commercial Data License
```

Commercial licensing:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Framework licensing:

```text
https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing
```

---

# 39. Payment Is Not Evidence

Required distinctions:

```text
402
≠
empirical validation
```

```text
settlement
≠
scientific confirmation
```

```text
payload delivery
≠
factual truth
```

```text
canonical status
≠
independent empirical support
```

Canonical orientation:

```text
RC-21 — Reference Implementation Distinction
```

---

# 40. Governance Header

Observed / production governance metadata may include:

```http
X-Robbie-Razor-Governance: Gr <= Es
```

The presence of this header indicates framework-governance metadata.

It does not demonstrate that the receiving or delivering system has empirically satisfied a universal physical law.

---

# 41. Cloudflare Log Signals

Historical observed log messages included:

```text
x402 route triggered
x402 detection result
x402 human/search bypass
x402 returning payment challenge
```

These logs support gateway-path observations.

They do not independently establish settlement.

---

# 42. Analytics Boundary

Configured telemetry may include:

```text
Cloudflare Analytics Engine
privacy-preserving analytics salt
```

Telemetry configuration does not by itself establish:

- payer count;
- transaction completion;
- commercial adoption.

Those require their own data.

---

# 43. Current Machine-Facing Flow

The production architecture is best described as:

```text
Canonical Authority
↓
Public Discovery
↓
Registry / Resolution
↓
State Signaling
↓
Resource Selection
↓
Availability Validation
↓
Access-Class Resolution
↓
Free Retrieval OR 402
↓
Payment Verification if required
↓
Settlement
↓
Payload Fidelity Validation
↓
Authorized Retrieval
```

Not every request uses every stage.

---

# 44. Resource Availability Before Payment

The central production safety rule remains:

```text
availability
before
payment
```

Never:

```text
route matches pricing tier
→ charge first
→ determine payload availability later
```

---

# 45. Regression Rule

Whenever a new price class or protected resource is activated, retest applicable existing routes for unintended changes.

The Atomic activation correctly included Structured Plate regression checks.

Future activation should follow the same pattern.

---

# 46. New Resource Test Record

For each new protected resource, record:

```text
Resource:
Canonical identifier:
Canonical authority:
Resource class:
Price:
Atomic units:
Availability state:

404 test:
409 test:
402 challenge test:

Settlement test:
Protected payload-delivery test:
Fidelity test:

Rights notice:
Validation date:
```

A missing settlement or delivery test must remain explicitly marked as untested.

---

# 47. Historical Enriched Activation Requirement

The August 20 record required any later Enriched Query activation to add a new dated record rather than rewriting the earlier reserved state.

The new record should include at minimum:

```text
explicit resource
canonical identifier
availability state
402 challenge
25000 units
enriched tier
404 test
409 test
settlement status
delivery status
```

Historical reserved records should remain in Git history.

---

# 47A. Enriched Production Activation
## 2026-08-24

Registered production route:

```text
/v1/query/enriched/robbie-george-biography-plate
```

Configuration:

```text
Access class: enriched
Price: 0.025 USDC
Atomic units: 25000
Resource class: enriched-query
Schema: naturepedia.enriched-query.v1
```

Observed challenge behavior:

```text
STATUS: 402
AMOUNT: 25000
TIER: enriched
PAYMENT REQUIRED: true
```

Unknown Enriched identifier behavior:

```text
STATUS: 404
PAYMENT REQUIRED: false
```

Validation boundary:

```text
payment supplied: no
settlement attempted: no
protected Enriched payload delivery tested: no
```

Result:

```text
PASS
```

Interpretation:

```text
Biography Enriched Query challenge verified
≠
every Enriched resource active
```

Only explicitly registered, governed, deterministic Enriched payloads are payment-eligible.

---

# 48. Evidence Discipline

A production test statement should answer:

```text
what was tested?
when?
against which route?
what was observed?
what was not tested?
```

This is stronger than broad statements such as:

```text
snapshot retrieval active
```

without resource-specific context.

---

# 49. Final Interpretation Rules

This test record must preserve:

```text
specific tested resource
≠
entire resource class
```

```text
pricing class
≠
blanket availability
```

```text
route template
≠
resource existence
```

```text
402 challenge
≠
settlement
```

```text
historical settlement
≠
new-route settlement
```

```text
historical delivery
≠
new-route delivery
```

```text
public control plane
≠
protected snapshot
```

```text
Enriched price
≠
Enriched activation
```

```text
payment
≠
commercial rights
```

```text
payment
≠
scientific evidence
```

---

# Current Verified Matrix

```text
HISTORICAL END-TO-END x402
Challenge: verified
Settlement: verified
Protected delivery: verified

TREE SYSTEM MAP
Price: 5.00 USDC
Units: 5000000
Tier: subtree
Challenge: verified
New settlement test: not performed
New delivery test: not performed

GEOLOGY KNOWLEDGE MESH
Price: 25.00 USDC
Units: 25000000
Tier: snapshot
Challenge: verified
New settlement test: not performed
New delivery test: not performed

ATOMIC BIOGRAPHY QUERY
Price: 0.005 USDC
Units: 5000
Tier: atomic
Challenge: verified
Settlement in activation round: not performed
Protected delivery in activation round: not performed

ATOMIC KNOWN-INCOMPLETE
Status: 409
Payment challenge: no
Verified: yes

ATOMIC UNKNOWN
Status: 404
Payment challenge: no
Verified: yes

STRUCTURED PLATES
Price: 0.25 USDC
Units: 250000
Tier: single-plate
Three registered challenge routes verified
New settlement in regression round: not performed

ENRICHED QUERY
Price: 0.025 USDC
Units: 25000
Status: ACTIVE FOR THE REGISTERED BIOGRAPHY ENRICHED QUERY
Challenge: 402 / 25000 / enriched verified on 2026-08-24
Settlement in activation round: not performed
```

---

# Attribution

Naturepedia™, Robbie’s Razor™, Plate™ Architecture, RRIP™, Graph Registry™, Knowledge Mesh terminology, and associated original Grand Compression machine-infrastructure concepts originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

These materials are governed by the **Authorship Conservation Rule (ACR)**.

x402, Base, USDC, Cloudflare, HTTP, MCP, JSON, cryptographic methods, and related external technologies and standards retain their independent provenance and ownership.
