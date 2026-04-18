- Avoid repeated blind Enter spam; it can create noisy duplicate submits once the pane becomes idle.

### Safe Manual Intervention (last resort)

Use only after checking `omx team status <team>` and mailbox/state evidence:

1. Capture pane tail to confirm current worker state:
   - `tmux capture-pane -t %<worker-pane> -p -S -120`
   - If a larger-tail read or bounded summary would help, prefer explicit opt-in inspection via `omx sparkshell --tmux-pane %<worker-pane> --tail-lines 400` before improvising extra tmux commands.
2. If the pane is stuck in an interactive state, safely return to idle prompt first:
   - optional interrupt `C-c` or escape flow (CLI-specific) once, then re-check pane capture
3. Send one concise trigger (single line) and wait for evidence: