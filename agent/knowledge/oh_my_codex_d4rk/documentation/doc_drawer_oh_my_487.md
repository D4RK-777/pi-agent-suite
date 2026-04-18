ning — they are carried into the actual worker startup instruction surface and live worker metadata.

This release:
- persists routed worker roles into live team config and worker identity
- composes per-worker startup `AGENTS.md` files from the resolved role prompt
- keeps role-based default reasoning allocation active unless an explicit launch override is present
- verifies the live worker launch path with runtime, tmux-session, and worker-bootstrap coverage

PR: [#643](https://github.com/Yeachan-Heo/oh-my-codex/pull/643)

### Scale-up task bootstrap now preserves canonical task identity