import unittest
from packages.core import Engine, ContextVector, AgentDecision, Event

class TestCore(unittest.TestCase):
    def test_store_context_vector(self):
        engine = Engine('shared_memory_store', 'metrics_aggregator')
        context_vector = ContextVector('agent_id', [1.0, 2.0])
        engine.store_context_vector(context_vector)
        self.assertEqual(engine.retrieve_context_vector('agent_id').vector, [1.0, 2.0])

    def test_process_agent_decision(self):
        engine = Engine('shared_memory_store', 'metrics_aggregator')
        agent_decision = AgentDecision('agent_id', 'decision')
        engine.process_agent_decision(agent_decision)
        self.assertEqual(engine.get_event_sourcing('agent_id')[0].agent_decision.agent_id, 'agent_id')