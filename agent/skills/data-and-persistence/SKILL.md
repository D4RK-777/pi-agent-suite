---
name: data-and-persistence
description: >-
  Use when designing or changing schemas, queries, migrations, persistence boundaries, data
  lifecycle rules, or storage models. Triggers on "database", "schema", "migration", "query",
  "persistence", "data model", "table", "index", or "backfill".
trigger: database, schema, migration
tags:
  - backend
  - database
  - persistence
  - schema
  - migration
  - query
---

# Data And Persistence

## Purpose

Use this skill when the core of the task is data shape, storage behavior, query safety, or data
lifecycle. It covers schema changes, persistence boundaries, migration safety, and query design.

This skill complements `backend-engineering` rather than replacing it. Use it when the data
model itself is the hard part.

## When to Use

- Designing or revising schemas or data models
- Writing or reviewing migrations and backfills
- Query performance, correctness, or lifecycle concerns
- Defining deletion, archival, retention, or ownership rules
- Designing indexes, pagination, or lookup paths

## Rules

- Model invariants before tables, fields, or documents.
- Make migrations forward-safe and rollback-aware.
- Treat backfills as operational work, not casual scripts.
- Avoid destructive data changes without explicit lifecycle reasoning.
- Prefer explicit ownership and retention rules over implicit assumptions.
- Protect against duplicate writes, orphaned records, and ambiguous deletes.
- If the main issue is runtime breakage during rollout, involve `reliability`.

## Workflow

1. Define the data truth.
   - What entities exist, what must remain true, and who owns them?
2. Define lifecycle.
   - Create, update, delete, archive, recover, and backfill behavior.
3. Design the access path.
   - Queries, indexes, pagination, consistency, and cardinality.
4. Plan the change.
   - Migration order, safety checks, rollout risk, and cleanup path.
5. Verify impact.
   - Existing reads, writes, jobs, analytics, and downstream consumers.

## Expected Output

- clearer data model or migration plan
- safe persistence recommendations
- notes on operational or rollout risk when relevant
