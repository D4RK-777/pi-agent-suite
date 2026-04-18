# oh-my-codex v0.9.0

<p align="center">
  <img src="https://raw.githubusercontent.com/Yeachan-Heo/oh-my-codex/v0.9.0/docs/shared/omx-character-spark-initiative.jpg" alt="OMX character sparked for the Spark Initiative" width="720">
</p>

`0.9.0` is the Spark Initiative release: OMX now has a stronger native fast path for repository discovery, shell-native inspection, and cross-platform native distribution.

## Highlights

### `omx explore`

- adds a dedicated read-only exploration entrypoint
- uses a Rust-backed explore harness
- keeps shell-native exploration constrained, allowlisted, and read-only
- supports packaged native resolution plus source/repo-local fallback paths

### `omx sparkshell`