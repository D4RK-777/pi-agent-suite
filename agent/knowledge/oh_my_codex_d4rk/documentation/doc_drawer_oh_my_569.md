and are waiting for completion. |
| `backlog.delivered` | Dispatches that completed successfully. |
| `backlog.failed` | Dispatches that completed with failure. |
| `replay.cursor` | Durable replay cursor, if any. |
| `replay.pending_events` | Number of replayable events not yet applied. |
| `replay.last_replayed_event_id` | Last replayed event marker. |
| `replay.deferred_leader_notification` | Whether leader notification was intentionally deferred. |
| `readiness.ready` | Whether the runtime is ready for operator traffic. |
| `readiness.reasons` | Human-readable blockers when the runtime is not ready. |

## JSON serialization format

Commands use `#[serde(tag = "command")]` — the variant name becomes the `"command"` field, remaining fields are flattened inline: