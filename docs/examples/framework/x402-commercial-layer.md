# x402 Commercial Infrastructure Layer
## Protected Retrieval, Pricing, Rights, and Settlement Boundaries

## Document Status

**Status:** Production commercial-infrastructure reference  
**Current governing framework:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Production pricing manifest:** v3.0.0  
**Network:** Base — `eip155:8453`  
**Asset:** USDC  
**Settlement protocol:** x402-compatible protected retrieval  
**Production posture:** Fail closed

This document explains how x402 protected retrieval fits into the Naturepedia™ / Robbie’s Razor™ infrastructure.

The core distinction is:

```text
Public Discovery
≠
Protected Retrieval
≠
Commercial Data License
≠
Framework License
```

These layers may interact, but they grant different forms of access and authority.

---

# Canonical and Production Authority

Grand Compression Master Reference Document:

https://www.robbiegeorgephotography.com/grand-compression-master-reference-document

Canonical Claims Register:

https://www.robbiegeorgephotography.com/grand-compression-canonical-claims

Framework Licensing:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

Commercial Data License:

https://www.robbiegeorgephotography.com/commercial-data-license

Authoritative production pricing manifest:

https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json

Repository authority:

```text
docs/AUTHORITY.md
```

---

# 1. x402 Role

x402 is used as a machine-payment and protected-retrieval layer for explicitly registered resources.

Conceptually:

```text
resource identity
↓
availability validation
↓
access class
↓
fixed price
↓
402 challenge
↓
payment authorization
↓
verification / settlement
↓
protected retrieval
```

x402 does not determine:

- canonical framework truth;
- scientific validity;
- authorship;
- resource existence by itself;
- framework implementation rights.

---

# 2. External Technology Boundary

x402 is an external protocol.

Naturepedia’s integration, routing, resource governance, pricing architecture, and protected-delivery implementation may be authored within the Grand Compression / Naturepedia system.

But:

```text
Naturepedia uses x402
≠
Robbie George originated x402
```

Likewise, Base, USDC, Cloudflare, HTTP, JSON, and related technologies retain their independent provenance.

---

# 3. Four Distinct Access Layers

The system should preserve four distinct layers.

## Public Discovery

May expose:

- metadata;
- indexes;
- endpoint descriptions;
- public pages;
- AI discovery files;
- public control-plane resources.

Public discovery normally requires no x402 payment.

---

## Protected Retrieval

Provides one governed machine-readable retrieval of an explicitly registered protected resource.

This is the primary role of x402.

---

## Commercial Data License

May govern broader commercial use of applicable data assets where explicitly granted.

The written license controls.

---

## Framework License

May govern implementation or deployment rights for protected Grand Compression / Robbie’s Razor™ framework material where explicitly granted.

The written agreement controls.

---

# 4. Core Separation Rule

Required distinction:

```text
x402 Retrieval Access
≠
Commercial Data License
≠
Robbie’s Razor™ Framework License
```

Also:

```text
payment
≠
ownership
```

```text
payment
≠
training rights
```

```text
payment
≠
framework implementation rights
```

```text
payment
≠
empirical validation
```

---

# 5. Production Pricing Authority

The authoritative production manifest is:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current version:

```text
3.0.0
```

Network:

```text
eip155:8453
```

Asset:

```text
USDC
```

Current production pricing uses fixed prices.

A repository document must not create a second independent pricing authority.

---

# 6. Current Pricing Classes

| Access class | Price | Atomic units | Production interpretation |
|---|---:|---:|---|
| Public discovery / previews | Free | `0` | Public where exposed |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active only for explicitly registered deterministic resources |
| Enriched relationship query | `$0.025 USDC` | `25000` | Reserved |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active only for explicitly registered and validated Plate payloads |
| Bounded subtree / Registry / System Map class | `$5.00 USDC` | `5000000` | Pricing class defined; individual resource availability is registration-specific |
| Full Registry / Knowledge Mesh snapshot class | `$25.00 USDC` | `25000000` | Pricing class defined; individual resource availability is registration-specific |

Required distinction:

```text
pricing class exists
≠
specific resource exists
```

---

# 7. Resource Before Price

The production gateway should resolve:

```text
resource identity
before
price
```

not:

```text
URL resembles paid route
→ assign price
→ assume resource exists
```

The correct order is:

```text
canonical resource
↓
availability
↓
access class
↓
price
```

