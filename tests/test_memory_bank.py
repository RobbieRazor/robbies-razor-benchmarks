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

    def test_store_same_query_overwrites_and_no_lru_duplicates(self):
        # Store once
        self.bank.store("q1", "s1", 0.95)
        # Store again (same query, new solution)
        self.bank.store("q1", "s1_updated", 0.95)

        # Must retrieve latest solution
        sol, conf = self.bank.retrieve("q1")
        self.assertEqual(sol, "s1_updated")
        self.assertEqual(conf, 0.95)

        # LRU queue should contain each key at most once
        lru_keys = list(self.bank.lru_queue)
        self.assertEqual(len(lru_keys), len(set(lru_keys)))

    def test_retrieve_increments_access_count_and_updates_recency(self):
        self.bank.store("q1", "s1", 0.95)
        self.bank.store("q2", "s2", 0.95)
        self.bank.store("q3", "s3", 0.95)

        # Access q1 twice
        self.bank.retrieve("q1")
        self.bank.retrieve("q1")

        key1 = self.bank._hash_query("q1")
        entry1 = self.bank.entries[key1]

        # Access count should be 2
        self.assertEqual(entry1.access_count, 2)

        # q1 should be most-recent (at end of LRU)
        self.assertEqual(list(self.bank.lru_queue)[-1], key1)

    def test_overwrite_updates_timestamp(self):
        self.bank.store("q1", "s1", 0.95)
        key = self.bank._hash_query("q1")
        t1 = self.bank.entries[key].timestamp

        # Wait a tiny moment so timestamps differ deterministically
        time.sleep(0.01)

        # Overwrite should update timestamp
        self.bank.store("q1", "s1_new", 0.95)
        t2 = self.bank.entries[key].timestamp

        self.assertGreater(t2, t1)

if __name__ == "__main__":
    unittest.main()


