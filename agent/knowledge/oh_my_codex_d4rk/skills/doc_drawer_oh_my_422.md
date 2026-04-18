d.

## Cancellation

User can cancel with `/cancel` which clears the state file.

## Important Rules

1. **PARALLEL when possible** - Run diagnosis while preparing potential fixes
2. **TRACK failures** - Record each failure to detect patterns
3. **EARLY EXIT on pattern** - 3x same failure = stop and surface
4. **CLEAR OUTPUT** - User should always know current cycle and status
5. **CLEAN UP** - Clear state file on completion or cancellation

## STATE CLEANUP ON COMPLETION

When goal is met OR max cycles reached OR exiting early, run `$cancel` or call:

`state_clear({mode: "ultraqa"})`

Use MCP state cleanup rather than deleting files directly.

---

Begin ULTRAQA cycling now. Parse the goal and start cycle 1.