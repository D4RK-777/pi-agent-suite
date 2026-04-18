wnership. |
| `queue-dispatch` | `request_id`, `target` | Add one dispatch request to the backlog. |
| `mark-notified` | `request_id`, `channel` | Record that a queued dispatch has been delivered to an observer or target. |
| `mark-delivered` | `request_id` | Record successful delivery completion. |
| `mark-failed` | `request_id`, `reason` | Record failed delivery completion. |
| `request-replay` | `cursor` | Ask the runtime to replay from a durable cursor. |
| `capture-snapshot` | none | Emit the current semantic snapshot. |

## Event shapes