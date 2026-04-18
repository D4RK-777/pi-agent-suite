ic rejects or iterates, execute this closed loop:
   a. Collect all feedback from Architect + Critic
   b. Pass feedback to Planner to produce a revised plan
   c. **Return to Step 3** — Architect reviews the revised plan
   d. **Return to Step 4** — Critic evaluates the revised plan
   e. Repeat until Critic approves OR max 5 iterations reached
   f. If max iterations reached without approval, present the best version to user via `AskUserQuestion` with note that expert consensus was not reached