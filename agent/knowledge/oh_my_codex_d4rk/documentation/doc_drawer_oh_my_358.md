hould treat user updates as **scoped overrides**, not full prompt resets.

Representative locations:

| Surface | Evidence |
|---|---|
| `AGENTS.md` | `AGENTS.md:31`, `AGENTS.md:300` |
| `templates/AGENTS.md` | `templates/AGENTS.md:31`, `templates/AGENTS.md:300` |
| `src/config/generator.ts` | `src/config/generator.ts:77` |
| `prompts/executor.md` | `prompts/executor.md:49-50`, `prompts/executor.md:60`, `prompts/executor.md:141-147` |
| `prompts/planner.md` | `prompts/planner.md:37`, `prompts/planner.md:118-126` |
| `prompts/verifier.md` | `prompts/verifier.md:38`, `prompts/verifier.md:91-99` |