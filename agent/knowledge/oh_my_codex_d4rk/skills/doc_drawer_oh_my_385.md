oject `AGENTS.md`
5. Resolve canonical shared state root from leader cwd (`<leader-cwd>/.omx/state`)
6. Split current tmux window into worker panes
7. Launch workers with:
   - `OMX_TEAM_WORKER=<team>/worker-<n>`
   - `OMX_TEAM_STATE_ROOT=<leader-cwd>/.omx/state`
   - `OMX_TEAM_LEADER_CWD=<leader-cwd>`
   - worker CLI selected by `OMX_TEAM_WORKER_CLI` / `OMX_TEAM_WORKER_CLI_MAP` (`codex` or `claude`)
   - optional worktree metadata envs when `--worktree` is used
7. Wait for worker readiness (`capture-pane` polling)
8. Write per-worker `inbox.md` and trigger via `tmux send-keys`
9. Return control to leader; follow-up uses `status` / `resume` / `shutdown`

Important: