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

---

## Known Duplicates

* soil-systems-plate_naturepedia-earth-systems_soil-systems_robbie-george copy.png

* soil-systems-plate_naturepedia-earth-systems_soil-systems_robbie-george copy 2.png

* ecosystem-feedbacks-plate_naturepedia-earth-systems_ecosystem-feedbacks_robbie-george copy.png

* balsam-fir-plate_naturepedia_firs-of-north-america_robbie-george copy.png

* grizzly-bear_species-plate_ursus-arctos-horribilis_north-america_robbie-george.jpg

Additional duplicate discoveries should be appended here.

---

# SUPERSEDED

Definition:

Older plates replaced by a newer canonical version.

Only the newest version remains in KEEP.

Older versions remain archived.

---

## Known Superseded Plates

KEEP VERSION

* commercial-intelligence-pricing-plate_enterprise-recursive-access-governance_robbie-george_v2.png

SUPERSEDED

* commercial-intelligence-pricing-plate_governance-license_naturepedia_robbie-george.png

---

KEEP VERSION

* fisher_species-plate_pekania-pennanti_naturepedia_robbie-george_v2.png

SUPERSEDED

* fisher_species-plate_pekania-pennanti_north-america_forest-habitat_robbie-george.png

---

KEEP VERSION

* wool-carder-bee_species-plate_anthidium-manicatum_naturepedia_robbie-george_v2.png

SUPERSEDED

* previous wool-carder-bee version

---

KEEP VERSION

* plant-communication-plate_naturepedia_plant-intelligence_robbie-george_v2.png

SUPERSEDED

* plant-communication-plate_naturepedia_plant-intelligence_robbie-george.png

---

Additional v2 replacements should be appended here.

---

# ARTIST RENDITION

Definition:

Conceptual visualization plates.

These plates support interpretation but are not counted as canonical knowledge nodes.

They remain valuable assets but should not contribute to registry totals.

---

## Tree Artist Renditions

* Aspen Forest Artist Rendition Plate™

* Aspen Root Colony Artist Rendition Plate™

* Golden Aspen Canopy Artist Rendition Plate™

* Birch Forest Artist Rendition Plate™

* Birch Forest Succession Artist Rendition Plate™

* White Bark Ecology Artist Rendition Plate™

* Maple Forest Artist Rendition Plate™

* Maple Sap Flow Artist Rendition Plate™

* Autumn Maple Canopy Artist Rendition Plate™

* Oak Forest Artist Rendition Plate™

* Acorn Ecology Artist Rendition Plate™

* Pine Forest Artist Rendition Plate™

* Pine Cone Artist Rendition Plate™

* Mountain Pine Forest Artist Rendition Plate™

---

## Pollinator Artist Renditions

* Bee Goldenrod Plate™

* Bee Milkweed Plate™

* Bee Coneflower Plate™

* Honeybee Sunflower Plate™

* Pollination Network Plate™

* Nectar Corridor Plate™

* Pollinator Layer Plate™

* Floral Resource Network Architecture Plate™

* Flower Resource Flow Plate™

* Bloom Timing Intelligence Plate™

* Resource Distribution Plate™

* Coevolution Plate™

* Ecological Network Stability Plate™

* Biodiversity Production Plate™

* Underground-To-Flower Plate™

---

## Restoration Artist Renditions

* Habitat Recovery Artist Rendition Plate™

* Pollinator Recovery Artist Rendition Plate™

* Soil Regeneration Artist Rendition Plate™

* Wildlife Habitat Production Artist Rendition Plate™

* Native Plant Intelligence Artist Rendition Plate™

* Native Seed Production Artist Rendition Plate™

---

## Infrastructure Artist Renditions

* Future Knowledge Network Artist Rendition Plate™
* Machine-to-Machine Commerce Artist Rendition Plate™

---

Additional artist renditions should be appended here.

---

# DRAFT

Definition:

Temporary design exports and non-canonical development assets.

Draft files are excluded from registry counts.

---

## Draft Files

* ChatGPT Image Apr 24, 2026, 04_04_12 PM.png
* ChatGPT Image Apr 24, 2026, 06_25_52 AM.png

Additional drafts should be appended here.

---

# FINAL CANONICAL COUNT

Status:

PENDING RECONCILIATION

Formula:

FINAL COUNT =
KEEP
− DUPLICATES
− SUPERSEDED
− DRAFTS
− ARTIST RENDITIONS

---

Current Worker Count

163

Status:

Do Not Modify Yet

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
