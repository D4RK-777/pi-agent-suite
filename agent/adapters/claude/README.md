# Claude Code Adapter

Integrates the Pi Harness with Claude Code via hooks, MCP servers, and slash commands.

## What gets configured

| Component | Location | Purpose |
|---|---|---|
| `UserPromptSubmit` hook | `~/.claude/settings.json` | Auto-injects top-3 MemPalace memories before every prompt |
| `Stop` hook | `~/.claude/settings.json` | Auto-mines conversation to MemPalace every N exchanges |
| `PreCompact` hook | `~/.claude/settings.json` | Saves session before context compression |
| MemPalace MCP server | `~/.claude/settings.json` | 29 tools for direct memory access in Claude Code |
| `/memory` command | `~/.claude/commands/memory.md` | Slash command to search MemPalace |

## Automatic setup

Run the installer:
```bash
bash installer/install.sh   # answer Y to "Patch Claude Code?"
```

Or run the multi-client setup script:
```powershell
.\setup-ai-harness.ps1 -AI claude
```

## Manual setup

Add to `~/.claude/settings.json`:
```json
{
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
  },
  "mcpServers": {
    "mempalace": {
      "command": "python",
      "args": ["-m", "mempalace.mcp_server", "--palace", "~/.mempalace/palace"]
    }
  }
}
```

## Skill files

Place skill `.md` files in `~/.claude/skills/` to make them available globally.

Sync all Pi skills to Claude Code:
```powershell
.\agent\scripts\sync-skills.ps1 -ClaudeSkillsPath "~/.claude/skills"
```

## Project-local CLAUDE.md

For repo-specific routing, add to your project's `CLAUDE.md`:

```markdown
## Memory System
Before starting any task, your UserPromptSubmit hook has already injected
relevant MemPalace context. Read the <mempalace-context> blocks first.

For explicit search:
  python ~/.pi/agent/bin/mempalace_fast.py search "query"

Route complex tasks:
  python -m harness route "task description"  (from ~/.pi/agent/)
```

## MCP tools available

After configuring the MCP server, Claude Code has these MemPalace tools:
`mempalace_search`, `mempalace_add_drawer`, `mempalace_list_wings`,
`mempalace_get_taxonomy`, `mempalace_get_stats`, and 24 more.

See [docs/02-claude-code.md](../../../docs/02-claude-code.md) for full details.
