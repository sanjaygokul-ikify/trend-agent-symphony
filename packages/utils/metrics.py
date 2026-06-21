class MetricsAggregator:
    def __init__(self):
        self.agent_decision_count = {}

    def increment_agent_decision_count(self, agent_id: str):
        if agent_id not in self.agent_decision_count:
            self.agent_decision_count[agent_id] = 0
        self.agent_decision_count[agent_id] += 1
metrics_aggregator = MetricsAggregator()