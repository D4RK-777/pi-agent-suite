"autopilot", current_phase: "execution"})`
  `state_write({mode: "autopilot", current_phase: "qa"})`
  `state_write({mode: "autopilot", current_phase: "validation"})`
- **On completion**:
  `state_write({mode: "autopilot", active: false, current_phase: "complete", completed_at: "<now>"})`
- **On cancellation/cleanup**:
  run `$cancel` (which should call `state_clear(mode="autopilot")`)


## Scenario Examples

**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.

**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.