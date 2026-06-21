from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ContextVector:
    agent_id: str
    vector: List[float]

@dataclass
class AgentDecision:
    agent_id: str
    decision: str

@dataclass
class Event:
    agent_decision: AgentDecision
    timestamp: float

class EventType:
    AGENT_DECISION = 'agent_decision'

class EventStatus:
    PENDING = 'pending'
    PROCESSED = 'processed'