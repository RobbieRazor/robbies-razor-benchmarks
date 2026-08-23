# Master Naturepedia Registry Reconciliation™
## Historical Registry Reconciliation Record

**Status:** Historical / Completed Registry-Reconciliation Working Record  
**Author & Architect of Record:** Robbie George  
**Current governing framework:** The Grand Compression Cosmology — Master Reference Document, MRD v2.0  
**Canonical identifier:** `GC-MRD-v2.0`  
**Current inventory authority:** `docs/examples/json-ld/canonical-plate-registry.json`

---

# Current Status Notice

This document preserves the historical reconciliation process used to classify and reconcile Naturepedia™ Plate assets across earlier registry, discovery, Worker, and documentation surfaces.

It is **not the current authoritative machine-readable Plate inventory**.

The current canonical machine-readable registry is:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

Current canonical registry metadata records:

```text
registryVersion: 2026.08.19
canonicalKeepCount: 757
duplicateRemovedCount: 33
```

The historical classifications and family lists below remain useful as provenance and audit material.

Required distinction:

```text
historical reconciliation record
≠
current canonical inventory
```

---

# Purpose

This document is retained to preserve the reconciliation process among historical resources including:

- `MasterPlateList.txt`
- `master-naturepedia-plate-census.md`
- earlier Plate registry files
- `llms.txt`
- `llms-full.txt`
- Cloudflare Worker registry state
- repository documentation
- human-readable Plate indexes
- historical x402 documentation

Its purpose is now:

```text
historical audit
+
reconciliation provenance
```

rather than:

```text
current production authority
```

When exact current Plate identity or inventory state is required, resolve against:

```text
docs/examples/json-ld/canonical-plate-registry.json
```

---

# Authority Hierarchy

For current interpretation:

```text
MRD v2.0
↓
Canonical Claims Register
↓
Repository authority / doctrine
↓
Canonical machine-readable Plate registry
↓
Human-readable indexes
↓
Historical census / reconciliation records
```

This document belongs to the final category.

It does not override the current canonical registry.

---

# Historical Reconciliation Rules

The historical reconciliation process classified source assets into categories including:

1. KEEP
2. DUPLICATE
3. SUPERSEDED
4. ARTIST RENDITION
5. DRAFT

The purpose of those categories was inventory reconciliation.

They should not be confused with:

- scientific evidence state;
- machine-resource availability;
- payment eligibility;
- licensing status;
- Graph Registry™ membership;
- RRIP™ inheritance;
- Knowledge Mesh membership.

---

# Classification Boundary

Required distinctions:

```text
KEEP
≠
scientifically validated
```

```text
KEEP
≠
paid resource automatically
```

```text
KEEP
≠
RRIP object automatically
```

```text
KEEP
≠
Graph Registry node automatically
```

```text
KEEP
≠
Knowledge Mesh node automatically
```

The historical census classification answers:

```text
Was this asset retained in the Plate inventory at that reconciliation stage?
```

It does not answer:

```text
What current machine products exist for it?
```

---

# KEEP

Historical definition:

A `KEEP` classification identifies a Plate that the reconciliation process determined should remain part of the canonical Naturepedia™ Plate collection.

Examples may include:

- system Plates™;
- species Plates™;
- track Plates™;
- field-location Plates™;
- photography-guide Plates™;
- governance Plates™;
- framework Plates™;
- relationship Plates™;
- other retained Plate families.

A `KEEP` Plate may be eligible for inclusion in appropriate discovery or registry surfaces.

However, every downstream status must be resolved independently.

Do **not** infer:

```text
KEEP
→ Worker paid payload
```

```text
KEEP
→ x402 resource
```

```text
KEEP
→ RRIP relationship
```

```text
KEEP
→ Graph Registry membership
```

```text
KEEP
→ Knowledge Mesh membership
```

Current resource existence requires explicit implementation and registration.

---

# Current Machine-Resource Boundary

For a current machine resource, resolve separately:

```text
Plate identity
↓
current registry membership
↓
resource implementation
↓
availability
↓
access class
↓
pricing if protected
```

Current protected-resource behavior is:

```text
unknown
→ 404
→ no payment challenge
```

```text
known but incomplete
→ 409
→ no payment challenge
```

```text
registered + complete + protected
→ eligible 402
```

Historical `KEEP` status alone is insufficient to reach the final state.

---

# Current x402 Boundary

A Plate retained in the canonical inventory does not automatically have:

- an Atomic Query;
- a Structured Plate™ payload;
- a `$5` Registry or System Map product;
- a `$25` Knowledge Mesh or snapshot product.

Required distinction:

```text
canonical Plate
≠
paid machine resource
```

Production pricing and availability are governed separately.

---

# RKCA / RRIP Boundary

Current canonical orientations include:

```text
MRD v2.0 §12.7
→ Recursive Knowledge Compression Architecture (RKCA™)

MRD v2.0 §12.8
→ Recursive Registry Inheritance Principle (RRIP™)

MRD v2.0 §12.9
→ Comparative Compression Geometry™ (CCG)
```

A possible RKCA architecture may include:

```text
Plate™
→ Registry
→ Meta-Registry
→ Graph Registry™
→ Knowledge Mesh
```

But historical Plate retention does not prove that every higher-order layer exists.

Required rule:

```text
Plate retained
≠
higher-order resource instantiated
```

---

# Evidence Boundary

Inventory reconciliation is not scientific evaluation.

A retained Plate may contain:

- established external knowledge;
- field observations;
- framework interpretation;
- hypotheses;
- canonical Grand Compression claims;
- visual or conceptual material.

Those components retain their own evidence classifications.

Required distinction:

```text
inventory state
≠
evidence state
```

---

# Artist Rendition Boundary

Historical `ARTIST RENDITION` classification indicates an authored conceptual or illustrative representation.

It does not independently establish:

- causal relationships;
- scientific support;
- universality;
- material identity.

Visual interpretation remains separate from evidentiary support.

---

# Duplicate and Supersession Boundary

Historical:

```text
DUPLICATE
```

and:

```text
SUPERSEDED
```

classifications preserve reconciliation history.

They should not be rewritten merely because the current canonical registry has evolved.

Historical classification records are useful provenance.

---

# Current Count Boundary

The current canonical machine registry records:

```text
canonicalKeepCount: 757
duplicateRemovedCount: 33
```

Future registry versions may supersede these values.

Agents should therefore prefer:

```text
latest canonical registry metadata
```

over:

```text
hard-coded counts in historical reconciliation documents
```

---

