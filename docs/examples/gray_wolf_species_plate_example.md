# Gray Wolf Species Plate™ Example

**Status:** Example Implementation — Naturepedia Species Plate™  
**Author & Originator:** Robbie George  
**System:** Naturepedia / Recursive Knowledge Compression Architecture (RKCA)  
**Plate Type:** Species Plate  
**Subject:** Gray Wolf (*Canis lupus*)

---

## 1. Overview

This document provides a real implementation example of a **Naturepedia Species Plate™** using the Gray Wolf Species Plate™.

The Gray Wolf Plate™ demonstrates how a Plate functions as a **Recursive Compression Interface (RCI)** within the **Recursive Knowledge Compression Architecture (RKCA)**.

It converts gray wolf knowledge into:

- human-readable visual structure
- machine-readable semantic structure
- reusable ecological knowledge
- recursive Naturepedia graph connections

---

## 2. Live Plate

Website implementation:

https://www.robbiegeorgephotography.com/naturepedia

Plate image:

https://d15yhgn2ui21mw.cloudfront.net/production/3790/MDAwMDAwMDAwMDAw7QGraePd6CACehR_ZcfBFYwXu2FyveAYEUnRGwCTQQQLtneRwWETeR63PcJYcyCo7L3wiuOGn-kt3KDxISuxlEEZsG0dKuFccjsgzQqsAoHDR379gMP1OXDeLHXrvjKkFq-lb4wqeKaEiSJPYN5tNzJpWWieetrhAWLSY0IMv5CAEyYwOf8gqdxSUPCpQ-sEgt0ui7VdWkww9KWvSKevmSdShfOsIeuIRUwZ4Ab9Pe8x58FqVTqEh784cosrHhQ3z8mMXsEQDzSU8GINzIf4EkwhKvNt-FQ8EOMDr11HO8qu-cFAvht2G_ljD2nOEi7QRGqzSZXf4pEgrEPboQ.png

---

## 3. Plate Schema Mapping

### 3.1 Metadata Layer

```json
{
  "plate_id": "gray_wolf_species_plate",
  "plate_type": "species",
  "title": "Gray Wolf Species Plate™",
  "author": "Robbie George",
  "system": "Naturepedia | RKCA",
  "version": "1.0"
}
```
### 3.2 Compression Layer

```json
{
  "core_entities": [
    "Gray Wolf",
    "Canis lupus",
    "Pack Structure",
    "Habitat",
    "Diet",
    "Adaptations",
    "Ecological Role",
    "Conservation Status"
  ],
  "key_variables": [
    "territory",
    "pack behavior",
    "prey availability",
    "habitat range",
    "human conflict",
    "ecosystem balance"
  ],
  "system_summary": "The Gray Wolf Species Plate compresses gray wolf identity, behavior, diet, adaptations, habitat, threats, conservation status, and ecological role into a single structured wildlife knowledge node."
}
```
### 3.3 Expression Layer

```json
{
  "visual_structure": "Annotated Naturepedia field-guide plate with gray wolf imagery, species identity, diet icons, adaptation panels, habitat range, threat summary, ecological role, and conservation context.",
  "patterns": [
    "apex predator",
    "pack-based social structure",
    "opportunistic carnivore",
    "large-range habitat use",
    "ecological regulation of prey populations"
  ],
  "relationships": [
    "Gray Wolf regulates prey populations",
    "Pack structure supports cooperative hunting",
    "Habitat range affects conservation pressure",
    "Human conflict influences wolf conservation outcomes"
  ]
}
```
### 3.4 Memory Layer

```json
{
  "entities": [
    {
      "name": "Gray Wolf",
      "type": "species",
      "properties": {
        "scientific_name": "Canis lupus",
        "ecological_role": "apex predator",
        "diet": "opportunistic carnivore",
        "social_structure": "pack"
      }
    },
    {
      "name": "Pack Structure",
      "type": "behavioral_system",
      "properties": {
        "function": "cooperative hunting, territory defense, social bonding"
      }
    },
    {
      "name": "Habitat",
      "type": "ecological_context",
      "properties": {
        "range": "North America, Europe, and Asia",
        "habitat_types": "forests, tundra, mountains, grasslands, deserts"
      }
    }
  ],
  "relationships": [
    {
      "source": "Gray Wolf",
      "target": "Pack Structure",
      "type": "uses"
    },
    {
      "source": "Gray Wolf",
      "target": "Habitat",
      "type": "occupies"
    },
    {
      "source": "Gray Wolf",
      "target": "Prey Populations",
      "type": "regulates"
    }
  ]
}
```
### 3.5 Recursion Layer

