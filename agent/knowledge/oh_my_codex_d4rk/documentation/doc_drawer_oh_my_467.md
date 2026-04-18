# oh-my-codex v0.8.6

Released: 2026-03-07

4 non-merge commits from `main..dev`.
Contributor: [@Yeachan-Heo](https://github.com/Yeachan-Heo).

## Highlights

### Event-aware team waiting and runtime coordination

OMX team orchestration can now wait on canonical team events in addition to terminal completion.

This release adds:
- additive `wake_on=event` / `after_event_id` support to `omx_run_team_wait`
- shared event reading, normalization, and cursor helpers in the team state layer
- canonical event typing across contracts, runtime state, and API interop
- `omx team await <team-name>` CLI support
- runtime emission of `worker_state_changed` while preserving legacy `worker_idle` compatibility