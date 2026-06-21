import unittest
from packages.core import Engine, ContextVector, AgentDecision, Event
from packages.services import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine('shared_memory_store', 'metrics_aggregator')
        orchestrator = Orchestrator(engine)
        context_vector = ContextVector('agent_id', [1.0, 2.0])
        engine.store_context_vector(context_vector)
        agent_decision = AgentDecision('agent_id', 'decision')
        engine.process_agent_decision(agent_decision)
        orchestrator.run()
        self.assertEqual(engine.retrieve_context_vector('agent_id').vector, [1.0, 2.0])