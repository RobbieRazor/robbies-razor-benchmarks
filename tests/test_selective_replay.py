import unittest

from src.razor.selective_replay import SelectiveReplayBuffer


class TestSelectiveReplayBuffer(unittest.TestCase):
    def setUp(self):
        # Seeded for repeatability
        self.buf = SelectiveReplayBuffer(capacity=5, seed=123)

    def test_capacity_eviction_keeps_high_scores(self):
        # Add more than capacity with increasing loss (higher score)
        for i in range(10):
            self.buf.add_example(
                query=f"q{i}",
                target=f"t{i}",
                loss=float(i),           # increasing entropy
                confidence=1.0 - i / 10.0 # decreasing confidence
            )

        self.assertEqual(len(self.buf.buffer), 5)
        remaining = {e.query for e in self.buf.buffer}

        # Expect top-scoring items (last few) to remain
        for q in ["q9", "q8", "q7", "q6", "q5"]:
            self.assertIn(q, remaining)

    def test_empty_buffer_returns_empty(self):
        empty = SelectiveReplayBuffer(capacity=5, seed=123)
        batch = empty.sample_batch(batch_size=10, replace=False)
        self.assertEqual(batch, [])

    def test_no_duplicates_when_no_replacement(self):
        for i in range(5):
            self.buf.add_example(f"q{i}", f"t{i}", loss=1.0, confidence=0.5)

        batch = self.buf.sample_batch(batch_size=5, replace=False)
        queries = [q for q, _ in batch]
        self.assertEqual(len(queries), len(set(queries)))  # no duplicates

    def test_weighted_sampling_bias(self):
        # One low score, one high score
        self.buf = SelectiveReplayBuffer(capacity=10, seed=123)

        self.buf.add_example("low", "t_low", loss=0.1, confidence=0.95)    # low score
        self.buf.add_example("high", "t_high", loss=10.0, confidence=0.1)  # high score

        counts = {"low": 0, "high": 0}
        for _ in range(400):
            q, _ = self.buf.sample_batch(batch_size=1, replace=True)[0]
            counts[q] += 1

        self.assertGreater(counts["high"], counts["low"])

    def test_rarity_influence(self):
        # Same loss/confidence, different rarity
        self.buf = SelectiveReplayBuffer(capacity=10, seed=123)

        self.buf.add_example("q_low", "t", loss=5.0, confidence=0.5, rarity=0.0)
        self.buf.add_example("q_high", "t", loss=5.0, confidence=0.5, rarity=1.0)

        counts = {"q_low": 0, "q_high": 0}
        for _ in range(400):
            q, _ = self.buf.sample_batch(batch_size=1, replace=True)[0]
            counts[q] += 1

        self.assertGreater(counts["q_high"], counts["q_low"])

    def test_score_prioritizes_loss_and_low_confidence(self):
        buf = SelectiveReplayBuffer(capacity=10, seed=123)

        # Same rarity, compare two examples:
        # A) low loss + high confidence
        # B) high loss + low confidence (should score higher)
        score_a = buf.add_example("a", "ta", loss=0.1, confidence=0.95, rarity=0.0)
        score_b = buf.add_example("b", "tb", loss=10.0, confidence=0.10, rarity=0.0)

        self.assertGreater(score_b, score_a)

        # Ensure top-scoring item appears in buffer
        top = max(buf.buffer, key=lambda e: e.score)
        self.assertEqual(top.query, "b")

    def test_sampling_replace_true_can_repeat(self):
        buf = SelectiveReplayBuffer(capacity=10, seed=123)
        for i in range(3):
            buf.add_example(f"q{i}", f"t{i}", loss=1.0, confidence=0.5)

        batch = buf.sample_batch(batch_size=50, replace=True)
        queries = [q for q, _ in batch]

        # With replacement and many draws, repeats are expected
        self.assertLess(len(set(queries)), len(queries))

    def test_equal_scores_do_not_crash_and_sample_valid(self):
        buf = SelectiveReplayBuffer(capacity=10, seed=123)

        # Add items with identical scores
        for i in range(5):
            buf.add_example(f"q{i}", f"t{i}", loss=1.0, confidence=0.5, rarity=0.0)

        batch = buf.sample_batch(batch_size=5, replace=False)
        self.assertEqual(len(batch), 5)

        # All returned items should be among inserted queries
        inserted = {f"q{i}" for i in range(5)}
        returned = {q for q, _ in batch}
        self.assertTrue(returned.issubset(inserted))

if __name__ == "__main__":
    unittest.main()