---

# 8. Fail-Closed Availability Model

Protected retrieval must fail closed.

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

This protects agents from paying for unavailable resources.

---

# 9. Atomic Canonical Query

Public route template:

```text
/v1/query/atomic/{resource}
```

Current verified Atomic resource:

```text
/v1/query/atomic/robbie-george-biography-plate
```

Canonical internal compatibility route:

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
Schema: naturepedia.atomic-query.v1
```

---

# 10. Verified Atomic Challenge

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

This establishes the payment challenge for that registered resource.

During that activation validation:

```text
new Atomic payment: not supplied
new Atomic settlement: not performed
protected Atomic HTTP 200 delivery: not retested
```

Therefore:

```text
Atomic challenge verified
≠
new Atomic settlement verified
```

---

# 11. Atomic Safety Tests

Known but incomplete resource:

```text
/v1/query/atomic/robbies-razor-plate
```

Observed:

```text
409
no payment challenge
```

Unknown Atomic resource:

```text
404
no payment challenge
```

Current Atomic safety model:

```text
registered + complete
→ 402 / 5000 / atomic

known incomplete
→ 409 / no payment

unknown
→ 404 / no payment
```

---

# 12. Enriched Query

Current pricing:

```text
0.025 USDC
25000 atomic units
```

Current state:

```text
RESERVED
```

A published price does not activate an Enriched resource.

Required rule:

```text
Enriched pricing class exists
≠
Enriched product exists
```

Activation requires:

- explicit registration;
- governed deterministic payload;
- availability gating;
- fidelity requirements;
- production validation.

---

# 13. Structured Plate™ Retrieval

Current verified Structured Plate routes include:

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

Observed challenge result for the tested resources:

```text
STATUS: 402
AMOUNT: 250000
TIER: single-plate
PAYMENT REQUIRED: true
```

Unknown Plates:

```text
404
no payment
```

Known but incomplete Plates:

```text
409
no payment
```

---

# 14. `$5` Bounded-Resource Class

Current price:

```text
5.00 USDC
5000000 atomic units
```

This pricing class may apply to qualifying:

- taxonomy subtrees;
- Registries;
- identity graphs;
- System Maps.

But:

```text
$5 class exists
≠
every bounded resource is active
```

Specific resource availability must be registered.

---

# 15. Verified `$5` Resource

Production evidence includes the specific:

```text
/v1/plates/tree-system-map
```

resource.

Pricing-v3 challenge:

```text
402 Payment Required
5000000 atomic units
tier: subtree
```

Historical testing also recorded successful settlement and protected delivery on the Tree System Map route.

Therefore:

```text
Tree System Map
→ resource-specific $5 evidence exists
```

but:

```text
Tree System Map verified
≠
every $5-class resource verified
```

---

# 16. `$25` Snapshot Class

Current price:

```text
25.00 USDC
25000000 atomic units
```

This pricing class may apply to qualifying explicitly registered:

- full Registry snapshots;
- Knowledge Mesh snapshots;
- other governed large protected resources.

But:

```text
$25 class exists
≠
every Knowledge Mesh is active
```

---

# 17. Verified `$25` Resource

Production evidence includes:

```text
/v1/knowledge-mesh/geology
```

Observed pricing-v3 challenge:

```text
402 Payment Required
25000000 atomic units
tier: snapshot
```

This supports:

```text
Geology Knowledge Mesh
→ challenge-verified under $25 class
```

It does not establish:

```text
all Knowledge Meshes active
```

---

# 18. Public v2 Control Plane

Current public machine-facing endpoints include:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These exact endpoints are public control-plane resources.

They should **not** be listed as examples of paid x402 retrieval.

Required distinction:

```text
public control-plane endpoint
≠
protected x402 resource
```

---

# 19. Naturepedia Discovery Endpoint

```text
/api/v2/naturepedia/index.md
```

Role:

- machine discovery;
- ecosystem navigation;
- resource-family awareness;
- routing orientation.

Payment:

```text
public
```

unless a future production change explicitly states otherwise.

---

# 20. Plate Registry Endpoint

```text
/api/v2/plates/registry.md
```

Role:

- Plate™ discovery;
- registry navigation;
- resource identity;
- machine routing.

It should not automatically be described as:

- Graph Registry access;
- paid Registry retrieval;
- Knowledge Mesh traversal.

Its current public endpoint contract governs.

---

# 21. RRIP Resolver

```text
/api/v2/rrip/resolve
```

Role:

- RRIP-oriented relationship resolution;
- inheritance-path lookup where implemented.

Current canonical orientation:

```text
MRD v2.0 §12.8
```

The public resolver itself is not automatically a `$25` product.

---

# 22. State Token

```text
/api/v2/razor/state-token
```

Role:

- registry-state signaling;
- version comparison;
- synchronization metadata;
- cache coordination.

It does not independently verify:

- truth;
- scientific validity;
- physical entropy;
- substantive framework compliance.

Required distinction:

```text
state agreement
≠
evidence validation
```

---

# 23. Public vs Protected Resource

A client may discover a protected resource through the public control plane.

Conceptually:

```text
public discovery
↓
resource resolution
↓
availability check
↓
public or protected
```

If public:

```text
retrieve directly
```

If protected:

```text
402
↓
payment authorization
↓
settlement
↓
protected retrieval
```

---

# 24. x402 Is Not a Sitewide Paywall

Naturepedia contains both:

```text
public human-readable content
```

and:

```text
public machine-readable discovery
```

alongside:

```text
selected protected machine resources
```

x402 should therefore be interpreted as:

```text
resource-specific protected retrieval
```

not:

```text
sitewide access control
```

---

# 25. Commercial Data License

The Commercial Data License governs applicable commercial data-use rights where explicitly granted.

It may govern uses such as:

- structured-data reuse;
- commercial dataset use;
- certain ingestion or redistribution rights;
- other rights expressly described by the agreement.

The written license controls.

Do not infer rights merely from this repository document.

---

# 26. Commercial Data License Boundary

The Commercial Data License should not be represented as automatically controlling:

- every Naturepedia page;
- every public discovery resource;
- all framework implementation;
- all private deployments;
- all x402 retrieval.

Required distinction:

```text
data-use rights
≠
framework implementation rights
```

---

# 27. Framework Licensing

Framework Licensing may govern protected implementation rights for Grand Compression / Robbie’s Razor™ architecture where the agreement applies.

Potentially covered framework-specific concepts may include:

- Robbie’s Razor™;
- RKCA™;
- RRIP™;
- Plate™ Architecture;
- Graph Registry™ architecture;
- Knowledge Mesh architecture;
- ACR governance.

The exact agreement governs.

---

# 28. Framework License Boundary

Framework Licensing is not a technical runtime layer.

Required distinction:

```text
framework license
≠
API gateway
```

and:

```text
framework license
≠
payment protocol
```

It is a rights/governance layer operating alongside implementation.

---

# 29. Authorship Conservation Rule

Current doctrine name:

```text
Authorship Conservation Rule (ACR)
```

Use the singular form.

ACR governs provenance preservation.

x402 governs protected retrieval payment where applicable.

Conceptually:

```text
ACR
→ provenance governance

