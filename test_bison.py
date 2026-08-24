import unittest
from bison import Component, BisonSystem

class TestBison(unittest.TestCase):
    def test_under_capacity_no_queue(self):
        s = BisonSystem({"a":Component(100,100)})
        out = s.step({"a":50})
        self.assertEqual(out["components"]["a"]["queue"],0.0)

    def test_overload_builds_queue(self):
        s = BisonSystem({"a":Component(100,100)})
        out = s.step({"a":150})
        self.assertGreater(out["components"]["a"]["queue"],0.0)

    def test_queue_bound_detected(self):
        s = BisonSystem({"a":Component(10,5)}, critical_latency_limit=99)
        out = s.step({"a":30})
        self.assertGreaterEqual(out["total_violations"],1)

if __name__ == "__main__":
    unittest.main()
