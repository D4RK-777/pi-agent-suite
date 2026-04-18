ing between workers

### Quick Start

Use a deterministic task slug so the team name is predictable:

```bash
export TEAM_TASK="e2e team demo"
export TEAM_NAME="e2e-team-demo"   # slugified from TEAM_TASK

# Mixed worker CLIs (5+ workers, codex + claude)
export OMX_TEAM_WORKER_CLI=auto
export OMX_TEAM_WORKER_CLI_MAP=codex,codex,codex,claude,claude,claude
export OMX_TEAM_WORKER_LAUNCH_ARGS='-c model_reasoning_effort="low"'

# 5-worker baseline
omx team 5:executor "parallel team smoke"

# 6-worker mixed-CLI E2E run
omx team 6:executor "$TEAM_TASK"

# Discover team command help
omx team --help
omx team api --help

# Lifecycle commands
omx team status "$TEAM_NAME"
omx team resume "$TEAM_NAME"
omx team shutdown "$TEAM_NAME"
```