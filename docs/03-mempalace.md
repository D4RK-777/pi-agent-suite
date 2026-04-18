# 03 — MemPalace

The semantic memory engine powering Pi Agent Suite.

---

## What is MemPalace?

MemPalace is a local ChromaDB-backed vector database designed for AI agent memory. It stores any text as embeddings and recalls the most semantically similar items in ~22ms.

- **No API key required** — runs entirely locally
- **96.6% recall accuracy** on LongMemEval benchmark
- **~2500 drawers** in a typical developer setup
- **Wings/rooms/drawers** architecture for organized storage
- **29 MCP tools** for Claude Code integration
- **Verbatim storage** — never paraphrases what you put in

**Source:** github.com/milla-jovovich/mempalace (MIT license)

---

## Concepts

### Drawers

The atomic unit of memory. Each drawer stores:
- `content` — verbatim text (code, decision, note, transcript excerpt)
- `source` — where it came from (file path, session ID, etc.)
- `wing` — namespace (see below)
- `tags` — list of tags for filtering
- `timestamp` — when it was stored
- `embedding` — vector used for semantic search (auto-generated)

### Wings

Top-level namespaces. Think of them like folders. Default wings:

| Wing | Contents |
|---|---|
| `code` | Code patterns, implementations, snippets |
| `decisions` | Architectural choices, technology decisions |
| `sessions` | Conversation transcript excerpts |
| `knowledge` | Domain knowledge, documentation notes |
| project-specific | e.g., `gloss`, `konekt`, your project name |

List your wings:
```python
from mempalace import list_wings
print(list_wings())
```

### Rooms

Sub-namespaces within a wing. Optional — not all wings have rooms.

### Taxonomy

The full wing → room → drawer hierarchy:
```python
from mempalace import get_taxonomy
print(get_taxonomy())
```

---

## Installation

MemPalace installs via pip:
```bash
pip install mempalace
```

Data is stored at `~/.mempalace/palace/` by default. Override with:
```bash
export MEMPALACE_PALACE="/custom/path/palace"
```

---

## Mining your codebase

Before MemPalace can recall anything, it needs to learn your project:

```bash
# Mine a directory
mempalace mine ~/your-project

# Mine with a specific wing
mempalace mine ~/your-project --wing code

# Mine with exclusions (recommended for large repos)
mempalace mine ~/your-project \
  --exclude "node_modules,.obsidian,__pycache__,.git,*.pyc,*.min.js"

# Verbose mode to see what's being indexed
mempalace mine ~/your-project --verbose
```

**What gets indexed:** Source files (`.py`, `.ts`, `.js`, `.md`, `.json`, `.yaml`, etc.)
**What to exclude:** Build artifacts, bundled JS, `.obsidian/` plugin files (they OOM the HNSW index), binary files

---

## Searching

```bash
# CLI
mempalace search "react pagination hook"

# Python
from mempalace import search
results = search("JWT auth patterns", n=5)

# With wing filter
results = search("login component", wing="code", n=3)

# Fast wrapper (used by hooks)
python ~/.pi/agent/bin/mempalace_fast.py search "react hooks"
```

---

## Adding drawers manually

```bash
# CLI
mempalace add --content "Always use httpOnly cookies for session tokens" \
              --wing decisions \
              --tags "security,auth,sessions"

# Python
from mempalace import add_drawer
add_drawer(
    content="Always use httpOnly cookies for session tokens",
    wing="decisions",
    source="manual",
    tags=["security", "auth", "sessions"]
)
```

**Important:** MemPalace's core promise is **verbatim** storage. Never paraphrase before adding — the exact wording matters for recall accuracy.

---

## Statistics

```bash
# CLI
mempalace status

# Python
from mempalace import get_stats
stats = get_stats()
print(f"Total drawers: {stats['total_drawers']}")
print(f"Wings: {stats['wings']}")

# Via pi-harness
python ~/.pi/agent/bin/mempalace_fast.py stats
```

---

## MCP tools in Claude Code

When MemPalace runs as an MCP server, Claude Code can use these tools directly:

```
mempalace_search          - semantic search
mempalace_add_drawer      - store a memory
mempalace_list_wings      - list namespaces
mempalace_get_taxonomy    - full structure
mempalace_get_stats       - counts and sizes
mempalace_delete_drawer   - remove a drawer
mempalace_update_drawer   - update content
mempalace_get_drawer      - get by ID
mempalace_list_drawers    - list with filters
... (29 tools total)
```

Claude Code will invoke these automatically based on context, or you can ask:
```
Search memory for any previous work on authentication middleware
Add this pattern to memory: [pattern text]
```

---

## Hook integration

### UserPromptSubmit hook

`mempalace_prompt_hook.py` runs on every prompt:

```python
# Simplified logic
results = search(prompt_text, n=3)
for result in results:
    print(f"<mempalace-context>")
    print(f"## Memory: {result['source']}")
    print(result['content'][:500])
    print("</mempalace-context>")
```

### Stop hook

`mempal_save_hook.sh` mines the session transcript:

```bash
# Every MEMPAL_SAVE_INTERVAL (default: 15) exchanges
mempalace mine /tmp/claude-transcript-*.json --wing sessions
```

### PreCompact hook

`mempal_precompact_hook.sh` saves the full session before compression:

```bash
# Runs once before context compression
mempalace mine /tmp/claude-precompact-*.json --wing sessions --tags "precompact"
```

---

## Performance tuning

**Slow search:**
- Ensure palace is on SSD (not spinning disk or network drive)
- Keep palace under 50k drawers (beyond this, HNSW index rebuild slows cold start)
- Split large palaces into multiple specialized palaces

**High memory usage during mining:**
- Use `--exclude` to skip large files
- Never mine `.obsidian/` plugin bundles — they OOM the HNSW index (this has burned people before)
- Mine in smaller batches: `mempalace mine src/` then `mempalace mine docs/`

**Palace size:**
```bash
du -sh ~/.mempalace/palace/
# Typical: 50–500MB for a full developer memory
```

---

## Backup and restore

```bash
# Backup
cp -r ~/.mempalace/palace ~/palace-backup-$(date +%Y%m%d)

# Restore
cp -r ~/palace-backup-20240315 ~/.mempalace/palace

# Export to JSON (for migration)
python -m mempalace.cli export --output ~/mempalace-export.json
```

---

## Troubleshooting

See [TROUBLESHOOTING.md](../TROUBLESHOOTING.md#mempalace) for common issues.
