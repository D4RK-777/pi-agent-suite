orced — invalid transitions (e.g. `pending -> delivered`) return `DispatchError::InvalidTransition`.

## Replay / recovery
- Replay is cursor-based and durable.
- Replayed items must be deduplicated.
- Deferred leader notification is tracked explicitly so observers can tell why delivery has not been surfaced yet.
- `ReplayState` (in `crates/omx-runtime-core/src/replay.rs`) tracks the current `cursor`, deduplicates by `event_id` via an internal `HashSet`, and records whether leader notification was intentionally deferred via `defer_leader_notification()` / `clear_deferred()`.