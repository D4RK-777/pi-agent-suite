intended public export surface for the `team-ops` gateway after the event-aware wait changes landed.

Fix: remove the accidental `teamEventLogPath` re-export so the strict `team-ops` module contract test remains stable.

PR: [#610](https://github.com/Yeachan-Heo/oh-my-codex/pull/610)

## Compare stats

- Commit window: **4 non-merge commits** (`2026-03-07`)
- Diff snapshot (`main...dev`): **69 files changed, +1,745 / -71**

## Full commit log (v0.8.5..v0.8.6)

```
9d3e2a2 fix(team): harden leader follow-up and event-aware waiting (#609)
c13290a fix(team): keep team-ops gateway contract stable (#610)
9d4b1ea feat: apply GPT-5.4 prompt-guidance patterns
76e3918 feat: expand GPT-5.4 prompt guidance across prompts and skills
```