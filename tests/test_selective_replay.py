"""
Selective Replay Tests — Robbie's Razor Compliance Framework

Purpose:
- Validate repository-level SelectiveReplayBuffer behavior.
- Confirm capacity-based retention of higher-scoring examples.
- Confirm weighted replay-priority behavior.
- Confirm sampling with and without replacement.
- Confirm deterministic test reproducibility under the declared seed.
- Confirm that supplied rarity, loss, and confidence inputs influence the
  composite priority score according to the implementation contract.

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
- src/razor/selective_replay.py

Interpretation boundary:
- These tests validate software behavior only.
- Passing tests do not independently establish that selective replay reduces
  catastrophic forgetting, hallucination, semantic drift, or real-world
  compute requirements.
- The implementation's `loss` value is a caller-supplied priority input.
  These tests do not establish that it is information-theoretic entropy.
- The `confidence` and `rarity` values used here are synthetic test inputs.
- Higher replay priority means only higher score or sampling probability under
  the configured implementation.
- A replay-priority result is not a correctness, truth, evidence, or empirical
  validation score.
- The bounded batch-size tests validate behavior under a software replay
  budget; they do not independently establish an energetic or physical law.
- Historical frozen or versioned artifacts may retain earlier MRD references
  when required for genuine provenance and should not be silently rewritten.

Reference-implementation boundary:
- Passing repository tests demonstrates conformance to the tested software
  contract.
- Test success does not redefine canonical theory.
- Test success does not independently validate Robbie's Razor or the
  Grand Compression Framework.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
"""

import unittest

from src.razor.selective_replay import SelectiveReplayBuffer


class TestSelectiveReplayBuffer(unittest.TestCase):
    def setUp(self):
        # Seeded for repeatable repository tests.
        self.buf = SelectiveReplayBuffer(
            capacity=5,
            seed=123,
        )

    def test_capacity_eviction_keeps_high_scores(self):
        """
        When capacity is exceeded, the implementation retains the
        highest composite-score examples.
        """
        # Add more examples than capacity with increasing loss and
        # decreasing confidence, both of which increase score under
        # the configured implementation.
        for i in range(10):
            self.buf.add_example(
                query=f"q{i}",
                target=f"t{i}",
                loss=float(i),
                confidence=1.0 - i / 10.0,
            )

        self.assertEqual(
            len(self.buf.buffer),
            5,
        )

        remaining = {
            e.query
            for e in self.buf.buffer
        }

        # Under this configured scoring rule, the final five examples
        # have the highest composite scores.
        for q in [
            "q9",
            "q8",
            "q7",
            "q6",
            "q5",
        ]:
            self.assertIn(
                q,
                remaining,
            )

    def test_empty_buffer_returns_empty(self):
        """
        Sampling an empty buffer returns an empty list.
        """
        empty = SelectiveReplayBuffer(
            capacity=5,
            seed=123,
        )

        batch = empty.sample_batch(
            batch_size=10,
            replace=False,
        )

        self.assertEqual(
            batch,
            [],
        )

    def test_no_duplicates_when_no_replacement(self):
        """
        Sampling without replacement must not return duplicate examples
        within the requested batch.
        """
        for i in range(5):
            self.buf.add_example(
                f"q{i}",
                f"t{i}",
                loss=1.0,
                confidence=0.5,
            )

        batch = self.buf.sample_batch(
            batch_size=5,
            replace=False,
        )

        queries = [
            q
            for q, _ in batch
        ]

        self.assertEqual(
            len(queries),
            len(set(queries)),
        )

    def test_weighted_sampling_bias(self):
        """
        An example with a substantially higher composite score should
        be sampled more frequently than a substantially lower-score
        example under repeated weighted sampling with replacement.
        """
        self.buf = SelectiveReplayBuffer(
            capacity=10,
            seed=123,
        )

        self.buf.add_example(
            "low",
            "t_low",
            loss=0.1,
            confidence=0.95,
        )

        self.buf.add_example(
            "high",
            "t_high",
            loss=10.0,
            confidence=0.1,
        )

        counts = {
            "low": 0,
            "high": 0,
        }

        for _ in range(400):
            q, _ = self.buf.sample_batch(
                batch_size=1,
                replace=True,
            )[0]

            counts[q] += 1

        self.assertGreater(
            counts["high"],
            counts["low"],
        )

    def test_rarity_influence(self):
        """
        With loss and confidence held constant, a higher supplied
        rarity value should increase the composite priority score and,
        under repeated weighted sampling, increase sampling frequency.
        """
        self.buf = SelectiveReplayBuffer(
            capacity=10,
            seed=123,
        )

        self.buf.add_example(
            "q_low",
            "t",
            loss=5.0,
            confidence=0.5,
            rarity=0.0,
        )

        self.buf.add_example(
            "q_high",
            "t",
            loss=5.0,
            confidence=0.5,
            rarity=1.0,
        )

        counts = {
            "q_low": 0,
            "q_high": 0,
        }

        for _ in range(400):
            q, _ = self.buf.sample_batch(
                batch_size=1,
                replace=True,
            )[0]

            counts[q] += 1

        self.assertGreater(
            counts["q_high"],
            counts["q_low"],
        )

    def test_score_prioritizes_loss_and_low_confidence(self):
        """
        Under the default weighting rule, higher supplied loss and lower
        supplied confidence should produce a higher composite score when
        rarity is held constant.
        """
        buf = SelectiveReplayBuffer(
            capacity=10,
            seed=123,
        )

        # Same rarity, different loss/confidence inputs.
        score_a = buf.add_example(
            "a",
            "ta",
            loss=0.1,
            confidence=0.95,
            rarity=0.0,
        )

        score_b = buf.add_example(
            "b",
            "tb",
            loss=10.0,
            confidence=0.10,
            rarity=0.0,
        )

        self.assertGreater(
            score_b,
            score_a,
        )

        top = max(
            buf.buffer,
            key=lambda e: e.score,
        )

        self.assertEqual(
            top.query,
            "b",
        )

    def test_sampling_replace_true_can_repeat(self):
        """
        Sampling with replacement permits the same example to appear
        multiple times.
        """
        buf = SelectiveReplayBuffer(
            capacity=10,
            seed=123,
        )

        for i in range(3):
            buf.add_example(
                f"q{i}",
                f"t{i}",
                loss=1.0,
                confidence=0.5,
            )

        batch = buf.sample_batch(
            batch_size=50,
            replace=True,
        )

        queries = [
            q
            for q, _ in batch
        ]

        self.assertLess(
            len(set(queries)),
            len(queries),
        )

    def test_equal_scores_do_not_crash_and_sample_valid(self):
        """
        Equal-score examples should remain sampleable without error,
        and returned examples must belong to the inserted set.
        """
        buf = SelectiveReplayBuffer(
            capacity=10,
            seed=123,
        )

        for i in range(5):
            buf.add_example(
                f"q{i}",
                f"t{i}",
                loss=1.0,
                confidence=0.5,
                rarity=0.0,
            )

        batch = buf.sample_batch(
            batch_size=5,
            replace=False,
        )

        self.assertEqual(
            len(batch),
            5,
        )

        inserted = {
            f"q{i}"
            for i in range(5)
        }

        returned = {
            q
            for q, _ in batch
        }

        self.assertTrue(
            returned.issubset(inserted)
        )

    def test_budget_dominance_high_priority_items(self):
        """
        Under a small software replay batch size, examples with much
        higher composite priority scores should dominate repeated
        weighted selections in this synthetic test.

        `batch_size=1` is the bounded replay-selection budget here.

        This test validates the repository's sampling rule only.
        It does not establish an energetic, physical, or universal
        resource-constraint result.
        """
        buf = SelectiveReplayBuffer(
            capacity=200,
            seed=123,
        )

        # Add five examples with deliberately high composite-priority inputs.
        high_queries = [
            f"high_{i}"
            for i in range(5)
        ]

        for q in high_queries:
            buf.add_example(
                query=q,
                target="t_high",
                loss=20.0,
                confidence=0.05,
                rarity=1.0,
            )

        # Add fifty examples with deliberately lower composite-priority inputs.
        low_queries = [
            f"low_{i}"
            for i in range(50)
        ]

        for q in low_queries:
            buf.add_example(
                query=q,
                target="t_low",
                loss=0.1,
                confidence=0.95,
                rarity=0.0,
            )

        # Repeated sampling with replacement allows the test to compare
        # aggregate selection frequency under a tight batch-size budget.
        counts = {
            q: 0
            for q in high_queries
        }

        low_count = 0

        for _ in range(400):
            q, _t = buf.sample_batch(
                batch_size=1,
                replace=True,
            )[0]

            if q in counts:
                counts[q] += 1
            else:
                low_count += 1

        high_total = sum(
            counts.values()
        )

        # Under the configured score differences and seed, the combined
        # high-priority group should dominate the lower-priority group.
        self.assertGreater(
            high_total,
            low_count,
        )


if __name__ == "__main__":
    unittest.main()
