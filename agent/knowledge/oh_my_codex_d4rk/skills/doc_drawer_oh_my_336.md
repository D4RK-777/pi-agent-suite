not available, show "N/A"

---

### /skill add [name]

Interactive wizard for creating a new skill.

**Behavior:**
1. **Ask for skill name** (if not provided in command)
   - Validate: lowercase, hyphens only, no spaces
2. **Ask for description**
   - Clear, concise one-liner
3. **Ask for triggers** (comma-separated keywords)
   - Example: "error, fix, debug"
4. **Ask for argument hint** (optional)
   - Example: "<file> [options]"
5. **Ask for scope:**
   - `user` → `~/.codex/skills/<name>/SKILL.md`
   - `project` → `.codex/skills/<name>/SKILL.md`
6. **Create skill file** with template:

```yaml
---
name: <name>
description: <description>
triggers:
  - <trigger1>
  - <trigger2>
argument-hint: "<args>"
---

# <Name> Skill

## Purpose

[Describe what this skill does]

## When to Activate