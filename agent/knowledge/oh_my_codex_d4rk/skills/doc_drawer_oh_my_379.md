...` only when a later manual follow-up still needs a persistent single-owner fix/verification loop.
- **Deprecation:** `omx team ralph ...` has been removed. Use plain `omx team ...` for team execution or run `omx ralph ...` separately when you explicitly want a later Ralph loop.

### Claude teammates (v0.6.0+)

Important: `N:agent-type` (for example `2:executor`) selects the **worker role prompt**, not the worker CLI (`codex` vs `claude`).

To launch Claude teammates, use the team worker CLI env vars:

```bash
# Force all teammates to Claude CLI
OMX_TEAM_WORKER_CLI=claude omx team 2:executor "update docs and report"

# Mixed team (worker 1 = Codex, worker 2 = Claude)
OMX_TEAM_WORKER_CLI_MAP=codex,claude omx team 2:executor "split doc/code tasks"