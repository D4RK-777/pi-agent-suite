limited impact or difficult exploitation
**LOW** - Best practice violation or minor security concern

## Remediation Priority

1. **Rotate exposed secrets** - Immediate (within 1 hour)
2. **Fix CRITICAL** - Urgent (within 24 hours)
3. **Fix HIGH** - Important (within 1 week)
4. **Fix MEDIUM** - Planned (within 1 month)
5. **Fix LOW** - Backlog (when convenient)


## Scenario Examples

**Good:** The user says `continue` after the workflow already has a clear next step. Continue the current branch of work instead of restarting or re-asking the same question.

**Good:** The user changes only the output shape or downstream delivery step (for example `make a PR`). Preserve earlier non-conflicting workflow constraints and apply the update locally.