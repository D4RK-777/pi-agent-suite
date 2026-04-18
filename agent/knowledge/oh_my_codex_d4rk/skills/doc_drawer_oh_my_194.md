ns/cache/omc/oh-my-codex
echo "Plugin cache cleared. Restart Codex CLI to fetch latest version."
```

### Fix: Stale Cache (multiple versions)
```bash
# Keep only latest version
cd ~/.codex/plugins/cache/omc/oh-my-codex/
ls | sort -V | head -n -1 | xargs rm -rf
```

### Fix: Missing/Outdated AGENTS.md
Fetch latest from GitHub and write to `~/.codex/AGENTS.md`:
```
WebFetch(url: "https://raw.githubusercontent.com/Yeachan-Heo/oh-my-codex/main/docs/AGENTS.md", prompt: "Return the complete raw markdown content exactly as-is")
```

### Fix: Legacy Curl-Installed Content

Remove legacy agents/commands plus the historical `~/.agents/skills` tree if it overlaps with the canonical `${CODEX_HOME:-~/.codex}/skills` install: