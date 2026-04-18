completed with failure. |
| `replay-requested` | `cursor` | Replay or recovery work was requested. |
| `snapshot-captured` | none | A snapshot was emitted for observers. |

## Snapshot fields

| Field | Meaning |
|---|---|
| `schema_version` | Contract version for the runtime snapshot. |
| `authority.owner` | The current semantic owner, if any. |
| `authority.lease_id` | Lease identifier for the current owner. |
| `authority.leased_until` | Lease expiry marker. |
| `authority.stale` | Whether the current owner is stale or expired. |
| `backlog.pending` | Dispatches awaiting notification. |
| `backlog.notified` | Dispatches that were notified and are waiting for completion. |
| `backlog.delivered` | Dispatches that completed successfully. |