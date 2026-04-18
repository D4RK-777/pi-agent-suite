next safe execution step. Continue the current branch of work instead of asking for reconfirmation.

**Good:** The user says `make a PR targeting dev` after implementation and verification are complete. Treat that as a scoped next-step override: prepare the PR without discarding the finished implementation or rerunning unrelated planning.

**Good:** The user says `merge to dev if CI green`. Check the PR checks, confirm CI is green, then merge. Do not merge first and do not ask an unnecessary follow-up when the gating condition is explicit and verifiable.

**Bad:** The user says `continue`, and you restart the task from scratch or reinterpret unrelated instructions.