# Authorship Conservation Rule

Current governance terminology is:

```text
Authorship Conservation Rule (ACR)
```

ACR preserves provenance in both directions:

```text
Grand Compression framework material
→ preserve Grand Compression authorship
```

```text
external mathematics / science
→ preserve external provenance
```

```text
independent evidence
→ preserve evaluator provenance
```

Historical reconciliation does not transfer authorship of underlying external knowledge.

---

# Agent Interpretation Guidance

Agents reading the family inventories below should:

1. Treat `KEEP`, `DUPLICATE`, `SUPERSEDED`, `ARTIST RENDITION`, and `DRAFT` as historical reconciliation classifications.
2. Preserve the historical lists rather than silently modernizing them.
3. Resolve current Plate existence against the canonical machine-readable registry.
4. Resolve current machine-resource availability separately.
5. Resolve RRIP, Graph Registry, and Knowledge Mesh relationships separately.
6. Resolve x402 payment eligibility separately.
7. Preserve evidence and provenance boundaries.

The governing interpretation is:

```text
historical reconciliation
→ provenance

canonical registry
→ current inventory

resource registry / Worker
→ current machine availability
```

---

## KEEP — Major Naturepedia Families

### Trees of North America™

KEEP

* Tree Systems Plate™
* Tree Intelligence Plate™
* Tree Communities Plate™
* Tree Life Cycle Plate™
* Tree Mycelial Network Plate™
* Tree Pollinator Relationship Plate™
* Tree Watershed Connection Plate™
* Tree Wildlife Shelter Plate™
* Wildlife Tree Relationships Plate™

---

### Aspen Systems™

KEEP

* Aspen Systems Plate™
* Aspen Identification Plate™
* Aspen Leaf Plate™
* Aspen Bark Plate™
* Aspen Clonal Colony Plate™
* Aspen Forest Succession Plate™
* Aspen Wildlife Relationships Plate™
* Aspen Biodiversity Plate™
* Aspen Carbon Storage Plate™
* Aspen Wildfire Recovery Plate™
* Bigtooth Aspen Plate™
* Quaking Aspen Plate™

---

### Birch Systems™

KEEP

* Birch Identification Plate™
* Birch Bark & Leaf Plate™
* Birch Mycelial Network Plate™
* Birch Seasonal Ecology Plate™
* Birch Wetland Edge Plate™
* Birch Wildlife Relationships Plate™
* Paper Birch Plate™
* River Birch Plate™
* Yellow Birch Plate™

### Cedar Systems™

KEEP

* Cedar Systems Plate™
* Cedar Identification Plate™
* Cedar Leaf Plate™
* Cedar Cone Plate™
* Cedar Bark Plate™
* Cedar Swamp Forest Plate™
* Cedar Wildlife Relationships Plate™
* Cedar Forest Community Plate™
* Cedar Carbon Storage Plate™
* Cedar Climate Resilience Plate™
* Eastern Red Cedar Plate™
* Northern White Cedar Plate™
* Western Red Cedar Plate™
* Incense Cedar Plate™

### Cypress Systems™

KEEP

* Cypress Systems Plate™
* Cypress Identification Plate™
* Cypress Leaf Plate™
* Cypress Cone Plate™
* Cypress Bark & Knee Plate™
* Cypress Swamp Forest Plate™
* Cypress Wildlife Relationships Plate™
* Cypress Forest Community Plate™
* Cypress Carbon Storage Plate™
* Cypress Climate Resilience Plate™
* Cypress Water Storage Plate™
* Bald Cypress Plate™
* Pond Cypress Plate™
* Monterey Cypress Plate™
* Arizona Cypress Plate™
* Atlantic White Cedar Plate™

### Hemlock Systems™

KEEP

* Hemlock Systems Plate™
* Hemlock Identification Plate™
* Hemlock Needle Plate™
* Hemlock Cone Plate™
* Hemlock Bark Plate™
* Hemlock Stream Ecology Plate™
* Hemlock Wildlife Relationships Plate™
* Hemlock Forest Community Plate™
* Hemlock Carbon Storage Plate™
* Hemlock Conservation Plate™
* Eastern Hemlock Plate™
* Western Hemlock Plate™
* Mountain Hemlock Plate™
* Carolina Hemlock Plate™

### Fir Systems™

KEEP

* Fir Systems Plate™
* Fir Identification Plate™
* Fir Needle Plate™
* Fir Cone Plate™
* Fir Bark Plate™
* Fir Mountain Forest Plate™
* Fir Wildlife Relationships Plate™
* Fir Snowpack Ecology Plate™
* Fir Forest Community Plate™
* Fir Carbon Storage Plate™
* Fir Climate Resilience Plate™
* Balsam Fir Plate™
* Fraser Fir Plate™
* Noble Fir Plate™
* Subalpine Fir Plate™
* Grand Fir Plate™

### Cottonwood Systems™

KEEP

* Cottonwood Systems Plate™
* Cottonwood Identification Plate™
* Cottonwood Leaf Plate™
* Cottonwood Seed Plate™
* Cottonwood Bark Plate™
* Cottonwood River Systems Plate™
* Cottonwood Wildlife Relationships Plate™
* Cottonwood Floodplain Forest Plate™
* Cottonwood Ecological Restoration Plate™
* Cottonwood Biodiversity Plate™
* Eastern Cottonwood Plate™
* Fremont Cottonwood Plate™
* Black Cottonwood Plate™
* Plains Cottonwood Plate™

### Hickory Systems™

KEEP

* Hickory Systems Plate™
* Hickory Identification Plate™
* Hickory Leaf Plate™
* Hickory Nut Plate™
* Hickory Bark Plate™
* Hickory Wildlife Relationships Plate™
* Hickory Mast Production Plate™
* Hickory Forest Community Plate™
* Hickory Ecological Restoration Plate™
* Hickory Biodiversity Plate™
* Shagbark Hickory Plate™
* Shellbark Hickory Plate™
* Pignut Hickory Plate™
* Mockernut Hickory Plate™
* Bitternut Hickory Plate™

### Maple Systems™

KEEP

* Maple Systems Plate™
* Maple Identification Plate™
* Maple Leaf Plate™
* Maple Sap Flow Plate™
* Maple Autumn Color Plate™
* Maple Wildlife Relationships Plate™
* Maple Forest Community Plate™
* Maple Seed & Samara Plate™
* Maple Carbon Storage Plate™
* Sugar Maple Plate™
* Red Maple Plate™
* Silver Maple Plate™
* Bigleaf Maple Plate™
* Striped Maple Plate™

