vel `developer_instructions` text in `src/config/generator.ts`

## Scope and current source of truth

Issue [#615](https://github.com/Yeachan-Heo/oh-my-codex/issues/615) uses examples like `src/prompts/role-planner.ts`, but the current prompt sources in this repository live in **`prompts/*.md`**, then get installed to `~/.codex/prompts/`.

The GPT-5.4 contract is currently distributed across:

- orchestration surfaces: `AGENTS.md`, `templates/AGENTS.md`
- canonical XML-tagged subagent role prompt surfaces: `prompts/*.md`
- generated top-level Codex config guidance: `src/config/generator.ts`
- regression tests: `src/hooks/__tests__/prompt-guidance-*.test.ts`