behavior.** Posture/tier updates belong in routing docs/tests unless they also change prompt prose.
6. **Update regression coverage when the contract changes.** Start with `src/hooks/__tests__/prompt-guidance-contract.test.ts`, `prompt-guidance-wave-two.test.ts`, `prompt-guidance-scenarios.test.ts`, and `prompt-guidance-catalog.test.ts`; add native/runtime/scaling/bootstrap coverage when the mini-only seam changes.

## Validation workflow for contributors

For prompt-guidance edits, run at least:

```bash
npm run build   # TypeScript build
node --test \
  dist/hooks/__tests__/prompt-guidance-contract.test.js \
  dist/hooks/__tests__/prompt-guidance-wave-two.test.js \
  dist/hooks/__tests__/prompt-guidance-scenarios.test.js \
  dist/hooks/__tests__/prompt-guidance-catalog.test.js
```