### Oak Systems™

KEEP

* Oak Systems Plate™
* Oak Identification Plate™
* Oak Leaf & Acorn Plate™
* Oak Wildlife Relationships Plate™
* Oak Keystone Species Plate™
* Oak Pollinator & Insect Plate™
* Oak Forest Community Plate™
* Oak Carbon Storage Plate™
* White Oak Plate™
* Red Oak Plate™
* Bur Oak Plate™
* Live Oak Plate™

### Pine Systems™

KEEP

* Pine Systems Plate™
* Pine Identification Plate™
* Pine Needle Plate™
* Pine Cone Plate™
* Pine Bark Plate™
* Pine Cone Ecology Plate™
* Pine Wildlife Relationships Plate™
* Pine Fire Ecology Plate™
* Pine Forest Community Plate™
* Pine Carbon Storage Plate™
* Eastern White Pine Plate™
* Ponderosa Pine Plate™
* Lodgepole Pine Plate™
* Longleaf Pine Plate™

### Spruce Systems™

KEEP

* Spruce Systems Plate™
* Spruce Identification Plate™
* Spruce Needle Plate™
* Spruce Cone Plate™
* Spruce Bark Plate™
* Spruce Boreal Forest Plate™
* Spruce Wildlife Relationships Plate™
* Spruce Forest Community Plate™
* Spruce Carbon Storage Plate™
* Spruce Climate Resilience Plate™
* White Spruce Plate™
* Black Spruce Plate™
* Red Spruce Plate™
* Engelmann Spruce Plate™

### Willow Systems™

KEEP

* Willow Systems Plate™
* Willow Identification Plate™
* Willow Leaf Plate™
* Willow Catkin Plate™
* Willow Bark Plate™
* Willow Riparian Systems Plate™
* Willow Wildlife Relationships Plate™
* Willow Beaver Relationships Plate™
* Willow Ecological Restoration Plate™
* Willow Biodiversity Plate™
* Black Willow Plate™
* Bebb Willow Plate™
* Scouler Willow Plate™
* Peachleaf Willow Plate™

## Wildlife Species™

KEEP

### Mammals of North America™

* Mammals of North America Plate™

* Gray Wolf Species Plate™
* Red Wolf Species Plate™
* Black Bear Species Plate™
* Grizzly Bear Species Plate™
* Mountain Lion Species Plate™
* Bobcat Species Plate™
* Coyote Species Plate™
* Red Fox Species Plate™
* Fisher Species Plate™
* River Otter Species Plate™
* Beaver Species Plate™
* Moose Species Plate™
* Elk Species Plate™
* American Bison Species Plate™
* White-tailed Deer Species Plate™
* Mule Deer Species Plate™
* Pronghorn Species Plate™
* Bighorn Sheep Species Plate™
* Mountain Goat Species Plate™
* Badger Species Plate™
* Snowshoe Hare Species Plate™

---

### Raptors & Birds of Prey™

* Birds of Prey Plate™

* Bald Eagle Species Plate™
* Golden Eagle Species Plate™
* Great Horned Owl Species Plate™
* Peregrine Falcon Species Plate™
* Red-tailed Hawk Species Plate™
* Osprey Species Plate™
* Snowy Owl Species Plate™

---

### Waterfowl & Wetland Birds™

* Waterfowl & Wetland Birds Plate™

* Tundra Swan Species Plate™
* Wood Duck Species Plate™
* Whooping Crane Species Plate™

---

### Songbirds, Seabirds & Other Birds™

* Songbirds, Seabirds & Other Birds Plate™

* Atlantic Puffin Species Plate™

---

### Wildlife Systems & Ecology™

* Wildlife Systems & Ecology Plate™

* Wildlife Adaptation & Survival Plate™
* Wildlife Behavior & Ecology Plate™
* Wildlife Conservation & Habitat Plate™
* Wildlife Habitats & Ecosystem Zones Plate™
* Wildlife Migration & Seasonal Patterns Plate™
* Wildlife Observation & Field Techniques Plate™
* Wildlife Observation Locations Plate™
* Wildlife Sign & Tracking Plate™

---

### Keystone Wildlife Relationships™

* Keystone Species & Trophic Cascades Plate™
* Food Webs & Ecological Relationships Plate™

---

## Animal Tracks™

KEEP

### North American Animal Tracks™

* North American Animal Tracks Plate™

---

### Predator Track Plates™

* Gray Wolf Track Plate™
* Coyote Track Plate™
* Red Fox Track Plate™
* Bobcat Track Plate™
* Mountain Lion Track Plate™
* Black Bear Track Plate™

---

### Ungulate Track Plates™

* Elk Track Plate™
* White-tailed Deer Track Plate™
* Moose Track Plate™
* American Bison Track Plate™

---

### Small Mammal Track Plates™

* Raccoon Track Plate™
* Snowshoe Hare Track Plate™

---

### Comparison Track Plates™

* Wolf vs Coyote Track Plate™
* Fox vs Coyote Track Plate™

---

### Wildlife Sign Systems™

* Wildlife Sign & Tracking Plate™
* Animal Scat Identification Plate™

---

## Pollinator Systems™

KEEP

### Bees of North America™

* Bees of North America System Plate™

* Bee Life Cycle Plate™

* Western Honey Bee Species Plate™

* American Bumble Bee Species Plate™

* Common Eastern Bumble Bee Species Plate™

* Rusty Patched Bumble Bee Species Plate™

* Mason Bee Species Plate™

* Leafcutter Bee Species Plate™

* Carpenter Bee Species Plate™

* Mining Bee Species Plate™

* Blue Orchard Bee Species Plate™

* Sweat Bee Species Plate™

* Metallic Green Bee Species Plate™

* Squash Bee Species Plate™

* Wool Carder Bee Species Plate™

---

### Butterflies of North America™

* Butterflies of North America System Plate™

* Butterfly Life Cycle Plate™

* Monarch Butterfly Plate™

* Eastern Tiger Swallowtail Plate™

* Black Swallowtail Plate™

* Painted Lady Butterfly Plate™

* Viceroy Butterfly Plate™

* Glasswing Butterfly Plate™

* Blue Morpho Butterfly Plate™

* Zebra Swallowtail Plate™

* Pipevine Swallowtail Plate™

* Mourning Cloak Butterfly Plate™

* Question Mark Butterfly Plate™

* Buckeye Butterfly Plate™

* Red-Spotted Purple Plate™

* Gulf Fritillary Plate™

* Owl Butterfly Plate™

---

### Hummingbirds of North America™

* Hummingbirds of North America System Plate™

* Ruby-throated Hummingbird Plate™

* Anna's Hummingbird Plate™

* Rufous Hummingbird Plate™

* Broad-tailed Hummingbird Plate™

* Black-chinned Hummingbird Plate™

* Costa's Hummingbird Plate™

* Allen's Hummingbird Plate™

* Calliope Hummingbird Plate™

* Rivoli's Hummingbird Plate™

* Blue-throated Mountain-gem Plate™

* Lucifer Hummingbird Plate™

* Violet-crowned Hummingbird Plate™

---

### Hummingbird Support Plates™

* Hummingbird Flight & Energy Plate™
* Hovering Flight Intelligence Plate™
* Iridescence & Feather Optics Plate™
* Pollination Precision Plate™

---

### Moths of North America™

* Moths of North America System Plate™

* Moth Life Cycle Plate™

* Luna Moth Plate™

* Glovers Silk Moth Plate™

* Cecropia Moth Plate™

* Polyphemus Moth Plate™

* White-lined Sphinx Plate™

* Hummingbird Clearwing Plate™

* Giant Leopard Moth Plate™

* Io Moth Plate™

* Plume Moth Plate™

* Atlas Moth Plate™

---

### Floral Resource Networks™

* Floral Resource Networks System Plate™

* Floral Resource Network Architecture Plate™

* Flower Resource Flow Plate™

* Pollinator Layer Plate™

* Nectar Corridor Plate™

* Bloom Timing Intelligence Plate™

* Plant Reproduction Plate™

* Biodiversity Production Plate™

* Underground-To-Flower Plate™

* Pollination Network Plate™

* Floral Resource Intelligence Plate™

* Ecological Network Stability Plate™

* Coevolution Plate™

* Resource Distribution Plate™

---

### Pollinator Intelligence™

* Pollination Intelligence Plate™
* Hive Intelligence Plate™
* Waggle Dance Communication Plate™
* Ultraviolet Flower Guidance Plate™
* Wing Pattern Intelligence Plate™
* Seasonal Emergence Intelligence Plate™

---

### Pollinator Connector Plates™

* Bee Resource Connector Plate™
* Butterfly Resource Connector Plate™
* Moth Resource Connector Plate™
* Hummingbird Resource Connector Plate™

---

## Field Locations™

KEEP

### National Park Field Locations™

* Yellowstone National Park Field Location Plate™
* Grand Teton National Park Field Location Plate™
* Acadia National Park Field Location Plate™

---

### National Wildlife Refuge Field Locations™

* Blackwater National Wildlife Refuge Field Location Plate™
* Chincoteague National Wildlife Refuge Field Location Plate™
* Aransas National Wildlife Refuge Field Location Plate™
* Bosque del Apache National Wildlife Refuge Field Location Plate™

---

### Coastal & Marine Field Locations™

* Machias Seal Island Field Location Plate™

---

### Freshwater & Wetland Field Locations™

* Lake Mattamuskeet Field Location Plate™

---

### Mountain & Landscape Field Locations™

* Maroon Bells Field Location Plate™

---

## Photography Guides™

KEEP

### Yellowstone Photography Guide™

* Yellowstone Photography Guide Plate™
* Yellowstone Thermal Photography Plate™

---

### Grand Teton Photography Guide™

* Grand Teton Photography Guide Plate™

---

### Blackwater Photography Guide™

* Blackwater Photography Guide Plate™

---

### Chincoteague Photography Guide™

* Chincoteague Photography Guide Plate™
* Barrier Island Photography Plate™
* Wild Horse Photography Plate™
* Coastal Light & Atmospheric Photography Plate™

---

### Mattamuskeet Photography Guide™

* Mattamuskeet Photography Guide Plate™
* Waterfowl Photography Plate™
* Lake Light Photography Plate™
* Migration Photography Plate™

---

### Machias Seal Island Photography Guide™

* Machias Photography Guide Plate™
* Atlantic Puffin Photography Plate™
* Seabird Colony Photography Plate™
* Island Wildlife Photography Plate™

---

### Aransas Photography Guide™

* Aransas Photography Guide Plate™
* Whooping Crane Photography Plate™
* Coastal Marsh Photography Plate™
* Wintering Bird Photography Plate™

---

### Bosque del Apache Photography Guide™

* Bosque Photography Guide Plate™
* Waterfowl Flight Photography Plate™
* Sunrise Blast-Off Photography Plate™
* Migration Photography Plate™

---

## Information Systems in Nature™

KEEP

* Information Systems in Nature Plate™

* Biological Communication Plate™

* Signal Propagation Plate™

* Ecological Networks Plate™

* Biological Memory Plate™

* Feedback Loop Architecture Plate™

* Distributed Intelligence Plate™

* Ecological Computation Plate™

* Living Information Fields Plate™

* Future Information Systems Plate™

---

## Governance & Framework Infrastructure™

KEEP

### Naturepedia Core Infrastructure™

* Naturepedia Master System Plate™
* Naturepedia System Navigation Plate™

---

### Robbie's Razor Infrastructure™

* Robbie's Razor Plate™
* Robbie's Razor Systems Plate™

---

### Compression & Registry Architecture™

* Knowledge Compression Flow Plate™
* Plate Architecture Plate™
* Graph Registry Plate™

---

### Governance & Attribution Systems™

* Authorship Conservation Rules Plate™
* Commercial Data License Plate™

---

### Commercial Infrastructure™

* Commercial Intelligence Pricing Plate™
* x402 Commercial Settlement Plate™

---

## Quantum & Elemental Intelligence™

KEEP

### Hydrogen Systems™

* Hydrogen Plate™

---

### Photon Systems™

* Photon Plate™

---

### Quantum Fields™

* Quantum Fields Plate™

---

### Gravitational Systems™

* Gravitons Plate™

---

### Plasma Systems™

* Plasma Plate™

---

### Magnetism & Polarity™

* Magnetism & Polarity Plate™

---

### Universal Principles™

* Resonance Plate™
* Vibration Plate™

---

## Earth Systems™

KEEP

* Earth Systems Plate™
* Geosphere Plate™
* Hydrosphere Plate™
* Atmosphere Plate™
* Biosphere Plate™
* Cryosphere Plate™
* Climate Systems Plate™
* Water Cycle Plate™
* Plate Tectonics & Earth Engine Plate™
* Human Impact on Earth Systems Plate™
* Earth Systems Photography Plate™

---

## Soil Systems™

