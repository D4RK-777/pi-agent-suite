send-keys`
9. Return control to leader; follow-up uses `status` / `resume` / `shutdown`

Important:

- Leader remains in existing pane
- Worker panes are independent full Codex/Claude CLI sessions
- Workers may run in separate git worktrees (`omx team --worktree[=<name>]`) while sharing one team state root
- Worker ACKs go to `mailbox/leader-fixed.json`
- Notify hook updates worker heartbeat and nudges leader during active team mode
- Submit routing uses this CLI resolution order per worker trigger:
  1) explicit worker CLI provided by runtime state (persisted on worker identity/config),
  2) `OMX_TEAM_WORKER_CLI_MAP` entry for that worker index,
  3) fallback `OMX_TEAM_WORKER_CLI` / auto detection.
- Mixed CLI-map teams are supported for both startup and trigger submit behavior.