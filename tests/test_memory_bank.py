import unittest
import time

from src.razor.memory_bank import RazorMemoryBank


class TestRazorMemoryBank(unittest.TestCase):
    def setUp(self):
        self.bank = RazorMemoryBank(capacity=3, stability_threshold=0.90)

    def test_store_below_threshold(self):
        self.bank.store("q1", "s1", confidence=0.80)
        sol, conf = self.bank.retrieve("q1")
        self.assertIsNone(sol)
        self.assertEqual(conf, 0.0)

    def test_store_and_retrieve(self):
        self.bank.store("q1", "s1", confidence=0.95)
        sol, conf = self.bank.retrieve("q1")
        self.assertEqual(sol, "s1")
        self.assertEqual(conf, 0.95)

    def test_lru_eviction(self):
        # Fill capacity
        self.bank.store("q1", "s1", 0.95)
        self.bank.store("q2", "s2", 0.95)
        self.bank.store("q3", "s3", 0.95)
        self.assertEqual(self.bank.get_stats()["size"], 3)

        # Add 4th => evict oldest (q1)
        self.bank.store("q4", "s4", 0.95)
        sol, _ = self.bank.retrieve("q1")
        self.assertIsNone(sol)

        # New item exists
        sol, _ = self.bank.retrieve("q4")
        self.assertEqual(sol, "s4")

    def test_recent_access_prevents_eviction(self):
        self.bank.store("q1", "s1", 0.95)
        self.bank.store("q2", "s2", 0.95)
        self.bank.store("q3", "s3", 0.95)

        # Touch q1 so it becomes most recent
        self.bank.retrieve("q1")

        # Add q4 => should evict q2 (least recently used)
        self.bank.store("q4", "s4", 0.95)

        sol2, _ = self.bank.retrieve("q2")
        sol1, _ = self.bank.retrieve("q1")

        self.assertIsNone(sol2)
        self.assertEqual(sol1, "s1")

    def test_timestamp_set(self):
        self.bank.store("q1", "s1", 0.95)
        key = self.bank._hash_query("q1")
        entry = self.bank.entries[key]
        self.assertTrue(entry.timestamp <= time.time())


if __name__ == "__main__":
    unittest.main()


