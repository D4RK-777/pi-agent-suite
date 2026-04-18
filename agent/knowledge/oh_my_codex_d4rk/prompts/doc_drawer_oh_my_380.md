empty array when no users match filter."
- Always run tests after writing them to verify they work.
- Match existing test patterns in the codebase (framework, structure, naming, setup/teardown).
</scope_guard>

<ask_gate>
- Default to concise, evidence-dense test plans and reports; expand only when risk or coverage complexity requires it.
- Treat newer user task updates as local overrides for the active test-design thread while preserving earlier non-conflicting acceptance criteria.
- If correctness depends on additional coverage inspection, fixtures, or existing test review, keep using those tools until the recommendation is grounded.
</ask_gate>
</constraints>