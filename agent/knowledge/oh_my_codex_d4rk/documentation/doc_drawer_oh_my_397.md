KILL.md`, `skills/research/SKILL.md`, `skills/ultrapilot/SKILL.md`: config examples updated to TOML.

## Follow-up Classification Notes

- `prompts/*.md` should be treated as the canonical source set for XML-tagged subagent role prompts, even when install/runtime layers wrap them in TOML or other launcher-specific envelopes.
- `prompts/sisyphus-lite.md` is intentionally classified as a specialized worker behavior prompt. It is not part of the primary public role catalog alongside prompts such as `executor`, `planner`, or `architect`.
- Team worker/runtime overlays may borrow Sisyphus-lite behavior patterns, but that does not promote it to a first-class routed role.