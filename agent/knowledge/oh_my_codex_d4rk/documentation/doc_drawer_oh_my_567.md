rable cursor. |
| `capture-snapshot` | none | Emit the current semantic snapshot. |

## Event shapes

| Event | Required fields | Meaning |
|---|---|---|
| `authority-acquired` | `owner`, `lease_id`, `leased_until` | A new authority lease is active. |
| `authority-renewed` | `owner`, `lease_id`, `leased_until` | The active lease was renewed. |
| `dispatch-queued` | `request_id`, `target` | A request entered backlog. |
| `dispatch-notified` | `request_id`, `channel` | A request moved out of pending and into notification. |
| `dispatch-delivered` | `request_id` | The request completed successfully. |
| `dispatch-failed` | `request_id`, `reason` | The request completed with failure. |
| `replay-requested` | `cursor` | Replay or recovery work was requested. |