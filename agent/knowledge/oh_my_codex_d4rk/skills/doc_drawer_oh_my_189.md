```bash
# Count versions in cache
ls ~/.codex/plugins/cache/omc/oh-my-codex/ 2>/dev/null | wc -l
```

**Diagnosis**:
- If > 1 version: WARN - multiple cached versions (cleanup recommended)

### Step 6: Check for Legacy Curl-Installed Content

Check for legacy agents, commands, and historical legacy skill roots from older installs/migrations:

```bash
# Check for legacy agents directory
ls -la ~/.codex/agents/ 2>/dev/null

# Check for legacy commands directory
ls -la ~/.codex/commands/ 2>/dev/null

# Check canonical current skills directory
ls -la ${CODEX_HOME:-~/.codex}/skills/ 2>/dev/null

# Check historical legacy skill directory
ls -la ~/.agents/skills/ 2>/dev/null
```