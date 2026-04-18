# Pi Agent Suite — Architecture

## Overview

Pi Agent Suite is a three-layer intelligence system that gives any AI coding assistant long-term memory, specialist agent routing, and structured knowledge management.

```
┌─────────────────────────────────────────────────────────────────────┐
│                           AI CLIENT LAYER                           │
│   Claude Code  │  Cursor  │  Cline  │  Codex  │  Windsurf  │  ...  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  hooks / adapters
┌──────────────────────────────▼──────────────────────────────────────┐
│                         PI HARNESS LAYER                            │
│                                                                     │
│   Brain (router.py)                                                 │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │  6-signal scoring → picks best specialist agent              │   │
│   │  explicit name | skill keywords | skill tags |              │   │
│   │  domain focus  | role/note      | intent keywords           │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│   Agents (8 specialists)                                            │
│   advisor · backend · debugger · frontend · librarian              │
│   reviewer · scout · _template                                      │
│                                                                     │
│   Skills (composable units)    Bundles (curated skill sets)        │
│   auto-memory · mempalace-tools · obsidian-tools · pi-spawn        │
│   adaptive-recovery · pi-tasks · hook-connector · ...              │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
        ┌──────────────────────┴──────────────────────┐
        │                                             │
┌───────▼────────┐                         ┌──────────▼──────────┐
│   MEMPALACE    │                         │  OBSIDIAN VAULT      │
│   (ChromaDB)   │                         │  (OmegaD4rkMynd      │
│                │                         │   pattern)           │
│  ~2500 drawers │                         │                      │
│  wings/rooms   │                         │  wiki/ (Karpathy)    │
│  96.6% recall  │                         │  decisions/          │
│  22ms latency  │                         │  patterns/           │
│                │                         │  sessions/           │
│  MCP: 29 tools │                         │  MCP: obsidian-mcp   │
└────────────────┘                         └──────────────────────┘
```

---

## Component deep-dives

### MemPalace (ChromaDB)

The semantic memory engine. Stores code patterns, decisions, and conversation context as embeddings that can be recalled in milliseconds.

```
~/.mempalace/
├── palace/                    # ChromaDB data
│   ├── chroma.sqlite3
│   └── ...
└── hook_state/                # hook counters and session IDs
    ├── exchange_counter
    └── last_session_id
```

**Wings** — top-level namespaces (like folders):
- `code` — patterns, implementations
- `decisions` — architectural choices
- `sessions` — conversation transcripts
- `knowledge` — domain knowledge
- `gloss` / project-specific wings

**Drawers** — individual memory entries. Each drawer has:
- `content` — verbatim text
- `metadata` — source, wing, timestamp, tags
- `embedding` — semantic vector for similarity search

**Recall flow:**
1. `UserPromptSubmit` hook fires on every Claude Code prompt
2. `mempalace_prompt_hook.py` runs, searches top-3 drawers matching the prompt
3. Results are injected as `<mempalace-context>` tags into the conversation
4. Claude Code reads these automatically before responding

---

### Pi Harness (Brain + Router)

The task routing and orchestration engine.

```
agent/
├── brain/
│   ├── router.py              # SKILL_REGISTRY + 6-signal scoring
│   ├── launch.py              # session lifecycle + mining
│   └── skill_governance.py   # skill audit + deduplication
├── harness/
│   ├── router.py              # manifest-based routing
│   ├── orchestrator.py        # CLI dispatcher
│   ├── memory.py              # MemPalace integration
│   └── enforcement.py        # compliance watching
├── agents/                    # 8 specialist agent directories
├── manifests/                 # agent capability declarations
├── skills/                    # composable skill modules
├── bundles/                   # curated skill sets
├── cookbooks/                 # multi-step workflows
└── adapters/                  # AI client integrations
```

**6-signal routing algorithm** (in `brain/router.py`):

| Signal | Points | Description |
|---|---|---|
| Explicit name/alias | 10 | User names an agent directly |
| Skill keywords | 1.5–2.0 | Task words match skill vocabulary |
| Skill tags | 1.0 | Task words match agent tags |
| Domain focus | 0.5/word | Task domain matches agent domain |
| Role/note | 0.25–0.5/word | Task matches agent role description |
| Intent keywords | 0.5–1.0 | General intent signals |

The agent with the highest score wins. Ties fall back to the `advisor` agent.

---

### Claude Code Hooks

Three hooks wire the Pi Harness into Claude Code's lifecycle:

```
UserPromptSubmit ──► mempalace_prompt_hook.py
                     • searches top-3 memories for current prompt
                     • injects <mempalace-context> blocks
                     • must complete in < 500ms (silent fail past that)

Stop ─────────────► mempal_save_hook.sh
                     • fires every MEMPAL_SAVE_INTERVAL (default: 15) exchanges
                     • mines the Claude Code transcript to MemPalace
                     • runs in background (30s timeout)

PreCompact ────────► mempal_precompact_hook.sh
                     • fires before Claude Code compresses the context window
                     • saves the full session before any truncation
                     • ensures nothing is lost to compression
```

---

### Obsidian Vault (OmegaD4rkMynd pattern)

The curated long-term knowledge store. Uses the **Karpathy LLM Wiki** pattern: Claude is the maintainer, you are the curator.

```
vault/
├── raw/                       # immutable source documents (Claude: read-only)
│   └── articles/
├── wiki/                      # Claude-maintained knowledge graph
│   ├── sources/               # summaries of raw docs
│   ├── concepts/              # atomic concept pages
│   ├── entities/              # people, orgs, products
│   ├── comparisons/           # A-vs-B pages
│   ├── syntheses/             # cross-cutting analyses
│   ├── index.md               # master index
│   ├── hot.md                 # 10-15 recently touched concepts
│   └── log.md                 # append-only operation log
├── decisions/                 # architectural commitments
├── patterns/                  # reusable code patterns
└── sessions/                  # session notes
```

**Three operations:**
- `ingest <source>` — reads a raw doc, creates/updates wiki pages, updates index and log
- `query <question>` — searches wiki, optionally creates synthesis pages
- `lint` — reports orphans, stale pages, contradictions, index drift

**Source of truth rule:** Obsidian wins over MemPalace. If a wiki page contradicts a MemPalace drawer, the page is right.

---

### Adapters

Thin integration layers for AI clients other than Claude Code:

```
agent/adapters/
├── claude/       # Claude Code — hooks + MCP + skills
├── codex/        # OpenAI Codex — skill files
├── cline/        # Cline VSCode extension
├── cursor/       # Cursor — .cursorrules injection
├── windsurf/     # Windsurf — .windsurfrules injection
└── gemini/       # Google Gemini CLI
```

Each adapter provides the same MemPalace search capability but adapted to the client's extension point (skill files, config files, hooks, MCP servers).

---

## Data flows

### Coding task (full flow)

```
User types prompt in Claude Code
         │
         ▼
UserPromptSubmit hook fires
mempalace_prompt_hook.py runs
Top-3 semantic matches injected as <mempalace-context>
         │
         ▼
Claude Code receives prompt + injected context
Responds using recalled patterns + current conversation
         │
         ▼
(every 15 exchanges)
Stop hook fires
mempal_save_hook.sh runs
Transcript mined → new drawers in MemPalace
         │
         ▼
Next conversation picks up accumulated memory
```

### Manual routing query

```
python -m harness route "build a login form with JWT"
         │
         ▼
brain/router.py scores all agents using 6 signals
Backend agent wins (auth + API keywords)
         │
         ▼
Agent manifest loaded from manifests/
System prompt + skills injected
Task launched with session tracking
         │
         ▼
brain/launch.py runs session start/end hooks
Session saved to MemPalace on completion
```

---

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `PI_AGENT_HOME` | `~/.pi` | Root of Pi install |
| `MEMPALACE_PALACE` | `~/.mempalace/palace` | ChromaDB data directory |
| `MEMPAL_SAVE_INTERVAL` | `15` | Exchanges between auto-saves |
| `MEMPAL_INGEST_DIR` | _(empty)_ | Extra directory to mine on save |
| `OBSIDIAN_VAULT` | _(empty)_ | Path to Obsidian vault |
| `OBSIDIAN_API_KEY` | _(empty)_ | Local REST API key |
| `OBSIDIAN_VAULT_NAME` | _(empty)_ | Vault name for MCP server |

---

## Extending the system

- **Add a skill** → create `agent/skills/my-skill.md`, register in `brain/router.py` SKILL_REGISTRY
- **Add an agent** → copy `agents/_template/`, fill AGENT.md manifest, add to `manifests/`
- **Add a bundle** → create `bundles/my-bundle.json` listing skills
- **Add an adapter** → create `adapters/my-client/` with client-specific integration files

See [docs/07-customization.md](docs/07-customization.md) for full instructions.
