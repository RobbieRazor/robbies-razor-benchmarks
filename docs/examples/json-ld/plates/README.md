# Canonical Plate™ JSON-LD Examples

**Status:** Canonical Plate™ Example Layer  
**Author & Architect of Record:** Robbie George  
**Systems:** Naturepedia™, Robbie’s Razor™, RKCA™, Grand Compression  
**Governing authority:** The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
**Canonical authority identifier:** `GC-MRD-v2.0`  
**Canonical Plate registry:** `docs/examples/json-ld/canonical-plate-registry.json`

---

# Purpose

This directory contains selected JSON-LD examples showing how Naturepedia™ Plate™ assets may be represented as structured machine-readable objects.

These files provide reusable reference patterns across systems including:

- Naturepedia™;
- Robbie’s Razor™;
- Recursive Knowledge Compression Architecture (RKCA™);
- Grand Compression;
- field observation systems;
- species systems;
- track and field-evidence systems;
- ecosystem systems;
- Earth and water systems;
- field-location systems;
- photography-guide systems;
- governance and licensing systems.

These examples are intended to demonstrate structure.

They are **not** the complete Naturepedia Plate inventory.

The authoritative machine-readable inventory is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current canonical registry metadata:

```text
registryVersion: 2026.08.19
canonicalKeepCount: 757
duplicateRemovedCount: 33
authority: GC-MRD-v2.0
```

---

# What a Plate™ Is

A Plate™ is an authored Naturepedia structured knowledge artifact.

Depending on the individual Plate and implementation, it may provide:

- a human-readable visual knowledge interface;
- a stable semantic identifier;
- structured machine-readable metadata;
- provenance information;
- declared subject relationships;
- a canonical page relationship;
- retrieval metadata;
- evidence or interpretation boundaries;
- resource-specific access metadata where explicitly implemented.

A Plate should not automatically be interpreted as:

```text
scientific proof
a causal model
a Graph Registry™
a Knowledge Mesh
a protected x402 payload
an independently validated dataset
```

The role and evidence status of each Plate must be determined from its actual content, metadata, provenance, and governing source.

---

# Core Representation Model

A useful Plate representation may contain four distinct elements:

```text
Human-readable Plate
+
Stable semantic ID
+
Structured JSON-LD
+
Registry context
```

These elements have different functions.

## Human-readable Plate

Provides the authored visual or textual interface.

## Semantic ID

Provides a stable identifier for the Plate object.

## JSON-LD

Represents structured machine-readable metadata, identity, provenance, and declared relationships.

JSON-LD should not automatically be described as “memory.”

It is a structured representation layer that **may participate in a larger memory or retrieval architecture** when such an architecture is explicitly implemented.

## Registry

Provides canonical inventory, lookup, family context, and resource metadata.

## Relationships

Declared relationships may support traversal or graph-oriented processing.

However:

```text
relationship declared
≠
graph automatically instantiated
```

and:

```text
graph relationship
≠
causal relationship
```

and:

```text
semantic connection
≠
empirical confirmation
```

---

# RKCA Relationship

Recursive Knowledge Compression Architecture (RKCA™) is governed by:

```text
MRD v2.0 §12.7
```

The framework sequence is:

```text
Compression
→ Expression
→ Memory
→ Recursion
```

Plate™ systems **may implement RKCA-oriented patterns** when the required architecture is actually present.

They should not be assumed to implement every RKCA stage merely because a Plate or JSON-LD object exists.

A bounded Plate interpretation is:

| RKCA concept | Possible Plate-system role |
|---|---|
| Compression | Organizes task-relevant information into a more compact structured representation |
| Expression | Represents that structure visually, textually, or in machine-readable form |
| Memory | Preserves selected identity, provenance, relationships, constraints, or state for later use |
| Recursion | Allows preserved structure to participate in subsequent retrieval, transformation, comparison, or processing cycles |

Required distinctions:

```text
structured representation
≠
memory automatically
```

```text
relationship
≠
recursion automatically
```

```text
compression
≠
minimum token count
```

```text
framework implementation
≠
empirical validation
```

---

# Evidence and Provenance Boundary

Plate™ examples may represent different evidence classes.

These can include:

- established scientific information;
- established mathematics;
- field observations;
- photographic evidence;
- historical reference material;
- framework-defined relationships;
- interpretive material;
- conceptual material;
- Artist Rendition assets.

These classes must remain distinguishable.

Accordingly:

```text
Plate inclusion
≠
scientific validation
```