x402
→ protected-retrieval settlement
```

Neither replaces the other.

---

# 30. ACR Is Not Required Because x402 Exists

Avoid the deterministic claim:

```text
ACR + x402 are both required for responsible retrieval
```

as a universal rule.

A better interpretation is:

```text
ACR governs provenance where applicable
x402 governs protected payment where applicable
```

A public resource may use ACR provenance without x402.

A protected resource may use both.

---

# 31. RRIP Relationship

Current canonical orientation:

```text
MRD v2.0 §12.8
→ Recursive Registry Inheritance Principle (RRIP™)
```

RRIP may govern inheritance relationships among explicitly registered resources.

Avoid:

```text
RRIP determines what relationships exist
```

RRIP governs an inheritance principle.

It does not define all possible semantic relationships in Naturepedia.

---

# 32. Graph Registry™ Relationship

A Graph Registry™ may represent typed governed relationships.

It does not automatically determine:

- protected endpoints;
- prices;
- access classes;
- payment eligibility.

Required distinction:

```text
Graph Registry
≠
pricing engine
```

---

# 33. Knowledge Mesh Relationship

A Knowledge Mesh may organize higher-order governed relationships where explicitly implemented.

Avoid:

```text
Knowledge Mesh determines how large-scale intelligence emerges
```

Preferred:

```text
Knowledge Mesh may organize higher-order machine-readable relationships
```

A Knowledge Mesh is infrastructure, not automatically cognition.

---

# 34. RKCA Structural Orientation

A possible architecture may include:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

This should be interpreted as:

```text
possible governed resource progression
```

not:

```text
mandatory automatic evolution
```

Required distinction:

```text
architecture permits layer
≠
resource exists
```

---

# 35. Registry Is Not Automatically Memory

A Registry may preserve state useful for later retrieval.

But:

```text
Registry
≠
memory automatically
```

Useful memory requires:

- stable identity;
- retrievability;
- freshness;
- interpretation;
- validation appropriate to the task.

---

# 36. Knowledge Mesh Is Not Automatically Intelligence

Avoid:

```text
Knowledge Mesh
=
large-scale intelligence structure
```

Preferred terminology:

```text
higher-order relationship infrastructure
```

or:

```text
governed structured knowledge infrastructure
```

---

# 37. State Synchronization Model

A public state-token workflow may help reduce unnecessary refreshes.

Example:

```text
Agent
↓
State Check
↓
Registry Changed?
```

If no:

```text
cached state may remain usable
subject to resource validity and freshness rules
```

If yes:

```text
refresh or revalidation may be appropriate
```

This is a synchronization pattern, not a truth-verification system.

---

# 38. Cache Boundary

A matching registry state does not establish that:

- externally changing facts remain current;
- cached conclusions remain correct;
- scientific evidence has not changed.

Required distinction:

```text
registry unchanged
≠
world unchanged
```

---

# 39. MCP Relationship

The Naturepedia MCP server is a separate protocol interface.

Required distinctions:

```text
MCP
≠
x402
```

```text
MCP discovery
≠
payment
```

```text
HTTP endpoint
≠
MCP tool automatically
```

A wallet-capable agent may combine MCP discovery with x402 retrieval where appropriate.

---

# 40. Agent-Wallet Boundary

Receiving a `402` does not itself authorize payment.

A wallet-capable agent may evaluate:

- resource identity;
- price;
- policy;
- user authorization;
- budget;
- rights.

Required distinction:

```text
402
≠
automatic wallet authorization
```

---

# 41. Historical Settlement Evidence

Production records include a historical successful Base USDC settlement.

Historical transaction:

```text
0x4b43cc4b1d891219b372699791e7e4127836935262bdd5747850d9143ea87376
```

This demonstrates:

```text
production settlement capability
```

It does not demonstrate:

```text
every current protected route settled
```

---

# 42. Challenge vs Settlement vs Delivery

These states must remain separate.

```text
402 challenge
≠
settlement
```

```text
settlement
≠
protected delivery on every route
```

```text
historical end-to-end success
≠
new-route end-to-end test
```

---

# 43. Retrieval Rights Boundary

One successful x402 payment grants the identified endpoint-level retrieval under the applicable access conditions.

It does not automatically grant:

- training rights;
- embedding rights;
- bulk ingestion;
- redistribution;
- resale;
- synchronization;
- private-dataset construction;
- derivative-dataset rights;
- commercial implementation rights;
- framework implementation rights;
- ownership rights.

---

# 44. Attribution Boundary

Payment does not remove attribution or provenance.

Required distinction:

```text
payment
≠
authorship transfer
```

Likewise:

```text
public access
≠
origin-free content
```

The applicable provenance rules remain relevant.

---

# 45. Evidence Boundary

Successful machine commerce demonstrates machine-commerce behavior.

It does not independently establish:

- scientific validity;
- Grand Compression universal correctness;
- external consensus;
- causal superiority;
- economic superiority.

Canonical orientation:

```text
RC-21 — Reference Implementation Distinction
```

---

# 46. Commercial Success Boundary

A transaction demonstrates:

```text
at least one successful transaction
```

It does not automatically demonstrate:

- broad market demand;
- product-market fit;
- sustainable revenue;
- agent adoption at scale.

Those require separate evidence.

---

# 47. Machine Retrieval Efficiency

Structured protected retrieval may reduce some retrieval burden in particular workflows.

That is a testable claim.

Do not assume:

```text
x402
→ lower compute
```

or:

```text
paid retrieval
→ better answer
```

The payment mechanism itself does not determine retrieval quality.

---

# 48. Graph Presence vs Resource Availability

A resource appearing in:

- a Registry;
- Graph Registry;
- Knowledge Mesh;
- AI catalog;

does not automatically establish that a paid resource exists.

The availability gate remains authoritative.

---

# 49. Production Resource Rule

Before a resource is payment-eligible, verify:

```text
canonical identity
explicit registration
complete governed payload
resource class
availability
price
rights scope
```

Only then:

```text
eligible 402
```

---

# 50. New Protected Resource Checklist

```text
[ ] canonical identifier
[ ] canonical authority
[ ] resource registration
[ ] complete governed payload
[ ] resource-class assignment
[ ] deterministic price
[ ] availability state
[ ] 404 behavior
[ ] 409 behavior where applicable
[ ] 402 challenge validation
[ ] provenance
[ ] rights notice
[ ] version
[ ] settlement status recorded separately
[ ] delivery status recorded separately
```

---

# 51. Enriched Activation Checklist

Enriched currently remains:

```text
RESERVED
```

Before activation:

```text
[ ] explicit resource exists
[ ] governed deterministic payload exists
[ ] availability gate implemented
[ ] 404 tested
[ ] 409 tested
[ ] 402 / 25000 tested
[ ] fidelity requirements defined
[ ] machine discovery synchronized
[ ] settlement status recorded
[ ] protected delivery status recorded
```

Do not mark Enriched active merely because its price is configured.

---

# 52. Current Production Summary

```text
NETWORK
Base
eip155:8453

