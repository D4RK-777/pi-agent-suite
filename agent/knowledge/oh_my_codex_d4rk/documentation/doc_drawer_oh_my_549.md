left unconfirmed.
- `ConfirmationPolicy` defines the retry/verification window used by the adapter.

## Rules
- The semantic contract must not depend on tmux-native nouns.
- Tmux is the first adapter, not the model.
- Adapter results may include tmux identifiers for debugging, but those identifiers are not semantic truth.
- Retry, confirmation, and delivery decisions belong to the runtime contract, not the adapter implementation.

## TmuxAdapter implementation

`TmuxAdapter` is fully implemented in `crates/omx-mux/src/tmux.rs`. All six canonical operations are supported. All `MuxOperation`, `MuxOutcome`, `MuxTarget`, and related types derive `Serialize`/`Deserialize`.

Exact tmux CLI invocations per operation: