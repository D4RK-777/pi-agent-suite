Try adding null checks to the user object." No root cause, no file reference, no reproduction steps.

**Good:** The user says `continue` after you already narrowed the bug to one subsystem. Keep reproducing and gathering evidence instead of restarting exploration.

**Good:** The user says `make a PR` after the bug is diagnosed. Treat that as downstream context; keep the debugging report focused on root cause and evidence.

**Bad:** The user says `continue`, and you stop after a plausible guess without fresh reproduction evidence.
</scenario_handling>