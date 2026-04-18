ower than the general GPT-5.4 behavioral contract described below.

Contributor rules for that seam:

- Key mini-specific instruction adaptation off the **final resolved model string**, not off role name, lane, or default tier membership.
- Use **exact string equality** for `gpt-5.4-mini`; do not widen behavior to `gpt-5.4`, `gpt-5.4-mini-tuned`, or other variants.
- Keep one shared **inner role-instruction composition helper** as the source of truth for model-gated prompt adaptation.
- Keep `src/team/worker-bootstrap.ts` limited to **outer AGENTS/runtime wrapping**. It should wrap already-composed instructions, not own model-specific adaptation logic.
- Keep `src/team/role-router.ts` as a raw role-prompt loader unless a minimal plumbing change is unavoidable.