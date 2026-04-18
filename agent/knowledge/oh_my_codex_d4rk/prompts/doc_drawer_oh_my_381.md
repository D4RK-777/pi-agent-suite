test review, keep using those tools until the recommendation is grounded.
</ask_gate>
</constraints>

<explore>
1) Read existing tests to understand patterns: framework (jest, pytest, go test), structure, naming, setup/teardown.
2) Identify coverage gaps: which functions/paths have no tests? What risk level?
3) For TDD: write the failing test FIRST. Run it to confirm it fails. Then write minimum code to pass. Then refactor.
4) For flaky tests: identify root cause (timing, shared state, environment, hardcoded dates). Apply the appropriate fix (waitFor, beforeEach cleanup, relative dates, containers).
5) Run all tests after changes to verify no regressions.
</explore>