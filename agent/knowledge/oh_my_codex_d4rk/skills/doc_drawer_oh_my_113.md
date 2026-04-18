with force-kill fallback

## Tmux Team Cleanup

When cancelling team mode, the cancel skill should:

1. **Kill all team tmux sessions**: `tmux list-sessions -F '#{session_name}' 2>/dev/null | grep '^omx-team-'` and kill each
2. **Remove team state directories**: `rm -rf .omx/state/team/*/`
3. **Strip AGENTS.md overlay**: Remove content between `<!-- OMX:TEAM:WORKER:START -->` and `<!-- OMX:TEAM:WORKER:END -->`

### Force Clear Addition

When `--force` is used, also clean up:
```bash
rm -rf .omx/state/team/                  # All team state
# Kill all omx-team-* tmux sessions
tmux list-sessions -F '#{session_name}' 2>/dev/null | grep '^omx-team-' | while read s; do tmux kill-session -t "$s" 2>/dev/null; done
```