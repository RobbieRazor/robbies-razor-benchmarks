"""
Selective Replay Buffer (R4 Memory Phase Support)

Purpose:
- Prioritize replay of high-entropy / low-confidence / rare examples
- Reduce catastrophic forgetting with minimal overhead
- Model-agnostic reference implementation (no ML framework required)

Author: Robbie George
Governed by MRD v1.8 and the Authorship Conservation Rule (ACR).
"""

from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class ReplayExample:
    query: str
    target: str
    score: float
    timestamp: float


class SelectiveReplayBuffer:
    """
    High-entropy selective replay for continual learning.

    Scoring (Razor-aligned):
    - High loss/entropy => unstable expression => prioritize
    - Low confidence => recursion trigger signal => prioritize
    - High rarity => compression edge-case => prioritize

    Sampling:
    - Weighted by softmax(score)
    - Implemented with Python stdlib (no numpy, no torch)
    """

    def __init__(
        self,
        capacity: int = 5_000,
        entropy_weight: float = 0.5,
        confidence_weight: float = 0.3,
        rarity_weight: float = 0.2,
        seed: Optional[int] = None,
    ):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")

        self.capacity = capacity
        self.entropy_weight = float(entropy_weight)
        self.confidence_weight = float(confidence_weight)
        self.rarity_weight = float(rarity_weight)

        self._buffer: List[ReplayExample] = []
        if seed is not None:
            random.seed(seed)

    @property
    def buffer(self) -> List[ReplayExample]:
        return self._buffer

    def add_example(
        self,
        query: str,
        target: str,
        loss: float,
        confidence: float,
        rarity: float = 0.0,
    ) -> float:
        """
        Add an example with a composite priority score.

        Args:
            loss: proxy for entropy (higher => higher priority)
            confidence: [0,1], lower => higher priority
            rarity: [0,1] optional (higher => higher priority)

        Returns:
            score assigned to this example
        """
        confidence = max(0.0, min(1.0, float(confidence)))
        loss = float(loss)
        rarity = float(rarity)

        score = (
            self.entropy_weight * loss
            + self.confidence_weight * (1.0 - confidence)
            + self.rarity_weight * rarity
        )

        self._buffer.append(
            ReplayExample(query=query, target=target, score=score, timestamp=time.time())
        )

        # Keep only highest-score examples if over capacity
        if len(self._buffer) > self.capacity:
            self._buffer.sort(key=lambda e: e.score, reverse=True)
            self._buffer = self._buffer[: self.capacity]

        return score

    def _softmax_probs(self) -> List[float]:
        if not self._buffer:
            return []

        scores = [e.score for e in self._buffer]
        m = max(scores)
        exps = [math.exp(s - m) for s in scores]
        total = sum(exps)

        if total <= 0:
            return [1.0 / len(exps)] * len(exps)
        return [v / total for v in exps]

    def sample_batch(self, batch_size: int = 64, replace: bool = False) -> List[Tuple[str, str]]:
        """
        Weighted sample of (query, target) pairs.

        Args:
            batch_size: number of samples requested
            replace: if True, sampling with replacement; else without

        Returns:
            list of (query, target)
        """
        if batch_size <= 0 or not self._buffer:
            return []

        k = min(batch_size, len(self._buffer)) if not replace else batch_size
        probs = self._softmax_probs()

        indices = list(range(len(self._buffer)))
        chosen: List[int] = []

        if replace:
            chosen = random.choices(indices, weights=probs, k=k)
        else:
            # Weighted sampling without replacement: iterative draw + renormalize
            pool = indices[:]
            pool_probs = probs[:]
            for _ in range(k):
                pick = random.choices(pool, weights=pool_probs, k=1)[0]
                chosen.append(pick)

                j = pool.index(pick)
                pool.pop(j)
                pool_probs.pop(j)

                if not pool:
                    break

                s = sum(pool_probs)
                pool_probs = [p / s for p in pool_probs] if s > 0 else [1.0 / len(pool)] * len(pool)

        return [(self._buffer[i].query, self._buffer[i].target) for i in chosen]
