ple:
`ralph -i refs/hn.png -i refs/hn-item.png --images-dir ./screenshots "match HackerNews layout"`

### PRD Workflow
1. Run deep-interview in quick mode before creating PRD artifacts:
   - Execute: `$deep-interview --quick <task>`
   - Complete a compact requirements pass (context, goals, scope, constraints, validation)
   - Persist interview output to `.omx/interviews/{slug}-{timestamp}.md`
2. Create canonical PRD/progress artifacts:
   - PRD: `.omx/plans/prd-{slug}.md`
   - Progress ledger: `.omx/state/{scope}/ralph-progress.json` (session scope when available, else root scope)
3. Parse the task (everything after `--prd` flag)
4. Break down into user stories: