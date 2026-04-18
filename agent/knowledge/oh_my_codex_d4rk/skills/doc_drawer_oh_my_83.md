## Agent Delegation

```
delegate(
  role="build-fixer",
  tier="STANDARD",
  prompt="BUILD FIX TASK

Fix all build and TypeScript errors with minimal changes.

Requirements:
- Run tsc/build to collect errors
- Fix errors one at a time
- Verify each fix doesn't introduce new errors
- NO refactoring, NO architectural changes
- Stop when build passes

Output: Build error resolution report with:
- List of errors fixed
- Lines changed per fix
- Final build status"
)
```

## Stop Conditions

The build-fixer agent stops when:
- Type check command exits with code 0
- Build command completes successfully
- No new errors introduced

## Output Format

```
BUILD FIX REPORT
================

Errors Fixed: 12
Files Modified: 8
Lines Changed: 47