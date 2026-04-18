eeds through planning steps (Planner/Architect/Critic) but outputs the final plan without executing.

1. **Planner** creates initial plan and a compact **RALPLAN-DR summary** before any Architect review. The summary **MUST** include:
   - **Principles** (3-5)
   - **Decision Drivers** (top 3)
   - **Viable Options** (>=2) with bounded pros/cons for each option
   - If only one viable option remains, an explicit **invalidation rationale** for the alternatives that were rejected
   - In **deliberate mode**: a **pre-mortem** (3 failure scenarios) and an **expanded test plan** covering **unit / integration / e2e / observability**