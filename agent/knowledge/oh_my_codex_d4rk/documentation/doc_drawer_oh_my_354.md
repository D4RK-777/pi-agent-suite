4 core GPT-5.4 patterns OMX currently enforces

### 1. Compact, information-dense output by default

Contributors should preserve the default posture of concise outputs that still include the evidence needed to act safely.

Representative locations:

| Surface | Evidence |
|---|---|
| `AGENTS.md` | `AGENTS.md:29` |
| `templates/AGENTS.md` | `templates/AGENTS.md:29` |
| `prompts/executor.md` | `prompts/executor.md:47`, `prompts/executor.md:121` |
| `prompts/planner.md` | `prompts/planner.md:35`, `prompts/planner.md:79` |
| `prompts/verifier.md` | `prompts/verifier.md:29` |
| contract tests | `src/hooks/__tests__/prompt-guidance-contract.test.ts:15-19`, `src/hooks/__tests__/prompt-guidance-wave-two.test.ts:27-30`, `src/hooks/__tests__/prompt-guidance-catalog.test.ts:35-39` |