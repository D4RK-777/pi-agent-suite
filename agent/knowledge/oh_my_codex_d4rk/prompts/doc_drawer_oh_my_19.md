utput for `omx status` (no active modes):**
```
No active modes.
```

## Demo 4: Skills in Codex CLI

Skills are automatically discovered by Codex CLI. In a Codex session:

```
> $autopilot "build a REST API for task management"
```

**Expected:** Full autonomous pipeline: requirements analysis -> technical design -> parallel implementation -> QA cycling -> multi-perspective validation.

```
> $team 3:executor "fix all TypeScript errors"
```

**Expected:** Spawns 3 coordinated executor agents working on a shared task list with staged pipeline (plan -> prd -> exec -> verify -> fix loop).

## Demo 5: MCP State Management

The MCP servers are configured in `config.toml` and provide state/memory tools to the agent: