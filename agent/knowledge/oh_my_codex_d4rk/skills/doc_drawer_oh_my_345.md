logger, logging
File: ~/.codex/skills/custom-logger/SKILL.md

--- CONTENT ---
# Custom Logger Skill

## Purpose
Enhanced logging with structured JSON output...
[rest of content]
```

---

### /skill sync

Sync skills between user and project scopes.

**Behavior:**
1. **Scan both scopes:**
   - User skills: `~/.codex/skills/`
   - Project skills: `.codex/skills/`
2. **Compare and categorize:**
   - User-only skills (not in project)
   - Project-only skills (not in user)
   - Common skills (in both)
3. **Display sync opportunities:**

```
SYNC REPORT:

User-only skills (5):
  - error-handler
  - api-builder
  - custom-logger
  - test-generator
  - deploy-helper

Project-only skills (2):
  - test-runner
  - backend-scaffold

Common skills (3):
  - frontend-ui-ux
  - git-master
  - planner