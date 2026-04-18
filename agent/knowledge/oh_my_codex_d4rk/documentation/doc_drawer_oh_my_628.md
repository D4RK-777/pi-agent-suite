xargs -I{} -P5 node bin/omx.js sparkshell git --version` | PASS (bounded sample verified locally) |

Environment limitation during this doc pass:
- `tmux -V` worked, but detached tmux socket access failed with `error connecting to /tmp/tmux-1000/default (Operation not permitted)`, so the `--tmux-pane` examples below are **documented but not end-to-end verified in this session**.

## Evidence capture template

For every heavy/manual scenario record:
- scenario id
- command(s) run
- captured stdout/stderr or screenshot/snippet
- observed summary/guidance/fallback behavior
- pass/fail result
- residual notes

## Exit criteria for the heavy/manual lane