# razor_metrics/shear.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class ShearConfig:
    """
    Configuration for Shear Capacity (SC) computation.

    core_boundary_threshold:
      - steps with boundary >= threshold are treated as "core"
      - everything else is treated as potentially shearable overhead
    """
    core_boundary_threshold: float = 0.80
    cost_key: str = "cost"
    boundary_key: str = "boundary"  # optional per-step value in [0,1]


def compute_shear_capacity(steps: List[Dict[str, Any]], cfg: ShearConfig = ShearConfig()) -> Dict[str, float]:
    """
    Shear Capacity (SC): fraction of total compute cost that is non-core overhead.

    Definitions:
      - total_cost = sum(cost_t)
      - core_cost  = sum(cost_t for steps with boundary_t >= threshold)
      - SC = 1 - core_cost / total_cost

    Notes:
      - If "boundary" is missing from the run logs, SC is returned as NaN (undefined),
        so we do not accidentally imply "perfect" SC.
      - Lower SC is generally better (less overhead).
    """
    total_cost = 0.0
    core_cost = 0.0

    has_boundary = any(cfg.boundary_key in s for s in steps)

    for s in steps:
        cost = float(s.get(cfg.cost_key, 0.0))
        total_cost += cost

        if has_boundary:
            b = s.get(cfg.boundary_key, None)
            if b is not None and float(b) >= cfg.core_boundary_threshold:
                core_cost += cost

    if total_cost <= 0.0:
        return {
            "total_cost": 0.0,
            "core_cost": 0.0,
            "shear_capacity": float("nan"),
        }

    # If boundary isn't present, we do not fabricate SC.
    if not has_boundary:
        return {
            "total_cost": total_cost,
            "core_cost": 0.0,
            "shear_capacity": float("nan"),
        }

    sc = 1.0 - (core_cost / total_cost)

    # Clamp for numeric safety
    sc = max(0.0, min(1.0, sc))

    return {
        "total_cost": total_cost,
        "core_cost": core_cost,
        "shear_capacity": sc,
    }
