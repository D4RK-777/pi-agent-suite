d a **team verification path** (what team proves before shutdown, what Ralph verifies after handoff)
7. On Critic approval (with improvements applied): *(--interactive only)* If running with `--interactive`, use `AskUserQuestion` to present the plan with these options:
   - **Approve and execute** — proceed to implementation via ralph+ultrawork
   - **Approve and implement via team** — proceed to implementation via coordinated parallel team agents
   - **Request changes** — return to step 1 with user feedback
   - **Reject** — discard the plan entirely
   If NOT running with `--interactive`, output the final approved plan and stop. Do NOT auto-execute.
8. *(--interactive only)* User chooses via the structured `AskUserQuestion` UI (never ask for approval in plain text)