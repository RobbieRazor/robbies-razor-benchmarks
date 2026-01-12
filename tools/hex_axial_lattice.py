"""
Hex axial-coordinate lattice utilities (q, r) for experiments and visualization.

IMPORTANT:
- This file is NOT required by the benchmark evaluation pipeline.
- It is provided as an optional geometric utility for researchers who wish to
  explore hex-neighborhood adjacency, drift, and scale behavior in controlled tests.
"""

from __future__ import annotations
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional


AxialCoord = Tuple[int, int]
Cartesian = Tuple[float, float]


@dataclass(frozen=True)
class HexAxialLattice:
    """
    Implements an axial-coordinate (q, r) hex grid with O(1) neighbor lookup.
    Uses the standard "pointy-top" axial-to-Cartesian mapping.

    References (informal):
    - Common axial coordinate systems used in hex grid math and pathfinding.
    """

    size: float = 1.0  # side length / scale of the hex

    @staticmethod
    def phi() -> float:
        """Return golden ratio (phi). Provided as a convenience helper."""
        return (1.0 + math.sqrt(5.0)) / 2.0

    def axial_to_cartesian(self, q: int, r: int) -> Cartesian:
        """
        Map axial (q, r) to Cartesian (x, y) for pointy-top hexes.
        """
        x = self.size * (math.sqrt(3.0) * q + (math.sqrt(3.0) / 2.0) * r)
        y = self.size * (3.0 / 2.0) * r
        return (x, y)

    def neighbors(self, q: int, r: int) -> List[AxialCoord]:
        """
        Return the 6 axial neighbors of (q, r).
        """
        directions = [
            (1, 0), (1, -1), (0, -1),
            (-1, 0), (-1, 1), (0, 1),
        ]
        return [(q + dq, r + dr) for dq, dr in directions]

    def axial_distance(self, a: AxialCoord, b: AxialCoord) -> int:
        """
        Hex distance on axial coords using cube-coordinate equivalence.
        """
        aq, ar = a
        bq, br = b
        # Convert axial (q, r) to cube (x=q, z=r, y=-x-z)
        ax, az = aq, ar
        ay = -ax - az
        bx, bz = bq, br
        by = -bx - bz
        return max(abs(ax - bx), abs(ay - by), abs(az - bz))

    def scaled_cartesian(
        self,
        q: int,
        r: int,
        level: int,
        scale: Optional[float] = None,
    ) -> Cartesian:
        """
        Optional scaling of the Cartesian position across recursion "levels".

        If scale is None, uses phi() ** level.
        This method is provided for experiments; it does not imply any canonical
        requirement or exclusivity of phi-scaling.
        """
        if level < 0:
            raise ValueError("level must be >= 0")

        if scale is None:
            scale = self.phi() ** level

        x, y = self.axial_to_cartesian(q, r)
        return (x / scale, y / scale)


if __name__ == "__main__":
    # Minimal sanity check / demo usage
    lattice = HexAxialLattice(size=1.0)
    q, r = 0, 0
    print("origin:", (q, r), "->", lattice.axial_to_cartesian(q, r))
    print("neighbors:", lattice.neighbors(q, r))
    print("scaled(origin, level=2):", lattice.scaled_cartesian(q, r, level=2))