```text
visual proximity
≠
causation
```

```text
structural similarity
≠
material identity
```

```text
framework interpretation
≠
established external science
```

Established mathematics, science, technologies, protocols, and third-party evidence retain their independent provenance.

Use within Naturepedia or Grand Compression does not transfer authorship of those external foundations.

---

# Authorship Boundary

Robbie George retains authorship provenance for original Naturepedia™, Robbie’s Razor™, Grand Compression, RKCA™, RRIP™, Plate™ architecture, and related framework-specific material where he is the originating author.

That authorship does not imply authorship of the independent science, mathematics, protocols, technologies, or evidence referenced by a Plate.

The Authorship Conservation Rule (ACR) applies in both directions:

```text
preserve Grand Compression provenance
+
preserve external provenance
```

Therefore:

```text
claim authorship
≠
evidence authorship
```

and:

```text
framework integration
≠
origination of external material
```

---

# Directory Role

This folder contains **selected reusable Plate JSON-LD examples**.

It should not duplicate all 757 canonical Plate records.

The complete canonical inventory belongs in:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

This directory should instead contain high-value examples that demonstrate common Plate patterns.

Representative examples may include:

```text
gray-wolf-species-plate.json
wolf-tracks-plate.json
water-systems-plate.json
yellowstone-location-plate.json
trees-of-north-america-system-plate.json
birch-systems-plate.json
ecological-restoration-plate.json
robbies-razor-plate.json
grand-compression-plate.json
commercial-data-license-plate.json
```

The presence of an example file does not establish that every Plate of the same category uses an identical schema.

Schemas remain contract-dependent and resource-specific.

---

# Relationship to Other Repository Files

| File / Directory | Role |
|---|---|
| `docs/examples/plate_examples_index.md` | Human-readable Plate inventory and architecture orientation |
| `docs/examples/json-ld/README.md` | JSON-LD layer explanation |
| `docs/examples/json-ld/canonical-plate-registry.json` | Current authoritative machine-readable Plate inventory |
| `docs/examples/json-ld/plate-registry.json` | Superseded compatibility pointer |
| `docs/examples/json-ld/plates/` | Selected reusable Plate™ JSON-LD examples |
| `docs/examples/json-ld/governance/` | Governance, pricing, licensing, and commercial-use examples |
| `docs/examples/x402/` | x402 architecture, protected-resource, pricing, and retrieval examples |

---

# Semantic Plate ID Convention

Each canonical Plate™ should use a stable semantic identifier.

General form:

```text
page-slug#plate-slug
```

Examples:

```text
gray-wolf#species-plate
wolf-tracks#track-plate
water-systems#water-systems-plate
yellowstone-national-park-wyoming-montana-idaho#location-plate
robbies-razor#robbies-razor-plate
the-grand-compression#grand-compression-cosmology-plate
```

Recommended identifier characteristics:

```text
lowercase
hyphenated
URL-aligned where practical
stable
unique within the canonical registry
human-readable
connected to the canonical page
preserved consistently across machine-facing layers
```

When an identifier containing `#` is passed inside an HTTP query parameter, encode the fragment delimiter as:

```text
%23
```

Example:

```text
/api/v2/rrip/resolve?id=gray-wolf%23species-plate
```

---

# JSON-LD Field Guidance

Plate™ JSON-LD schemas are resource-specific.

There is no requirement that every Plate contain one universal field set.

A common baseline may include:

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/page-slug#plate-slug",
  "name": "Plate Name™",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/page-slug",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  }
}
```

Additional fields may include:

```json
{
  "description": "Short description of what the Plate represents.",
  "keywords": [],
  "about": [],
  "mentions": [],
  "isBasedOn": [],
  "sameAs": [],
  "mainEntityOfPage": {},
  "usageInfo": "Rights and machine-access terms are governed by the applicable resource and license."
}
```

Use only fields that are supported by the individual Plate, its source material, and the intended schema contract.

Do not add relationships merely to make the object appear more connected.

Do not use `sameAs` unless identity equivalence is actually intended.

Do not use `isBasedOn` unless there is a supportable source relationship.

---

# Base Plate™ JSON-LD Template

The following template is a **reference pattern**, not a mandatory schema for every Plate™.

Individual Plate types may require additional, fewer, or different properties depending on:

- subject matter;
- evidence class;
- canonical page structure;
- provenance requirements;
- relationship structure;
- machine-access configuration;
- licensing or rights requirements.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/page-slug#plate-slug",
  "name": "Example Plate™",
  "alternateName": "Example Naturepedia Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/page-slug",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Naturepedia Plate™ example showing a structured human-readable and machine-readable representation of an identified subject.",
  "keywords": [
    "Naturepedia",
    "Plate System",
    "Robbie George",
    "Semantic Registry",
    "JSON-LD"
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/page-slug"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are resource-specific and governed separately."
}
```