```json
{
  "related_plates": [
    "wolf_track_plate"
  ],
  "parent_systems": [
    "Naturepedia",
    "Naturepedia Species Plates™",
    "Recursive Knowledge Compression Architecture"
  ],
  "child_systems": [
    "gray_wolf_diet",
    "gray_wolf_pack_behavior",
    "gray_wolf_habitat",
    "gray_wolf_conservation"
  ],
  "cross_domain_links": [
    "https://www.robbiegeorgephotography.com/naturepedia",
    "https://www.robbiegeorgephotography.com/seasonal-wildlife-calendar",
    "https://www.robbiegeorgephotography.com/field-tools",
    "https://www.robbiegeorgephotography.com/yellowstone-wildlife-photography-guide",
    "https://www.robbiegeorgephotography.com/grand-teton-wildlife-photography-guide",
    "https://www.robbiegeorgephotography.com/winter-wildlife-snow-photography",
    "https://www.robbiegeorgephotography.com/spring-wildlife-nature-photography"
  ]
}
```
## 4. JSON-LD Implementation

The website implementation should include a JSON-LD block immediately after the visible Gray Wolf Species Plate™.

<!-- 🤖 MACHINE-READABLE SPECIES PLATE DATA — Gray Wolf Species Plate™ -->

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/naturepedia#gray-wolf-species-plate",
  "name": "Gray Wolf Species Plate™",
  "alternateName": "Naturepedia Gray Wolf Plate",
  "headline": "Gray Wolf Species Plate™ — Canis lupus",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/nature-photographer"
  },
  "author": {
    "@type": "Person",
    "name": "Robbie George"
  },
  "isPartOf": {
    "@type": "CreativeWorkSeries",
    "name": "Naturepedia Species Plates™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "about": {
    "@type": "Taxon",
    "name": "Canis lupus",
    "alternateName": "Gray Wolf",
    "taxonRank": "Species"
  },
  "image": "https://d15yhgn2ui21mw.cloudfront.net/production/3790/MDAwMDAwMDAwMDAw7QGraePd6CACehR_ZcfBFYwXu2FyveAYEUnRGwCTQQQLtneRwWETeR63PcJYcyCo7L3wiuOGn-kt3KDxISuxlEEZsG0dKuFccjsgzQqsAoHDR379gMP1OXDeLHXrvjKkFq-lb4wqeKaEiSJPYN5tNzJpWWieetrhAWLSY0IMv5CAEyYwOf8gqdxSUPCpQ-sEgt0ui7VdWkww9KWvSKevmSdShfOsIeuIRUwZ4Ab9Pe8x58FqVTqEh784cosrHhQ3z8mMXsEQDzSU8GINzIf4EkwhKvNt-FQ8EOMDr11HO8qu-cFAvht2G_ljD2nOEi7QRGqzSZXf4pEgrEPboQ.png",
  "description": "A Naturepedia Species Plate™ for the gray wolf, compressing identity, diet, adaptations, habitat, ecological role, threats, conservation status, and field-to-fine-art context into a human-readable and machine-readable knowledge node.",
  "keywords": [
    "Gray Wolf",
    "Canis lupus",
    "Naturepedia Species Plate",
    "wolf ecology",
    "wolf habitat",
    "wolf diet",
    "wolf conservation",
    "apex predator",
    "Robbie George",
    "Recursive Knowledge Compression Architecture",
    "Recursive Compression Interface"
  ],
  "learningResourceType": "Species Plate",
  "educationalUse": "wildlife education, ecological systems, field identification, AI-readable knowledge graph",
  "copyrightHolder": {
    "@type": "Person",
    "name": "Robbie George"
  },
  "copyrightNotice": "Gray Wolf Species Plate™ and Naturepedia Species Plates™ originate with Robbie George.",
  "mainEntity": {
    "@type": "Thing",
    "name": "Gray Wolf",
    "alternateName": "Canis lupus",
    "description": "A highly social apex predator that helps maintain healthy ecosystems by regulating prey populations and influencing trophic dynamics."
  },
  "relatedLink": [
    "https://www.robbiegeorgephotography.com/naturepedia",
    "https://www.robbiegeorgephotography.com/seasonal-wildlife-calendar",
    "https://www.robbiegeorgephotography.com/field-tools",
    "https://www.robbiegeorgephotography.com/yellowstone-wildlife-photography-guide",
    "https://www.robbiegeorgephotography.com/grand-teton-wildlife-photography-guide",
    "https://www.robbiegeorgephotography.com/winter-wildlife-snow-photography",
    "https://www.robbiegeorgephotography.com/spring-wildlife-nature-photography"
  ]
}
</script>
```

## 5. Canonical Interpretation

This Gray Wolf Species Plate™ demonstrates the Plate architecture:

RKCA Layer	Gray Wolf Implementation
Compression	Species identity, diet, habitat, adaptations, threats, ecological role
Expression	Visual field-guide plate
Memory	JSON / JSON-LD machine-readable structure
Recursion	Links to Naturepedia, seasons, field locations, habitats, and related plates
6. Attribution

Gray Wolf Species Plate™, Naturepedia Species Plates™, Recursive Knowledge Compression Architecture, Recursive Compression Interfaces, and Plates™ originate with Robbie George.

All use is governed by the Authorship Conservation Rule (ACR)
