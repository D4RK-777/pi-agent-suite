Y change
- Must stay green

### 4. REPEAT
- Next failing test
- Continue cycle

## Enforcement Rules

| If You See | Action |
|------------|--------|
| Code written before test | STOP. Delete code. Write test first. |
| Test passes on first run | Test is wrong. Fix it to fail first. |
| Multiple features in one cycle | STOP. One test, one feature. |
| Skipping refactor | Go back. Clean up before next feature. |

## Commands

Before each implementation:
```bash
# Run the project's test command - should have ONE new failure
```

After implementation:
```bash
# Run the project's test command - new test should pass, all others still pass
```

## Output Format

When guiding TDD:

```
## TDD Cycle: [Feature Name]