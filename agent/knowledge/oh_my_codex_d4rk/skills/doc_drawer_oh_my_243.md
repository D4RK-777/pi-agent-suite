ilure scenarios) and an **expanded test plan** covering **unit / integration / e2e / observability**
2. **User feedback** *(--interactive only)*: If running with `--interactive`, **MUST** use `AskUserQuestion` to present the draft plan **plus the RALPLAN-DR Principles / Decision Drivers / Options summary for early direction alignment** with these options:
   - **Proceed to review** — send to Architect and Critic for evaluation
   - **Request changes** — return to step 1 with user feedback incorporated
   - **Skip review** — go directly to final approval (step 7)
   If NOT running with `--interactive`, automatically proceed to review (step 3).