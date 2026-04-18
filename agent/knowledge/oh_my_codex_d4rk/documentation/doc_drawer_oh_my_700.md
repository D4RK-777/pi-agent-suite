tor`.
  Note: `deep-executor` is deprecated; route implementation to `executor`.

## Selection Rules

1. Start at `STANDARD` for most code changes.
2. Use `LOW` only when the task is bounded and non-invasive.
3. Escalate to `THOROUGH` for:
   - security/auth/trust-boundary changes
   - architectural decisions with system-wide impact
   - large refactors across many files
4. For Ralph completion checks, use at least `STANDARD` architect verification.

## Posture Guidance

- `frontier-orchestrator`:
  - Best for steerable frontier models and leader-style roles.
  - Prioritizes intent classification, delegation, verification, and architectural judgment.
  - Typical roles: `planner`, `analyst`, `architect`, `critic`, `code-reviewer`.