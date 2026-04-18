e so session metadata stays stable across native and derived events

## Noise and duplicate controls

- `notify-hook` turn dedupe suppresses duplicate `agent-turn-complete` processing by `thread_id + turn_id + type`.
- `session-idle` emission still uses the idle cooldown gate.
- assistant-text heuristics emit follow-up signals (`retry-needed`, `handoff-needed`) but do not duplicate session completion/failure lifecycle events.
- team dispatch retry and failure events emit only on explicit queue transition branches.
- rollout-derived command events are correlated by `call_id` and only emit once per matching command lifecycle.

## Consumer guidance

clawhip should: