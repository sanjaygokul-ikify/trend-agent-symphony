import logging
from typing import List, Dict
from .types import ContextVector, AgentDecision, Event
from .exceptions import InvalidContextVectorError, EventSourcingError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, shared_memory_store, metrics_aggregator):
        self.shared_memory_store = shared_memory_store
        self.metrics_aggregator = metrics_aggregator
        self.event_sourcing = {}

    def store_context_vector(self, context_vector: ContextVector):
        try:
            self.shared_memory_store.store_context_vector(context_vector)
        except Exception as e:
            logger.error(f'Error storing context vector: {e}')
            raise InvalidContextVectorError('Failed to store context vector')

    def retrieve_context_vector(self, agent_id: str) -> ContextVector:
        try:
            return self.shared_memory_store.retrieve_context_vector(agent_id)
        except Exception as e:
            logger.error(f'Error retrieving context vector: {e}')
            raise InvalidContextVectorError('Failed to retrieve context vector')

    def process_agent_decision(self, agent_decision: AgentDecision):
        try:
            event = Event(agent_decision)
            self.event_sourcing[agent_decision.agent_id] = event
            self.shared_memory_store.store_event(event)
            self.metrics_aggregator.increment_agent_decision_count(agent_decision.agent_id)
        except Exception as e:
            logger.error(f'Error processing agent decision: {e}')
            raise EventSourcingError('Failed to process agent decision')

    def get_event_sourcing(self, agent_id: str) -> List[Event]:
        try:
            return self.event_sourcing.get(agent_id, [])
        except Exception as e:
            logger.error(f'Error retrieving event sourcing: {e}')
            raise EventSourcingError('Failed to retrieve event sourcing')