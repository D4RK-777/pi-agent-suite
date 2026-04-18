y or invalid input |
| `1` | Task lifecycle or API call failed |

#### Example: Custom Configuration

```bash
# Run with 8 workers and custom task
WORKER_COUNT=8 \
TEAM_TASK="load test $(date +%s)" \
OMX_TEAM_WORKER_CLI_MAP=codex,codex,codex,codex,claude,claude,claude,claude \
./scripts/demo-team-e2e.sh
```