"""
Hex recursion stress test (demo utility).

Purpose:
- Demonstrate the difference between adjacency-constrained recursion
  and unconstrained recursion on a hex axial lattice.
- Produces non-trivial metrics (not guaranteed 100% "stable").

IMPORTANT:
- This is NOT part of the benchmark evaluation pipeline.
- It is a diagnostic / visualization-friendly tool.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

from tools.hex_axial_lattice import HexAxialLattice, AxialCoord


@dataclass
class StepLog:
    step: int
    prev: AxialCoord
    cur: AxialCoord
    step_dist: int
    jumped: bool


def _random_neighbor(lattice: HexAxialLattice, q: int, r: int) -> AxialCoord:
    return random.choice(lattice.neighbors(q, r))


def _random_far_jump(q: int, r: int, radius: int) -> AxialCoord:
    """
    Random "non-local" jump within a square window; not guaranteed to land on a perfect ring.
    That's fine for a demo stress test.
    """
    dq = random.randint(-radius, radius)
    dr = random.randint(-radius, radius)
    return (q + dq, r + dr)


def run_path(
    lattice: HexAxialLattice,
    steps: int = 500,
    jump_prob: float = 0.02,
    jump_radius: int = 25,
    seed: int = 0,
    constrained: bool = True,
) -> List[StepLog]:
    """
    Generate a path on the lattice.

    constrained=True:
      always move to a neighbor (no jumps)
    constrained=False:
      with probability jump_prob, do a non-local jump of size ~jump_radius
    """
    random.seed(seed)

    q, r = 0, 0
    logs: List[StepLog] = []

    for i in range(1, steps + 1):
        prev = (q, r)

        jumped = False
        if (not constrained) and (random.random() < jump_prob):
            q, r = _random_far_jump(q, r, radius=jump_radius)
            jumped = True
        else:
            q, r = _random_neighbor(lattice, q, r)

        cur = (q, r)
        step_dist = lattice.axial_distance(prev, cur)

        logs.append(StepLog(step=i, prev=prev, cur=cur, step_dist=step_dist, jumped=jumped))

    return logs


def summarize(logs: List[StepLog]) -> Dict[str, float]:
    """
    Summarize path behavior.
    A "closure failure" here is operationally defined as a non-local step (distance > 1).
    """
    steps = len(logs)
    if steps == 0:
        return {}

    jump_count = sum(1 for s in logs if s.jumped)
    closure_failures = sum(1 for s in logs if s.step_dist > 1)

    avg_step_dist = sum(s.step_dist for s in logs) / steps
    max_step_dist = max(s.step_dist for s in logs)

    return {
        "steps": float(steps),
        "jump_rate": jump_count / steps,
        "closure_failure_rate": closure_failures / steps,
        "avg_step_distance": avg_step_dist,
        "max_step_distance": float(max_step_dist),
    }


def main() -> None:
    lattice = HexAxialLattice(size=1.0)

    steps = 500

    constrained_logs = run_path(
        lattice=lattice,
        steps=steps,
        constrained=True,
        seed=42,
    )

    unconstrained_logs = run_path(
        lattice=lattice,
        steps=steps,
        constrained=False,
        jump_prob=0.03,     # tweak to taste
        jump_radius=40,     # tweak to taste
        seed=42,
    )

    c = summarize(constrained_logs)
    u = summarize(unconstrained_logs)

    print("--- Hex Recursion Stress Test (Demo) ---")
    print(f"steps: {steps}")
    print("")
    print("[Constrained: neighbor-only]")
    for k, v in c.items():
        print(f"  {k}: {v}")
    print("")
    print("[Unconstrained: occasional non-local jumps]")
    for k, v in u.items():
        print(f"  {k}: {v}")
    print("")
    print("Interpretation:")
    print("- Constrained path should show closure_failure_rate ~ 0 and max_step_distance = 1.")
    print("- Unconstrained path should show non-zero closure_failure_rate and larger max_step_distance.")


if __name__ == "__main__":
    main()
