# Diagnostics

This folder contains **architecture- and reasoning-level diagnostic checks**
used to detect inefficiency, Boundary Avoidance, and representational inflation
under Robbie’s Razor.

Diagnostics differ from tests:
- Tests verify correctness
- Diagnostics verify *structural fitness*

---

## Canonical Reference (MRD Alignment)

The architectural framework governing diagnostic interpretation is defined in:

**Master Reference Document (MRD v1.9) — Section 12  
Structural Intelligence Engineering**

Diagnostics operate within the applied recursion stability layer described in MRD §12, including:

- Complexity Threshold Collapse (CTC)
- The Governor Principle
- Energy–Recursion Coupling
- Boundary Avoidance under substrate constraint

For avoidance of doubt:

- Diagnostics do **not** modify evaluation contracts
- Diagnostics do **not** introduce required metrics
- Diagnostics do **not** alter scoring, thresholds, or pass/fail outcomes
- Diagnostics provide structural signals only

Canonical authority remains exclusively in the MRD.

## Available Diagnostics

- **Precision-Limit Check (PLC)**  
  Flags non-functional numeric precision when representation exceeds physical
  reconstruction requirements (Finite Representation Invariant).
