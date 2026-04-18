- Cancellation MUST NOT mutate mode state in unrelated sessions.

## Implementation alignment points

- `src/cli/index.ts` (`cancelModes`) enforces scoped cancellation and linked cleanup ordering.
- `skills/cancel/SKILL.md` documents scope-aware cancellation behavior and compatibility fallback policy.