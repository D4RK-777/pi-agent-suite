---
name: observability-and-monitoring
description: >-
  Use when designing or improving logs, metrics, traces, health checks, dashboards, or alerts.
  Triggers on "monitoring", "observability", "logging", "tracing", "dashboard", "health check",
  "alerting", "incident visibility", or "what should we measure?".
trigger: monitoring, observability, logging
tags:
  - reliability
  - monitoring
  - observability
  - logging
  - tracing
  - alerting
---

# Observability And Monitoring

## Purpose

Use this skill when the task is to make system behavior visible, measurable, and actionable in
production or staging. It covers logs, metrics, traces, health checks, dashboards, and alerts.

The goal is not more telemetry by default. The goal is actionable visibility tied to user impact
and operational response.

## When to Use

- Monitoring coverage is missing or weak
- Logs are noisy, unstructured, or unhelpful
- Health checks do not reflect real readiness
- Alerts are missing, noisy, or not actionable
- A system needs better incident visibility

## Rules

- Instrument user-facing impact first, then internal detail.
- Prefer structured logs over ad hoc text.
- Every alert should point to an action, not just a symptom.
- Avoid vanity metrics that do not change decisions.
- Health checks must reflect dependency readiness, not just process liveness.
- Add enough context for diagnosis without leaking secrets or sensitive payloads.

## Workflow

1. Identify what failure matters.
   - User pain, business impact, and operational blind spots.
2. Choose the signal.
   - Logs, metrics, traces, checks, dashboards, or alerts.
3. Make it actionable.
   - Who responds, what threshold matters, what next step follows?
4. Reduce noise.
   - Remove duplicate, low-signal, or unactionable monitoring.
5. Verify the path.
   - Confirm that real failures would be visible and understandable.

## Expected Output

- practical monitoring and instrumentation recommendations
- better health-check and alert design
- explicit visibility gaps and how to close them
