ithub.com/Yeachan-Heo/oh-my-codex/pull/634)

### Team reasoning effort can be allocated per teammate

Team execution now carries reasoning-effort decisions deeper into runtime and worker-launch paths instead of treating worker configuration as one undifferentiated default.

This release:
- extends team model-contract logic for teammate-specific reasoning effort
- updates runtime, scaling, and tmux-session behavior to propagate those settings
- adds regression coverage for runtime, tmux session, and model-contract paths
- refreshes README and team skill guidance to reflect the new behavior

PR: [#642](https://github.com/Yeachan-Heo/oh-my-codex/pull/642)

## Bug fixes and operational polish

### Deep-interview auto-approval lock hardening