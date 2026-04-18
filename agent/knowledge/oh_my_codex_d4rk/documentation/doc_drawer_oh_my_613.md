kaged native binary under `bin/native/linux-x64/omx-sparkshell`
- adds focused CLI + packaging tests

### `omx team status` inspection improvements
- leader/hud/worker pane ids in text and JSON output
- direct sparkshell inspection commands per pane
- prioritized inspection queue and `inspect_next`
- dead/non-reporting worker targeting
- richer recommended inspection metadata, including:
  - worker CLI, role, liveness, index, turn/activity context
  - task id, subject, description, status, lifecycle, approvals, claims, dependencies
  - worktree/runtime paths and team/worker state artifact paths
  - structured `recommended_inspect_items` JSON payloads