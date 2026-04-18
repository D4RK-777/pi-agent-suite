---
name: note
description: Save notes to notepad.md for compaction resilience
---

# Note Skill

Save important context to `.omx/notepad.md` that survives conversation compaction.

## Usage

| Command | Action |
|---------|--------|
| `/note <content>` | Add to Working Memory with timestamp |
| `/note --priority <content>` | Add to Priority Context (always loaded) |
| `/note --manual <content>` | Add to MANUAL section (never pruned) |
| `/note --show` | Display current notepad contents |
| `/note --prune` | Remove entries older than 7 days |
| `/note --clear` | Clear Working Memory (keep Priority + MANUAL) |

## Sections