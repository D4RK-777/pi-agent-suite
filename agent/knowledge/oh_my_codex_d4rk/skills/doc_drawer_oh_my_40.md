Pass 3: Naming/error handling cleanup - [concise fix]
4. Pass 4: Test reinforcement - [concise fix]

Quality Gates:
- Regression tests: PASS/FAIL
- Lint: PASS/FAIL
- Typecheck: PASS/FAIL
- Tests: PASS/FAIL
- Static/security scan: PASS/FAIL or N/A

Changed Files:
- [path] - [simplification]

Remaining Risks:
- [none or short deferred item]
```

## Scenario Examples

**Good:** The user says `continue` after tests already lock behavior and the next smell pass is clear. Continue with the next bounded cleanup pass.

**Good:** The user narrows the scope to a specific file after planning. Keep the regression-tests-first workflow, but apply the new scope locally.

**Bad:** Start rewriting architecture before protecting behavior with tests.