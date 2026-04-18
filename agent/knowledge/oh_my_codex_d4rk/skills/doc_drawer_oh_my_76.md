terExpansion = false
pauseAfterPlanning = false
skipQa = false
skipValidation = false
```

## Resume

If autopilot was cancelled or failed, run `/autopilot` again to resume from where it stopped.

## Recommended Clarity Pipeline

For ambiguous requests, prefer:

```
deep-interview -> ralplan -> autopilot
```

- `deep-interview`: ambiguity-gated Socratic requirements
- `ralplan`: consensus planning (planner/architect/critic)
- `autopilot`: execution + QA + validation

## Best Practices for Input

1. Be specific about the domain -- "bookstore" not "store"
2. Mention key features -- "with CRUD", "with authentication"
3. Specify constraints -- "using TypeScript", "with PostgreSQL"
4. Let it run -- avoid interrupting unless truly needed

## Pipeline Orchestrator (v0.8+)