very & Lifecycle**
   - Cancel/cleanup/resume behavior and state transitions.

### Optional sections

- Tool catalogs and model routing guidance.
- Skill discovery/reference sections.
- Team composition/pipeline presets.
- Session/runtime context blocks (when injected by runtime overlays).

## Global Compatibility Contracts (Must Stay Stable)

### Marker contracts

- `<!-- OMX:RUNTIME:START --> ... <!-- OMX:RUNTIME:END -->`
- `<!-- OMX:TEAM:WORKER:START --> ... <!-- OMX:TEAM:WORKER:END -->`

### Worker task/mailbox contracts

- Task file path format: `.omx/state/team/<team>/tasks/task-<id>.json` (example: `task-3.json`)
- State/MCP API id format: `task_id: "<id>"` (example: `"3"`, never `"task-3"`)
- Mailbox path: `.omx/state/team/<team>/mailbox/<worker>.json`

## Mapping Matrix