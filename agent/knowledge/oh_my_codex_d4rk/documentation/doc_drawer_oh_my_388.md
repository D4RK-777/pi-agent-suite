... <!-- OMX:RUNTIME:END -->`
  - `<!-- OMX:TEAM:WORKER:START --> ... <!-- OMX:TEAM:WORKER:END -->`

Behavior note: this follow-up is additive and wording-focused; no task-state model or MCP API contract changes were introduced.

---

## Skill Prompt Migration (`skills/*/SKILL.md`)

### Summary

Skill docs are operational runbooks. The migration focused on:
- Removing Claude-era paths/terminology
- Aligning config guidance with Codex-first paths (`~/.codex/…`, `CODEX_HOME`)
- Preserving each skill's contract/intent while improving correctness for Codex CLI users

### Behavior Notes