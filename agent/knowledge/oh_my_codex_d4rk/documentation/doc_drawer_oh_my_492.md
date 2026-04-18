ll usage

### Important Spark Initiative notes

For `0.9.0`, the important distribution contract is:

- users can install OMX normally with `npm install -g oh-my-codex`
- the npm package intentionally does **not** bundle all native binaries directly
- tagged releases publish cross-platform native archives for:
  - `omx-explore-harness`
  - `omx-sparkshell`
- packaged installs hydrate the matching native binary from the GitHub Release assets through `native-release-manifest.json`
- CI now validates the Rust path more directly with:
  - explicit Rust toolchain setup in the full build lane
  - `cargo fmt --all --check`
  - `cargo clippy --workspace --all-targets -- -D warnings`

This keeps npm installs simple for users while still shipping verified cross-platform native helpers.