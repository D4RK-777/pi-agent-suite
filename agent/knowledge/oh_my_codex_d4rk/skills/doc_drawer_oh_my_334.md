---
name: skill
description: Manage local skills - list, add, remove, search, edit, setup wizard
argument-hint: "<command> [args]"
---

# Skill Management CLI

Meta-skill for managing oh-my-codex skills via CLI-like commands.

## Subcommands

### /skill list

Show all local skills organized by scope.

**Behavior:**
1. Scan user skills at `~/.codex/skills/`
2. Scan project skills at `.codex/skills/`
3. Parse YAML frontmatter for metadata
4. Display in organized table format:

```
USER SKILLS (~/.codex/skills/):
| Name              | Triggers           | Quality | Usage | Scope |
|-------------------|--------------------|---------|-------|-------|
| error-handler     | fix, error         | 95%     | 42    | user  |
| api-builder       | api, endpoint      | 88%     | 23    | user  |