---
name: backend-engineering
description: >-
  Use when building or changing backend implementation: API routes, server actions, middleware,
  background jobs, webhooks, integration contracts, validation, or server-side business logic.
  Triggers on "API", "endpoint", "backend", "server", "middleware", "webhook", "job", "worker",
  "server action", or when logic runs off the browser.
trigger: backend, API, server, middleware
tags:
  - backend
  - api
  - server
  - middleware
  - validation
  - integration
---

# Backend Engineering

## Purpose

Use this skill for backend implementation and server-side system design. It covers request
boundaries, validation, mutation paths, domain logic placement, integration contracts, and
failure handling.

This skill is for building server behavior correctly. Pair it with `security-and-auth` for
high-risk flows, with `data-and-persistence` for schema/query work, and with reliability skills
when the main problem is operational rather than implementation.

## When to Use

- Building or changing API routes, endpoints, or handlers
- Implementing server actions or mutation paths
- Writing middleware, webhook handlers, jobs, or workers
- Defining input validation and response contracts
- Designing provider boundaries and service abstractions
- Refactoring server logic into clearer layers

## Rules

- Validate every external input before it reaches domain logic.
- Make contracts explicit: request shape, response shape, error shape, side effects.
- Keep orchestration separate from business rules where possible.
- Make write paths idempotent when retries are plausible.
- Prefer explicit failure handling over silent fallbacks.
- Never leak internal errors, secrets, or provider implementation details to clients.
- If the change touches auth, permissions, secrets, or sensitive data, load `security-and-auth`.
- If the change touches schema design, migrations, query safety, or lifecycle rules, load `data-and-persistence`.

## Workflow

1. Define the boundary.
   - What triggers this code: request, event, job, or internal call?
2. Define the contract.
   - Inputs, outputs, validation rules, ownership checks, and error model.
3. Place the logic.
   - Separate transport concerns from domain rules and provider integration.
4. Implement for retries and failure.
   - Handle partial failure, duplicate events, timeouts, and downstream instability.
5. Verify the change.
   - Confirm behavior, error handling, and security boundaries before closing.

## Expected Output

- production-ready server logic
- explicit contracts and validation
- safe error behavior
- clear notes on related persistence, security, or reliability follow-up
