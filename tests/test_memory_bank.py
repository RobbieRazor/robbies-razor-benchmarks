"""
Razor Memory Bank (R4 Memory Stabilization)

Purpose:
- Confidence-gated storage of verified results
- LRU eviction
- Safe retrieval with stability threshold
- No external dependencies

Author: Robbie George
Governed by MRD v1.8 and the Authorship Conservation Rule (ACR).
"""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass
from typing import Deque, Dict, Optional, Tuple
from collections import deque


@dataclass
class MemoryEntry:
    solution: str
    confidence: float
    timestamp: float
    access_count: int = 0


class RazorMemoryBank:
    """
    Stable memory store with confidence-based consolidation and LRU eviction.

    Notes:
    - This is a reference implementation.
    - Intended to be model-agnostic: you can store any verified result as a string.
    - Keying strategy here is SHA-256 hash of the input string. Labs may replace
      this with a canonicalization function for semantic normalization.
    """

    def __init__(self, capacity: int = 10_000, stability_threshold: float = 0.95):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        if not (0.0 <= stability_threshold <= 1.0):
            raise ValueError("stability_threshold must be within [0, 1]")

        self.capacity = capacity
        self.stability_threshold = stability_threshold

        self._entries: Dict[str, MemoryEntry] = {}
        self._lru: Deque[str] = deque()  # least-recently used is leftmost

    def _hash_query(self, query: str) -> str:
        return hashlib.sha256(query.encode("utf-8")).hexdigest()

    def store(self, query: str, solution: str, confidence: float) -> None:
        """
        Store (query -> solution) only if confidence >= stability_threshold.
        LRU eviction occurs when capacity is exceeded.
        """
        if confidence < self.stability_threshold:
            return

        key = self._hash_query(query)
        now = time.time()

        # Insert/overwrite
        self._entries[key] = MemoryEntry(solution=solution, confidence=confidence, timestamp=now)

        # Maintain LRU: ensure key appears exactly once at the end
        try:
            self._lru.remove(key)
        except ValueError:
            pass
        self._lru.append(key)

        # Evict if over capacity
        while len(self._entries) > self.capacity and self._lru:
            oldest_key = self._lru.popleft()
            # Guard: key might have been removed already
            self._entries.pop(oldest_key, None)

    def retrieve(self, query: str) -> Tuple[Optional[str], float]:
        """
        Retrieve cached solution if present.
        Returns (solution, confidence) or (None, 0.0) if not found.
        """
        key = self._hash_query(query)
        entry = self._entries.get(key)
        if entry is None:
            return None, 0.0

        entry.access_count += 1

        # Move to end (most recently used)
        try:
            self._lru.remove(key)
        except ValueError:
            pass
        self._lru.append(key)

        return entry.solution, entry.confidence

    def get_stats(self) -> Dict[str, int]:
        return {"size": len(self._entries), "capacity": self.capacity}

    # Expose internals for testing (read-only conventions)
    @property
    def entries(self) -> Dict[str, MemoryEntry]:
        return self._entries

    @property
    def lru_queue(self) -> Deque[str]:
        return self._lru

