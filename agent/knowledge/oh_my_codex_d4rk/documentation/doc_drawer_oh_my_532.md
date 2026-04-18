a, decision policy, and resume failure conditions: `docs/contracts/autoresearch-command-contract.md`
- runtime implements active-run lock, per-run manifest files, allowlisted runtime excludes, candidate parsing, evaluator-backed decisions, reset-to-last-kept behavior, and resume validation: `src/autoresearch/runtime.ts`
- worktree planning test locks run-tagged autoresearch branch/path naming: `src/team/__tests__/worktree.test.ts`

## Parity checklist

### 1. Thin-supervisor iteration model
**Pass.**
- `buildAutoresearchInstructions()` tells the launched Codex session to perform exactly one experiment cycle and write the candidate artifact before exit.
- `runAutoresearchLoop()` relaunches Codex after `processAutoresearchCandidate()` unless the run aborts/errors.