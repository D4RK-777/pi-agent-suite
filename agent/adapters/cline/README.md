# Cline Adapter

Integrates the Pi Harness with the Cline VSCode extension.

## What gets configured

| Component | Location | Purpose |
|---|---|---|
| Skill file | `~/.cline/skills/pi-harness.md` | Instructs Cline to search MemPalace before coding |
| Project rules | `.clinerules` | Repo-specific Pi Harness routing |

## Automatic setup

```powershell
.\setup-ai-harness.ps1 -AI cline
```

## Manual setup

Create `~/.cline/skills/pi-harness.md`:

```markdown
# Pi Harness Memory Search

Before starting any coding task, search MemPalace for relevant patterns:

  python ~/.pi/agent/bin/mempalace_fast.py search "<task keywords>"

Route complex tasks to the best specialist agent:

  python -m harness route "<task description>"
  (Run from ~/.pi/agent/)
```

## Project-level rules

Add to `.clinerules` in your project root:

```markdown
## Memory System (Pi MemPalace)

Before starting any task:
1. Search memory: python ~/.pi/agent/bin/mempalace_fast.py search "<keywords>"
2. Use recalled patterns and past decisions in your implementation
3. Route complex multi-step tasks: python -m harness route "<task>"

The memory system contains your codebase patterns, past decisions, and coding preferences.
Always check it first.
```

## Sync Pi skills to Cline

```powershell
.\agent\scripts\sync-skills.ps1 -ClineSkillsPath "~/.cline/skills"
```
