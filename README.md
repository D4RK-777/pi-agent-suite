# Pi Agent Suite

**Persistent memory + intelligent routing for any AI coding assistant.**

Pi Agent Suite gives your AI three things it doesn't have by default:

1. **Persistent memory** — every conversation saved locally, recalled in <20ms with 96.6% accuracy (MemPalace)
2. **Intelligent routing** — deterministic 6-signal scoring routes tasks to the right specialist agent automatically
3. **Self-maintaining knowledge** — an Obsidian vault that builds its own wiki from your sessions

Works with Claude Code, OpenAI Codex, Cline, Cursor, Windsurf, and any AI client that supports system prompts or hooks.

---

## What you get

| Component | What it does |
|-----------|-------------|
| **MemPalace** | Local ChromaDB vector store. Mines your conversations verbatim, recalls them at query time. No API key. No cloud. |
| **Pi Harness** | Python routing engine. 6-signal scoring picks the right agent (frontend, backend, security, etc.) for each task. |
| **Claude Code hooks** | `UserPromptSubmit` injects top-3 relevant memories before every prompt. `Stop` and `PreCompact` auto-save in the background. |
| **Obsidian Vault template** | A structured wiki (Karpathy pattern + PARA) that Claude maintains as you work. |
| **AI adapters** | Config templates for Claude Code, Codex, Cline, Cursor, Windsurf, and a generic adapter. |

---

## Prerequisites

| Tool | Required | Notes |
|------|----------|-------|
| Python 3.9+ | Yes | For MemPalace and the harness engine |
| pip | Yes | To install MemPalace |
| Bash (Git Bash on Windows) | Yes | For hook scripts |
| Claude Code CLI | Recommended | Full hook + MCP integration |
| Obsidian | Optional | For the knowledge vault |
| Node.js 18+ | Optional | For the npm CLI installer |

---

## Installation

### Option A — Bash installer (Mac / Linux / Windows Git Bash)

```bash
curl -sSL https://raw.githubusercontent.com/D4RK-777/pi-agent-suite/main/installer/install.sh | bash
```

Or clone and run locally:

```bash
git clone https://github.com/D4RK-777/pi-agent-suite.git
cd pi-agent-suite
bash installer/install.sh
```

### Option B — PowerShell installer (Windows)

```powershell
git clone https://github.com/D4RK-777/pi-agent-suite.git
cd pi-agent-suite
.\installer\install.ps1
```

### Option C — npm (installs the CLI, then runs setup)

```bash
npm install -g pi-agent-suite
pi-agent setup
```

### Option D — Manual

See [docs/01-installation.md](docs/01-installation.md) for step-by-step instructions.

---

## Quick start (after install)

### 1. Verify the install

```bash
bash installer/verify.sh
# or on Windows:
python ~/.pi/agent/bin/mempalace_fast.py
```

### 2. Mine your first project

```bash
mempalace mine ~/path/to/your/project
```

### 3. Start Claude Code — hooks fire automatically

Every prompt now gets the top-3 relevant memories injected before Claude reasons. Every session is auto-saved in the background.

### 4. Search your memory directly

```bash
mempalace search "react hooks typescript"
# or via the harness:
pi search "react hooks typescript"
```

---

## Architecture overview

```
┌─────────────────────────────────────────────────────┐
│  Your AI client (Claude Code, Cline, Cursor, Codex) │
└────────────────────────┬────────────────────────────┘
                         │ every prompt
                         ▼
┌─────────────────────────────────────────────────────┐
│  UserPromptSubmit hook  (mempalace_prompt_hook.py)  │
│  → search MemPalace → inject top-3 drawers          │
└────────────────────────┬────────────────────────────┘
                         │ enriched prompt
                         ▼
┌─────────────────────────────────────────────────────┐
│  Pi Harness  (harness/router.py)                    │
│  6-signal routing: name, alias, skills, domain,     │
│  role, intent → selects best agent + skill set      │
└────────────────────────┬────────────────────────────┘
                         │ selected agent
                         ▼
┌──────────────────────────────────────────────────┐
│  Agents: director · advisor · frontend · backend │
│           security · auth · reviewer · debugger  │
└────────────────────────┬─────────────────────────┘
                         │ task execution
                         ▼
┌─────────────────────────────────────────────────────┐
│  Stop / PreCompact hooks                            │
│  → mempalace mine (background) → palace updated     │
└────────────────────────┬────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│  MemPalace  (ChromaDB, ~/.mempalace/palace/)        │
│  Verbatim drawers · wings · rooms · BM25+vector     │
└────────────────────────┬────────────────────────────┘
                         │ source of truth
                         ▼
┌─────────────────────────────────────────────────────┐
│  Obsidian Vault  (YourVault or your own)        │
│  Karpathy wiki · decisions · patterns · sessions    │
└─────────────────────────────────────────────────────┘
```

