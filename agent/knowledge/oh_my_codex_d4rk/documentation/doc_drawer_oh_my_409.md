ild:full` validated as the one-shot release-oriented build path

## Important Spark Initiative notes

- Users can install OMX normally with `npm install -g oh-my-codex`.
- The npm tarball intentionally excludes staged cross-platform native binaries.
- Tagged releases publish verified native archives for `omx-explore-harness` and `omx-sparkshell`.
- Packaged installs hydrate the matching native binary through `native-release-manifest.json`.
- CI now hardens the Rust path with explicit toolchain setup, `cargo fmt --all --check`, and `cargo clippy --workspace --all-targets -- -D warnings`.

## Upgrade note

If you use project-scoped OMX installs, rerun:

```bash
omx setup --force --scope project
```

after upgrading so managed config/native-agent paths are refreshed.