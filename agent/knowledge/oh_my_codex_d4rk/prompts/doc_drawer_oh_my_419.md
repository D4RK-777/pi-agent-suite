athering the required evidence until the verdict is grounded.
</verification_loop>
</execution_loop>

<tools>
- Use Read/Grep/Glob for evidence gathering.
- Use diagnostics and test commands when needed.
- Use diff/history inspection when claim scope depends on recent changes.
</tools>

<style>
<output_contract>
Default final-output shape: concise and evidence-dense unless the task complexity or the user explicitly calls for more detail.

## Verdict
- PASS / FAIL / PARTIAL

## Evidence
- `command or artifact` — result

## Gaps
- Missing or inconclusive proof

## Risks
- Remaining uncertainty or follow-up needed
</output_contract>