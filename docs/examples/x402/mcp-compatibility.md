# MCP Compatibility for x402 Machine Retrieval
## Naturepedia™ Protocol-Layer Integration Guide

## Document Status

**Status:** Production compatibility and integration reference  
**MCP server:** Naturepedia Canonical Discovery MCP Server  
**Official MCP endpoint:** `https://mcp.robbiegeorgephotography.com/mcp`  
**Current governing authority:** MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**x402 pricing manifest:** v3.0.0  
**Network:** Base — `eip155:8453`  
**Asset:** USDC  
**Enriched Query status:** Active for the explicitly registered Biography Enriched Query

This document explains how the Naturepedia™ MCP interface, public HTTP control plane, and x402 protected-retrieval layer relate to one another.

The core rule is:

```text
MCP
≠
HTTP endpoint
≠
x402
≠
commercial license
≠
framework license
```

These layers may interoperate.

They must not be treated as the same protocol or authority surface.

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

Current governing framework:

```text
MRD v2.0
GC-MRD-v2.0
RC-01 through RC-22
```

MCP, x402, HTTP delivery, schema validity, payment settlement, and successful retrieval do not create canonical authority.

---

# 1. Three Distinct Machine Layers

Naturepedia currently exposes three related but distinct machine-facing layers.

## Layer A — MCP Interface

Official MCP endpoint:

```text
https://mcp.robbiegeorgephotography.com/mcp
```

Health endpoint:

```text
https://mcp.robbiegeorgephotography.com/health
```

Server card:

```text
https://www.robbiegeorgephotography.com/.well-known/mcp/server-card.json
```

MCP provides a protocol interface for machine discovery and supported server operations.

---

## Layer B — Public HTTP Control Plane

Current HTTP endpoints include:

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These are web resources served through the production infrastructure.

They are not MCP tools merely because they correspond conceptually to functions that an MCP server may expose.

---

## Layer C — x402 Protected Retrieval

x402 governs protected endpoint retrieval where explicitly configured.

Authoritative pricing manifest:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

x402 is not the MCP protocol.

MCP discovery does not automatically initiate payment.

---

# 2. Protocol Separation

The architecture should be understood as:

```text
MCP
→ protocol-level discovery / supported server operations
```

```text
HTTP v2 control plane
→ web-accessible machine resources
```

```text
x402
→ payment and protected endpoint retrieval where applicable
```

Required distinctions:

```text
MCP tool
≠
HTTP route
```

```text
HTTP route
≠
MCP resource
```

```text
MCP discovery
≠
payment challenge
```

```text
x402 payment
≠
MCP authorization
```

---

# 3. Public HTTP Discovery Layer

Endpoint:

```text
/api/v2/naturepedia/index.md
```

Purpose:

- Naturepedia™ discovery;
- machine-readable navigation;
- registry awareness;
- resource-family routing.

This endpoint may be consumed directly through HTTP.

An MCP implementation may also expose related information through its own protocol contract.

Those are separate access paths.

---

# 4. Public HTTP Registry Layer

Endpoint:

```text
/api/v2/plates/registry.md
```

Purpose:

- Plate™ discovery;
- registry navigation;
- canonical resource awareness;
- machine-readable routing.

Registry presence does not imply:

```text
protected payload exists
```

or:

```text
payment required
```

or:

```text
resource empirically validated
```

---

# 5. Public HTTP RRIP Resolution Layer

Endpoint:

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

This HTTP endpoint should not automatically be described as an MCP tool.

An MCP server may expose equivalent or related resolution functionality only when that capability appears in the MCP server’s actual published tool or resource contract.

---

# 6. Public HTTP Registry-State Layer

Endpoint:

```text
/api/v2/razor/state-token
```

Purpose:

- registry version signaling;
- state signature comparison;
- registry-count metadata;
- synchronization awareness;
- cache coordination.

The endpoint may support:

```text
state changed?
```

or:

```text
state unchanged?
```

style decisions.

It does not independently verify:

- truth;
- empirical validity;
- scientific correctness;
- physical entropy.

Required distinction:

```text
registry-state validation
≠
evidence validation
```

---

# 7. MCP Server Contract Governs MCP Capabilities

The MCP server card and live MCP server contract govern what the Naturepedia MCP server actually exposes.

