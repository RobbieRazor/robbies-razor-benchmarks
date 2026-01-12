# Hex Lattice Geometry Utility (Non-Canonical)

This document describes an optional hex-geometry utility provided for experiments and visualization.

- The canonical theory for Robbie’s Razor remains defined outside this repository (MRD).
- The benchmark evaluation pipeline does not require hex lattice coordinates to run.
- The utility exists to support researchers who want to test adjacency-constrained reasoning paths,
  drift measures, or scale behavior using standard axial-coordinate hex math.

## File

- `tools/hex_axial_lattice.py`

## What it provides

- Axial coordinates `(q, r)` with O(1) 6-neighbor lookups
- Axial-to-Cartesian mapping for plotting and visualization
- Hex distance (via cube-coordinate equivalence)
- Optional scaled Cartesian helper (phi default) for recursion-scale experiments

## What it does *not* claim

- It is not a formal proof of geometric exclusivity
- It does not imply the repo’s benchmarks already require or enforce hex geometry
- It does not claim prevention of hallucinations by itself

## Related utilities

- A non-canonical stress-test / demonstration script exploring constrained vs. unconstrained recursion paths is available at `tools/stress_test_hex_recursion.py`.
