# razor_metrics/facets.py
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Tuple, List

import numpy as np

Axial = Tuple[int, int]  # (q, r)


@dataclass(frozen=True)
class HexFacetConfig:
    # Controls the granularity (smaller -> more cells)
    cell_size: float = 0.25
    # Deterministic projection seed (stable facet assignment)
    seed: int = 1337


def _deterministic_project_to_2d(vec: np.ndarray, seed: int) -> np.ndarray:
    """
    Deterministic random projection from R^d -> R^2.
    Stable across machines given the same seed.
    """
    rng = np.random.default_rng(seed)
    W = rng.standard_normal((2, vec.shape[0]))
    xy = W @ vec
    return xy.astype(float)


def _axial_round(q: float, r: float) -> Axial:
    """
    Round axial coords using cube-rounding.
    """
    x = q
    z = r
    y = -x - z

    rx = round(x)
    ry = round(y)
    rz = round(z)

    dx = abs(rx - x)
    dy = abs(ry - y)
    dz = abs(rz - z)

    if dx > dy and dx > dz:
        rx = -ry - rz
    elif dy > dz:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return int(rx), int(rz)


def embedding_to_facet(embedding: Iterable[float], cfg: HexFacetConfig = HexFacetConfig()) -> Axial:
    """
    Map an embedding vector -> hex facet axial coords (q, r).
    """
    v = np.asarray(list(embedding), dtype=float)

    # Normalize for scale-invariance
    n = np.linalg.norm(v)
    if n > 0:
        v = v / n

    xy = _deterministic_project_to_2d(v, cfg.seed)
    x, y = float(xy[0]), float(xy[1])

    # Convert 2D point -> axial hex coords (pointy-top layout)
    size = cfg.cell_size
    q = (math.sqrt(3) / 3 * x - 1 / 3 * y) / size
    r = (2 / 3 * y) / size

    return _axial_round(q, r)


def neighbors(facet: Axial) -> List[Axial]:
    q, r = facet
    dirs = [(+1, 0), (+1, -1), (0, -1), (-1, 0), (-1, +1), (0, +1)]
    return [(q + dq, r + dr) for dq, dr in dirs]


def is_same_or_neighbor(a: Axial, b: Axial) -> bool:
    return a == b or b in set(neighbors(a))


def facet_distance(a: Axial, b: Axial) -> int:
    """
    Hex grid distance (cube distance) between axial coords.
    """
    aq, ar = a
    bq, br = b
    return (abs(aq - bq) + abs((aq + ar) - (bq + br)) + abs(ar - br)) // 2
