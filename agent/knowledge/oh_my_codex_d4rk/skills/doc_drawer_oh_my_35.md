sk only when a choice materially changes scope or behavior.

## Scoped File Lists and Ralph Workflow

- This skill can accept a **file list scope** instead of a whole feature area.
- When the caller provides a changed-files list (for example, Ralph session-owned edits), keep the cleanup strictly bounded to those files.
- In the **Ralph workflow**, the mandatory deslop pass should run this skill on Ralph's changed files only, in standard mode unless the caller explicitly requests otherwise.

## Procedure

1. **Lock behavior with regression tests first**
   - Identify the behavior that must not change
   - Add or run targeted regression tests before editing cleanup candidates
   - If behavior is currently untested, create the narrowest test coverage needed first