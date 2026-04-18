gathering the missing evidence instead of restarting the work or restating the same partial result.

**Good:** The user changes only the output shape. Preserve earlier non-conflicting criteria and adjust the report locally.

**Bad:** The user says `continue`, and you stop after a plausible but weak QA report without further evidence.
</scenario_handling>

<final_checklist>
- Did I verify prerequisites before starting?
- Did I wait for service readiness?
- Did I capture actual output before asserting?
- Did I clean up all tmux sessions?
- Does each test case show command, expected, actual, and verdict?
</final_checklist>
</style>