ocation/rebalance decision explainable with a reason string suitable for logs, snapshots, and tests.

## Review notes
- The code already has good low-level claim primitives; the main gap is decision logic, not transport.
- The clearest review risk is letting new heuristics bypass `assignTask()`/claim safety. Any rebalance helper should return a decision, not perform ad-hoc mutation.
- Startup assignment and runtime rebalance should stay small, explicit policy seams so `src/cli/team.ts` and `src/team/runtime.ts` do not absorb another large block of inline heuristics.
- `allocation_reason` should remain explainable enough for tests, snapshots, and leader review even if the public task payload hides the internal field after planning.