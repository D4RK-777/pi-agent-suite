keep checking that shell-only/read-only boundaries stay intact while sparkshell routing is enabled.
- `omx sparkshell --tmux-pane` is operator-critical for team debugging, so pane summarization behavior should be treated as a release-facing feature, not a hidden internal detail.
- `npm pack --dry-run` remaining green is important because packaged installs intentionally exclude staged native binaries; the release workflow must supply those binaries through GitHub Release assets instead.
- Cross-platform Windows-specific fixes landed in the release window, but this Linux smoke pass cannot validate Windows runtime behavior directly; that still depends on CI/release-matrix confirmation.

## Final local verdict