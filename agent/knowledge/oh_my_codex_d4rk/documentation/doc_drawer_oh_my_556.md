(illustrative):
starting
- `executing`
- `verifying`
- `fixing`
- `complete`

## Frozen scope policy

1. If `session_id` is present (explicit argument or current `.omx/state/session.json`), session scope (`.omx/state/sessions/{session_id}/...`) is authoritative.
2. Root scope (`.omx/state/*.json`) is compatibility fallback only.
3. Writes MUST target one scope (authoritative scope), never broadcast to unrelated sessions.

## Consumer compatibility matrix