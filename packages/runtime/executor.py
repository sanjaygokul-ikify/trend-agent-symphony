from typing import List, Dict
from packages.core.engine import Engine
from packages.core.types import ContextVector, AgentDecision, Event

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute_agent_decision(self, agent_decision: AgentDecision):
        self.engine.process_agent_decision(agent_decision)

    def store_context_vector(self, context_vector: ContextVector):
        self.engine.store_context_vector(context_vector)

    def retrieve_context_vector(self, agent_id: str) -> ContextVector:
        return self.engine.retrieve_context_vector(agent_id)

    def get_event_sourcing(self, agent_id: str) -> List[Event]:
        return self.engine.get_event_sourcing(agent_id)