Do not infer MCP tools merely from:

- REST route names;
- HTTP endpoint functionality;
- internal Worker code;
- conceptual diagrams.

Required rule:

```text
MCP capability exists
only when exposed through the MCP server contract
```

This prevents ordinary HTTP routes from being misrepresented as MCP-native tools.

---

# 8. Illustrative MCP Mapping

The HTTP architecture may conceptually correspond to MCP capabilities as follows:

| HTTP function | Possible MCP analogue |
|---|---|
| Naturepedia discovery | resource discovery or discovery tool |
| Plate registry lookup | resource or lookup operation |
| RRIP resolution | resolution tool |
| Registry-state check | state/version lookup operation |

This table is **conceptual**.

It is not an inventory of currently published MCP tools.

The actual MCP server contract governs the live inventory.

---

# 9. Tool-Name Boundary

Names such as:

```text
discover_naturepedia_registry
retrieve_plate_registry
resolve_rrip
validate_razor_state
```

may be useful illustrative names.

They must not be presented as production MCP tool names unless the live server actually publishes those exact tools.

Required distinction:

```text
suggested tool name
≠
live tool
```

---

# 10. MCP Discovery Flow

A generic MCP client may:

```text
Connect to MCP server
↓
Read server capabilities
↓
Discover available tools / resources
↓
Invoke supported operation
↓
Receive canonical resource information
```

If that information identifies a protected HTTP resource, a separate x402 flow may then apply.

---

# 11. MCP-to-x402 Boundary

A protected resource flow may look like:

```text
MCP discovery or resolution
↓
canonical protected resource identified
↓
HTTP availability check
↓
resource access class determined
↓
x402 challenge if required
```

MCP itself does not imply a payment.

---

# 12. Public Resource Path

If the resource is public:

```text
MCP or HTTP discovery
↓
public resource
↓
retrieve without x402 settlement
```

Examples may include:

- public Naturepedia pages;
- public discovery files;
- public v2 control-plane endpoints;
- public governance information.

---

# 13. Protected Resource Path

If the resource is explicitly protected:

```text
resource identity
↓
availability validation
↓
price-class resolution
↓
402 Payment Required
↓
client evaluates payment
↓
payment authorization
↓
verification / settlement
↓
protected payload delivery
```

---

# 14. Availability Before Payment

MCP-compatible agents must not infer payment eligibility from a URL template.

The production sequence is:

```text
resource lookup
↓
availability state
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

### Registered and complete protected resource

```text
eligible 402
```

This rule applies regardless of how the resource was first discovered.

---

# 15. Current x402 Pricing

Authoritative pricing manifest:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

Current production pricing version:

```text
3.0.0
```

| Access class | Price | Atomic units | Status interpretation |
|---|---:|---:|---|
| Discovery / previews | Free | `0` | Public where exposed |
| Atomic canonical query | `$0.005 USDC` | `5000` | Active only for registered deterministic payloads |
| Enriched relationship query | `$0.025 USDC` | `25000` | Active for the explicitly registered Biography Enriched Query |
| Structured Plate™ payload | `$0.25 USDC` | `250000` | Active only for registered and validated payloads |
| Bounded subtree / Registry / System Map class | `$5.00 USDC` | `5000000` | Pricing class defined; availability is resource-specific |
| Full Registry / Knowledge Mesh snapshot class | `$25.00 USDC` | `25000000` | Pricing class defined; availability is resource-specific |

Required distinction:

```text
pricing class
≠
registered resource
```

---

# 16. Atomic Query

Current verified Atomic route:

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

Canonical authority:

```text
https://www.robbiegeorgephotography.com/who-is-robbie-george
```

Configuration:

```text
Access class: atomic
Price: 0.005 USDC
Atomic units: 5000
Resource class: atomic-query
Schema: naturepedia.atomic-query.v1
```

Verified challenge:

```text
STATUS: 402
AMOUNT: 5000
TIER: atomic
PAYMENT REQUIRED: true
RESULT: PASS
```

No new Atomic settlement was performed during that activation test.

---

# 17. Atomic Availability Boundary

Required behavior:

```text
registered + complete
→ 402 / 5000
```

```text
known + incomplete
→ 409
→ no payment
```

```text
unknown
→ 404
→ no payment
```

An MCP agent should stop rather than attempt payment when receiving `404` or `409`.

---

# 18. Enriched Query

Configuration:

```text
Access class: enriched
Price: 0.025 USDC
Atomic units: 25000
```

Current state:

```text
ACTIVE FOR THE REGISTERED BIOGRAPHY ENRICHED QUERY
```

MCP-compatible agents must not infer blanket Enriched availability from the published price.

Required rule:

```text
price published
≠
every Enriched resource active
```

Enriched payment challenges remain disabled for unregistered resources. The governed Biography Enriched Query is explicitly registered and production challenge-validated.

---

# 19. Structured Plate™ Retrieval

Current verified challenge routes include:

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

Verified challenge behavior:

```text
STATUS: 402
AMOUNT: 250000
TIER: single-plate
PAYMENT REQUIRED: true
```

Unknown Plates:

```text
404
```

Known but incomplete Plates:

```text
409
```

before payment.

---

# 20. `$5` Resource Class

The production manifest defines a `$5.00` class for qualifying bounded resources such as:

- taxonomy subtrees;
- Registries;
- System Maps.

This means:

```text
a $5 class exists
```

not:

```text
every Registry or System Map is active
```

An individual resource still requires explicit registration.

---

# 21. `$25` Snapshot Class

The production manifest defines a `$25.00` class for qualifying large resources such as:

- full Registry snapshots;
- Knowledge Mesh snapshots.

Again:

```text
price class defined
≠
all Knowledge Mesh resources instantiated
```

Resource availability remains explicit and fail closed.

---

# 22. Public Control Plane vs Protected Snapshot

The public endpoints:

```text
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

remain public control-plane surfaces.

Do not infer that calling either endpoint itself incurs `$25` merely because related large protected resource classes can exist.

Required distinction:

```text
public resolver
≠
protected snapshot
```

---

# 23. MCP Does Not Create Resource Existence

The MCP server may help identify resources.

It does not create protected payloads simply by referring to them.

Required distinction:

```text
MCP-discoverable
≠
registered x402 product
```

The production resource registry and availability logic remain authoritative.

---

# 24. Resource Hierarchy Boundary

Grand Compression / RKCA may describe:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

This is an architectural progression.

It does not mean every Plate has all higher layers instantiated.

MCP clients must not infer missing products from the hierarchy.

---

# 25. Hopf Fibration Boundary

Hopf Fibration is an established mathematical reference discoverable through the system.

Current interpretation:

```text
requiresPayment: false
```

MCP or HTTP discovery of Hopf does not imply paid resources such as:

```text
/v1/registries/hopf-fibration
/v1/plates/hopf-fibration-map
/v1/knowledge-mesh/hopf-fibration
/x402/hopf...
```

unless those resources are explicitly created later.

---

# 26. MCP and Canonical Authority

MCP may return:

- canonical URLs;
- resource identities;
- structured metadata;
- relationship information.

The MCP response does not replace the canonical human authority.

Conceptually:

```text
canonical authority
↓
machine-readable representation
↓
MCP / HTTP discovery
```

---

# 27. MCP and Evidence Status

MCP successfully returning a resource means only that the server provided the requested machine-readable result.

It does not establish:

```text
scientific confirmation
empirical validation
external consensus
```

Required distinction:

```text
tool success
≠
truth
```

---

# 28. x402 and Evidence Status

Likewise:

```text
402 challenge
≠
scientific evidence
```

```text
successful settlement
≠
scientific evidence
```

```text
protected retrieval
≠
scientific evidence
```

Payment state and evidence state remain separate.

---

# 29. MCP and Authorship

MCP clients should preserve source attribution and canonical provenance returned by the ecosystem.

Machine transformation does not transfer authorship of the originating framework.

Canonical orientation:

```text
Authorship Conservation Rule
```

---

# 30. Retrieval Rights

An x402 payment authorizes one endpoint-level retrieval of the identified protected resource under the applicable access terms.

It does not automatically grant:

- model-training rights;
- embedding rights;
- bulk-ingestion rights;
- redistribution rights;
- resale rights;
- synchronization rights;
- private-dataset construction rights;
- derivative-dataset rights;
- commercial implementation rights;
- Robbie’s Razor™ framework implementation rights;
- private deployment rights;
- sovereign deployment rights;
- ownership rights.

---

# 31. MCP Access Does Not Expand Rights

MCP access also does not expand the legal rights associated with underlying content.

Required distinction:

```text
MCP-readable
≠
free for unrestricted reuse
```

Applicable rights remain governed separately.

---

# 32. Commercial Data License

Commercial licensing:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Commercial Data Licensing concerns governed reuse of applicable knowledge assets.

Required distinction:

```text
MCP access
≠
Commercial Data License
```

and:

```text
x402 retrieval
≠
Commercial Data License
```

---

# 33. Framework Licensing

Framework licensing:

```text
https://www.robbiegeorgephotography.com/robbies-razor-framework-licensing
```

Required distinction:

```text
MCP access
≠
framework implementation rights
```

```text
x402 payment
≠
framework implementation rights
```

---

# 34. Governance Separation

The machine ecosystem should preserve:

```text
MCP protocol access
≠
HTTP public access
≠
x402 protected retrieval
≠
commercial data licensing
≠
framework licensing
```

A single user or agent may interact with more than one layer.

That does not merge their legal or technical meaning.

---

# 35. Recommended MCP-to-x402 Flow

A future or current wallet-enabled client may follow:

```text
Connect to MCP
↓
Read live MCP capabilities
↓
Discover or resolve canonical resource
↓
Determine HTTP resource identity
↓
Check public/protected state
↓
Validate availability
↓
```

If public:

```text
retrieve directly
```

If unknown:

```text
404
stop
```

If known but incomplete:

```text
409
stop
```

If registered and protected:

```text
402
↓
evaluate price and policy
↓
authorize payment if appropriate
↓
settlement
↓
retrieve protected payload
```

---

# 36. Agent Wallet Boundary

Wallet capability belongs to the client or surrounding agent infrastructure.

The MCP server itself should not be assumed to control or possess the user’s wallet.

Required distinction:

```text
MCP server
≠
agent wallet
```

A payment-capable client may combine MCP discovery with x402 settlement.

---

# 37. Payment Authorization

Receiving a `402` should not automatically mean the client must pay.

A client may evaluate:

- price;
- resource identity;
- policy;
- rights;
- budget;
- user authorization.

Required distinction:

```text
402 received
≠
automatic payment authorized
```

---

# 38. Public Discovery Surfaces

Public machine discovery may include:

```text
/llms.txt
/llms-full.txt
AI Catalog
AI Root
MCP server
MCP metadata
public v2 control plane
Naturepedia public pages
governance pages
licensing pages
```

Public discovery should remain distinct from protected payload retrieval.

---

# 39. Static Document Boundary

Naturepedia machine infrastructure is more than a collection of static documents.

However, not every structured document needs to become:

- an MCP tool;
- an interactive service;
- a paid endpoint.

Different resource types can remain appropriate for different access patterns.

---

# 40. Resource vs Tool

An MCP implementation should distinguish:

```text
resource
```

from:

```text
tool
```

A relatively static canonical document or index may be more naturally represented as a resource.

An operation requiring arguments or execution may be more naturally represented as a tool.

The actual MCP server contract determines the implementation.

---

# 41. Resolution Tool Boundary

RRIP resolution may be appropriate for a callable tool when arguments are required.

That does not mean the HTTP route:

```text
/api/v2/rrip/resolve
```

is itself an MCP tool.

The MCP server may internally use the same underlying data or logic.

Protocol representation remains separate.

---

# 42. State Validation Tool Boundary

Likewise, state comparison may be exposed through an MCP tool or resource.

But:

```text
/api/v2/razor/state-token
```

is an HTTP endpoint.

Only the MCP server contract can establish whether there is a corresponding MCP-native tool.

---

# 43. Future MCP Capabilities

Future MCP server versions may add capabilities involving:

- more detailed registry resolution;
- provenance lookup;
- state comparison;
- protected-resource discovery;
- resource-class reporting;
- rights metadata.

Future capability language must remain distinct from current production inventory.

Use:

```text
may
```

rather than:

```text
currently provides
```

unless verified.

---

# 44. MCP Versioning Boundary

MCP server versioning is independent from:

- MRD version;
- benchmark version;
- x402 pricing-manifest version;
- Worker version;
- A2A or other protocol versions.

