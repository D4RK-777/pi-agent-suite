2e-team-demo" \
WORKER_COUNT=6 \
OMX_TEAM_WORKER_LAUNCH_MODE=prompt \
./scripts/demo-team-e2e.sh
```

Equivalent manual one-shot command block:

```bash
set -euo pipefail

export TEAM_TASK="e2e team demo"
export TEAM_NAME="e2e-team-demo"
export OMX_TEAM_WORKER_CLI=auto
export OMX_TEAM_WORKER_CLI_MAP=codex,codex,codex,claude,claude,claude
export OMX_TEAM_WORKER_LAUNCH_ARGS='-c model_reasoning_effort="low"'

echo "[1/8] start team (6 workers mixed codex/claude)"
omx team 6:executor "$TEAM_TASK"

echo "[2/8] lifecycle status"
omx team status "$TEAM_NAME"