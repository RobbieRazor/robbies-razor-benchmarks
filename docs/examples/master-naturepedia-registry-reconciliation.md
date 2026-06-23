# Master Naturepedia Registry Reconciliation™

**Status:** Canonical Registry Audit In Progress

**Author & Architect of Record:** Robbie George

---

# Purpose

This document serves as the final reconciliation layer between:

* MasterPlateList.txt
* master-naturepedia-plate-census.md
* plate-registry-expanded.json
* llms.txt
* llms-full.txt
* Cloudflare Worker (cold-bird)
* README.md
* AGENTS.md
* plate_examples_index.md
* x402 documentation

This file exists to determine the final canonical Naturepedia™ inventory before any registry counts are updated.

---

# Registry Reconciliation Rules

Every file from MasterPlateList.txt must appear in exactly one category.

Categories:

1. KEEP
2. DUPLICATE
3. SUPERSEDED
4. ARTIST RENDITION
5. DRAFT

No file should remain unclassified.

---

# KEEP

Definition:

Canonical Naturepedia™ Plates that remain part of the live registry.

These plates:

* represent active system plates
* species plates
* track plates
* field location plates
* photography guide plates
* governance plates
* framework plates
* relationship plates
* machine-readable infrastructure plates

KEEP plates are eligible for:

* Worker registry inclusion
* llms-full inclusion
* AI catalog inclusion
* RRIP resolution
* x402 registry exposure

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

---

Continue adding every canonical family from:

* Earth Systems™
* Soil Systems™
* Carbon Cycle™
* Ecosystem Feedbacks™
* Bioelectric Systems™
* Quantum Agriculture™
* Plant Intelligence™
* Information Systems in Nature™
* Water Systems™
* Microbial Life Systems™
* Volcanic Landscapes™
* Geothermal Ecosystems™
* Yellowstone Thermal Features™
* Hydrothermal Ecosystems™
* Wildlife Species™
* Animal Tracks™
* Pollinator Systems™
* Field Locations™
* Photography Guides™
* Governance & Framework Infrastructure™
* Quantum & Elemental Intelligence™

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
KEEP section still requires full family-by-family population

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
