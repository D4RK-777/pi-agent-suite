ort

OMX team mode now supports **Gemini** as a worker CLI provider in addition to Codex and Claude.

Included in this update:
- Gemini worker launch support in runtime/session resolution
- mixed CLI maps with Codex / Claude / Gemini workers
- `--model` passthrough support for Gemini workers
- expanded runtime and tmux-session coverage for Gemini worker behavior

**Why this matters:**
- more flexibility for mixed-provider teams
- easier experimentation with provider-specific worker roles
- better parity across the team orchestration surface

### 2) Model fallback defaults are now centralized

Hardcoded default frontier-model fallback references were replaced with `DEFAULT_FRONTIER_MODEL`.