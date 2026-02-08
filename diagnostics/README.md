# Diagnostics

This folder contains **architecture- and reasoning-level diagnostic checks**
used to detect inefficiency, Boundary Avoidance, and representational inflation
under Robbie’s Razor.

Diagnostics differ from tests:
- Tests verify correctness
- Diagnostics verify *structural fitness*

## Available Diagnostics

- **Precision-Limit Check (PLC)**  
  Flags non-functional numeric precision when representation exceeds physical
  reconstruction requirements (Finite Representation Invariant).
