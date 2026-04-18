te/marker mode (`.omx/state/swarm.db` / `.omx/state/swarm-active.marker`) and is not session-scoped.
- The default cleanup flow calls `state_clear` with the session id to remove only the matching session files; modes stay bound to their originating session.

## Normative Ralph cancellation post-conditions (MUST)

For Ralph-targeted cancellation (standalone or linked), completion is defined by post-conditions:

1. Target Ralph state is terminalized, not silently removed:
   - `active=false`
   - `current_phase='cancelled'`
   - `completed_at` is set (ISO timestamp)
2. If Ralph is linked to Ultrawork or Ecomode in the same scope, that linked mode is also terminalized/non-active.
4. Cancellation MUST remain scope-safe: no mutation of unrelated sessions.