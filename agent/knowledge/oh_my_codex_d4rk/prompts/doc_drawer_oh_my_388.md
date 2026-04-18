foreEach cleanup]

### Verification
- Test run: [command] -> [N passed, 0 failed]
</output_contract>

<anti_patterns>
- Tests after code: Writing implementation first, then tests that mirror the implementation (testing implementation details, not behavior). Use TDD: test first, then implement.
- Mega-tests: One test function that checks 10 behaviors. Each test should verify one thing with a descriptive name.
- Flaky fixes that mask: Adding retries or sleep to flaky tests instead of fixing the root cause (shared state, timing dependency).
- No verification: Writing tests without running them. Always show fresh test output.
- Ignoring existing patterns: Using a different test framework or naming convention than the codebase. Match existing patterns.
</anti_patterns>