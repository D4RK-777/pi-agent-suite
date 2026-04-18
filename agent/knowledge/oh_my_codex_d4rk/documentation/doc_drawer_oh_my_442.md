anonically, and cleans stale legacy skill dirs on `--force` (`#575`, `#580`, `#584`, closes `#574`).
- `omx setup` now skips the deprecated **`[tui]`** config section for Codex CLI `>= 0.107.0` (`#572`, fixes `#564`).
- Fixed two additional patch-level bugs: unresolved OpenClaw placeholders (`#581`, closes `#578`) and keyword detection ordering/`/prompts` guarding (`#582`).

---

## What changed

### 1) Team mode: Gemini CLI worker support

OMX team mode now supports **Gemini** as a worker CLI provider in addition to Codex and Claude.