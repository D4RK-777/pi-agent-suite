Fix: convert the resolved path to a `file://` URL via `url.pathToFileURL()` before dynamic import.

PR: [#589](https://github.com/Yeachan-Heo/oh-my-codex/pull/589) ([@sjals93](https://github.com/sjals93))
Fixes: [#557](https://github.com/Yeachan-Heo/oh-my-codex/issues/557)

### tmux capture-pane returns empty output

`capture-pane` was called with `-l <N>` (invalid flag usage) instead of `-S -<N>`, so recent terminal output was never captured. This broke HUD recent-output display and notification content extraction.

Fix: use `-S -<N>` (negative start line offset) which is the correct tmux API for capturing the last N lines.

PR: [#593](https://github.com/Yeachan-Heo/oh-my-codex/pull/593)
Fixes: [#591](https://github.com/Yeachan-Heo/oh-my-codex/issues/591)