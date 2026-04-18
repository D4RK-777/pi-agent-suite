odex/pull/642)

## Bug fixes and operational polish

### Deep-interview auto-approval lock hardening

Notify-hook and keyword-detection logic were tightened so deep-interview auto-approval injection stays lock-protected and better covered by tests.

PR: [#637](https://github.com/Yeachan-Heo/oh-my-codex/pull/637)

### Packaging and routing contract fixes

This release also includes smaller contract corrections:
- normalizes the published npm bin path and updates package-bin regression coverage ([#638](https://github.com/Yeachan-Heo/oh-my-codex/pull/638))
- explicitly reserves the worker role for team mode in prompt-guidance routing, with regression coverage via PR [#641](https://github.com/Yeachan-Heo/oh-my-codex/pull/641)

## Compare stats