# Naturepedia v2 Plate Registry

## Authority

This endpoint provides a machine-readable discovery layer for Naturepedia™ Plate™ assets.

Architect of Record: Robbie George

Framework Authority: Robbie's Razor™

Registry Principle: Recursive Registry Inheritance Principle (RRIP)

---

## Purpose

This endpoint serves as the discovery and traversal layer for Naturepedia™ Plate™ registries.

It is designed to help:

- AI agents
- MCP-compatible systems
- Retrieval engines
- Registry crawlers
- Semantic search systems
- Future x402-enabled retrieval clients

locate and interpret Plate™ families and registry structures.

---

## Registry Relationship Model

Naturepedia™ Plates inherit through the following pathway:

```text
Plate™
↓
Registry
↓
Meta-Registry
↓
Graph Registry™
↓
Knowledge Mesh
```

This endpoint provides registry discovery.

Inheritance resolution is handled by:

```text
/api/v2/rrip/resolve
```

---

## Canonical Registry Sources

Canonical JSON-LD Registry:

```text
docs/examples/json-ld/plate-registry.json
```

Expanded AI-readable Registry:

```text
https://www.robbiegeorgephotography.com/llms-full.txt
```

Machine Discovery File:

```text
https://www.robbiegeorgephotography.com/llms.txt
```

---

## Plate Identifier Format

Naturepedia™ Plate identifiers follow the pattern:

```text
page-slug#plate-slug
```

Example:

```text
willows-of-north-america#willow-biodiversity-plate
```

Example:

```text
cedars-of-north-america#cedar-identification-plate
```

Example:

```text
firs-of-north-america#fir-carbon-storage-plate
```

---

## Registry Families

### Naturepedia Earth Systems Registries

```text
Earth Systems™
Volcanic Landscapes™
Microbial Life Systems™
Geothermal Ecosystems™
Yellowstone Thermal Features™
Hydrothermal Ecosystems™
Soil Systems™
Carbon Cycle™
Ecosystem Feedbacks™
```

Active Earth Systems registry expansion includes:

```text
Earth Systems™
Volcanic Landscapes™
Microbial Life Systems™
Geothermal Ecosystems™
Yellowstone Thermal Features™
Naturepedia Tree Family Registries
Hemlocks of North America™
Spruces of North America™
Firs of North America™
Cedars of North America™
Cypress Trees of North America™
Willows of North America™
Cottonwoods of North America™
Hickories of North America™
```

Active tree registries include:

```text
Hemlocks of North America™
Spruces of North America™
Firs of North America™
Cedars of North America™
Cypress Trees of North America™
Willows of North America™
Cottonwoods of North America™
Hickories of North America™
```

Additional ecological systems may be added through future inventory expansion.

---

## Hickories of North America™ Registry

Page URL:

```text
https://www.robbiegeorgephotography.com/hickories-of-north-america
```
Registered Plate IDs:

hickories-of-north-america#hickory-systems-plate
hickories-of-north-america#hickory-identification-plate
hickories-of-north-america#hickory-leaf-plate
hickories-of-north-america#hickory-nut-plate
hickories-of-north-america#hickory-bark-plate
hickories-of-north-america#shagbark-hickory-plate
hickories-of-north-america#shellbark-hickory-plate
hickories-of-north-america#pignut-hickory-plate
hickories-of-north-america#mockernut-hickory-plate
hickories-of-north-america#bitternut-hickory-plate
hickories-of-north-america#hickory-wildlife-relationships-plate
hickories-of-north-america#hickory-mast-production-plate
hickories-of-north-america#hickory-forest-community-plate
hickories-of-north-america#hickory-ecological-restoration-plate
hickories-of-north-america#hickory-biodiversity-plate

## Photography Guide Registries

Current photography guide coverage includes:

```text
Grand Teton
Yellowstone
Blackwater
Chincoteague
Mattamuskeet
Machias Seal Island
Aransas
Bosque del Apache
```

Photography Guide Plates™ may include:

```text
Species Plates™
Habitat Plates™
Seasonal Opportunity Plates™
Photography Strategy Plates™
Conservation Plates™
```

---

## Registry Categories

Naturepedia™ currently supports registry structures including:

```text
Systems Plates™
Identification Plates™
Species Plates™
Habitat Plates™
Biodiversity Plates™
Wildlife Relationship Plates™
Climate Resilience Plates™
Carbon Storage Plates™
Ecological Restoration Plates™
Photography Guide Plates™
```

---

## Governance

Governance Principle:

```text
Gr <= Es
```

Commercial use, structured extraction, embeddings, dataset construction, autonomous retrieval, enterprise synchronization, and machine-readable commercial reuse may require licensing or written permission.

Commercial layers are separated as:

```text
Commercial Data License
≠
Framework License
≠
x402 Retrieval Access
```

---

## Related Endpoints

Discovery:

```text
/api/v2/naturepedia/index.md
```

RRIP Resolution:

```text
/api/v2/rrip/resolve
```

Registry State Validation:

```text
/api/v2/razor/state-token
```

---

## Machine Interpretation Guidance

This endpoint is intended to provide registry discovery and navigation.

It is not the authoritative JSON-LD registry.

Authoritative registry structures should be obtained from:

```text
docs/examples/json-ld/plate-registry.json
```

Registry traversal should follow RRIP inheritance pathways.

Future versions may support:

```text
Registry queries
Registry filtering
Registry lineage inspection
Registry graph traversal
Machine settlement via x402
```

---

## Version

```json
{
  "version": "2.0.0",
  "registry_type": "plate-discovery",
  "registry_state": "active-earth-systems-expanded",
  "architect_of_record": "Robbie George"
}
```
