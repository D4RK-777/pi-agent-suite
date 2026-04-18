atalog is the installable specialized-agent set used by `/prompts:name` and native agent generation.

- Files like `prompts/executor.md`, `prompts/planner.md`, and `prompts/architect.md` are canonical XML-tagged role prompt surfaces.
- `prompts/sisyphus-lite.md` should be treated as a specialized worker-behavior prompt, not as a first-class main catalog role.
- Worker/runtime overlays may compose that behavior under worker protocol constraints without promoting it to the primary public role catalog.

## Contributor checklist for prompt changes

Before opening a PR that changes prompt text, confirm all of the following: