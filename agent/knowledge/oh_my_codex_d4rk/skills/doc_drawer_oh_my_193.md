iption]

### Recommended Fixes
[List fixes based on issues]
```

---

## Auto-Fix (if user confirms)

If issues found, ask user: "Would you like me to fix these issues automatically?"

If yes, apply fixes:

### Fix: Legacy Hooks in legacy settings.json
If `~/.codex/settings.json` exists, remove the legacy `"hooks"` section (keep other settings intact).

### Fix: Legacy Bash Scripts
```bash
rm -f ~/.codex/hooks/keyword-detector.sh
rm -f ~/.codex/hooks/persistent-mode.sh
rm -f ~/.codex/hooks/session-start.sh
rm -f ~/.codex/hooks/stop-continuation.sh
```

### Fix: Outdated Plugin
```bash
rm -rf ~/.codex/plugins/cache/omc/oh-my-codex
echo "Plugin cache cleared. Restart Codex CLI to fetch latest version."
```