ASSET
USDC

PRICING MANIFEST
v3.0.0

DISCOVERY
Free where exposed

ATOMIC
0.005 USDC
5000 atomic units
active only for explicitly registered deterministic resources

ENRICHED
0.025 USDC
25000 atomic units
RESERVED

STRUCTURED PLATE
0.25 USDC
250000 atomic units
active only for explicitly registered validated payloads

BOUNDED MULTI-RECORD CLASS
5.00 USDC
5000000 atomic units
resource-specific availability

LARGE SNAPSHOT CLASS
25.00 USDC
25000000 atomic units
resource-specific availability

TREE SYSTEM MAP
$5 challenge verified
historical settlement/delivery evidence exists

GEOLOGY KNOWLEDGE MESH
$25 challenge verified

AVAILABILITY
unknown → 404
known incomplete → 409
registered complete protected resource → eligible 402
```

---

# 53. Final Interpretation Rules

This document must preserve:

```text
x402
≠
Commercial Data License
```

```text
x402
≠
Framework License
```

```text
public control plane
≠
paid endpoint
```

```text
pricing class
≠
resource existence
```

```text
route pattern
≠
product
```

```text
Registry
≠
memory automatically
```

```text
Graph Registry
≠
pricing engine
```

```text
Knowledge Mesh
≠
intelligence automatically
```

```text
RRIP
≠
all semantic relationships
```

```text
402 challenge
≠
settlement
```

```text
settlement
≠
all-route protected delivery
```

```text
payment
≠
training rights
```

```text
payment
≠
authorship transfer
```

```text
payment
≠
scientific validation
```

```text
reference implementation
≠
independent confirmation
```

---

# Related Resources

x402 production architecture:

```text
docs/examples/x402/README.md
```

Live endpoint record:

```text
docs/examples/x402/live-endpoints.md
```

Worker architecture:

```text
docs/examples/x402/worker-architecture.md
```

MCP compatibility:

```text
docs/examples/x402/mcp-compatibility.md
```

Pricing mirror:

```text
docs/examples/x402/pricing-map-example.json
```

ACR:

```text
docs/examples/framework/acr-governance.md
```

Graph Registry:

```text
docs/examples/framework/graph-registry.md
```

Knowledge Mesh:

```text
docs/examples/framework/knowledge-mesh.md
```

Framework Licensing:

https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing

Commercial Data License:

https://www.robbiegeorgephotography.com/commercial-data-license

---

# Attribution

Naturepedia™, Robbie’s Razor™, RKCA™, RRIP™, Plate™ Architecture, Graph Registry™, Knowledge Mesh terminology as used within the Grand Compression framework, ACR, and associated original Grand Compression implementation concepts originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

The **Authorship Conservation Rule (ACR)** governs preservation of that framework provenance.

x402, Base, USDC, Cloudflare, MCP, HTTP, JSON, cryptographic payment methods, and other external standards and technologies retain their independent provenance.

Implementation, payment, licensing, settlement, machine transformation, retrieval, or similarity does not by itself establish empirical validation, derivation, shared authorship, or ownership transfer.