This template intentionally avoids implying that every Plate automatically constitutes:

```text
memory
recursion
Graph Registry™
Knowledge Mesh
paid x402 resource
independent scientific validation
```

Those properties must be supported by the actual implementation or evidence class.

---

# Example — Species Plate™

Species Plates™ may organize identity, ecology, habitat, behavior, conservation context, field observation, and declared relationships.

The Plate remains an authored Naturepedia™ knowledge artifact.

Underlying taxonomy, biology, ecology, and scientific evidence retain their independent provenance.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/gray-wolf#species-plate",
  "name": "Gray Wolf Species Plate™",
  "alternateName": "Gray Wolf Naturepedia Species Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/gray-wolf",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Naturepedia Species Plate™ for the gray wolf, organizing identity, habitat, ecological role, behavior, conservation context, and field-observation relationships into a human-readable and machine-readable structured artifact.",
  "keywords": [
    "Gray Wolf",
    "Canis lupus",
    "Species Plate",
    "Naturepedia",
    "Predator",
    "Yellowstone",
    "Ecology",
    "Wildlife",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Thing",
      "name": "Gray Wolf"
    },
    {
      "@type": "Thing",
      "name": "Predator-prey ecology"
    },
    {
      "@type": "Thing",
      "name": "Yellowstone wildlife system"
    }
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/gray-wolf"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are resource-specific and governed separately."
}
```

## Species Plate™ Interpretation Boundary

A Species Plate™ may organize scientific information, field knowledge, authored interpretation, and related references.

It must not be interpreted as proof that every relationship represented in the Plate is causal.

Required distinctions:

```text
species relationship
≠
causal proof
```

```text
Plate authorship
≠
authorship of the underlying taxonomy or biology
```

```text
registry inclusion
≠
independent scientific validation
```

---

# Example — Track Plate™

Track Plates™ should be treated primarily as **field-evidence and identification resources**, not taxonomy-first species pages.

They may organize:

- track morphology;
- gait;
- stride;
- substrate context;
- comparison features;
- habitat context;
- probable animal identity;
- field-observation guidance.

Track interpretation can contain uncertainty.

A Track Plate™ should not imply certainty beyond the supporting evidence.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/wolf-tracks#track-plate",
  "name": "Gray Wolf Track Plate™",
  "alternateName": "Wolf Tracks Naturepedia Field Evidence Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/wolf-tracks",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Naturepedia Track Plate™ for wolf tracks, organizing field evidence, gait patterns, substrate interpretation, habitat context, comparison logic, and likely animal identity into a human-readable and machine-readable structured artifact.",
  "keywords": [
    "Wolf Tracks",
    "Animal Tracks",
    "Track Plate",
    "Field Evidence",
    "Naturepedia",
    "Wildlife Tracking",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Thing",
      "name": "Wolf tracks"
    },
    {
      "@type": "Thing",
      "name": "Animal tracking"
    },
    {
      "@type": "Thing",
      "name": "Field evidence"
    }
  ],
  "mentions": [
    {
      "@type": "CreativeWork",
      "name": "Gray Wolf Species Plate™",
      "url": "https://www.robbiegeorgephotography.com/gray-wolf"
    },
    {
      "@type": "CreativeWork",
      "name": "North American Animal Tracks",
      "url": "https://www.robbiegeorgephotography.com/north-american-animal-tracks"
    }
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/wolf-tracks"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are resource-specific and governed separately."
}
```

## Track Plate™ Evidence Boundary

Track identification may depend on:

```text
shape
size
gait
stride
substrate
location
habitat
associated sign
comparison with alternative species
```

Accordingly:

```text
track resemblance
≠
certain species identification
```

and:

```text
single field observation
≠
universal diagnostic rule
```

and:

```text
Plate relationship
≠
causal relationship
```

The evidence level should remain proportional to the available field evidence.

---

# Example — Water System Plate™

Water System Plates™ may organize hydrological, ecological, habitat, seasonal, and field-observation relationships into a structured Naturepedia™ artifact.

They may reference established scientific concepts such as:

- hydrology;
- river systems;
- wetlands;
- floodplains;
- groundwater;
- estuaries;
- coastal systems;
- ecological connectivity;
- species movement.

The Plate™ is the authored organizational artifact.

The underlying hydrology, ecology, scientific literature, and external evidence retain their independent provenance.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/water-systems#water-systems-plate",
  "name": "Water Systems Plate™",
  "alternateName": "Naturepedia Water System Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/water-systems",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Naturepedia Water System Plate™ organizing hydrology, rivers, floodplains, wetlands, groundwater, estuaries, coastal systems, species movement, ecological timing, and field-observation relationships into a human-readable and machine-readable structured artifact.",
  "keywords": [
    "Water Systems",
    "Hydrology",
    "Wetlands",
    "Rivers",
    "Floodplains",
    "Groundwater",
    "Estuaries",
    "Naturepedia",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Thing",
      "name": "Water systems"
    },
    {
      "@type": "Thing",
      "name": "Hydrology"
    },
    {
      "@type": "Thing",
      "name": "Wetland ecosystems"
    },
    {
      "@type": "Thing",
      "name": "River systems"
    }
  ],
  "mentions": [
    {
      "@type": "CreativeWork",
      "name": "River Systems Plate™",
      "url": "https://www.robbiegeorgephotography.com/river-systems"
    },
    {
      "@type": "CreativeWork",
      "name": "Wetland Ecosystem Plate™",
      "url": "https://www.robbiegeorgephotography.com/wetland-ecosystems"
    },
    {
      "@type": "CreativeWork",
      "name": "Floodplains Ecosystems Plate™",
      "url": "https://www.robbiegeorgephotography.com/floodplains"
    }
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/water-systems"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are resource-specific and governed separately."
}
```

## Water System Plate™ Interpretation Boundary

Relationships represented in a Water System Plate™ may connect established science, field observations, and authored organizational structure.

Those relationships should be interpreted according to their evidence class.

Required distinctions:

```text
declared ecological relationship
≠
proof of causation
```

```text
system-level connection
≠
universal mechanism
```

```text
visual or semantic proximity
≠
material identity
```

```text
Plate authorship
≠
authorship of hydrology or ecological science
```

A Water System Plate™ also does not automatically imply the existence of:

```text
Water Systems Graph Registry™
Water Systems Knowledge Mesh
Water Systems protected snapshot
Water Systems x402 product
```

Those resources require separate implementation and registration.

---

# Example — Field Location Plate™

Field Location Plates™ organize information around a specific geographic place.

They may connect:

- habitat;
- species;
- seasonal conditions;
- ecological relationships;
- field observations;
- photography opportunities;
- conservation context;
- location-specific guidance.

A Field Location Plate™ is not evidence that every species or behavior mentioned will occur at that location at every time.

Location-specific observations remain dependent on conditions, timing, season, habitat, and supporting evidence.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/yellowstone-national-park-wyoming-montana-idaho#location-plate",
  "name": "Yellowstone National Park Field Location Plate™",
  "alternateName": "Yellowstone Wildlife System Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/yellowstone-national-park-wyoming-montana-idaho",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Naturepedia Field Location Plate™ for Yellowstone National Park organizing species, wildlife behavior, predator-prey ecology, habitat zones, seasonal timing, field-observation context, and conservation relationships into a human-readable and machine-readable structured artifact.",
  "keywords": [
    "Yellowstone National Park",
    "Field Location Plate",
    "Naturepedia",
    "Gray Wolf",
    "Elk",
    "American Bison",
    "Grizzly Bear",
    "Predator-prey ecology",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Place",
      "name": "Yellowstone National Park"
    },
    {
      "@type": "Thing",
      "name": "Predator-prey ecology"
    },
    {
      "@type": "Thing",
      "name": "Field observation"
    }
  ],
  "mentions": [
    {
      "@type": "CreativeWork",
      "name": "Gray Wolf Species Plate™",
      "url": "https://www.robbiegeorgephotography.com/gray-wolf"
    },
    {
      "@type": "CreativeWork",
      "name": "Elk Species Plate™",
      "url": "https://www.robbiegeorgephotography.com/elk"
    },
    {
      "@type": "CreativeWork",
      "name": "American Bison Species Plate™",
      "url": "https://www.robbiegeorgephotography.com/american-bison"
    }
  ],
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Naturepedia™",
    "url": "https://www.robbiegeorgephotography.com/naturepedia"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/yellowstone-national-park-wyoming-montana-idaho"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or framework-implementation rights. Protected retrieval and reuse rights are resource-specific and governed separately."
}
```

