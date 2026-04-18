launch hints, and a concrete **team verification** path. Otherwise, output the final plan and stop.
7. *(--interactive only)* User chooses: Approve (ralph or team), Request changes, or Reject
8. *(--interactive only)* On approval: invoke `$ralph` for sequential execution or `$team` for parallel team execution with the explicit available-agent-types roster, reasoning-by-lane guidance, role/staffing allocation guidance, launch hints, and verification-path guidance from the approved plan -- never implement directly

> **Important:** Steps 3 and 4 MUST run sequentially. Do NOT issue both agent calls in the same parallel batch. Always await the Architect result before invoking Critic.

Follow the Plan skill's full documentation for consensus mode details.

## Pre-context Intake