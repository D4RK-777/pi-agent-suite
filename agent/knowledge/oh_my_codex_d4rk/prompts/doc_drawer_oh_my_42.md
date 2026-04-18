ments passed to worker CLIs (worker model falls back to `OMX_DEFAULT_SPARK_MODEL`) |

#### Demo Flow

```
[1/8] Start team → Creates tmux session with N mixed workers
[2/8] Status check → Verifies all workers are healthy
[3/8] Create task → Creates a test task in the shared queue
[4/8] Claim task → Worker-1 claims the task with version token
[5/8] Complete task → Transitions task to completed status
[6/8] Mailbox flow → Sends message and validates delivery
[7/8] Summary check → Validates JSON envelope schema
[8/8] Cleanup → Graceful shutdown and state cleanup
```

#### Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All checks passed |
| `1` | Missing dependency or invalid input |
| `1` | Task lifecycle or API call failed |

#### Example: Custom Configuration