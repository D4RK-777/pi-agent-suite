# Runtime command / event / snapshot schema

This document defines the Rust-owned runtime contract used by the first greenfield cutover.

## Scope
- Commands describe semantic requests.
- Events describe semantic outcomes.
- Snapshots describe the current truth of the runtime.
- Transport details (JSON, IPC, files) are implementation details layered on top.

## Command shapes

| Command | Required fields | Meaning |
|---|---|---|
| `acquire-authority` | `owner`, `lease_id`, `leased_until` | Claim the single semantic authority lease. |
| `renew-authority` | `owner`, `lease_id`, `leased_until` | Extend the current lease without changing ownership. |
| `queue-dispatch` | `request_id`, `target` | Add one dispatch request to the backlog. |