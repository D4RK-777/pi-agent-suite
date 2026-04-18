kills/) - Available across all projects
- **Project-level** (.codex/skills/) - Only for this project

Validate the skill format and save to the chosen location.

---

### /skill scan

Quick command to scan both skill directories (subset of `/skill setup`).

**Behavior:**
Run the scan from Step 2 of `/skill setup` without the interactive wizard.

---

## Skill Templates

When creating skills via `/skill add` or `/skill setup`, offer quick templates for common skill types:

### Error Solution Template

```markdown
---
id: error-[unique-id]
name: [Error Name]
description: Solution for [specific error in specific context]
source: conversation
triggers: ["error message fragment", "file path", "symptom"]
quality: high
---

# [Error Name]