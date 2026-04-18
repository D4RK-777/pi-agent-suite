an `omx team shutdown <team>` (or removed `.omx/state/team/<team>`) before worker finished.

Checks:

1. `omx team status <team>` and confirm whether tasks were still `in_progress` when shutdown occurred
2. Verify whether `.omx/state/team/<team>/` exists
3. Inspect worker pane tail for post-shutdown writes
4. Confirm no external cleanup (`rm -rf .omx/state/team/<team>`) happened during execution

Prevention:

1. Enforce completion gate (no in-progress tasks) before shutdown
2. Use `shutdown` only for terminal completion or explicit abort
3. If aborting, expect late worker writes to fail and treat ENOENT as expected teardown artifact

### Shutdown reports success but stale worker panes remain

Cause:
- stale pane outside config tracking or previous failed run