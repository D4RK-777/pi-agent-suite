d hardened
- guidance/docs/tests were aligned around this contract

### Worker follow-through polish

- worker mailbox guidance now asks for concrete progress updates without implying work should stop after replying
- inbox/mailbox trigger wording now tells workers to continue assigned or next feasible work after reporting status
- runtime/bootstrap wording and associated tests were aligned around this behavior

### Release pipeline upgrades

- cross-platform native publishing for:
  - `omx-explore-harness`
  - `omx-sparkshell`
- native release manifest generation with per-target metadata
- packed-install smoke verification in the release workflow
- `build:full` validated as the one-shot release-oriented build path

## Important Spark Initiative notes