---

## Component docs

- [docs/01-installation.md](docs/01-installation.md) — detailed install steps
- [docs/02-mempalace.md](docs/02-mempalace.md) — MemPalace: wings, rooms, drawers, search
- [docs/03-harness.md](docs/03-harness.md) — Pi Harness: routing, agents, skills
- [docs/04-vault.md](docs/04-vault.md) — Obsidian Vault: ingest, query, lint ops
- [docs/05-hooks.md](docs/05-hooks.md) — Hook scripts: how the lifecycle works
- [docs/06-ai-setup.md](docs/06-ai-setup.md) — Per-client setup (Claude Code, Codex, Cline, Cursor)
- [docs/07-customization.md](docs/07-customization.md) — Adding agents, skills, adapters

---

## Directory layout

```
pi-agent-suite/
├── README.md
├── QUICKSTART.md
├── ARCHITECTURE.md
├── TROUBLESHOOTING.md
├── package.json
│
├── installer/
│   ├── install.sh          ← Mac/Linux/Git Bash installer
│   ├── install.ps1         ← Windows PowerShell installer
│   └── verify.sh           ← Post-install check
│
├── bin/                    ← Scripts installed to ~/.pi/agent/bin/
│   ├── mempalace_fast.py   ← Fast MemPalace wrapper (used by hooks)
│   └── mempalace_prompt_hook.py ← Claude Code UserPromptSubmit hook
│
├── hooks/                  ← Shell hook scripts
│   ├── mempal_save_hook.sh        ← Stop hook: auto-save every N exchanges
│   └── mempal_precompact_hook.sh  ← PreCompact hook: save before context compression
│
├── harness/                ← Python routing engine
│   ├── __init__.py
│   ├── __main__.py
│   ├── router.py           ← 6-signal deterministic agent router
│   ├── memory.py           ← MemPalace integration for the harness
│   ├── enforcement.py      ← Output validation and quality gates
│   └── orchestrator.py     ← CLI dispatcher
│
├── manifests/              ← Registry files
│   ├── agents.json         ← Agent definitions with aliases, skills, domains
│   ├── skills.json         ← Skill registry with paths and tags
│   └── domains.json        ← Domain definitions with lead/support agents
│
├── agents/                 ← Agent markdown definitions
│   ├── _template/          ← Copy this to create a new agent
│   ├── advisor/
│   ├── frontend/
│   ├── backend/
│   ├── debugger/
│   └── reviewer/
│
├── adapters/               ← Per-client configuration
│   ├── claude/             ← Claude Code (hooks + MCP)
│   ├── codex/              ← OpenAI Codex (AGENTS.md)
│   ├── cline/              ← Cline (.clinerules)
│   ├── cursor/             ← Cursor (.cursorrules)
│   ├── generic/            ← System prompt template
│   └── README.md
│
├── vault-template/         ← Obsidian vault starter
│   ├── CLAUDE.md           ← Ops manual (ingest / query / lint)
│   ├── wiki/               ← Auto-maintained wiki
│   ├── decisions/          ← Architectural decisions
│   ├── patterns/           ← Reusable code/design patterns
│   ├── sessions/           ← Session notes
│   └── raw/                ← Source material (read-only for Claude)
│
├── config/
│   └── claude-settings.json  ← Claude Code settings.json template
│
└── docs/                   ← Full documentation
```

---

## Environment variables

| Variable | Default | What it does |
|----------|---------|-------------|
| `PI_AGENT_HOME` | `~/.pi` | Root of the installed pi agent harness |
| `MEMPALACE_PALACE` | `~/.mempalace/palace` | ChromaDB data directory |
| `OBSIDIAN_VAULT` | (none) | Path to your Obsidian vault |
| `OBSIDIAN_API_KEY` | (none) | Key from Obsidian Local REST API plugin |

---

## Credits

- **MemPalace** — [github.com/milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace) — MIT license
- **Pi Harness** — Built on top of MemPalace, inspired by the D4rkMynd agent pattern
- **Obsidian** — [obsidian.md](https://obsidian.md) — the knowledge vault

---

## License

MIT — see [LICENSE](LICENSE).
