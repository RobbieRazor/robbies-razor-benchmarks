# Plate™ Schema Standard

**Status:** Canonical — Machine-Readable Knowledge Specification  
**Author & Originator:** Robbie George  

---

## 1. Overview

This document defines the standard schema for **Plates™**, the canonical implementation of Recursive Compression Interfaces (RCIs) within the **Recursive Knowledge Compression Architecture (RKCA)**.

Plates™ convert complex systems into:

- human-readable structures  
- machine-readable semantic nodes  
- reusable recursive knowledge units  

They operationalize:

**compression → expression → memory → recursion**

---

## 2. Core Principle

> A Plate™ is a structured knowledge object that preserves relational intelligence in a reusable, machine-readable format.

Plates are not:
- images  
- infographics  
- summaries  

They are:
- structured semantic nodes  
- memory-preserved knowledge units  
- graph-linked entities  

---

## 3. Required Plate Structure

Every Plate™ must contain the following layers:

---
### 3.1 Metadata Layer

Defines identity and classification.

```json
{
  "plate_id": "unique_identifier",
  "plate_type": "species | track | location | system",
  "title": "Plate Name",
  "author": "Robbie George",
  "system": "Naturepedia | RKCA",
  "version": "1.0"
}
```
### 3.2 Compression Layer

Defines core system reduction.

```json
{
  "core_entities": [],
  "key_variables": [],
  "system_summary": ""
}
```
### 3.3 Expression Layer

Defines human-readable structure.

```json
{
  "visual_structure": "description of layout",
  "patterns": [],
  "relationships": []
}
```
### 3.4 Memory Layer

Defines machine-readable structure.

```json
{
  "entities": [
    {
      "name": "",
      "type": "",
      "properties": {}
    }
  ],
  "relationships": [
    {
      "source": "",
      "target": "",
      "type": ""
    }
  ]
}
```
### 3.5 Recursion Layer

Defines graph connections.

```json
{
  "related_plates": [],
  "parent_systems": [],
  "child_systems": [],
  "cross_domain_links": []
}
```
