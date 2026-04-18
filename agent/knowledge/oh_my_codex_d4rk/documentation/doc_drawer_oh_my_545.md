nt branch.**
Those tests are not present yet.

## Documentation follow-ups once implementation lands

1. Update `README.md` with the new novice entry surfaces:
   - `omx autoresearch` as a deep-interview-style refinement flow
   - top-level seeded novice flags
   - explicit confirm-before-launch behavior
2. Update `docs/contracts/autoresearch-command-contract.md` to add:
   - canonical draft artifact path
   - launch-readiness placeholder rejection rules
   - confirm/refine bridge semantics
3. Extend `skills/deep-interview/SKILL.md` with the PRD-required `Autoresearch specialization` section and required artifact headings.
4. Keep help text explicit about the split between novice refinement mode and expert `init --flags` / `<mission-dir>` / `--resume` flows.

## Reviewer conclusion