import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from anarchi_system import Signal, route_signal


class RouterTests(unittest.TestCase):
    def test_executes_high_confidence_low_risk_signal(self):
        decision = route_signal(Signal("dashboard", "metric", 0.9, 0.2, {}))

        self.assertEqual(decision.action, "execute")
        self.assertFalse(decision.requires_ai)

    def test_blocks_high_risk_signal(self):
        decision = route_signal(Signal("treasury", "transfer", 0.95, 0.9, {}))

        self.assertEqual(decision.action, "hold")
        self.assertFalse(decision.requires_ai)

    def test_escalates_only_after_low_confidence(self):
        decision = route_signal(Signal("market", "ambiguous_news", 0.3, 0.4, {}))

        self.assertEqual(decision.action, "escalate")
        self.assertTrue(decision.requires_ai)

    def test_rejects_invalid_bounds(self):
        decision = route_signal(Signal("sensor", "bad", 1.2, 0.1, {}))

        self.assertEqual(decision.action, "reject")


if __name__ == "__main__":
    unittest.main()

