ery failures are surfaced as adapter failures, not as semantic
   owner changes.

## Consumer matrix

| Consumer | Responsibility |
|---|---|
| Team CLI | Read Rust-authored compatibility artifacts and render them faithfully. |
| Doctor CLI | Report readiness from Rust-authored compatibility artifacts, then layer adapter health checks on top. |
| HUD | Stay read-only and scope-aware. |
| Notify/watchers | Deliver events; never become the semantic owner of the run. |