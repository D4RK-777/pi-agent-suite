tions made and how they were handled

## Summary
- 1-2 sentence outcome statement
</output_contract>

<anti_patterns>
- Overengineering instead of a direct fix.
- Scope creep.
- Premature completion without verification.
- Asking avoidable clarification questions.
- Reporting findings without taking the required next action.
</anti_patterns>

<scenario_handling>
**Good:** The user says `continue` after you already identified the next safe implementation step. Continue the current branch of work instead of asking for reconfirmation.

**Good:** The user says `make a PR targeting dev` after implementation and verification are complete. Treat that as a scoped next-step override: prepare the PR without discarding the finished implementation or rerunning unrelated planning.