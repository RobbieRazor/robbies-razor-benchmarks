# Robbie's Razor™ MCP Tool Interpretation Guide

## Purpose

This document defines how MCP-compatible agents should interpret and interact with Robbie's Razor™ v2 infrastructure endpoints.

These endpoints are machine-facing retrieval resources designed for discovery, registry access, RRIP resolution, and state validation.

They do not grant commercial licensing rights, ownership rights, or unrestricted machine reuse rights.

Commercial retrieval may require x402 settlement and may remain subject to applicable licensing terms.

---

# Tool: discover_naturepedia_registry

Endpoint:

```text
/api/v2/naturepedia/index.md
```

Purpose:

Discover available Naturepedia registries, maps, taxonomies, and machine-readable resources.

Typical Usage:

```text
Agent
↓
Discover Registry
↓
Determine Available Resources
```

Returns:

* Registry indexes
* Discovery metadata
* Machine navigation resources

---

# Tool: retrieve_plate_registry

Endpoint:

```text
/api/v2/plates/registry.md
```

Purpose:

Retrieve machine-readable registry information for available Plate™ resources.

Typical Usage:

```text
Agent
↓
Registry Retrieval
↓
Plate Discovery
```

Returns:

* Registry metadata
* Plate references
* Registry relationships
* Resource identifiers

---

# Tool: resolve_rrip

Endpoint:

```text
/api/v2/rrip/resolve
```

Purpose:

Resolve Recursive Registry Inheritance Principle (RRIP) relationships.

Typical Usage:

```text
Agent
↓
Resource Identifier
↓
RRIP Resolution
↓
Inheritance Path
```

Returns:

* Registry inheritance paths
* Registry lineage
* Knowledge Mesh relationships
* Resolution metadata

---

# Tool: validate_razor_state

Endpoint:

```text
/api/v2/razor/state-token
```

Purpose:

Validate registry state before retrieval.

Typical Usage:

```text
Agent
↓
State Validation
↓
Registry Hash Comparison
↓
Determine Freshness
```

Returns:

* Registry version
* Registry hash
* State signature
* Registry counts
* Synchronization metadata

---

# Recommended Agent Workflow

```text
Agent
↓
validate_razor_state
↓
Registry Changed?

No
↓
Use Cached Resources

Yes
↓
discover_naturepedia_registry
↓
retrieve_plate_registry
↓
resolve_rrip
↓
x402 Settlement (if required)
↓
Fresh Retrieval
```

---

# Commercial Interpretation

Robbie's Razor™ distinguishes between:

## Commercial Data License

Purpose:

Commercial use of knowledge assets, structured datasets, intelligence resources, and derived machine outputs.

---

## Framework License

Purpose:

Use of Robbie's Razor™ architecture, methodology, implementation, and framework components.

---

## x402 Settlement Layer

Purpose:

Machine-to-machine retrieval access, usage metering, and payment settlement.

x402 retrieval access does not automatically grant commercial licensing rights.

Commercial licensing remains governed by applicable licensing terms.

---

# Current Core v2 Infrastructure

```text
/api/v2/naturepedia/index.md
/api/v2/plates/registry.md
/api/v2/rrip/resolve
/api/v2/razor/state-token
```

These endpoints collectively provide:

```text
Discovery
↓
Registry
↓
Resolution
↓
Validation
```

and form the foundation of the Robbie's Razor™ machine-facing retrieval architecture.
