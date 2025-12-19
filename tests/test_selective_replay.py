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


if __name__ == "__main__":
    unittest.main()


