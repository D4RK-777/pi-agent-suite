: "ralph", iteration: <current>, current_phase: "executing"})`
- **On verification/fix transition**:
  `state_write({mode: "ralph", current_phase: "verifying"})` or `state_write({mode: "ralph", current_phase: "fixing"})`
- **On completion**:
  `state_write({mode: "ralph", active: false, current_phase: "complete", completed_at: "<now>"})`
- **On cancellation/cleanup**:
  run `$cancel` (which should call `state_clear(mode="ralph")`)


## Scenario Examples

**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.