execution path

This would make the intended workflow clearer:

```text
ralplan -> team -> ralph
```

## Why this is good
- Clarifies why `team` exists alongside `ultrawork`: team mode is about coordination and runtime control, not only fanout.
- Reduces the gap between planning output and actual orchestration.
- Makes one of OMX's strongest workflows more discoverable for advanced users.
- Improves execution quality on runtime-edge-case and orchestration-edge-case work, where durable coordination matters more than raw task splitting.
- Fits OMX's architecture well because the runtime already supports worker roles, mixed CLIs, runtime state, and inspectable team lifecycle commands.