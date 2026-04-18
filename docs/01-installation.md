# 01 — Installation

Complete installation guide with all options and advanced configurations.

---

## Prerequisites

### Required

| Tool | Minimum | Check |
|---|---|---|
| Python | 3.9 | `python --version` |
| pip | any | `pip --version` |
| Git | any | `git --version` |

### Optional (enables specific features)

| Tool | Purpose |
|---|---|
| Claude Code | Full hook integration (auto-memory injection) |
| Node.js 18+ | npm install option; obsidian-mcp-server |
| Obsidian | Vault knowledge management |
| Git for Windows | Bash hooks on Windows |

---

## Install options

### Option A — Bash installer (macOS, Linux, Windows/WSL)

```bash
git clone https://github.com/YOUR_ORG/pi-agent-suite
cd pi-agent-suite
bash installer/install.sh
```

**With flags:**
```bash
# Non-interactive with defaults
bash installer/install.sh --non-interactive

# Custom install location
bash installer/install.sh --pi-home ~/my-agents

# Custom palace location
bash installer/install.sh --palace /data/mempalace

# Skip Claude Code settings patching
bash installer/install.sh --no-claude

# Include vault template setup
bash installer/install.sh --with-vault
```

### Option B — PowerShell installer (Windows)

```powershell
git clone https://github.com/YOUR_ORG/pi-agent-suite
cd pi-agent-suite
powershell -ExecutionPolicy Bypass -File installer/install.ps1
```

**With parameters:**
```powershell
# Non-interactive
.\installer\install.ps1 -NonInteractive

# Custom paths
.\installer\install.ps1 -PiHome "D:\agents\pi" -Palace "D:\mempalace\palace"

# Skip Claude Code
.\installer\install.ps1 -NoClaude

# With vault
.\installer\install.ps1 -WithVault
```

### Option C — npm (installs globally, runs interactive setup)

```bash
npm install -g pi-agent-suite
pi-agent-suite install
```

### Option D — Manual

1. Install MemPalace:
   ```bash
   pip install mempalace
   ```

2. Create directories:
   ```bash
   mkdir -p ~/.pi/agent ~/.pi/hooks ~/.mempalace/palace ~/.mempalace/hook_state
   ```

3. Copy agent files:
   ```bash
   cp -r agent/ ~/.pi/agent/
   cp hooks/*.sh ~/.pi/hooks/
   chmod +x ~/.pi/hooks/*.sh
   ```

4. Set environment variables (add to `~/.bashrc` or `~/.zshrc`):
   ```bash
   export PI_AGENT_HOME="$HOME/.pi"
   export MEMPALACE_PALACE="$HOME/.mempalace/palace"
   ```

5. Wire Claude Code manually — see [docs/02-claude-code.md](02-claude-code.md).

---

## Environment variables

All paths are configurable via environment variables. Set these before running the installer or export them in your shell profile.

| Variable | Default | Description |
|---|---|---|
| `PI_AGENT_HOME` | `~/.pi` | Root of Pi Agent install |
| `MEMPALACE_PALACE` | `~/.mempalace/palace` | ChromaDB data directory |
| `MEMPAL_SAVE_INTERVAL` | `15` | Exchanges between auto-mine |
| `MEMPAL_INGEST_DIR` | _(empty)_ | Additional dir to mine on save |
| `OBSIDIAN_VAULT` | _(empty)_ | Path to Obsidian vault directory |
| `OBSIDIAN_API_KEY` | _(empty)_ | Local REST API plugin key |
| `OBSIDIAN_VAULT_NAME` | _(empty)_ | Vault name for MCP server |

---

## Directory layout after install

```
$PI_AGENT_HOME/               (default: ~/.pi/)
├── agent/
│   ├── bin/
│   │   ├── mempalace_fast.py         # thin search wrapper
│   │   └── mempalace_prompt_hook.py  # UserPromptSubmit hook
│   ├── brain/
│   │   ├── router.py                  # 6-signal task router
│   │   ├── launch.py                  # session lifecycle
│   │   └── skill_governance.py        # skill audit
│   ├── harness/
│   │   ├── orchestrator.py            # CLI dispatcher
│   │   ├── router.py                  # manifest router
│   │   ├── memory.py                  # MemPalace integration
│   │   └── enforcement.py             # compliance watcher
│   ├── agents/                        # 8 specialist agents
│   ├── manifests/                     # agent capabilities
│   ├── skills/                        # composable skills
│   ├── bundles/                       # skill bundles
│   ├── cookbooks/                     # multi-step workflows
│   └── adapters/                      # AI client adapters
├── hooks/
│   ├── mempal_save_hook.sh            # Stop hook (auto-mine)
│   └── mempal_precompact_hook.sh      # PreCompact hook
└── env.sh                            # environment variables

$MEMPALACE_PALACE/../           (default: ~/.mempalace/)
├── palace/                           # ChromaDB data
│   └── chroma.sqlite3
└── hook_state/                       # hook counters
    ├── exchange_counter
    └── last_session_id
```

---

## Verification

```bash
bash installer/verify.sh
```

All items should show `[OK]`. See [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) for any failures.

---

## Upgrading

```bash
cd pi-agent-suite
git pull
bash installer/install.sh --non-interactive
```

The installer is idempotent — re-running it updates files without losing your data.

---

## Uninstalling

```bash
# Remove Pi Agent files
rm -rf ~/.pi

# Remove MemPalace data (WARNING: this deletes all memories)
rm -rf ~/.mempalace

# Remove Claude Code hooks (edit ~/.claude/settings.json and remove hooks section)

# Remove from shell profile
# Delete the `source ~/.pi/env.sh` line from ~/.bashrc or ~/.zshrc
```
