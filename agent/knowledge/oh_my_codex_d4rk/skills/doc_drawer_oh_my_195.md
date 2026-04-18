`~/.agents/skills` tree if it overlaps with the canonical `${CODEX_HOME:-~/.codex}/skills` install:

```bash
# Backup first (optional - ask user)
# mv ~/.codex/agents ~/.codex/agents.bak
# mv ~/.codex/commands ~/.codex/commands.bak
# mv ~/.agents/skills ~/.agents/skills.bak

# Or remove directly
rm -rf ~/.codex/agents
rm -rf ~/.codex/commands
rm -rf ~/.agents/skills
```

**Note**: Only remove if these contain oh-my-codex-related files. If user has custom agents/commands/skills, warn them and ask before removing.

---

## Post-Fix

After applying fixes, inform user:
> Fixes applied. **Restart Codex CLI** for changes to take effect.