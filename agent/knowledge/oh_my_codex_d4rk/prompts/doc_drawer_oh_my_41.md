uto-Cleanup** | Trap-based cleanup ensures resources are freed on exit |

#### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `WORKER_COUNT` | `6` | Number of workers to spawn (minimum: 5) |
| `TEAM_TASK` | `e2e team demo <timestamp>` | Task description for the team |
| `TEAM_NAME` | (slugified from TEAM_TASK) | Unique team identifier |
| `OMX_TEAM_WORKER_CLI` | `auto` | Worker CLI selection mode |
| `OMX_TEAM_WORKER_CLI_MAP` | (auto-generated) | Comma-separated CLI assignments per worker |
| `OMX_TEAM_WORKER_LAUNCH_ARGS` | `-c model_reasoning_effort="low"` | Arguments passed to worker CLIs (worker model falls back to `OMX_DEFAULT_SPARK_MODEL`) |

#### Demo Flow