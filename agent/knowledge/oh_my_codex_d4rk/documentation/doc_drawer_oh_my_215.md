`turn_id`, `mode`

## Common context fields

When available, OMX includes these fields in `context`:

- `normalized_event`
- `session_name`
- `repo_path`
- `repo_name`
- `worktree_path`
- `branch`
- `issue_number`
- `pr_number`
- `pr_url`
- `command`
- `tool_name`
- `status`
- `error_summary`

## Normalized events

| `context.normalized_event` | Typical raw `event` values | Source | Notes |
| --- | --- | --- | --- |
| `started` | `session-start` | native | Session launch began. |
| `blocked` | `session-idle`, `blocked` | native/derived | Session is waiting on input or another dependency. |
| `finished` | `session-end`, `finished` | native/derived | Session or turn finished successfully. |
| `failed` | `session-end`, `failed` | native/derived | Session, dispatch, or turn failed. |