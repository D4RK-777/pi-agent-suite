`) for the coordinated team run; mention a later separate Ralph follow-up only when genuinely needed
- if the ideal role is unavailable, choose the closest role from the roster and say so

## Current Runtime Behavior (As Implemented)

`omx team` currently performs:

1. Parse args (`N`, `agent-type`, task)
2. Sanitize team name from task text
3. Initialize team state:
   - `.omx/state/team/<team>/config.json`
   - `.omx/state/team/<team>/manifest.v2.json`
   - `.omx/state/team/<team>/tasks/task-<id>.json`
4. Compose team-scoped worker instructions file at:
   - `.omx/state/team/<team>/worker-agents.md`
   - Uses project `AGENTS.md` content (if present) + worker overlay, without mutating project `AGENTS.md`
5. Resolve canonical shared state root from leader cwd (`<leader-cwd>/.omx/state`)