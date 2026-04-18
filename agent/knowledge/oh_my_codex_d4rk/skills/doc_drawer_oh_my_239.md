lly branching, destructive, or preference-dependent
</Execution_Policy>

<Steps>

### Mode Selection

| Mode | Trigger | Behavior |
|------|---------|----------|
| Interview | Default for broad requests | Interactive requirements gathering |
| Direct | `--direct`, or detailed request | Skip interview, generate plan directly |
| Consensus | `--consensus`, "ralplan" | Planner -> Architect -> Critic loop until agreement with RALPLAN-DR structured deliberation (short by default, `--deliberate` for high-risk); outputs plan by default |
| Consensus Interactive | `--consensus --interactive` | Same as Consensus but pauses for user feedback at draft and approval steps, then hands off to execution |
| Review | `--review`, "review this plan" | Critic evaluation of existing plan |