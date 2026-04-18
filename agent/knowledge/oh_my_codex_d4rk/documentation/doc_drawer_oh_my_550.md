get`, and related types derive `Serialize`/`Deserialize`.

Exact tmux CLI invocations per operation:

| Operation | tmux command |
|---|---|
| `ResolveTarget` | `tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}'` — verifies the handle appears in the pane list |
| `SendInput` | `tmux send-keys -t <target> -l '<text>'` (literal text), then one `tmux send-keys -t <target> C-m` per press defined by `SubmitPolicy::Enter { presses, delay_ms }` |
| `CaptureTail` | `tmux capture-pane -t <target> -p -S -<lines>` |
| `InspectLiveness` | `tmux has-session -t <session>` (session name extracted from the handle, e.g. `"mysess:0.1"` → `"mysess"`) |
| `Attach` | `tmux attach-session -t <target>` |
| `Detach` | `tmux detach-client -t <target>` |