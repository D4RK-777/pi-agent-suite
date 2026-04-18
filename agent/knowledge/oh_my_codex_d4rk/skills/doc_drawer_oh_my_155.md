ug}-{timestamp}.md` (UTC `YYYYMMDDTHHMMSSZ`) and reference it in mode state.

## Phase 1: Initialize

1. Parse `{{ARGUMENTS}}` and depth profile (`--quick|--standard|--deep`).
2. Detect project context:
   - Run `explore` to classify **brownfield** (existing codebase target) vs **greenfield**.
   - For brownfield, collect relevant codebase context before questioning.
3. Initialize state via `state_write(mode="deep-interview")`: