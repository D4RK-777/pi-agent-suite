# Runtime authority, backlog, replay, and readiness semantics

This document captures the Rust-owned runtime semantics that replace JS-side truth.

## Authority
- The runtime has one active authority lease at most.
- A lease has:
  - `owner`
  - `lease_id`
  - `leased_until`
- A stale or expired lease must be marked stale before another owner is granted authority.
- `AuthorityLease` (in `crates/omx-runtime-core/src/authority.rs`) implements the state machine with three transitions:
  - `acquire(owner, lease_id, leased_until)` — succeeds if no lease is held or the requesting owner already holds it; fails with `AlreadyHeldByOther` otherwise.
  - `renew(owner, lease_id, leased_until)` — succeeds only if the same owner currently holds the lease; fails with `NotHeld` or `OwnerMismatch`.