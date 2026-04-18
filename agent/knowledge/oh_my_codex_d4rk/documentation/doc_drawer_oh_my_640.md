# Ralph Persistence Release Gate

This checklist is a hard gate for Ralph persistence rollout.
CI/release validation MUST fail when any required scenario below is missing or failing.

## Rollout policy (fixed for this port)

- Release N: behind explicit opt-in flag `OMX_RALPH_PERSISTENCE_PORT=1`.
- Release N+1 default enablement decision only after:
  - parity drift remains clean,
  - cancellation metrics show no cross-session corruption,
  - gate scenarios V1–V10 stay green in CI.

## Verification matrix gate