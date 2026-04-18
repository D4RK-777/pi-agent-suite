patterns above, but they are not a separate routing or reasoning system.

Representative locations:

- `prompts/executor.md:137-147`
- `prompts/planner.md:116-126`
- `prompts/verifier.md:89-99`
- `src/hooks/__tests__/prompt-guidance-scenarios.test.ts:13-33`
- `src/hooks/__tests__/prompt-guidance-wave-two.test.ts:45-61`

## Relationship to the guidance schema

`docs/guidance-schema.md` defines the **section layout contract** for AGENTS and worker surfaces.
This document defines the **behavioral wording contract** that should appear within those sections after the GPT-5.4 rollout.

Use both documents together:

- `docs/guidance-schema.md` for structure
- `docs/prompt-guidance-contract.md` for behavior

## Relationship to posture-aware routing