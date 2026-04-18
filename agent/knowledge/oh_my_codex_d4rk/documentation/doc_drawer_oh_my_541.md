ontract()`.
  - no draft artifact is written under `.omx/specs/`.
- `skills/deep-interview/SKILL.md`
  - the generic execution bridge exists, but the autoresearch specialization section required by the PRD is absent on this branch.

### Test/doc alignment findings
- `src/cli/__tests__/autoresearch-guided.test.ts`
  - covers mission/scaffold creation and flag parsing for the older init/guided flow only.
- `src/cli/__tests__/autoresearch.test.ts`
  - still asserts the older `omx autoresearch init [--topic ...]` help surface and non-interactive `mission-dir is required` failure.
- worker-2 has an in-progress test addition that correctly starts locking the expected deep-interview specialization text in `src/hooks/__tests__/deep-interview-contract.test.ts`.

## PRD checklist assessment