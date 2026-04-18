ader notification was intentionally deferred via `defer_leader_notification()` / `clear_deferred()`.

## Readiness
- Readiness is a Rust-authored snapshot, not an inferred CLI opinion.
- The runtime is not ready when the lease is missing, stale, or otherwise invalid.
- The snapshot should include the exact blockers so operators can see why recovery is paused.
- `derive_readiness()` (in `crates/omx-runtime-core/src/engine.rs`) computes `ReadinessSnapshot` from the current `AuthorityLease`, `DispatchLog`, and `ReplayState`. It returns `ReadinessSnapshot::ready()` only when the authority lease is held and not stale, and there are no pending replay events. All blocking reasons are collected into `readiness.reasons`.