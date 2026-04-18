r runtime, but not the new novice deep-interview intake surface from this PRD.

## Evidence observed

### Code-path findings
- `src/cli/autoresearch.ts`
  - `parseAutoresearchArgs()` only recognizes no-arg guided mode, `init`, `--resume`, and `<mission-dir>`.
  - top-level `--topic/--evaluator/--keep-policy/--slug` seeded novice flags are not routed.
  - guided/init flows still call `spawnAutoresearchTmux()` immediately after mission creation.
- `src/cli/autoresearch-guided.ts`
  - `guidedAutoresearchSetup()` still prompts directly for `Evaluator command`.
  - no placeholder/readiness rejection exists beyond `parseSandboxContract()`.
  - no draft artifact is written under `.omx/specs/`.
- `skills/deep-interview/SKILL.md`