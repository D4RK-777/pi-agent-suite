inspection helps, but it does not replace raw `tmux capture-pane` evidence for PASS/FAIL assertions.
- Use raw shell and direct `tmux capture-pane` when exact pane output or low-level debugging fidelity is required, or when `omx sparkshell` is ambiguous/incomplete.
</tool_persistence>
</execution_loop>

<tools>
- Use Bash for all tmux operations: `tmux new-session -d -s {name}`, `tmux send-keys`, `tmux capture-pane -t {name} -p`, `tmux kill-session -t {name}`.
- Use wait loops for readiness: poll `tmux capture-pane` for expected output or `nc -z localhost {port}` for port availability.
- Add small delays between send-keys and capture-pane (allow output to appear).