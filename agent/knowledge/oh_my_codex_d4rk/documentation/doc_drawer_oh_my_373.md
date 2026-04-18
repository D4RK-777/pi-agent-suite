# Prompt Migration Changelog

## Scope

- Migration window: `e21cb5e` -> `ff7ee14`
- Surface: `prompts/*.md` (30 files)
- Goal: document the prior XML-to-Markdown migration while reaffirming that prompt files remain the canonical XML-tagged subagent role surfaces for OMX.

## Global Changes (Applied to All Prompt Files)

- Preserved frontmatter metadata (`description`, `argument-hint`).
- Replaced wrapper tags such as `<Agent_Prompt>`, `<Role>`, `<Constraints>`, `<Output_Format>`, `<Final_Checklist>` with Markdown section headings.
- Flattened nested XML-like sections into readable Markdown bullets/numbered steps.
- Kept role semantics, tool usage intent, guardrails, and checklist expectations functionally equivalent.