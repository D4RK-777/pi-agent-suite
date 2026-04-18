est.ts:30-32`, `src/hooks/__tests__/prompt-guidance-scenarios.test.ts:13-33` |

Example prompt text:

> - Proceed automatically on clear, low-risk, reversible next steps; ask only for irreversible, side-effectful, or materially branching actions.
>
> **Good:** The user says `continue` after you already identified the next safe implementation step. Continue the current branch of work instead of asking for reconfirmation.

### 3. Localized task-update overrides that preserve earlier non-conflicting instructions

Contributors should treat user updates as **scoped overrides**, not full prompt resets.

Representative locations: