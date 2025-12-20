import unittest

from src.razor.memory_bank import RazorMemoryBank


class TestControllerIntegration(unittest.TestCase):
    """
    Minimal integration test for Razor-aligned composition.

    This test intentionally avoids model dependencies.
    It validates that a MemoryBank hit can short-circuit work in a
    controlled reasoning pipeline.
    """

    def test_memory_hit_short_circuits_work(self):
        bank = RazorMemoryBank(capacity=10, stability_threshold=0.95)

        query = "What is 17 × 23?"
        solution = "391"

        # Store a high-confidence result
        bank.store(query, solution, confidence=0.99)

        # Simulated "controller" logic:
        # First check memory; if found, return immediately.
        cached, conf = bank.retrieve(query)

        self.assertEqual(cached, solution)
        self.assertGreaterEqual(conf, 0.95)

        # Access count should have incremented
        key = bank._hash_query(query)
        self.assertEqual(bank.entries[key].access_count, 1)

        # Second retrieval increments again
        cached2, conf2 = bank.retrieve(query)
        self.assertEqual(cached2, solution)
        self.assertGreaterEqual(conf2, 0.95)
        self.assertEqual(bank.entries[key].access_count, 2)


if __name__ == "__main__":
    unittest.main()
