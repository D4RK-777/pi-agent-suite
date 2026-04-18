# Pi Agent Suite — Quickstart

Get up and running in under 5 minutes.

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.9+ | `python --version` |
| pip | any | bundled with Python |
| Claude Code | latest | optional but recommended |
| Obsidian | any | optional — vault features only |

---

## Step 1 — Install

**macOS / Linux:**
```bash
git clone https://github.com/YOUR_ORG/pi-agent-suite
cd pi-agent-suite
bash installer/install.sh
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/YOUR_ORG/pi-agent-suite
cd pi-agent-suite
powershell -ExecutionPolicy Bypass -File installer/install.ps1
```

The installer will:
- Install `mempalace` via pip
- Copy the agent engine to `~/.pi/`
- Install hooks into `~/.pi/hooks/`
- Wire up Claude Code settings (optional)
- Write `~/.pi/env.sh` / `env.ps1` with env vars

---

## Step 2 — Mine a project

Tell MemPalace about your codebase so it can recall patterns:

```bash
mempalace mine ~/your-project
```

For a large monorepo, mine sub-directories:
```bash
mempalace mine ~/your-project/src
mempalace mine ~/your-project/docs
```

---

## Step 3 — Test the harness

```bash
# Route a task to the best agent
python -m harness route "build a login form with JWT auth"

# Search memory directly
python ~/.pi/agent/bin/mempalace_fast.py search "react hooks patterns"

# Get routing statistics
python -m harness info
```

---

## Step 4 — Open Claude Code

Hooks fire automatically on every conversation:

- **UserPromptSubmit** → injects top-3 MemPalace memories into your prompt
- **Stop** → mines the conversation transcript into MemPalace every 15 exchanges
- **PreCompact** → saves session context before context compression

You should see `<mempalace-context>` blocks appear in Claude Code's context when you start coding.

---

## Step 5 — Try a full workflow

In Claude Code, type:
```
Build me a REST API endpoint for user registration
```

Claude will:
1. Receive top-3 MemPalace memories auto-injected (auth patterns, your stack, etc.)
2. Route the task through the harness (backend agent + security agent)
3. Apply patterns from your ingested codebase
4. Save the conversation to MemPalace on completion

---

## Verify everything is working

```bash
bash installer/verify.sh
```

Expected output:
```
[OK] Python 3.x.x
[OK] mempalace installed
[OK] chromadb installed
[OK] Harness files present
[OK] Palace data exists
[OK] Routing test passed
```

---

## Common first-run issues

**`mempalace` not found after install:**
```bash
source ~/.pi/env.sh   # or restart your terminal
```

**Palace is empty:**
```bash
mempalace mine ~/your-project
```

**Claude Code hooks not firing:**
Check `~/.claude/settings.json` — hooks should appear under `hooks.UserPromptSubmit`.
If missing, re-run: `bash installer/install.sh --non-interactive`

**Windows: execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Next steps

- [Architecture overview](ARCHITECTURE.md) — how all the pieces fit together
- [Full installation guide](docs/01-installation.md) — advanced options
- [Customizing agents](docs/07-customization.md) — add your own skills
- [Troubleshooting](TROUBLESHOOTING.md) — when things go wrong
