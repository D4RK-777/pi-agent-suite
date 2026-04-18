lls/ 2>/dev/null

# Check historical legacy skill directory
ls -la ~/.agents/skills/ 2>/dev/null
```

**Diagnosis**:
- If `~/.codex/agents/` exists with oh-my-codex-related files: WARN - legacy agents (now provided by plugin)
- If `~/.codex/commands/` exists with oh-my-codex-related files: WARN - legacy commands (now provided by plugin)
- If `${CODEX_HOME:-~/.codex}/skills/` exists with OMX skills: OK - canonical current user skill root
- If `~/.agents/skills/` exists: WARN - historical legacy skill root that can overlap with `${CODEX_HOME:-~/.codex}/skills/` and cause duplicate Enable/Disable Skills entries