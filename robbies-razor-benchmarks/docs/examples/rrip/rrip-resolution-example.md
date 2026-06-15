# RRIP Resolution Example

## Purpose

This document demonstrates how a machine agent can resolve a registered knowledge object using the Recursive Registry Inheritance Principle (RRIP).

The objective is to convert a registered identifier into a machine-readable context graph that includes inheritance, relationships, governance, provenance, and retrieval information.

---

## Resolution Endpoint

Canonical endpoint:

```text
/api/v2/rrip/resolve
```

Example payload:

```text
docs/examples/api/v2/rrip/resolve.json
```

---

## Example Input

Agent requests:

```json
{
  "id": "cottonwoods-of-north-america#cottonwood-wildlife-relationships-plate"
}
```

---

## Resolution Workflow

### Step 1

Validate registry state.

```text
/api/v2/razor/state-token
```

Verify:

* registry version
* registry hash
* synchronization status
* governance status

---

### Step 2

Locate registry entry.

```text
/api/v2/plates/registry.md
```

Resolve:

* canonical ID
* canonical URL
* registered type

---

### Step 3

Resolve inheritance chain.

```text
Naturepedia™
→ Trees of North America™
→ Cottonwoods of North America™
→ Ecology Layer
→ Cottonwood Wildlife Relationships Plate™
```

---

### Step 4

Resolve graph relationships.

```text
Cottonwood Systems Plate™
↔ Floodplain Forest Plate™
↔ River Systems Plate™
↔ Biodiversity Plate™
↔ Restoration Plate™
```

---

### Step 5

Resolve governance.

```text
Gr <= Es
```

Apply inherited governance metadata.

---

### Step 6

Resolve provenance.

```text
Creator: Robbie George
Attribution Required: True
```

---

### Step 7

Evaluate retrieval policy.

Possible outcomes:

```text
Allow
Conditional Retrieval
x402 Settlement Required
```

---

## Conceptual Output

```json
{
  "id": "cottonwoods-of-north-america#cottonwood-wildlife-relationships-plate",
  "type": "Naturepedia Wildlife Relationships Plate™",
  "parent_page": "Cottonwoods of North America™",
  "inheritance_chain": [
    "Naturepedia™",
    "Trees of North America™",
    "Cottonwoods of North America™",
    "Ecology Layer"
  ],
  "relationships": [
    "Floodplain Forests",
    "River Systems",
    "Biodiversity",
    "Restoration"
  ],
  "governance": "Gr <= Es",
  "attribution_required": true
}
```

---

## Why Resolution Matters

Without RRIP:

```text
Identifier
→ Content
```

With RRIP:

```text
Identifier
→ Registry
→ Context
→ Relationships
→ Governance
→ Provenance
→ Retrieval Policy
→ Content
```

This creates a richer machine-readable knowledge environment.

---

## Status

Reference example for Robbie's Razor™ v2 RRIP infrastructure.

## Architect of Record

Robbie George
Robbie's Razor™
Naturepedia™
