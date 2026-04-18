am ralph ...` launch hints
- linked-Ralph-specific tests and compatibility paths inside team runtime

### Updated
- team help/usage text now documents only `omx team [N:agent-type] "<task>"`
- planning, ralplan, team, and deep-interview guidance now describe a **team verification path** rather than a built-in `team -> ralph` lifecycle
- follow-up planner and pipeline launch hints now generate plain `omx team ...`
- shutdown/resume/state flows now operate on standalone team semantics only

### Behavior change
- `omx team ralph ...` is now rejected with an explicit deprecation error:
  - use `omx team ...` for coordinated team execution
  - use `omx ralph ...` separately if a later persistent follow-up loop is still needed