KEEP

* Soil Systems Plate™
* Soil Horizons Plate™
* Soil Microbiome Plate™
* Soil Biodiversity Plate™
* Soil Carbon Plate™
* Soil Water Systems Plate™
* Mycorrhizal Networks Plate™
* Nutrient Cycling Plate™
* Living Soil Food Web Plate™
* Living Soil Intelligence Plate™
* Regenerative Soil Systems Plate™

---

## Carbon Cycle™

KEEP

* Carbon Cycle Plate™
* Photosynthesis Plate™
* Respiration Plate™
* Decomposition Plate™
* Carbon Sequestration Plate™
* Forest Carbon Plate™
* Soil Carbon Plate™
* Ocean Carbon Plate™
* Carbon & Microbial Life Plate™
* Regenerative Carbon Systems Plate™
* Carbon Farming Plate™

---

## Ecosystem Feedbacks™

KEEP

* Ecosystem Feedbacks Plate™
* Positive Feedback Loops Plate™
* Negative Feedback Loops Plate™
* Soil Feedbacks Plate™
* Forest Feedbacks Plate™
* Water & Climate Feedbacks Plate™
* Microbial Feedbacks Plate™
* Mycelial Feedback Networks Plate™
* Disturbance & Recovery Plate™
* Regenerative Feedback Systems Plate™

---

## Bioelectric Systems™

KEEP

* Bioelectric Systems Plate™
* Harold Burr's Life Fields Plate™
* Michael Levin Plate™
* Bioelectric Morphogenesis Plate™
* Regeneration & Healing Plate™
* Plant Electrophysiology Plate™
* Soil Electrical Networks Plate™
* Bioelectric Medicine Plate™
* Electrical Ecology Plate™
* Bioelectric Photography Plate™

---

## Quantum Agriculture™

KEEP

* Quantum Agriculture Plate™
* Living Soil Intelligence Plate™
* Bioelectric Farming Plate™
* Light & Photons in Agriculture Plate™
* Water Intelligence Plate™
* Plant Communication Plate™
* Mycorrhizal Partnerships Plate™
* Nutrient Cycling & Bioavailability Plate™
* Regenerative Farming Systems Plate™
* Carbon Farming Plate™
* Biodiversity & Ecosystem Balance Plate™
* Future Food Systems Plate™

---

## Plant Intelligence™

KEEP

* Plant Intelligence Plate™
* Plant Communication Plate™
* Plant Electrophysiology Plate™
* Root Intelligence Plate™
* Plant Memory Plate™
* Plant Defense Systems Plate™
* Plant Sensory Biology Plate™
* Plant Cooperation Plate™
* Plants & Mycorrhizal Networks Plate™
* Future Plant Intelligence Plate™

---

## Water Systems™

KEEP

* Water Systems Plate™
* Water Cycle Plate™
* River Systems Plate™
* Wetland Ecosystem Plate™
* Floodplains Plate™
* Groundwater Systems Plate™
* Estuaries & Coastal Systems Plate™
* Chesapeake Bay System Plate™
* Water Memory Plate™

---

## Microbial Life Systems™

KEEP

* Microbial Life Systems Plate™
* Microbial Identification Plate™
* Bacteria Plate™
* Archaea Plate™
* Biofilms Plate™
* Microbial Mats Plate™
* Thermophiles Plate™
* Extremophiles Plate™
* Photosynthesis Plate™
* Chemosynthesis Plate™
* Nutrient Cycling Plate™
* Microbial Biodiversity Plate™
* Microbial Ecosystem Services Plate™
* Origins of Life Plate™
* Microbial Photography Plate™

---

## Volcanic Landscapes™

KEEP

* Volcanic Landscapes Plate™
* Magma Chambers Plate™
* Volcanic Islands Plate™
* Calderas Plate™
* Plate Tectonics Plate™
* Ring of Fire Plate™
* Volcano Identification Plate™
* Lava Flows Plate™
* Volcanic Eruptions Plate™
* Supervolcanoes Plate™
* Volcanic Soils Plate™
* Volcanic Ecosystems Plate™
* Volcanic Succession Plate™
* Volcanic Biodiversity Plate™
* Volcanic Hazards Plate™
* Volcanic Photography Plate™
* Volcanoes Beyond Earth Plate™

---

## Geothermal Ecosystems™

KEEP

* Geothermal Ecosystems Plate™
* Geothermal Identification Plate™
* Geothermal Water Systems Plate™
* Thermophile Life Plate™
* Extremophile Life Plate™
* Geothermal Microbial Mats Plate™
* Geothermal Wildlife Relationships Plate™
* Geothermal Biodiversity Plate™
* Geothermal Ecosystem Services Plate™
* Hydrothermal Vent Ecosystems Plate™
* Global Geothermal Regions Plate™
* Geothermal Photography Plate™

---

## Yellowstone Thermal Features™

KEEP

* Yellowstone Thermal Systems Plate™
* Yellowstone Thermal Identification Plate™
* Yellowstone Geysers Plate™
* Old Faithful Plate™
* Yellowstone Hot Springs Plate™
* Grand Prismatic Spring Plate™
* Mammoth Hot Springs Plate™
* Yellowstone Mud Pots Plate™
* Yellowstone Fumaroles Plate™
* Norris Geyser Basin Plate™
* Yellowstone Microbial Life Plate™
* Yellowstone Thermal Ecology Plate™
* Yellowstone Water & Heat Systems Plate™
* Yellowstone Thermal Photography Plate™

---

## Hydrothermal Ecosystems™

KEEP

* Hydrothermal Ecosystems Plate™
* Hydrothermal Vent Identification Plate™
* Hydrothermal Microbial Life Plate™
* Hydrothermal Mineral Systems Plate™
* Hydrothermal Astrobiology Plate™
* Europa & Enceladus Analogs Plate™
* Origins of Life Hydrothermal Plate™
* Black Smokers Plate™
* White Smokers Plate™
* Giant Tube Worm Plate™
* Vent Mussels & Clams Plate™
* Vent Crabs & Shrimp Plate™
* Vent Extremophiles Plate™
* Chemosynthetic Food Web Plate™
* Hydrothermal Vent Biodiversity Plate™
* Deep Ocean Exploration Plate™
* Hydrothermal Photography Plate™

---

## Additional KEEP — Supplemental Ecosystem, Habitat, Restoration & Framework Plates

KEEP

### Additional Tree System Plates™

* Birch Forest Succession Plate™
* Carbon Storage Tree Plate™
* Forest Structure Plate™
* Keystone Tree Species Plate™
* Riparian Tree Systems Plate™
* Seasonal Tree Ecology Plate™

---

### Ecosystem & Habitat Systems™

* Arctic Tundra & Boreal Ecosystems Plate™
* Biodiversity Ecosystem Balance Plate™
* Biodiversity Intelligence Plate™
* Coastal Estuary Wildlife Systems Plate™
* Ecological Resilience Plate™
* Ecosystem Stability Plate™
* Forest Ecosystems Plate™
* Grassland Ecosystems Plate™
* Habitat Connectivity Plate™
* Habitat Fragmentation Plate™
* Habitat Intelligence Plate™
* Mountain Alpine Ecosystems Plate™
* Wetlands & Peat Plate™

---

### Restoration & Recovery Systems™

* Ecological Recovery Timeline Plate™
* Ecological Restoration Plate™
* Habitat Recovery Plate™
* Native Species Recovery Plate™
* Pollinator Recovery Plate™
* Restoration Intelligence Plate™
* Soil Regeneration Plate™

---

### Additional Quantum Agriculture Plates™

* Hydrogen Water Soil Systems Plate™

---

### Additional Hydrothermal Plates™

* Seafloor Geology Plate™

---

### Additional Governance & Foundation Plates™

* Grand Compression Cosmology Plate™
* Naturepedia Knowledge Mesh Framework Hero™
* Quantum & Elemental Intelligence Ring 1 Plate™
* Robbie George Biography Plate™
* The Grand Compression Naturepedia Knowledge Plate™

---

# DUPLICATE

Definition:

Files duplicated by:

* copy
* copy 2
* alternate export
* duplicate format

These files are NOT counted toward the canonical registry.

## Confirmed Duplicate Files

These files are excluded from the final canonical KEEP count.

- `balsam-fir-plate_naturepedia_firs-of-north-america_robbie-george copy.png`
- `ecosystem-feedbacks-plate_naturepedia-earth-systems_ecosystem-feedbacks_robbie-george copy.png`
- `soil-systems-plate_naturepedia-earth-systems_soil-systems_robbie-george copy.png`
- `soil-systems-plate_naturepedia-earth-systems_soil-systems_robbie-george copy 2.png`
- `grizzly-bear_species-plate_ursus-arctos-horribilis_north-america_robbie-george.jpg`

Canonical versions remain in KEEP.

---

# SUPERSEDED

Definition:

Older plates replaced by a newer canonical version.

Only the newest version remains in KEEP.

Older versions remain archived.

## Confirmed Superseded Files

Older versions replaced by newer canonical files.

### Commercial Intelligence Pricing Plate™

KEEP VERSION

- `commercial-intelligence-pricing-plate_enterprise-recursive-access-governance_robbie-george_v2.png`

SUPERSEDED

- `commercial-intelligence-pricing-plate_governance-license_naturepedia_robbie-george.png`

---

### Fisher Species Plate™

KEEP VERSION

- `fisher_species-plate_pekania-pennanti_naturepedia_robbie-george_v2.png`

SUPERSEDED

- `fisher_species-plate_pekania-pennanti_north-america_forest-habitat_robbie-george.png`

---

### Plant Communication Plate™

KEEP VERSION

- `plant-communication-plate_naturepedia_plant-intelligence_robbie-george_v2.png`

SUPERSEDED

- `plant-communication-plate_naturepedia_plant-intelligence_robbie-george.png`

NOTE:

- `plant-communication-plate_naturepedia_quantum-agriculture_robbie-george.png` remains a separate Quantum Agriculture™ system-context plate unless intentionally merged later.

---

### Wool Carder Bee Species Plate™

KEEP VERSION

- `wool-carder-bee_species-plate_anthidium-manicatum_naturepedia_robbie-george_v2.png`

SUPERSEDED

- earlier non-v2 Wool Carder Bee export if found in archived inventory.

---

# ARTIST RENDITION

Definition:

Conceptual visualization plates.

These plates support interpretation but are not counted as canonical knowledge nodes.

They remain valuable assets but should not contribute to registry totals.

## Artist Rendition — Tree Systems

Conceptual support plates excluded from the final canonical KEEP count unless later promoted.

- `acorn-ecology-artist-rendition-plate_naturepedia_oaks-of-north-america_robbie-george.png`
- `aspen-forest-artist-rendition-plate_naturepedia_aspens-of-north-america_robbie-george.png`
- `aspen-root-colony-artist-rendition-plate_naturepedia_aspens-of-north-america_robbie-george.png`
- `autumn-maple-canopy-artist-rendition-plate_naturepedia_maples-of-north-america_robbie-george.png`
- `birch-forest-artist-rendition-plate_naturepedia_birches-of-north-america_robbie-george.png`
- `forest-ecology-artist-rendition-plate_naturepedia_trees-of-north-america_robbie-george.png`
- `golden-aspen-canopy-artist-rendition-plate_naturepedia_aspens-of-north-america_robbie-george.png`
- `maple-forest-artist-rendition-plate_naturepedia_maples-of-north-america_robbie-george.png`
- `maple-sap-flow-artist-rendition-plate_naturepedia_maples-of-north-america_robbie-george.png`
- `mountain-pine-forest-artist-rendition-plate_naturepedia_pines-of-north-america_robbie-george.png`
- `oak-forest-artist-rendition-plate_naturepedia_oaks-of-north-america_robbie-george.png`
- `pine-cone-artist-rendition-plate_naturepedia_pines-of-north-america_robbie-george.png`
- `pine-forest-artist-rendition-plate_naturepedia_pines-of-north-america_robbie-george.png`
- `tree-systems-artist-rendition-plate_naturepedia_trees-of-north-america_robbie-george.png`
- `white-bark-ecology-artist-rendition-plate_naturepedia_birches-of-north-america_robbie-george.png`
- `wildlife-tree-relationships-artist-rendition-plate_naturepedia_trees-of-north-america_robbie-george.png`

## Artist Rendition — Pollinator & Floral Network Systems

Conceptual support plates excluded from the final canonical KEEP count unless later promoted.

- `bee-coneflower_artist-rendition-plate-v2_naturepedia_robbie-george.png`
- `bee-goldenrod_artist-rendition-plate_naturepedia_robbie-george.png`
- `bee-milkweed_artist-rendition-plate_naturepedia_robbie-george.png`
- `bee-resource-connector-plate-naturepedia-artist-rendition.png`
- `bumblebee-lupine_artist-rendition-plate_naturepedia_robbie-george.png`
- `butterfly-resource-connector-plate-naturepedia-artist-rendition.png`
- `coevolution-plate-naturepedia-artist-rendition.png`
- `floral-resource-intelligence-plate-naturepedia-artist-rendition.png`
- `floral-resource-network-architecture-plate-naturepedia-artist-rendition.png`
- `floral-resource-networks-system-plate-naturepedia-artist-rendition.png`
- `flower-resource-flow-plate-naturepedia-artist-rendition.png`
- `honeybee-sunflower_artist-rendition-plate_naturepedia_robbie-george.png`
- `hummingbird-resource-connector-plate-naturepedia-artist-rendition.png`
- `moth-resource-connector-plate-naturepedia-artist-rendition.png`
- `nectar-corridor-plate-naturepedia-artist-rendition.png`
- `plant-reproduction-plate-naturepedia-artist-rendition.png`
- `pollination-network-plate-naturepedia-artist-rendition.png`
- `pollinator-layer-plate-naturepedia-artist-rendition.png`
- `resource-distribution-plate-naturepedia-artist-rendition.png`
- `underground-to-flower-plate-naturepedia-artist-rendition.png`

## Artist Rendition — Habitat, Restoration & Ecological Systems

Conceptual support plates excluded from the final canonical KEEP count unless later promoted.

- `carbon-soil-storage-plate_artist-rendition_naturepedia_robbie-george.png`
- `ecological-connectivity-plate_artist-rendition_naturepedia_robbie-george.png`
- `ecological-network-stability-plate-naturepedia-artist-rendition.png`
- `ecological-succession-plate_artist-rendition_naturepedia_robbie-george.png`
- `edge-habitat-plate_artist-rendition_naturepedia_robbie-george.png`
- `habitat-recovery-artist-rendition-plate_restoration-art_naturepedia_robbie-george.png`
- `habitat-structure-plate_artist-rendition_naturepedia_robbie-george.png`
- `keystone-plant-species-plate_artist-rendition_naturepedia_robbie-george.png`
- `meadow-ecology-plate_artist-rendition_naturepedia_robbie-george.png`
- `native-plant-intelligence-plate_artist-rendition_naturepedia_robbie-george.png`
- `native-seed-production-plate_artist-rendition_naturepedia_robbie-george.png`
- `plant-community-diversity-plate_artist-rendition_naturepedia_robbie-george.png`
- `plant-community-system-plate-v2_artist-rendition_naturepedia_robbie-george.png`
- `pollinator-habitat-corridor-plate_artist-rendition_naturepedia_robbie-george.png`
- `pollinator-recovery-artist-rendition-plate_pollinator-restoration-art_naturepedia_robbie-george.png`
- `riparian-plant-communities-plate_artist-rendition_naturepedia_robbie-george.png`
- `root-network-plate_artist-rendition_naturepedia_robbie-george.png`
- `seasonal-habitat-continuity-plate_artist-rendition_naturepedia_robbie-george.png`
- `soil-regeneration-artist-rendition-plate_soil-ecology-art_naturepedia_robbie-george.png`
- `wildlife-habitat-production-plate_artist-rendition_naturepedia_robbie-george.png`

## Artist Rendition — Governance & Future Infrastructure

Conceptual support plates excluded from the final canonical KEEP count unless later promoted.

- `future-knowledge-network-artist-rendition-plate_framework-licensing_robbie-george.png`
- `machine-to-machine-commerce-artist-rendition-plate_framework-licensing_robbie-george.png`

NOTE:

These remain important conceptual infrastructure assets but should not be counted as canonical live registry plates unless promoted later.

## Interpretation Plates

Interpretation plates are conceptual support plates and are excluded from the final canonical KEEP count unless later promoted.

- `buzz-pollination_interpretation-plate_naturepedia_robbie-george.png`
- `hive-intelligence_interpretation-plate_naturepedia_robbie-george.png`
- `native-bee-diversity_interpretation-plate_naturepedia_robbie-george.png`
- `pollination-intelligence_interpretation-plate_naturepedia_robbie-george.png`
- `ultraviolet-flower-guidance_interpretation-plate_naturepedia_robbie-george.png`
- `waggle-dance-communication_interpretation-plate_naturepedia_robbie-george.png`

---

Additional artist renditions should be appended here.

---

# DRAFT

Definition:

Temporary design exports and non-canonical development assets.

Draft files are excluded from registry counts.

## Confirmed Draft Files

Temporary image-generation exports excluded from canonical registry counts.

- `ChatGPT Image Apr 24, 2026, 04_04_12 PM.png`
- `ChatGPT Image Apr 24, 2026, 06_25_52 AM.png`

These are design/export artifacts, not canonical Naturepedia™ Plates.

---

# Unresolved Classification Review

The following plates require explicit classification decisions before the final canonical Naturepedia™ count is calculated.

These files do not fit cleanly into the current Species™, Track™, System™, Photography Guide™, Field Location™, Governance™, Duplicate™, Superseded™, Draft™, or Artist Rendition categories.

Each plate should ultimately be assigned to:

* KEEP
* ARTIST RENDITION
* SUPERSEDED
* DUPLICATE
* DRAFT

No plate should remain unresolved before final count calculation.

---

## Ecosystem System Plates™

Recommended Classification:

KEEP

Reason:

These function as ecosystem-level knowledge nodes and relationship hubs.

Files:

* Arctic Tundra & Boreal Ecosystems Plate™
* Forest Ecosystems Plate™
* Grassland Ecosystems Plate™
* Mountain Alpine Ecosystems Plate™
* Wetland Ecosystem Plate™

Decision:

KEEP

---

## Biodiversity & Ecological Intelligence Plates™

Recommended Classification:

KEEP

Reason:

These operate as ecological relationship architecture plates rather than artist renditions.

Files:

* Biodiversity Intelligence Plate™
* Ecological Resilience Plate™
* Ecosystem Stability Plate™

Decision:

KEEP

---

## Habitat Relationship Plates™

Recommended Classification:

KEEP

Reason:

These represent habitat-scale ecological concepts and navigation nodes.

Files:

* Habitat Connectivity Plate™
* Habitat Fragmentation Plate™
* Habitat Intelligence Plate™

Decision:

KEEP

---

## Restoration & Recovery Systems™

Recommended Classification:

KEEP

Reason:

These function as restoration system nodes and ecological recovery pathways.

Files:

* Ecological Restoration Plate™
* Ecological Recovery Timeline Plate™
* Habitat Recovery Plate™
* Native Species Recovery Plate™
* Pollinator Recovery Plate™
* Restoration Intelligence Plate™
* Soil Regeneration Plate™

Decision:

KEEP

---

## Foundation & Knowledge Architecture Plates™

Recommended Classification:

KEEP

Reason:

These contribute to Naturepedia™ architecture, knowledge organization, compression systems, and framework development.

Files:

* Grand Compression Cosmology Plate™
* Quantum Elemental Intelligence Ring 1 Plate™
* The Grand Compression Naturepedia Knowledge Plate™
* Naturepedia Knowledge Mesh Framework Hero™

Decision:

KEEP

---

## Review Notes

Current Recommendation:

All unresolved plates listed above should remain in KEEP.

No evidence currently suggests they belong in:

* DUPLICATE
* SUPERSEDED
* DRAFT

Several could be interpreted as ARTIST RENDITION plates, but they currently function more like conceptual knowledge nodes and relationship hubs than illustrations.

Until a future registry simplification occurs, KEEP is the recommended classification.

---

## Reconciliation Completion Checklist

Before final count calculation:

☐ Every file classified

☐ No unresolved plates remain

☐ KEEP inventory finalized

☐ DUPLICATE inventory finalized

☐ SUPERSEDED inventory finalized

☐ ARTIST RENDITION inventory finalized

☐ DRAFT inventory finalized

☐ Registry totals balanced

☐ Final canonical count approved

---

# Canonical Count Worksheet

Purpose:

This worksheet serves as the final registry balancing mechanism before any Naturepedia™ counts are updated in:

* cold-bird
* plate-registry-expanded.json
* llms.txt
* llms-full.txt
* README.md
* AGENTS.md
* x402 documentation

Every file from MasterPlateList.txt must be represented exactly once.

---

## Registry Totals

Master Inventory Total:

```txt
648
```

Source:

MasterPlateList.txt

---

## KEEP

Definition:

Canonical Naturepedia™ Plates included in the active registry.

Current Count:

```txt
_____
```

Status:

PENDING

---

## DUPLICATE

Definition:

Copy files, alternate exports, duplicate formats.

Current Count:

```txt
_____
```

Status:

PENDING

Known Examples:

* soil-systems copy
* soil-systems copy 2
* ecosystem-feedbacks copy
* balsam-fir copy
* grizzly-bear jpg duplicate

---

## SUPERSEDED

Definition:

Older versions replaced by canonical versions.

Current Count:

```txt
_____
```

Status:

PENDING

Known Examples:

* commercial-intelligence-pricing original
* fisher original
* plant-communication original
* wool-carder-bee original

---

## ARTIST RENDITION

Definition:

Conceptual support illustrations and interpretation plates.

Current Count:

```txt
_____
```

Status:

PENDING

Includes:

* Artist Rendition Plates
* Interpretation Plates
* Concept Visualization Plates
* Pollinator Network Art Plates
* Restoration Art Plates
* Future Infrastructure Art Plates

---

## DRAFT

Definition:

Temporary design assets and development exports.

Current Count:

```txt
2
```

Status:

WORKING COUNT

Known Files:

* ChatGPT Image Apr 24, 2026, 04_04_12 PM.png
* ChatGPT Image Apr 24, 2026, 06_25_52 AM.png

---

# Registry Balance Check

Formula:

```txt
KEEP
+ DUPLICATE
+ SUPERSEDED
+ ARTIST RENDITION
+ DRAFT
=
648
```

Calculation:

```txt
571 KEEP

+ 5 DUPLICATE

+ 4 SUPERSEDED

+ 66 ARTIST RENDITION

+ 2 DRAFT

= 648 TOTAL
```

Expected Result:

```txt
648
```

Status:

☑ PASS

☐ FAIL

---

# Final Canonical Count

Current Working Canonical Naturepedia™ Count:

```txt
571 (Candidate Count)
```

This number becomes the official count used by:

* cold-bird
* ai-catalog.json
* llms.txt
* llms-full.txt
* plate-registry-expanded.json
* README.md
* AGENTS.md
* x402 documentation

After final verification.

---

# Approval Checklist

Before updating infrastructure:

☐ Every file classified

☐ Registry balance independently verified

☑ Duplicate inventory finalized

☑ Superseded inventory finalized

☑ Artist rendition inventory finalized

☑ Draft inventory finalized

☑ Unresolved review completed

☐ Final canonical count approved

---

# Infrastructure Update Authorization

Status:

PENDING FINAL VERIFICATION

Do not update:

* plateCount
* Worker registry metadata
* llms files
* README
* AGENTS
* x402 registry

until final count verification is completed.

---

# Canonical Count Approval

Approved Count:

571 (Candidate Count)

Final verification required before publication.

Status:

WORKING COUNT — NOT YET FINAL

Approved By:

Robbie George

Date:

06/24/2026

Verification Note:

The candidate count of 571 was derived through registry reconciliation and category balancing.

A final filename-by-filename verification against MasterPlateList.txt should be completed before propagating this count to:

- cold-bird
- ai-catalog.json
- llms.txt
- llms-full.txt
- plate-registry-expanded.json
- README.md
- AGENTS.md
- x402 documentation

---

# FINAL CANONICAL COUNT

Status:

PENDING FINAL RECONCILIATION

Do not update Worker `plateCount` yet.

Current Worker Count:

```txt
163
```

DUPLICATE section started
SUPERSEDED section started
ARTIST RENDITION section started
DRAFT section started
KEEP inventory substantially populated.
Final reconciliation audit still required.

FINAL CANONICAL COUNT =
all KEEP files
minus DUPLICATE
minus SUPERSEDED
minus ARTIST RENDITION
minus DRAFT

---

# Synchronization Checklist

After final count determination:

Update:

* cold-bird
* plate-registry-expanded.json
* llms.txt
* llms-full.txt
* README.md
* AGENTS.md
* plate_examples_index.md
* live-endpoints.md

---

# Cloudflare Purge Checklist

After deployment purge:

* /.well-known/ai-catalog.json
* /ai-catalog.json
* /llms.txt
* /llms-full.txt
* /api/v2/naturepedia/index.md
* /api/v2/plates/registry.md
* /api/v2/rrip/resolve
* /api/v2/razor/state-token
* /x402/plate-registry-expanded.json

---

# Reconciliation Status

Master Inventory Review:
IN PROGRESS

Canonical Count:
PENDING

Registry Synchronization:
NOT STARTED

Cloudflare Update:
NOT STARTED

Naturepedia Registry Reconciliation:
ACTIVE
