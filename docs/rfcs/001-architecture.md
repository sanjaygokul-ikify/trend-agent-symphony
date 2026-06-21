# RFC 001: Core Architecture

## System Contract
1. All agent interactions must be auditable
2. Memory store API must guarantee linearizability
3. Coordination service must implement bounded liveness

## Component Contracts
- Auth Service: Provide JWT bearer tokens with role-specific capabilities
- Memory Store: Support ACID transactions for critical operations
- Task Scheduler: Ensure deterministic scheduling for reproducible workflows

## Protocol Details
- gRPC with Protobuf for inter-service communication
- Memory store uses RocksDB for primary storage
- Event sourcing protocol follows Apache Kafka patterns