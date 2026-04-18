let `monitorTeam()` compute richer actions, but keep `assignTask()` as the only real dispatch path.

## Safety rules for v1
- Do not steal active work that still has a valid claim lease.
- Only auto-reassign when work is pending, explicitly released, reclaimed after lease expiry, or attached to a dead/non-recoverable worker.
- Keep tmux layout and scale-up behavior unchanged for the first milestone.
- Preserve `.omx/state/team/...` storage and `omx team api` contracts.
- Make every allocation/rebalance decision explainable with a reason string suitable for logs, snapshots, and tests.