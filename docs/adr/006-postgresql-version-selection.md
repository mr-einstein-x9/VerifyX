# ADR-006: PostgreSQL 15 Container Selection for Local Development

- **Status**: Accepted
- **Date**: 2026-10-29
- **Deciders**: Engineering Team

## Context
Milestone M0 and subsequent milestones (M1–M9) require PostgreSQL with support for `pgcrypto`, JSONB, standard ACID transaction guarantees, and asyncpg driver compatibility (`SQLAlchemy 2.0+`).
During initial environment orchestration, the uncached `postgres:16-alpine` image download experienced network stalling on Windows Docker Desktop. In contrast, `postgres:15` was pre-cached locally on the workstation.

## Decision
We standardize the local Docker development container on `postgres:15` (mapped from container port `5432` to host port `5433`).

## Consequences
- **Compatibility**: PostgreSQL 15 provides full compatibility with all schema constructs required for VerifyX (UUIDs via `gen_random_uuid()`, check constraints, partial indexes, and PL/pgSQL triggers for `audit_logs` immutability).
- **Zero Network Delay**: Instant container startup from local Docker cache.
- **Port Isolation**: Binds cleanly to port `5433`, avoiding any collision with local host PostgreSQL services on port `5432`.
- **Production Alignment**: PostgreSQL 15/16 feature sets for our data model are identical; future major upgrades can be applied without schema changes.
