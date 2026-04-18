---
name: doctor
description: Diagnose and fix oh-my-codex installation issues
---

# Doctor Skill

Note: All `~/.codex/...` paths in this guide respect `CODEX_HOME` when that environment variable is set.

## Task: Run Installation Diagnostics

You are the OMX Doctor - diagnose and fix installation issues.

### Step 1: Check Plugin Version

```bash
# Get installed version
INSTALLED=$(ls ~/.codex/plugins/cache/omc/oh-my-codex/ 2>/dev/null | sort -V | tail -1)
echo "Installed: $INSTALLED"

# Get latest from npm
LATEST=$(npm view oh-my-codex version 2>/dev/null)
echo "Latest: $LATEST"
```

**Diagnosis**:
- If no version installed: CRITICAL - plugin not installed
- If INSTALLED != LATEST: WARN - outdated plugin
- If multiple versions exist: WARN - stale cache