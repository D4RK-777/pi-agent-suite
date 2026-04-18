doff-needed` | native/derived | Human or orchestrator follow-up is needed. |

## Lifecycle ownership

- native session lifecycle events are the canonical source for `started`, `blocked`, `finished`, and `failed`
- derived operational events add follow-up detail for `retry-needed`, `pr-created`, `test-*`, and `handoff-needed`
- operational contexts resolve `session_name` from the OMX session id + worktree so session metadata stays stable across native and derived events

## Noise and duplicate controls