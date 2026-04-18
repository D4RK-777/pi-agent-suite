Brain

The generated `AGENTS.md` in your project root acts as the orchestration brain. It provides:

- Delegation rules (when to use which agent)
- Model routing guidance in AGENTS.md (complexity/role-based routing)
- 30-agent catalog with descriptions
- 40 skill descriptions with trigger patterns
- Team compositions for common workflows
- Verification protocols

Codex CLI loads this automatically at session start.

## Demo 3: CLI Status Commands

```bash
# Check version
omx version

# Check all active modes
omx status

# Cancel any active mode
omx cancel
```

**Expected output for `omx version`:**
```
oh-my-codex vX.Y.Z
Node.js v20+
Platform: linux x64
```

**Expected output for `omx status` (no active modes):**
```
No active modes.
```

## Demo 4: Skills in Codex CLI