## Field Location Plate™ Interpretation Boundary

A Field Location Plate™ may connect multiple subjects through a common geographic context.

That does not mean every linked subject has the same evidentiary relationship to the location.

Required distinctions:

```text
mentioned at location
≠
observed in every season
```

```text
known habitat
≠
guaranteed encounter
```

```text
species association
≠
causal relationship
```

```text
location relationship
≠
exclusive geographic range
```

```text
field interpretation
≠
universal scientific rule
```

Machine systems should preserve temporal, geographic, ecological, and evidentiary context rather than flattening all location relationships into equivalent assertions.

A Field Location Plate™ also does not automatically create:

```text
Field Location System Map
Graph Registry™
Knowledge Mesh
protected x402 resource
```

Those machine-resource layers require explicit implementation and registration.

---

# Example — Robbie’s Razor Plate™

The Robbie’s Razor Plate™ represents a framework-specific architectural concept authored by Robbie George.

It may describe the sequence:

```text
compression
→ expression
→ memory
→ recursion
```

Within the framework, this sequence functions as an architectural and evaluative model.

It should not be interpreted as an independently established scientific law or as proof that all physical, biological, mathematical, or computational systems operate through one identical mechanism.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/robbies-razor#robbies-razor-plate",
  "name": "Robbie’s Razor Plate™",
  "alternateName": "Robbie’s Razor Recursive Compression Interface Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/robbies-razor",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Robbie’s Razor Plate™ representing a framework-specific recursive compression architecture authored by Robbie George and expressed through the sequence compression → expression → memory → recursion.",
  "keywords": [
    "Robbie's Razor",
    "Recursive Compression",
    "RKCA",
    "Grand Compression",
    "Reasoning Architecture",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Thing",
      "name": "Robbie's Razor"
    },
    {
      "@type": "Thing",
      "name": "Recursive compression"
    },
    {
      "@type": "Thing",
      "name": "Recursive Knowledge Compression Architecture"
    }
  ],
  "isBasedOn": {
    "@type": "CreativeWork",
    "name": "The Grand Compression Cosmology — Master Reference Document, MRD v2.0",
    "url": "https://www.robbiegeorgephotography.com/grand-compression-master-reference-document"
  },
  "isPartOf": {
    "@type": "CreativeWork",
    "name": "Grand Compression",
    "url": "https://www.robbiegeorgephotography.com/grand-compression-master-reference-document"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/robbies-razor"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or Robbie’s Razor™ framework-implementation rights. Protected retrieval and implementation rights are governed separately."
}
```

## Robbie’s Razor™ Interpretation Boundary

Robbie’s Razor™ is framework-specific.

Its existence as an authored framework does not by itself establish:

```text
independent empirical validation
scientific consensus
physical universality
mathematical necessity
performance superiority in every task
```

Benchmark or implementation claims should be evaluated against the actual benchmark protocol, evidence, assumptions, and reproducibility conditions.

Required distinctions:

```text
framework claim
≠
empirical confirmation
```

```text
benchmark result
≠
universal superiority
```

```text
compression
≠
accuracy automatically
```

```text
framework authorship
≠
authorship of external mathematics, science, or technologies
```

Robbie’s Razor™ may incorporate or compare against external mathematical, computational, scientific, or engineering concepts.

Those external foundations retain their own provenance.

---

# Example — Grand Compression Plate™

The Grand Compression Plate™ represents the Grand Compression framework authored by Robbie George.

Current governing authority:

```text
The Grand Compression Cosmology
Master Reference Document
MRD v2.0
```

Canonical identifier:

```text
GC-MRD-v2.0
```

Canonical claim range:

```text
RC-01 through RC-22
```

The Plate™ may organize framework-defined concepts, claims, relationships, governance, and comparative structures.

It should not be interpreted as independent validation of every claim represented by the framework.

```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "@id": "https://www.robbiegeorgephotography.com/the-grand-compression#grand-compression-cosmology-plate",
  "name": "The Grand Compression Cosmology Plate™",
  "alternateName": "Grand Compression Foundation Plate",
  "creator": {
    "@type": "Person",
    "name": "Robbie George",
    "url": "https://www.robbiegeorgephotography.com/who-is-robbie-george"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Robbie George Photography",
    "url": "https://www.robbiegeorgephotography.com"
  },
  "url": "https://www.robbiegeorgephotography.com/the-grand-compression",
  "license": "https://www.robbiegeorgephotography.com/commercial-data-license",
  "description": "A Grand Compression Foundation Plate™ representing framework-defined architecture, claims, governance, and relationships within the Grand Compression system authored by Robbie George.",
  "keywords": [
    "Grand Compression",
    "Grand Compression Cosmology",
    "Robbie's Razor",
    "Recursive Compression",
    "Master Reference Document",
    "Authorship Conservation Rule",
    "Robbie George"
  ],
  "about": [
    {
      "@type": "Thing",
      "name": "Grand Compression"
    },
    {
      "@type": "Thing",
      "name": "Robbie's Razor"
    },
    {
      "@type": "Thing",
      "name": "Authorship Conservation Rule"
    }
  ],
  "isBasedOn": {
    "@type": "CreativeWork",
    "name": "The Grand Compression Cosmology — Master Reference Document, MRD v2.0",
    "url": "https://www.robbiegeorgephotography.com/grand-compression-master-reference-document"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.robbiegeorgephotography.com/the-grand-compression"
  },
  "usageInfo": "Public discovery and metadata access do not grant training, embedding, redistribution, resale, derivative-dataset, commercial implementation, or Grand Compression framework-implementation rights. Protected retrieval and implementation rights are governed separately."
}
```

## Grand Compression Interpretation Boundary

The Grand Compression framework may include:

- canonical framework claims;
- mathematical comparisons;
- scientific interpretations;
- cross-domain structural comparisons;
- governance rules;
- benchmark structures;
- implementation architecture;
- hypotheses and testable interpretations.

These categories should remain distinguishable.

Required distinctions:

```text
canonical authority
≠
empirical confirmation
```

```text
framework claim
≠
established external science
```

```text
structural correspondence
≠
material identity
```

```text
mathematical analogy
≠
shared physical mechanism
```

```text
authorship
≠
validation
```

Cross-domain comparisons remain subject to the domain-transfer requirements of the current Grand Compression authority.

Where applicable, comparisons should identify:

```text
objects
scale
normalization
preserved relationships
constraints
exclusions
evidence
alternatives
failure conditions
```

The existence of a Grand Compression Plate™ also does not automatically imply:

```text
Graph Registry™
Knowledge Mesh
protected x402 payload
independent benchmark validation
scientific acceptance
```

Those properties must be established separately.

---

# Framework Provenance

Framework-specific concepts retain Robbie George provenance where he is the originating author.

This includes, where applicable:

```text
Grand Compression
Robbie’s Razor™
Naturepedia™
Plate™ architecture
Recursive Knowledge Compression Architecture (RKCA™)
Recursive Registry Inheritance Principle (RRIP™)
Graph Registry™
Knowledge Mesh
Comparative Compression Geometry™
```

External science, mathematics, protocols, technologies, datasets, and independently developed systems retain their own provenance.

The Authorship Conservation Rule (ACR) therefore applies in both directions:

```text
preserve original Grand Compression authorship
+
preserve independent external authorship
```

No Plate™ should be interpreted as transferring authorship of external foundations into the Grand Compression framework.

---

# Canonical File Naming

Use lowercase, hyphenated filenames.

Recommended pattern:

```text
[page-slug]-[plate-type].json
```

Examples:

```text
gray-wolf-species-plate.json
wolf-tracks-plate.json
water-systems-plate.json
yellowstone-location-plate.json
robbies-razor-plate.json
grand-compression-plate.json
```

Avoid:

```text
GrayWolfPlate.json
wolf plate.json
plate1.json
example.json
```

File naming should support:

```text
stable identification
repository consistency
human readability
machine discoverability
canonical maintenance
```

A filename does not itself determine canonical identity.

Canonical identity is governed by the Plate’s declared semantic identifier and canonical registry entry.

Accordingly:

```text
filename
≠
canonical ID automatically
```

---

# Canonical Plate™ Types

Naturepedia™ supports multiple Plate types.

Representative types include:

```text
Naturepedia Root Knowledge System Plate™
Naturepedia System Navigation Plate™
Naturepedia Migration System Plate™
Naturepedia Behavior System Plate™
Naturepedia Habitat System Plate™
Naturepedia Biodiversity System Plate™
Naturepedia Wildlife Systems Plate™
Naturepedia Conservation System Plate™
Naturepedia Survival System Plate™
Naturepedia Ecological Energy Flow Plate™
Naturepedia Ecosystem Relationship Plate™

