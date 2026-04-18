x,claude,claude`
  - When present, overrides `OMX_TEAM_WORKER_CLI`
- `OMX_TEAM_AUTO_INTERRUPT_RETRY`
  - Trigger submit fallback (default: enabled)
  - `0` disables adaptive queue->resend escalation
- `OMX_TEAM_LEADER_NUDGE_MS`
  - Leader nudge interval in ms (default 120000)
- `OMX_TEAM_STRICT_SUBMIT=1`
  - Force strict send-keys submit failure behavior

## Failure Modes and Diagnosis

Operator note (important for Claude panes):
- Manual Enter injection (`tmux send-keys ... C-m`) can appear to "do nothing" when a worker is actively processing; Enter may be queued by the pane/task flow.
- This is not necessarily a runtime bug. Confirm worker/team state before diagnosing dispatch failure.
- Avoid repeated blind Enter spam; it can create noisy duplicate submits once the pane becomes idle.