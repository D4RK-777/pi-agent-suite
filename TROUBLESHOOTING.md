# Pi Agent Suite — Troubleshooting

## Quick diagnostics

```bash
bash installer/verify.sh
```

This runs all checks and reports pass/fail. Start here before anything else.

---

## MemPalace

### `import mempalace` fails

**Symptom:** `ModuleNotFoundError: No module named 'mempalace'`

**Fix:**
```bash
pip install mempalace
# or, if you installed as editable:
pip install -e ~/mempalace
```

Then verify:
```bash
python -c "import mempalace; print(mempalace.__version__)"
```

---

### `chromadb` version conflict

**Symptom:** `ImportError` or version mismatch errors when importing mempalace.

**Fix:** MemPalace requires chromadb 0.5.x–0.6.x. Check and pin if needed:
```bash
pip show chromadb
pip install "chromadb>=0.5,<0.7"
```

---

### Palace is empty after mining

**Symptom:** `mempalace search "anything"` returns 0 results.

**Check:**
```bash
python -c "from mempalace import status; print(status())"
```

If drawer count is 0, the mine didn't work. Re-run with verbose:
```bash
mempalace mine ~/your-project --verbose
```

**Common cause:** Large binary files or `.obsidian/` plugin bundles cause memory issues. Make sure your project has a `.gitignore` or use `--exclude`:
```bash
mempalace mine ~/your-project --exclude ".obsidian,node_modules,__pycache__,*.pyc"
```

---

### Palace is corrupt

**Symptom:** ChromaDB errors, segfaults, or incomplete results.

**Fix:**
```bash
# Check status
python -m mempalace.cli status

# Nuclear option — delete and re-mine
rm -rf ~/.mempalace/palace
mempalace mine ~/your-project
```

---

### MemPalace MCP server not connecting in Claude Code

**Symptom:** `mempalace_*` tools not available in Claude Code.

**Check** `~/.claude/settings.json` — should contain:
```json
"mcpServers": {
  "mempalace": {
    "command": "python",
    "args": ["-m", "mempalace.mcp_server", "--palace", "/path/to/palace"]
  }
}
```

**Fix:** Re-run the installer with `--patch-claude`:
```bash
bash installer/install.sh --non-interactive
```

Or add the MCP server manually using `claude mcp add mempalace python -- -m mempalace.mcp_server`.

---

## Hooks

### Hooks not firing in Claude Code

**Symptom:** No `<mempalace-context>` injected. Stop hook not mining.

**Check:**
1. Open Claude Code settings (`/config`)
2. Look for `hooks` section with `UserPromptSubmit`, `Stop`, `PreCompact`

**Fix:** Re-run installer or manually add to `~/.claude/settings.json`:
```json
"hooks": {
  "UserPromptSubmit": [{
    "matcher": "",
    "hooks": [{"type": "command", "command": "python ~/.pi/agent/bin/mempalace_prompt_hook.py", "timeout": 2}]
  }],
  "Stop": [{
    "matcher": "",
    "hooks": [{"type": "command", "command": "bash ~/.pi/hooks/mempal_save_hook.sh", "timeout": 30}]
  }],
  "PreCompact": [{
    "matcher": "",
    "hooks": [{"type": "command", "command": "bash ~/.pi/hooks/mempal_precompact_hook.sh", "timeout": 30}]
  }]
}
```

---

### `UserPromptSubmit` hook times out (>500ms)

**Symptom:** Hook fires but results are empty or missing; logs show timeout.

**Causes:**
- ChromaDB cold start — first query after restart is slow. Subsequent queries are fast.
- Palace is too large — consider splitting into wings.
- Slow disk — SSD recommended for palace directory.

**Quick fix:** Increase timeout in settings.json from `2` to `5`.

---

### Hook logs

Hook activity is logged to:
```
~/.mempalace/hook_state/
├── exchange_counter       # current exchange count
└── last_session_id        # last mined session
```

Check exchange counter to see if Stop hook is counting:
```bash
cat ~/.mempalace/hook_state/exchange_counter
```

---

## Pi Harness

### `python -m harness route "..."` fails

**Symptom:** `ModuleNotFoundError: No module named 'harness'`

**Fix:** The harness must be run from the `~/.pi/agent/` directory, or add it to PYTHONPATH:
```bash
cd ~/.pi/agent
python -m harness route "build a login form"

# Or set PYTHONPATH:
export PYTHONPATH="$PI_AGENT_HOME/agent:$PYTHONPATH"
python -m harness route "build a login form"
```

---

### Routing always picks the wrong agent

**Symptom:** Every task goes to `advisor` or the same agent.

**Check:** Run the routing test:
```bash
cd ~/.pi/agent
python -m harness test
```

**Fix:** The 6-signal router uses keyword matching. If your tasks use unusual vocabulary, update `brain/router.py`:
- Add keywords to `SKILL_REGISTRY`
- Adjust agent manifests in `manifests/`

---

### Manifests not loading

**Symptom:** `harness route` shows empty agent list.

**Check:**
```bash
ls ~/.pi/agent/manifests/
```

Manifests should be `.json` or `.yaml` files. The `harness/router.py` loads from `PI_ROOT/manifests/` where `PI_ROOT = PI_AGENT_HOME/agent`.

---

## Obsidian

### `obsidian_*` MCP tools not available

**Symptom:** Claude Code doesn't have `obsidian_search`, `obsidian_readFile`, etc.

**Fix:**
1. Install the `obsidian-mcp-server` npm package:
   ```bash
   npm install -g obsidian-mcp-server
   ```
2. Enable the Local REST API plugin in Obsidian
3. Copy the API key
4. Add the MCP server to Claude Code:
   ```bash
   claude mcp add obsidian npx -- obsidian-mcp-server --api-key YOUR_KEY --vault YOUR_VAULT_NAME
   ```

---

### Vault CLAUDE.md not being followed

**Symptom:** Claude Code ignores the vault ops manual.

**Fix:** The vault CLAUDE.md must be in Claude Code's context. Open Claude Code with the vault as working directory, or reference the file explicitly:
```
Read C:\Users\you\YourVault\CLAUDE.md and follow the ingest operation for raw/articles/my-doc.md
```

---

## Windows-specific

### PowerShell execution policy

**Symptom:** `cannot be loaded because running scripts is disabled`

**Fix:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Python found as `python3` but scripts use `python`

**Symptom:** Hooks fail because `python` not found.

**Fix:** On Windows, add a `python` alias or ensure `python.exe` is in PATH. The installers auto-detect both `python` and `python3`.

---

### Bash hooks not available on Windows

**Symptom:** `mempal_save_hook.sh` and `mempal_precompact_hook.sh` fail.

**Fix:** Install Git for Windows (includes bash) or WSL. Alternatively, use the PowerShell equivalent hooks in `hooks/mempal_save_hook.ps1` (create if needed) and update Claude Code settings to use `powershell -File` instead of `bash`.

---

### `EINVAL` error when spawning agents

**Symptom:** `pi-spawn-agent` fails with `EINVAL` on Windows.

**Cause:** Windows `.cmd` shims can't be spawned with `shell: false`.

**Fix:** Pi spawn-agent uses the raw Node.js entry point instead of the `.cmd` shim. This is handled automatically by the harness. If you see this in custom code, use `{ shell: true }` or point directly to the `.js` entry.

---

## Getting more help

1. Run `bash installer/verify.sh` — shows exactly what's failing
2. Check hook logs: `~/.mempalace/hook_state/`
3. Enable debug mode: `export MEMPAL_DEBUG=1` then re-run the failing command
4. Open an issue: https://github.com/YOUR_ORG/pi-agent-suite/issues
