### Step 3: Check for Legacy Bash Hook Scripts

```bash
ls -la ~/.codex/hooks/*.sh 2>/dev/null
```

**Diagnosis**:
- If `keyword-detector.sh`, `persistent-mode.sh`, `session-start.sh`, or `stop-continuation.sh` exist: WARN - legacy scripts (can cause confusion)

### Step 4: Check AGENTS.md

```bash
# Check if AGENTS.md exists
ls -la ~/.codex/AGENTS.md 2>/dev/null

# Check for OMX marker
grep -q "oh-my-codex Multi-Agent System" ~/.codex/AGENTS.md 2>/dev/null && echo "Has OMX config" || echo "Missing OMX config"
```

**Diagnosis**:
- If missing: CRITICAL - AGENTS.md not configured
- If missing OMX marker: WARN - outdated AGENTS.md

### Step 5: Check for Stale Plugin Cache

```bash
# Count versions in cache
ls ~/.codex/plugins/cache/omc/oh-my-codex/ 2>/dev/null | wc -l
```