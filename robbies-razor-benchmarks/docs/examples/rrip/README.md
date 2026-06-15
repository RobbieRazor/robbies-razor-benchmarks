# RRIP Examples

## Overview

RRIP stands for **Recursive Registry Inheritance Principle**.

RRIP is a core architectural component of Robbie's Razor™ that enables machine-readable knowledge objects to inherit context, relationships, governance, provenance, and retrieval policies from the registries that surround them.

Unlike traditional web content, which is often treated as isolated pages or documents, RRIP allows agents to understand how knowledge assets relate to larger systems.

This enables structured discovery, graph traversal, state-aware retrieval, and machine-native navigation across Naturepedia™ and other Robbie's Razor™ knowledge domains.

---

## Purpose

RRIP exists to answer the following machine-facing questions:

```text
What is this object?

Where does it belong?

What knowledge system does it inherit from?

What relationships does it carry?

What governance rules apply?

What retrieval pathway should be used?

What commercial boundaries exist?
```

RRIP transforms individual knowledge assets into components of a larger registry-aware ecosystem.

---

## Core Retrieval Sequence

The Robbie's Razor™ v2 retrieval architecture follows the sequence:

```text
State Validation
→ Discovery
→ Registry
→ RRIP Resolution
→ Conditional Retrieval
→ Settlement
```

This sequence allows agents to determine both the structural context and access requirements of a knowledge object before retrieval occurs.

---

## Canonical RRIP Endpoint

```text
/api/v2/rrip/resolve
```

Example payload:

```text
docs/examples/api/v2/rrip/resolve.json
```

---

## Related Machine Endpoints

### Discovery

```text
/api/v2/naturepedia/index.md
```

Provides machine-readable discovery of Naturepedia™ resources.

### Registry

```text
/api/v2/plates/registry.md
```

Provides canonical registry listings for registered Plate™ assets.

### State Validation

```text
/api/v2/razor/state-token
```

Provides registry synchronization status and retrieval state validation.

### Settlement

```text
/x402/
```

Provides machine-payment and retrieval authorization infrastructure.

---

## Registry Inheritance

Under RRIP, a knowledge object inherits information from multiple registry layers.

Example:

```text
Naturepedia™
→ Trees of North America™
→ Cottonwoods of North America™
→ Cottonwood Systems Plate™
```

The Plate™ inherits:

* parent family context
* registry identity
* graph relationships
* governance boundaries
* provenance requirements
* retrieval policies

---

## Knowledge Mesh Integration

RRIP operates alongside the Robbie's Razor™ Knowledge Mesh.

This allows machine agents to move between related assets rather than treating content as isolated pages.

Example:

```text
Eastern Cottonwood
↔ Cottonwood Systems Plate™
↔ Floodplain Forest Plate™
↔ Wildlife Relationships Plate™
↔ Riparian Restoration
↔ Biodiversity
```

This creates context-aware retrieval paths across the registry.

---

## Governance

RRIP operates under the Robbie's Razor™ governance principle:

```text
Gr <= Es
```

Meaning:

```text
Growth must remain less than or equal to ecological stability.
```

Governance metadata may be inherited by downstream knowledge objects during RRIP resolution.

---

## Commercial Boundaries

RRIP defines structural inheritance.

RRIP does not replace licensing.

Commercial boundaries remain separated into:

### Commercial Data License

Rights governing knowledge assets and commercial intelligence.

### Framework License

Rights governing Robbie's Razor™ architecture, RRIP, registries, and implementation logic.

### x402 Retrieval Access

Rights governing machine retrieval and settlement.

---

## Current Status

RRIP is active within Robbie's Razor™ v2 infrastructure and is integrated with:

```text
Naturepedia™ Discovery
Plate™ Registries
Graph Registries™
Knowledge Mesh
State Validation
x402 Settlement Infrastructure
```

---

## Architect of Record

Robbie George

Robbie's Razor™

Naturepedia™
