son` | Manifest-backed tmux/session identity is authoritative when both config and manifest exist. |
| HUD readers | `.omx/state/session.json`, `.omx/state/sessions/<session>/team-state.json`, `.omx/state/team-state.json`, `.omx/state/ralph-state.json` | Session-scoped files are authoritative when a session is active; root files are compatibility fallback only. |

## Rust-authored runtime files

The `RuntimeEngine` (in `crates/omx-runtime-core/src/engine.rs`) writes the following files via `persist()` and `write_compatibility_view()`: