ss, all others still pass
```

## Output Format

When guiding TDD:

```
## TDD Cycle: [Feature Name]

### RED Phase
Test: [test code]
Expected failure: [what error you expect]
Actual: [run result showing failure]

### GREEN Phase
Implementation: [minimal code]
Result: [run result showing pass]

### REFACTOR Phase
Changes: [what was cleaned up]
Result: [tests still pass]
```

## External Model Consultation (Preferred)

The tdd-guide agent SHOULD consult Codex for test strategy validation.

### Protocol
1. **Form your OWN test strategy FIRST** - Design tests independently
2. **Consult for validation** - Cross-check test coverage strategy
3. **Critically evaluate** - Never blindly adopt external suggestions
4. **Graceful fallback** - Never block if tools unavailable