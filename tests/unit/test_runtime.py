import unittest
from packages.utils import metrics_aggregator

class TestRuntime(unittest.TestCase):
    def test_metrics_aggregator(self):
        metrics_aggregator.increment_agent_decision_count('agent_id')
        metrics_aggregator.increment_agent_decision_count('agent_id')
        self.assertEqual(metrics_aggregator.agent_decision_count['agent_id'], 2)