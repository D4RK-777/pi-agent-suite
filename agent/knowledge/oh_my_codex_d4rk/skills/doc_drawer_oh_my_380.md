, worker 2 = Claude)
OMX_TEAM_WORKER_CLI_MAP=codex,claude omx team 2:executor "split doc/code tasks"

# Auto mode: Claude is selected when worker launch args/model contains 'claude'
OMX_TEAM_WORKER_CLI=auto OMX_TEAM_WORKER_LAUNCH_ARGS="--model claude-..." omx team 2:executor "run mixed validation"
```

## Preconditions

Before running `$team`, confirm:

1. `tmux` installed (`tmux -V`)
2. Current leader session is inside tmux (`$TMUX` is set)
3. `omx` command resolves to the intended install/build
4. If running repo-local `node bin/omx.js ...`, run `npm run build` after `src` changes
5. Check HUD pane count in the leader window and avoid duplicate `hud --watch` panes before split

Suggested preflight: