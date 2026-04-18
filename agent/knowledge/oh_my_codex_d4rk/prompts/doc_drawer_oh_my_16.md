Installation

```bash
omx doctor
```

**Expected output:**
```
oh-my-codex doctor
==================

  [OK] Codex CLI: installed
  [OK] Node.js: v20+
  [OK] Codex home: ~/.codex
  [OK] Config: config.toml has OMX entries
  [OK] Prompts: 30 agent prompts installed
  [OK] Skills: 40 skills installed
  [OK] AGENTS.md: found in project root
  [OK] State dir: .omx/state
  [OK] MCP Servers: 4 servers configured (OMX present)

Results: 9 passed, 0 warnings, 0 failed
```

## Demo 1: Agent/Skill Keywords

Start Codex CLI in any project directory:

```bash
omx
```

Then use role and workflow keywords:

```
> $architect "analyze the authentication module"
```

**Expected:** The architect agent analyzes code with file:line references, root cause diagnosis, and trade-off analysis.