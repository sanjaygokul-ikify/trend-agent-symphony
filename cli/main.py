import argparse
from packages.core import Engine
from packages.services import Orchestrator

def main():
    parser = argparse.ArgumentParser(description='Agent Symphony CLI')
    parser.add_argument('--shared-memory-store', type=str, help='shared memory store URL')
    parser.add_argument('--metrics-aggregator', type=str, help='metrics aggregator URL')
    args = parser.parse_args()

    engine = Engine(args.shared_memory_store, args.metrics_aggregator)
    orchestrator = Orchestrator(engine)
    orchestrator.run()