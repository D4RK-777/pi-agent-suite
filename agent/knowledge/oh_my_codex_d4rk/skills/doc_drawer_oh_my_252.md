agents across the staged pipeline for faster execution on large tasks.

### Review Mode (`--review`)

0. Treat review as a reviewer-only pass. The context that wrote the plan, cleanup proposal, or diff MUST NOT be the context that approves it.
1. Read plan file from `.omx/plans/`
2. Evaluate via Critic using `ask_codex` with `agent_role: "critic"`
3. For cleanup/refactor/anti-slop work, verify that the artifact includes a cleanup plan, regression tests or an explicit test gap, smell-by-smell passes, and quality gates.
4. Return verdict: APPROVED, REVISE (with specific feedback), or REJECT (replanning required)
5. If the current context authored the artifact, hand the review to `/review`, `critic`, `quality-reviewer`, `security-reviewer`, or `verifier` as appropriate.