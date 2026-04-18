c) once, then re-check pane capture
3. Send one concise trigger (single line) and wait for evidence:
   - `tmux send-keys -t %<worker-pane> "ack + continue current task; report status" C-m`
4. Re-check:
   - pane output via `capture-pane`
   - mailbox updates (`mailbox/leader-fixed.json` or worker mailbox)
   - `omx team status <team>`

### `worker_notify_failed:<worker>`

Meaning:
- Leader wrote inbox but trigger submit path failed

Checks:

1. `tmux list-panes -F '#{pane_id}\t#{pane_start_command}'`
2. `tmux capture-pane -t %<worker-pane> -p -S -120`
3. Verify worker process alive and not stuck on trust prompt
4. Rebuild if running repo-local (`npm run build`)

### Team starts but leader gets no ACK

Checks: