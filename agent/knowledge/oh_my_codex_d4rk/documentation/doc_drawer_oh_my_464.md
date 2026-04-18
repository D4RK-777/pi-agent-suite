achan-Heo/oh-my-codex/pull/593)
Fixes: [#591](https://github.com/Yeachan-Heo/oh-my-codex/issues/591)

### Legacy model alias leakage

15 prompt files and the runtime native-config generator still referenced `gpt-5.3-codex` and `o3` model aliases that were removed from the config layer in v0.8.2. With posture routing active, these stale references could confuse tier/model-class guidance.

Fix: scrubbed all legacy alias references from prompts and `definitions.ts` metadata.

Part of PR: [#592](https://github.com/Yeachan-Heo/oh-my-codex/pull/592) ([@HaD0Yun](https://github.com/HaD0Yun))

## Other changes