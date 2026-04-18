>' not found in user or project scope"

**Safety:** Never delete without explicit user confirmation.

**Example:**
```
User: /skill remove old-logger
Assistant: Found skill 'old-logger' in user scope:
  Description: Legacy logging utility
  Scope: user (~/.codex/skills/)

Delete 'old-logger' skill? (yes/no)

User: yes
Assistant: ✓ Removed skill 'old-logger' from user scope
```

---

### /skill edit <name>

Edit an existing skill interactively.