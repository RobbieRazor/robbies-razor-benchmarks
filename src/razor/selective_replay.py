"""
Selective Replay Buffer (R4 Memory Phase Support)

Purpose:
- Prioritize examples using declared loss, confidence, and rarity inputs
- Support selective replay with bounded storage overhead
- Provide a model-agnostic reference implementation
- Require no external ML framework

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
- This module is a repository-level reference implementation.
- It does not independently establish that selective replay reduces
  catastrophic forgetting, semantic drift, or any other failure mode.
- The `loss` input is treated as an implementation-level proxy used in
  priority scoring; this module does not independently calculate or prove
  information-theoretic entropy.
- The `confidence` input is supplied externally and is not independently
  validated by this module.
- The `rarity` input is supplied externally and depends on the caller's
  operational definition.
- A higher composite score means only that the example receives higher
  replay priority under the configured scoring rule.
- Replay priority does not establish factual correctness, evidence status,
  or canonical validity.
- Benchmark results must remain bounded to their declared system,
  workload, baseline, parameters, metrics, and evaluation conditions.
- Historical frozen or versioned artifacts may retain earlier MRD
  references when required for genuine provenance and should not be
  silently rewritten.

Reference-implementation boundary:
- Implementation does not redefine canonical theory.
- Operational success does not equal universal validation.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
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
    Selective replay reference implementation.

    Scoring:
    - Higher supplied loss increases replay priority
    - Lower supplied confidence increases replay priority
    - Higher supplied rarity increases replay priority

    These relationships are implementation choices used to construct
    the composite priority score. They are not independent evidence
    that the example is unstable, incorrect, rare in an objective
    population, or information-theoretically high-entropy.

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
            loss:
                Caller-supplied loss value used as a replay-priority proxy.
                Higher values increase priority under the configured rule.

            confidence:
                Caller-supplied confidence value. It is clamped to [0, 1].
                Lower values increase priority under the configured rule.

            rarity:
                Optional caller-supplied rarity value.
                Higher values increase priority under the configured rule.

        Returns:
            Composite priority score assigned to this example.

        The returned score is an implementation-level replay priority.
        It is not an independent correctness, evidence, or validation score.
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
            ReplayExample(
                query=query,
                target=target,
                score=score,
                timestamp=time.time(),
            )
        )

        # Keep only highest-score examples if over capacity.
        if len(self._buffer) > self.capacity:
            self._buffer.sort(key=lambda e: e.score, reverse=True)
            self._buffer = self._buffer[: self.capacity]

        return score

    def _softmax_probs(self) -> List[float]:
        """
        Convert current replay scores into normalized softmax weights.

        These probabilities control sampling priority only.
        They are not calibrated probabilities of correctness, error,
        uncertainty, or empirical support.
        """
        if not self._buffer:
            return []

        scores = [e.score for e in self._buffer]
        m = max(scores)
        exps = [math.exp(s - m) for s in scores]
        total = sum(exps)

        if total <= 0:
            return [1.0 / len(exps)] * len(exps)

        return [v / total for v in exps]

    def sample_batch(
        self,
        batch_size: int = 64,
        replace: bool = False,
    ) -> List[Tuple[str, str]]:
        """
        Weighted sample of (query, target) pairs.

        Args:
            batch_size:
                Number of samples requested.

            replace:
                If True, sample with replacement.
                If False, sample without replacement.

        Returns:
            List of (query, target) pairs selected according to the
            current replay-priority weights.

        Selection for replay does not independently verify the factual
        correctness or evidentiary status of an example.
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
            # Weighted sampling without replacement:
            # iterative draw followed by renormalization.
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
                pool_probs = (
                    [p / s for p in pool_probs]
                    if s > 0
                    else [1.0 / len(pool)] * len(pool)
                )

        return [
            (self._buffer[i].query, self._buffer[i].target)
            for i in chosen
        ]
