# Contributor Guidelines

**Architecture Governance**:
1. All architectural decisions documented in docs/rfcs/
2. Changes requiring system contract modifications must pass through RFC process
3. Contributions must include benchmarks for new features

**Code Standards**:
- Rust code follows https://doc.rust-lang.org/edition-guide/rust-2021/edition-guide.html
- Use rust fmt & clippy on all code
- Memory allocations must be optimized

**Test Coverage**:
- Unit tests: 100% branch coverage
- Stress tests for critical paths
- Agent simulation test suite with 1k+ scenarios

**Submission Process**:
1. Create draft PR early for RFC review
2. Include performance regression tests
3. Ensure CI passes for all arch/OS combinations