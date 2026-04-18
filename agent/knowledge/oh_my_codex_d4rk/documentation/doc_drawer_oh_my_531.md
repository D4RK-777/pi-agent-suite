earch-contract.test.js` → PASS
- `node --test dist/cli/__tests__/session-search-help.test.js` → PASS

### Code/doc alignment observed
- CLI help documents fresh launch + `--resume <run-id>`: `src/cli/autoresearch.ts`
- top-level help advertises thin-supervisor parity semantics: `src/cli/index.ts`, `src/compat/fixtures/help.stdout.txt`
- README now explains baseline seeding, repo-root per-run artifacts, candidate handoff, keep/discard/reset, relaunch loop, and resume behavior: `README.md`
- contract doc now defines run-tagged lanes, repo-root authority split, candidate artifact schema, decision policy, and resume failure conditions: `docs/contracts/autoresearch-command-contract.md`