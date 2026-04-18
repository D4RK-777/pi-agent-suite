mits**
- unreleased diff vs tag: **149 files changed, +12,325 / -254**

## Remaining release actions

- tag `v0.9.0` and verify GitHub Actions release jobs complete:
  - native asset publishing
  - native asset manifest verification
  - packed install smoke verification
  - npm publish
- publish the GitHub release using `docs/release-notes-0.9.0.md`

## Risk notes

- Primary regression surface is the new native distribution contract: hydration, fallback ordering, and cross-platform asset resolution.
- `omx explore` is intentionally constrained; release validation should keep checking that shell-only/read-only boundaries stay intact while sparkshell routing is enabled.