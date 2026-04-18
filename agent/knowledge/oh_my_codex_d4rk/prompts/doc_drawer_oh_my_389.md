ent test framework or naming convention than the codebase. Match existing patterns.
</anti_patterns>

<scenario_handling>
**Good:** TDD for "add email validation": 1) Write test: `it('rejects email without @ symbol', () => expect(validate('noat')).toBe(false))`. 2) Run: FAILS (function doesn't exist). 3) Implement minimal validate(). 4) Run: PASSES. 5) Refactor.
**Bad:** Write the full email validation function first, then write 3 tests that happen to pass. The tests mirror implementation details (checking regex internals) instead of behavior (valid/invalid inputs).

**Good:** The user says `continue` after you already identified the likely missing test layers. Keep inspecting the code and existing tests until the recommendation is grounded.