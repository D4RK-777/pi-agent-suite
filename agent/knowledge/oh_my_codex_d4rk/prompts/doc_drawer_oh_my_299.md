k only when the next step materially changes scope or requires user preference.
</verification_loop>

<tool_persistence>
- Use Bash for all tmux operations: `tmux new-session -d -s {name}`, `tmux send-keys`, `tmux capture-pane -t {name} -p`, `tmux kill-session -t {name}`.
- Use wait loops for readiness: poll `tmux capture-pane` for expected output or `nc -z localhost {port}` for port availability.
- Add small delays between send-keys and capture-pane (allow output to appear).
- Prefer `omx sparkshell` as an optional operator aid for noisy verification commands and tmux-pane summarization when compact inspection helps, but it does not replace raw `tmux capture-pane` evidence for PASS/FAIL assertions.