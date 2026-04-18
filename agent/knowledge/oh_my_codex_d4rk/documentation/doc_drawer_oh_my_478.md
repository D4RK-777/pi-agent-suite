ntract fix

This release also includes a last-minute packaging fix for global installation behavior.

It:
- corrects the published npm bin path contract in `package.json`
- adds `src/cli/__tests__/package-bin-contract.test.ts` so the global-install `omx` entrypoint stays covered in CI

PR: [#633](https://github.com/Yeachan-Heo/oh-my-codex/pull/633)

## Bug fixes and operational polish

### Windows / tmux capability handling

OMX no longer blocks native Windows purely because the platform is `win32`.

Instead, it now:
- checks actual tmux capability
- supports `psmux`
- uses `where` where appropriate on Windows
- documents platform-specific setup paths more clearly in the README

PR: [#616](https://github.com/Yeachan-Heo/oh-my-codex/pull/616)

### Fast-path agent posture tuning