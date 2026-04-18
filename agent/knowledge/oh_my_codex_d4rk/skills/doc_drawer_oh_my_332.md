le `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.

**Bad:** The user says `continue`, and the workflow restarts discovery or stops before the missing verification/evidence is gathered.

## Use with Other Skills

**With Team:**
```
/team "run security review on authentication module"
```
Uses: explore → security-reviewer → executor → security-reviewer (re-verify)

**With Swarm:**
```
/swarm 4:security-reviewer "audit all API endpoints"
```
Parallel security review across multiple endpoints.

**With Ralph:**
```
/ralph security-review then fix all issues
```
Review, fix, re-review until all issues resolved.

## Best Practices