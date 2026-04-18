argument, so even force mode still uses the session-aware paths first before deleting legacy files.

Legacy compatibility list (removed only under `--force`/`--all`):
- `.omx/state/autopilot-state.json`
- `.omx/state/ralph-state.json`
- `.omx/state/ralph-plan-state.json`
- `.omx/state/ralph-verification.json`
- `.omx/state/ultrawork-state.json`
- `.omx/state/ecomode-state.json`
- `.omx/state/ultraqa-state.json`
- `.omx/state/swarm.db`
- `.omx/state/swarm.db-wal`
- `.omx/state/swarm.db-shm`
- `.omx/state/swarm-active.marker`
- `.omx/state/swarm-tasks.db`
- `.omx/state/ultrapilot-state.json`
- `.omx/state/ultrapilot-ownership.json`
- `.omx/state/pipeline-state.json`
- `.omx/state/plan-consensus.json`
- `.omx/state/ralplan-state.json`
- `.omx/state/boulder.json`