# 06 — Other AI Clients

How to integrate Pi Agent Suite with AI clients other than Claude Code.

---

## Overview

The Pi Harness works with any AI client that supports one of:
- Custom system prompts or rules files
- Skill/tool files
- Shell command execution

The `agent/adapters/` directory contains client-specific integration files. The `setup-ai-harness.ps1` script installs them all at once:

```powershell
# Install for all clients
.\setup-ai-harness.ps1

# Install for one client only
.\setup-ai-harness.ps1 -AI claude
.\setup-ai-harness.ps1 -AI cursor
.\setup-ai-harness.ps1 -AI cline
.\setup-ai-harness.ps1 -AI codex
.\setup-ai-harness.ps1 -AI windsurf
```

---

## Cursor

**Integration point:** `.cursorrules` file

The installer appends a Pi Harness section to `~/.cursor/.cursorrules`:

```
============================================================
PI HARNESS — MEMORY CONTEXT
============================================================

Before starting any task, search Pi MemPalace for relevant patterns:

  powershell -ExecutionPolicy Bypass -File "$PI_AGENT_HOME\pi-harness.ps1" search "<task keywords>"

This returns the top matching memories from your local knowledge base.
Route complex tasks:
  powershell -ExecutionPolicy Bypass -File "$PI_AGENT_HOME\pi-harness.ps1" route "<task description>"
============================================================
```

Cursor reads `.cursorrules` on startup and includes it in every conversation.

**Manual setup:**
1. Open `~/.cursor/.cursorrules` (create if missing)
2. Add the Pi Harness block above, replacing the path with your `PI_AGENT_HOME`

---

## Cline (VSCode extension)

**Integration point:** Cline skill files

The installer creates `~/.cline/skills/pi-harness.md`:

```markdown
# Pi Harness
Search Pi MemPalace for relevant patterns before coding.

powershell -ExecutionPolicy Bypass -File "$PI_AGENT_HOME\pi-harness.ps1" search "query"
```

**Manual setup:**
1. Create `~/.cline/skills/pi-harness.md`
2. Add the content above

---

## Windsurf

**Integration point:** `.windsurfrules` file

Similar to Cursor — the installer appends to `~/.windsurfrules`.

**Manual setup:**
1. Open `~/.windsurfrules`
2. Add the Pi Harness block

---

## Codex (OpenAI CLI)

**Integration point:** Codex skill files

The installer creates `~/.codex/skills/pi-harness.md` with instructions to search MemPalace before coding tasks.

---

## Gemini CLI

**Integration point:** Gemini tool/skill files

See `agent/adapters/gemini/` for Gemini-specific integration files.

---

## Any AI client with a system prompt

For any AI client that lets you customize the system prompt or add context files, add this block:

```markdown
## Memory System (Pi MemPalace)

Before starting any coding task, retrieve relevant memories:

  python /path/to/.pi/agent/bin/mempalace_fast.py search "<task description>"

Or route to the best specialist agent:

  python -m harness route "<task description>"
  (Run from: /path/to/.pi/agent/)

The memory system has been trained on your codebase, past decisions, and coding patterns.
Always check it first to avoid repeating solutions you've already built.
```

---

## Manual memory search from any client

Any AI client can trigger a memory search by instructing the user to run:

```bash
# Bash (macOS/Linux)
python ~/.pi/agent/bin/mempalace_fast.py search "react pagination"

# PowerShell (Windows)
python $env:PI_AGENT_HOME\agent\bin\mempalace_fast.py search "react pagination"

# Via harness launcher
.\pi-harness.ps1 search "react pagination"
```

Then paste the output back into the AI client's conversation.

---

## Adapter files reference

```
agent/adapters/
├── claude/
│   ├── README.md              # Claude Code-specific setup
│   └── slash-commands/        # /memory, /route commands
├── codex/
│   └── skills/pi-harness.md
├── cline/
│   └── skills/pi-harness.md
├── cursor/
│   └── cursorrules-snippet.md
├── windsurf/
│   └── windsurfrules-snippet.md
└── gemini/
    └── README.md
```

---

## Hooks for non-Claude clients

The UserPromptSubmit/Stop/PreCompact hook mechanism is Claude Code-specific. For other clients, memory injection is either manual (run search, paste results) or semi-automatic via client-specific skill files.

For clients that support custom tool/function definitions, you can expose MemPalace as a callable:

```python
# Expose MemPalace as a tool (adapt to your client's format)
from mempalace import search

tool_definition = {
  "name": "search_memory",
  "description": "Search Pi MemPalace for relevant patterns and past decisions",
  "parameters": {
    "query": {"type": "string"}
  },
  "execute": lambda query: search(query, n=3)
}
```
