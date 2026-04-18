can describe what they want and receive working code without managing each step.
</Why_This_Exists>

<Execution_Policy>
- Each phase must complete before the next begins
- Parallel execution is used within phases where possible (Phase 2 and Phase 4)
- QA cycles repeat up to 5 times; if the same error persists 3 times, stop and report the fundamental issue
- Validation requires approval from all reviewers; rejected items get fixed and re-validated
- Cancel with `/cancel` at any time; progress is preserved for resume
- If a deep-interview spec exists, use it as high-clarity phase input instead of re-expanding from scratch
- If input is too vague for reliable expansion, offer/trigger `$deep-interview` first