succeeds only if the same owner currently holds the lease; fails with `NotHeld` or `OwnerMismatch`.
  - `force_release()` — unconditionally clears all lease fields including stale state.

## Backlog
- New work enters the backlog as `pending`.
- Notification moves work from `pending` to `notified`.
- Completion moves work from `notified` to either `delivered` or `failed`.
- `pending`, `notified`, `delivered`, and `failed` are counts in the runtime snapshot.