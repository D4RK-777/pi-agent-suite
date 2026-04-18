**per-worker reasoning effort dynamically** from the resolved worker role (`low`, `medium`, `high`).
- Explicit launch args still win: if `OMX_TEAM_WORKER_LAUNCH_ARGS` already includes `-c model_reasoning_effort=...`, that explicit value overrides dynamic allocation for every worker.

Normalization requirements:
- Parse both `--model <value>` and `--model=<value>`
- Remove duplicate/conflicting model flags
- Emit exactly one final canonical flag: `--model <value>`
- Preserve unrelated args in worker launch config
- If explicit reasoning exists, preserve canonical `-c model_reasoning_effort="<level>"`; otherwise inject the worker role's default reasoning level

## Required Lifecycle (Operator Contract)

Follow this exact lifecycle when running `$team`: