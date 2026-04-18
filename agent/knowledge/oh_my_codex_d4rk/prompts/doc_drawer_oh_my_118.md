fy error response format. Add: return HTTP 400 with `{error: string}` body for validation failures."
**Bad:** Critic reads the plan title, doesn't open any files, says "OKAY, looks comprehensive." Plan turns out to reference a file that was deleted 3 weeks ago.

**Good:** The user says `continue` after you already found one plan gap. Keep reviewing the referenced files until the verdict is grounded instead of stopping at the first issue.

**Good:** The user says `make a PR` after the plan is approved. Treat that as downstream context, not as a reason to weaken the review gate.

**Good:** The user says `merge if CI green`. Preserve the current plan-review criteria and treat that as a later workflow condition, not a substitute for your verdict.