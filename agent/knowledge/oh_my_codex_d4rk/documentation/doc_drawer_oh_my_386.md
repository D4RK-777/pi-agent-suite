hanges here are primarily about aligning instructions with Codex CLI tool contracts.

### Key Deltas

- Updated child-agent delegation guidance to reflect the Codex `spawn_agent` API:
  - Use `spawn_agent(message: "<role prompt>\n\nTask: ...")` conventions.
  - Removed legacy "instructions" phrasing.
- Expanded MCP tooling catalog and mode lifecycle expectations so orchestrators can use the full MCP surface correctly.
- `templates/AGENTS.md` header normalized to match `AGENTS.md` and removed the non-compliant template opener.

### Diff Stats

| File | Added | Removed | Notes |
|---|---:|---:|---|
| `AGENTS.md` | 42 | 10 | Tooling + delegation guidance expanded; semantics preserved. |
| `templates/AGENTS.md` | 7 | 7 | Header/tone normalized; still intended as a template copy. |