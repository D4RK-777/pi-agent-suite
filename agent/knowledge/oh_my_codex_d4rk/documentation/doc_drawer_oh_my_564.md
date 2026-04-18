and there are no pending replay events. All blocking reasons are collected into `readiness.reasons`.

## Dispatch classification
- `WorkerCli` selects the submit policy (`Claude` => 1 press, `Codex`/other => 2 presses).
- `DispatchOutcomeReason` and `QueueTransition` classify send success, retry, pending, and failure outcomes.
- Deferred leader-missing cases stay pending so the runtime can retry when a pane becomes available.
- Unconfirmed sends can stay pending while retries remain; otherwise they fail with an unconfirmed reason.