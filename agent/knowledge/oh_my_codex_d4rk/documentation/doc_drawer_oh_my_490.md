# oh-my-codex v0.9.0

Drafted: 2026-03-12

Pre-release draft based on unreleased `dev` changes since `v0.8.15`.

55 non-merge commits from `v0.8.15..dev`.
Contributors: Yeachan-Heo, Bellman, 2233admin, Seunghwan Eom, hoky1227.

## Highlights

### Spark Initiative: `omx explore` and `omx sparkshell`

OMX now has a stronger native fast path for repository discovery and shell-native inspection.

This release:
- introduces `omx explore` as the default read-only exploration entrypoint
- adds the Rust-backed explore harness plus packaging and source-fallback flow
- introduces `omx sparkshell <command> [args...]` as an explicit operator-facing native sidecar
- allows qualifying read-only shell-native `omx explore` tasks to route through `omx sparkshell`