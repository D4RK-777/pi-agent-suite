```

## Native event pipeline (v1)

Native events are emitted from existing lifecycle/notify paths:

- `session-start`
- `session-end`
- `turn-complete`
- `session-idle`

Pass one keeps this existing event vocabulary; it does **not** introduce an event-taxonomy redesign.

For clawhip-oriented operational routing, see [Clawhip Event Contract](./clawhip-event-contract.md).

Envelope fields include:

- `schema_version: "1"`
- `event`
- `timestamp`
- `source` (`native` or `derived`)
- `context`
- optional IDs: `session_id`, `thread_id`, `turn_id`, `mode`

## Derived signals (opt-in)

Best-effort derived events are gated and disabled by default.

```bash
export OMX_HOOK_DERIVED_SIGNALS=1
```

Derived signals include:

- `needs-input`
- `pre-tool-use`
- `post-tool-use`