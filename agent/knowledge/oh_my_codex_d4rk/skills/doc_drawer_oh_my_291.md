order (foundational work first)
7. Proceed to normal ralph loop using user stories as the task list

### Example
User input: `--prd build a todo app with React and TypeScript`
Workflow: Detect flag, extract task, create `.omx/plans/prd-{slug}.md`, create `.omx/state/{scope}/ralph-progress.json`, begin ralph loop.

### Legacy compatibility
- If `.omx/prd.json` exists and canonical PRD is absent, migrate one-way into `.omx/plans/prd-{slug}.md`.
- If `.omx/progress.txt` exists and canonical progress ledger is absent, import one-way into `.omx/state/{scope}/ralph-progress.json`.
- Keep legacy files unchanged for one release cycle.

## Background Execution Rules