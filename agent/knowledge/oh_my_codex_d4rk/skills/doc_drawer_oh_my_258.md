al **MUST** invoke `$ralph` for execution (step 9) -- never implement directly in the planning agent
- In consensus mode, execution follow-up handoff **MUST** include an explicit available-agent-types roster plus concrete staffing / role-allocation guidance grounded in that roster, suggested reasoning levels by lane, explicit `omx team` / `$team` launch hints, and a team verification path
</Tool_Usage>


## Scenario Examples

**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.

**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.