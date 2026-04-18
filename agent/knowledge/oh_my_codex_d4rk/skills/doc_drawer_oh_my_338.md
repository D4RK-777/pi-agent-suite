ated skill at ~/.codex/skills/custom-logger/SKILL.md
→ Edit with: /skill edit custom-logger
```

---

### /skill remove <name>

Remove a skill by name.

**Behavior:**
1. **Search for skill** in both scopes:
   - `~/.codex/skills/<name>/SKILL.md`
   - `.codex/skills/<name>/SKILL.md`
2. **If found:**
   - Display skill info (name, description, scope)
   - **Ask for confirmation:** "Delete '<name>' skill from <scope>? (yes/no)"
3. **If confirmed:**
   - Delete entire skill directory (e.g., `~/.codex/skills/<name>/`)
   - Report: "✓ Removed skill '<name>' from <scope>"
4. **If not found:**
   - Report: "✗ Skill '<name>' not found in user or project scope"

**Safety:** Never delete without explicit user confirmation.