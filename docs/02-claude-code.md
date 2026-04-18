# 02 — Claude Code Integration

How to wire Pi Agent Suite into Claude Code for full automatic memory injection and session mining.

---

## What gets configured

The installer sets up three things in Claude Code:

1. **Three hooks** (UserPromptSubmit, Stop, PreCompact)
2. **MemPalace MCP server** (29 tools available in Claude Code)
3. **`/memory` slash command** (optional convenience shortcut)

---

## Automatic setup

The installer handles this automatically if you answer `Y` to the Claude Code prompt:

```bash
bash installer/install.sh
# > Patch Claude Code settings.json? [Y/n]: Y
```

Or force it:
```bash
bash installer/install.sh --non-interactive  # defaults to patching Claude Code
```

---

## Manual setup

If you need to configure Claude Code manually, edit `~/.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "python /home/you/.pi/agent/bin/mempalace_prompt_hook.py",
        "timeout": 2
      }]
    }],
    "Stop": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash /home/you/.pi/hooks/mempal_save_hook.sh",
        "timeout": 30
      }]
    }],
    "PreCompact": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "bash /home/you/.pi/hooks/mempal_precompact_hook.sh",
        "timeout": 30
      }]
    }]
  },
  "mcpServers": {
    "mempalace": {
      "command": "python",
      "args": ["-m", "mempalace.mcp_server", "--palace", "/home/you/.mempalace/palace"]
    }
  }
}
```

Replace `/home/you/.pi` with your actual `PI_AGENT_HOME` path.

---

## Hooks explained

### UserPromptSubmit — auto memory injection

Fires before every prompt is sent to Claude. The hook:
1. Takes your prompt text as stdin
2. Searches MemPalace for the top 3 semantically similar drawers
3. Injects results as `<mempalace-context>` blocks into the conversation

**You don't need to do anything.** The injected context appears automatically, and Claude Code reads it before responding.

**Timeout:** 2 seconds. If the palace is slow to respond, the hook fails silently — Claude Code continues without context rather than blocking you.

**What you'll see in Claude Code context:**
```
<mempalace-context>
## Memory: JWT Auth Pattern (code wing)
[relevant code pattern you wrote before]

## Memory: React Query setup (code wing)
[your preferred data fetching setup]

## Memory: Session decision 2024-03-15 (decisions wing)
[decision: use httpOnly cookies, not localStorage]
</mempalace-context>
```

---

### Stop — auto session mining

Fires after every conversation ends or every `MEMPAL_SAVE_INTERVAL` (default: 15) exchanges.

The hook:
1. Reads the conversation transcript
2. Mines it into MemPalace as new drawers
3. Updates the exchange counter in `~/.mempalace/hook_state/`

**Effect:** Every coding session automatically adds to your memory. Next conversation, those patterns are available.

**Tuning the interval:**
```bash
export MEMPAL_SAVE_INTERVAL=10   # save more frequently
export MEMPAL_SAVE_INTERVAL=30   # save less frequently
```

---

### PreCompact — save before compression

Fires before Claude Code compresses the context window. Saves the full untruncated session first, ensuring no knowledge is lost to context compression.

---

## MCP Server (29 tools)

When `mempalace` is configured as an MCP server, Claude Code gets direct access to the full MemPalace API:

| Tool | Description |
|---|---|
| `mempalace_search` | Semantic search across all wings |
| `mempalace_add_drawer` | Store a new memory (verbatim) |
| `mempalace_list_wings` | List all wings |
| `mempalace_get_taxonomy` | Get wing/room structure |
| `mempalace_get_stats` | Memory statistics |
| ... | 24 more tools |

**Usage from Claude Code:**
Just ask — Claude Code will use these tools automatically when it needs to search or store memories. You can also request explicitly:

```
Search my memory for React patterns related to pagination
```

---

## Obsidian MCP server (optional)

For full vault integration, add the Obsidian MCP server:

```bash
npm install -g obsidian-mcp-server

claude mcp add obsidian npx -- obsidian-mcp-server \
  --api-key "your-local-rest-api-key" \
  --vault "YourVaultName"
```

This adds `obsidian_search`, `obsidian_readFile`, `obsidian_appendContent`, and `obsidian_createFile` tools.

**Prerequisite:** Obsidian must be running with the "Local REST API" community plugin enabled.

---

## Slash commands

The installer creates a `/memory` command in Claude Code:

```
/memory react hooks patterns
```

This is equivalent to running the Pi Harness search directly from Claude Code's command palette.

To add custom commands, create markdown files in `~/.claude/commands/`:

```markdown
# Route Task
# Usage: /route <task description>

Run the Pi Harness router for the given task.

$TASK = $args -join ' '
& powershell -ExecutionPolicy Bypass -File "$env:PI_AGENT_HOME\pi-harness.ps1" route $TASK
```

---

## Verifying the integration

1. Open Claude Code
2. Start a new conversation
3. Type any coding-related prompt
4. Check if `<mempalace-context>` appears in the context view (`/context` command)

If no context appears after mining your project, see [TROUBLESHOOTING.md](../TROUBLESHOOTING.md#hooks-not-firing-in-claude-code).

---

## settings.json reference

The full annotated config template is at `config/claude-settings.json`. It shows all available options with explanations.
