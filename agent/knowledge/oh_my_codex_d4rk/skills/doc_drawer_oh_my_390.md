level

## Required Lifecycle (Operator Contract)

Follow this exact lifecycle when running `$team`:

1. Start team and verify startup evidence (team line, tmux target, panes, ACK mailbox)
2. Monitor task and worker progress with runtime/state tools first (`omx team status <team>`, `omx team resume <team>`, mailbox/state files)
3. Wait for terminal task state before shutdown:
   - `pending=0`
   - `in_progress=0`
   - `failed=0` (or explicitly acknowledged failure path)
4. Only then run `omx team shutdown <team>`
5. Verify shutdown evidence and state cleanup

Do not run `shutdown` while workers are actively writing updates unless user explicitly requested abort/cancel.
Do not treat ad-hoc pane typing as primary control flow when runtime/state evidence is available.