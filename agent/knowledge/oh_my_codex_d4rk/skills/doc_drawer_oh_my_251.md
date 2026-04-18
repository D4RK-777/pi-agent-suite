e code files in the planning agent. The ralph skill handles execution via ultrawork parallel agents.
   - **Approve and implement via team**: **MUST** invoke `$team` with the approved plan path from `.omx/plans/` as context **plus the explicit available-agent-types roster, suggested reasoning levels, concrete staffing / worker-role allocation guidance, explicit `omx team` / `$team` launch hints, and the team verification path**. Do NOT implement directly. The team skill coordinates parallel agents across the staged pipeline for faster execution on large tasks.

### Review Mode (`--review`)