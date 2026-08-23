"""
Razor Memory Bank (R4 Memory Stabilization)

Purpose:
- Confidence-gated storage of results
- LRU eviction
- Safe retrieval using a declared stability threshold
- Model-agnostic local memory behavior
- No external dependencies

References:
- Razor Compliance Framework:
  https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- Razor Evaluation Protocol:
  https://www.robbiegeorgephotography.com/robbies-razor-lab-evaluation-protocol

Current governing framework authority:
- The Grand Compression Cosmology — Master Reference Document, MRD v2.0
- Canonical identifier: GC-MRD-v2.0
- Canonical claim range: RC-01 through RC-22

Repository evaluation authority:
- AGENTS.md
- docs/canonical-spec.md

Interpretation boundary:
- This module is a reference implementation of confidence-gated memory behavior.
- The supplied confidence value is an implementation input; this module does
  not independently establish that a stored solution is factually correct,
  empirically verified, or canonically validated.
- Meeting the stability threshold permits storage under this implementation.
  It does not convert confidence into truth.
- Successful retrieval establishes only that a matching stored entry exists.
- Retrieval does not independently establish correctness, evidence status,
  licensing rights, or empirical validation.
- Memory stabilization is an implementation behavior and must remain distinct
  from evidence validation.
- Historical frozen or versioned artifacts may retain earlier MRD references
  when required for genuine provenance and should not be silently rewritten.

Reference-implementation boundary:
- Implementation does not redefine canonical theory.
- Operational success does not equal universal validation.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
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

    Reference implementation.
    Model-agnostic.

    A stored confidence value is not an independent factual-verification signal.
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

        Passing this threshold authorizes storage under the reference
        implementation; it does not independently verify factual correctness.
        """
        if confidence < self.stability_threshold:
            return

        key = self._hash_query(query)
        now = time.time()

        self._entries[key] = MemoryEntry(
            solution=solution,
            confidence=confidence,
            timestamp=now,
        )

        # Maintain LRU
        try:
            self._lru.remove(key)
        except ValueError:
            pass
        self._lru.append(key)

        # Evict if over capacity
        while len(self._entries) > self.capacity and self._lru:
            oldest = self._lru.popleft()
            self._entries.pop(oldest, None)

    def retrieve(self, query: str) -> Tuple[Optional[str], float]:
        """
        Retrieve a cached solution if present.

        Retrieval reports the stored solution and confidence value only.
        It does not independently revalidate the solution.
        """
        key = self._hash_query(query)
        entry = self._entries.get(key)
        if entry is None:
            return None, 0.0

        entry.access_count += 1

        try:
            self._lru.remove(key)
        except ValueError:
            pass
        self._lru.append(key)

        return entry.solution, entry.confidence

    def get_stats(self) -> Dict[str, int]:
        return {"size": len(self._entries), "capacity": self.capacity}

    @property
    def entries(self) -> Dict[str, MemoryEntry]:
        return self._entries

    @property
    def lru_queue(self) -> Deque[str]:
        return self._lru