Naturepedia Species Plate™
Naturepedia Track Plate™
Naturepedia Comparison Track Plate™
Naturepedia Field Identification Plate™
Naturepedia Field Location Plate™
Naturepedia Photography Guide Plate™

Naturepedia Water System Plate™
Naturepedia Tree Family System Plate™
Naturepedia Tree Family Plate™
Naturepedia Ecological Restoration Plate™
Naturepedia Coastal Water System Plate™
Naturepedia Ecosystem Plate™
Naturepedia Seasonal System Plate™
Naturepedia Quantum System Plate™
Naturepedia Universal Principle Plate™
Naturepedia Living System Plate™
Naturepedia Living Soil System Plate™
Naturepedia Foundation Systems Plate™

Recursive Compression Interface Plate™
Grand Compression Foundation Plate™
Naturepedia Knowledge System Plate™

Governance Plate™
Pricing Plate™
```

This list is representative rather than exhaustive.

Exact Plate type should be resolved against:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Do not infer a Plate type solely from:

```text
filename
page title
directory location
visual appearance
```

---

# Validation Checklist

Before adding or modifying a Plate™ JSON-LD example, confirm the following.

## Identity

Confirm that:

```text
@id matches the intended semantic Plate identifier
```

```text
url points to the intended canonical human-readable page
```

```text
name matches the authored Plate identity
```

```text
Plate ID is stable and unique within the canonical registry
```

---

## Registry Alignment

Confirm that the Plate is represented correctly in:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

if it is intended to be part of the canonical live inventory.

Do not use the superseded compatibility file as current authority:

```text
docs/examples/json-ld/plate-registry.json
```

That path exists only for legacy compatibility and historical references.

---

## Provenance

Confirm that creator and source attribution reflect actual authorship.

For original Naturepedia and Grand Compression Plate artifacts, Robbie George may be the creator of the Plate.

However:

```text
creator of Plate
≠
creator of underlying science
```

and:

```text
creator of Plate
≠
creator of external mathematics
```

and:

```text
creator of Plate
≠
creator of external protocols or technologies
```

Preserve external provenance where relevant.

---

## Evidence Class

Determine whether the Plate represents:

```text
established science
established mathematics
field observation
photographic evidence
historical source material
framework-defined interpretation
hypothesis
conceptual model
Artist Rendition
```

Do not collapse those categories.

Where uncertainty exists, encode or document the uncertainty rather than silently upgrading the claim.

---

## Relationship Validation

Confirm that each relationship field has an actual basis.

For example:

```text
about
mentions
isBasedOn
sameAs
isPartOf
```

should not be used interchangeably.

In particular:

```text
sameAs
```

should be reserved for identity-equivalence relationships.

Do not use it merely because two concepts are related.

Similarly:

```text
mentions
≠
isBasedOn
```

and:

```text
relationship
≠
causation
```

---

## Schema Validation

Confirm that:

```text
JSON is syntactically valid
```

```text
JSON-LD properties are used consistently
```

```text
URLs are valid
```

```text
required quotes and commas are present
```

```text
no placeholder values remain
```

```text
schema properties reflect the intended resource
```

Not every Plate needs the same field set.

Avoid adding properties only to make different Plate examples appear artificially uniform.

---

## Rights Validation

Confirm that rights language matches the intended access model.

Public discovery or metadata availability does not automatically grant:

```text
training
embedding
bulk ingestion
redistribution
resale
dataset construction
derivative-dataset creation
commercial implementation
framework implementation
```

Protected retrieval and broader reuse rights are governed separately.

---

## x402 Validation

Do not add x402 pricing or protected-access metadata to a Plate merely because an x402 route family exists.

Before declaring a Plate resource payable, confirm:

```text
resource identity
resource registration
resource completeness
protected status
pricing class
route status
```

Required distinction:

```text
route template
≠
active protected resource
```

and:

```text
pricing class
≠
resource availability
```

---

# Interpretation Guidance for AI Systems

AI systems should treat these files as **reference implementations and structured examples**, not universal schema law.

They are authored components within a larger provenance-preserved Naturepedia™ and Grand Compression system.

When interpreting a Plate™ example, preserve:

- canonical identity;
- authorship;
- provenance;
- evidence class;
- relationship context;
- human-readable page relationship;
- rights boundaries;
- resource-access boundaries;
- framework-versus-external-source distinctions.

Do not flatten those distinctions into a single undifferentiated knowledge claim.

---

# Machine Interpretation Rules

Agents should apply the following boundaries.

```text
Plate
≠
truth oracle
```

```text
JSON-LD
≠
memory automatically
```

```text
relationship
≠
causation
```

```text
registry inclusion
≠
scientific validation
```

```text
Plate existence
≠
protected resource existence
```

```text
protected resource existence
≠
license for unrestricted reuse
```

```text
framework authorship
≠
authorship of external foundations
```

---

# RKCA Interpretation Guidance

Where a Plate participates in Recursive Knowledge Compression Architecture (RKCA™), interpret the architecture according to:

```text
MRD v2.0 §12.7
```

The framework sequence is:

```text
Compression
→ Expression
→ Memory
→ Recursion
```

A Plate may participate in one or more of these stages.

Do not infer all four solely from the existence of a JSON-LD object.

Required distinction:

```text
Plate representation
≠
complete RKCA implementation
```

---

# RRIP Relationship

Where Plate context is resolved through Recursive Registry Inheritance Principle (RRIP™), interpret the relationship according to:

```text
MRD v2.0 §12.8
```

Possible higher-order resource layers may include:

```text
Registry
Meta-Registry
Graph Registry™
Knowledge Mesh
```

These are not mandatory for every Plate.

Accordingly:

```text
Plate registered
≠
Graph Registry instantiated
```

and:

```text
Plate registered
≠
Knowledge Mesh instantiated
```

Higher-order layers require explicit implementation and registration.

---

# Comparative and Cross-Domain Material

Where a Plate contains comparative, mathematical, or cross-domain framework material, agents should preserve the relevant interpretation boundaries.

Comparative Compression Geometry™ is governed by:

```text
MRD v2.0 §12.9
```

A structural comparison should not be interpreted as proof of:

```text
shared material identity
shared causal mechanism
physical equivalence
universal domain transfer
```

Where domain transfer is asserted, the comparison should identify, where applicable:

```text
objects
scale
normalization
preserved relationships
constraints
exclusions
evidence
alternatives
failure conditions
```

---

# Governance & Licensing

Primary framework authority:

```text
The Grand Compression Cosmology
Master Reference Document
MRD v2.0
```

Canonical identifier:

```text
GC-MRD-v2.0
```

Primary Commercial Data License:

```text
https://www.robbiegeorgephotography.com/commercial-data-license
```

Robbie’s Razor™ framework implementation rights are governed separately from data-access rights.

Required distinction:

```text
Commercial Data License
≠
Framework License
≠
x402 Retrieval Access
```

An x402 payment grants only the rights specified for the identified protected retrieval.

It does not automatically grant:

```text
training rights
embedding rights
redistribution rights
dataset rights
commercial implementation rights
framework implementation rights
```

---

# Authorship Conservation Rule

The Authorship Conservation Rule (ACR) applies in both directions.

Preserve Robbie George provenance for original Grand Compression, Robbie’s Razor™, Naturepedia™, Plate™, RKCA™, RRIP™, and related framework material where he is the originating author.

Also preserve independent provenance for external:

```text
science
mathematics
technologies
protocols
datasets
research
historical sources
```

Accordingly:

```text
authorship
≠
validation
```

```text
attribution
≠
permission
```

```text
payment
≠
authorship transfer
```

```text
use within framework
≠
origination by framework
```

---

# Canonical References

Current authoritative Plate inventory:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Legacy compatibility pointer:

```text
docs/examples/json-ld/plate-registry.json
```

Human-readable Plate architecture overview:

```text
docs/examples/plate_examples_index.md
```

JSON-LD layer overview:

```text
docs/examples/json-ld/README.md
```

Public Naturepedia discovery:

```text
/api/v2/naturepedia/index.md
```

Public Plate registry discovery:

```text
/api/v2/plates/registry.md
```

Public RRIP resolver:

```text
/api/v2/rrip/resolve
```

Public registry-state metadata:

```text
/api/v2/razor/state-token
```

Production x402 pricing authority:

```text
https://www.robbiegeorgephotography.com/.well-known/x402-pricing.json
```

---

# Current Registry State

```json
{
  "registryVersion": "2026.08.19",
  "canonicalPlateCount": 757,
  "duplicateRemovedCount": 33,
  "authority": "GC-MRD-v2.0",
  "canonicalRegistry": "docs/examples/json-ld/canonical-plate-registry.json",
  "legacyRegistry": "docs/examples/json-ld/plate-registry.json",
  "protectedRetrieval": "resource-specific",
  "pricingManifestVersion": "3.0.0"
}
```