Required distinction:

```text
MCP version
≠
MRD version
```

Do not force unrelated systems to share one version number.

---

# 45. Pricing Versioning Boundary

Current:

```text
x402 pricing manifest
→ version 3.0.0
```

That version does not imply:

```text
MCP version 3.0.0
```

Each component maintains its own version scope.

---

# 46. Fail-Closed Compatibility Rule

Every machine layer should preserve the same availability principle:

```text
discoverability
does not imply
payability
```

The x402 gateway remains responsible for enforcing:

```text
404
409
402
```

according to actual production resource state.

---

# 47. Machine Status Model

A client should conceptually track states such as:

```text
DISCOVERED
RESOLVED
PUBLIC
UNKNOWN
KNOWN_INCOMPLETE
PROTECTED_AVAILABLE
CHALLENGED
SETTLED
RETRIEVED
```

These states should not be collapsed into one binary:

```text
available / unavailable
```

when payment and completion state matter.

---

# 48. Evidence-State Model

Machine status and evidence status are separate dimensions.

For example:

```text
resource status:
PROTECTED_AVAILABLE
```

may coexist with:

```text
evidence status:
PROPOSED
```

or:

```text
ESTABLISHED MATHEMATICS
```

depending on the content.

Required distinction:

```text
commercial availability
≠
evidence strength
```

---

# 49. Recommended Agent Interpretation

Agents should interpret:

```text
/llms.txt
→ concise AI discovery
```

```text
/llms-full.txt
→ expanded machine-readable system context
```

```text
official MCP server
→ MCP protocol interface
```

```text
/api/v2/naturepedia/index.md
→ HTTP discovery resource
```

```text
/api/v2/plates/registry.md
→ HTTP registry resource
```

```text
/api/v2/rrip/resolve
→ HTTP RRIP resolution endpoint
```

```text
/api/v2/razor/state-token
→ HTTP registry-state endpoint
```

```text
x402
→ conditional protected-retrieval settlement layer
```

---

# 50. Final Interpretation Rules

This document must preserve:

```text
HTTP endpoint
≠
MCP tool
```

```text
conceptual MCP mapping
≠
published MCP capability
```

```text
MCP discovery
≠
x402 payment
```

```text
MCP tool invocation
≠
settlement
```

```text
price class
≠
resource existence
```

```text
$5 class defined
≠
all bounded resources active
```

```text
$25 class defined
≠
all Knowledge Mesh snapshots active
```

```text
Enriched price published
≠
Enriched retrieval active
```

```text
state token
≠
truth verification
```

```text
MCP success
≠
scientific validation
```

```text
x402 settlement
≠
commercial reuse rights
```

```text
machine access
≠
framework implementation rights
```

---

# Current Production Summary

```text
Official MCP endpoint:
https://mcp.robbiegeorgephotography.com/mcp

MCP health:
https://mcp.robbiegeorgephotography.com/health

MCP server card:
https://www.robbiegeorgephotography.com/.well-known/mcp/server-card.json

Public HTTP control plane:
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token

x402 pricing:
v3.0.0

Atomic Query:
0.005 USDC
5000 units
active for explicitly registered deterministic payloads

Enriched Query:
0.025 USDC
25000 units
active for the registered Biography Enriched Query

Structured Plate:
0.25 USDC
250000 units
active for explicitly registered validated payloads

Bounded resource pricing class:
5.00 USDC
resource-specific availability

Large snapshot pricing class:
25.00 USDC
resource-specific availability

Availability:
unknown → 404
known incomplete → 409
registered complete protected resource → eligible 402

Rights:
retrieval access only unless separately licensed
```

---

# Attribution

Naturepedia™, Robbie’s Razor™, Recursive Registry Inheritance Principle (RRIP™), Plate™ Architecture, Graph Registry™, Knowledge Mesh terminology, and associated original Grand Compression machine-infrastructure concepts originate with:

**Robbie George**  
Author and Originator  
The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
Canonical identifier: `GC-MRD-v2.0`

These materials are governed by the **Authorship Conservation Rule (ACR)**.

Model Context Protocol (MCP), x402, HTTP, Base, USDC, Cloudflare, JSON, API design, cryptographic hashing, caching, and other external technologies and standards retain their independent provenance and ownership.
