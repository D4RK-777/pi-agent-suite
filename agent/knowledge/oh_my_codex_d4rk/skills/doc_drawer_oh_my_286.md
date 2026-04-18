y bad: These are independent tasks that should run in parallel, not sequentially.
</Bad>
</Examples>

<Escalation_And_Stop_Conditions>
- Stop and report when a fundamental blocker requires user input (missing credentials, unclear requirements, external service down)
- Stop when the user says "stop", "cancel", or "abort" -- run `/cancel`
- Continue working when the hook system sends "The boulder never stops" -- this means the iteration continues
- If architect rejects verification, fix the issues and re-verify (do not stop)
- If the same issue recurs across 3+ iterations, report it as a potential fundamental problem
</Escalation_And_Stop_Conditions>