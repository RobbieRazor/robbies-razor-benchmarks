"""
Context-rot resistance demo (toy simulation).

IMPORTANT:
- This is illustrative and non-canonical.
- Not a benchmark and not a claim about specific model performance.
- Purpose: show how an adjacency-constrained, goal-directed policy can resist
  drift under rising noise compared to an unguided policy.
"""

from __future__ import annotations
import random
from typing import Dict, Tuple, List

from tools.hex_axial_lattice import HexAxialLattice, AxialCoord


def choose_step_standard(lattice: HexAxialLattice, pos: AxialCoord, noise: float) -> AxialCoord:
    """Under noise, drift increases (more random choices)."""
    q, r = pos
    nbrs = lattice.neighbors(q, r)
    # standard: under noise, increasingly random
    if random.random() < noise:
        return random.choice(nbrs)
    return random.choice(nbrs)  # still unguided even when "not noisy"


def choose_step_razor(lattice: HexAxialLattice, pos: AxialCoord, goal: AxialCoord, noise: float, last: AxialCoord | None) -> AxialCoord:
    """
    Razor-like toy policy:
    - Prefer neighbors that reduce distance-to-goal.
    - Under noise, allow occasional suboptimal choice.
    - Avoid immediate backtracking when possible (tiny 'memory discipline').
    """
    q, r = pos
    nbrs = lattice.neighbors(q, r)

    # Score neighbors by distance-to-goal
    scored = sorted(nbrs, key=lambda n: lattice.axial_distance(n, goal))

    # Avoid immediate backtrack if possible
    if last is not None and len(scored) > 1 and scored[0] == last:
        # pick next best that isn't backtracking
        for cand in scored[1:]:
            if cand != last:
                scored = [cand] + [x for x in scored if x != cand]
                break

    # Under noise, sometimes pick a worse option
    if random.random() < noise:
        # choose among top 3 to keep it plausible, not fully random
        return random.choice(scored[: min(3, len(scored))])

    return scored[0]


def run_rot_demo(tokens: int = 100_000, step_size: int = 1_000, seed: int = 7) -> List[Dict]:
    random.seed(seed)
    lattice = HexAxialLattice(size=1.0)

    steps = tokens // step_size
    goal: AxialCoord = (25, -10)  # fixed target (toy)

    standard = (0, 0)
    razor = (0, 0)
    razor_last = None

    logs = []
    print(f"--- Context Rot Resistance Demo (toy) ---")
    print(f"tokens={tokens} step_size={step_size} steps={steps} goal={goal} seed={seed}")
    print(f"{'Tokens':<10} | {'Std dist->goal':<14} | {'Razor dist->goal':<16} | {'Noise'}")
    print("-" * 70)

    for i in range(1, steps + 1):
        cur_tokens = i * step_size
        noise = min(0.05 + (cur_tokens / tokens) * 0.6, 0.9)

        standard = choose_step_standard(lattice, standard, noise)
        std_goal_dist = lattice.axial_distance(standard, goal)

        nxt = choose_step_razor(lattice, razor, goal, noise, razor_last)
        razor_last = razor
        razor = nxt
        raz_goal_dist = lattice.axial_distance(razor, goal)

        if i % 10 == 0 or i == steps:
            print(f"{cur_tokens:<10} | {std_goal_dist:<14} | {raz_goal_dist:<16} | {noise:.2f}")

        logs.append({
            "tokens": cur_tokens,
            "noise": noise,
            "standard_pos": standard,
            "razor_pos": razor,
            "standard_goal_dist": std_goal_dist,
            "razor_goal_dist": raz_goal_dist,
        })

    return logs


if __name__ == "__main__":
    run_rot_demo()
