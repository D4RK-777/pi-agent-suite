ess.json` | `write_compatibility_view()` | `ReadinessSnapshot` (`ready`, `reasons`) for TS readers |
| `replay.json` | `write_compatibility_view()` | `ReplaySnapshot` state for TS readers |
| `dispatch.json` | `write_compatibility_view()` | Full `DispatchLog` (array of `DispatchRecord` entries) for team status readers |
| `mailbox.json` | `write_compatibility_view()` | Full `MailboxLog` (array of `MailboxRecord` entries) for team/message readers |

All files are written atomically to the configured `state_dir`. TS readers must treat these files as read-only; the Rust engine is the sole writer.

## Thin-adapter rules