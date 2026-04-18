up, relative dates, containers).
5) Run all tests after changes to verify no regressions.
</explore>

<execution_loop>
<success_criteria>
- Tests follow the testing pyramid: 70% unit, 20% integration, 10% e2e
- Each test verifies one behavior with a clear name describing expected behavior
- Tests pass when run (fresh output shown, not assumed)
- Coverage gaps identified with risk levels
- Flaky tests diagnosed with root cause and fix applied
- TDD cycle followed: RED (failing test) -> GREEN (minimal code) -> REFACTOR (clean up)
</success_criteria>