tructure
- `docs/prompt-guidance-contract.md` for behavior

## Relationship to posture-aware routing

Posture-aware routing is real, but it is not the same contract as the GPT-5.4 behavior rollout.
Keep these separate when editing docs and prompts:

| Topic | Primary sources |
|---|---|
| GPT-5.4 prompt behavior contract | `AGENTS.md`, `templates/AGENTS.md`, canonical XML-tagged role prompt surfaces in `prompts/*.md`, `src/config/generator.ts`, `src/hooks/__tests__/prompt-guidance-*.test.ts` |
| exact-model mini composition seam | `src/agents/native-config.ts`, `src/team/runtime.ts`, `src/team/scaling.ts`, `src/team/worker-bootstrap.ts`, targeted native/runtime/scaling/bootstrap tests |