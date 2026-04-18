mit on exit
- `base_commit` must resolve in git and match the supervisor-provided `last_kept_commit`

Supervisor behavior:
- `candidate` → run evaluator, classify keep/discard/ambiguous/error, update manifest/ledger/results, reset if discarded
- `noop` → log noop iteration and continue by default
- `abort` → stop run without reset
- `interrupted` → if dirty, stop for operator intervention; if clean, log interrupted/noop style outcome

## Decision policy