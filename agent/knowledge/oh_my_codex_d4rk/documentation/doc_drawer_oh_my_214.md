# Clawhip Event Contract

OMX emits hook events for clawhip through the existing hooks extensibility pipeline.

## Canonical routing rule

Route on `context.normalized_event`, not just raw `event`.

This keeps clawhip stable even when OMX uses legacy-compatible raw event names such as `session-start`, `session-end`, and `session-idle`.

## Envelope

All events use the existing hook envelope:

- `schema_version: "1"`
- `event`
- `timestamp`
- `source`
- `context`
- optional IDs: `session_id`, `thread_id`, `turn_id`, `mode`

## Common context fields

When available, OMX includes these fields in `context`: