t role semantics, tool usage intent, guardrails, and checklist expectations functionally equivalent.
- Important current-state clarification: although the prompt text is now Markdown-first, each file in `prompts/*.md` is still the canonical XML-tagged subagent role surface consumed by OMX install/generation flows.

## Behavior Notes

- No intentionally introduced functional behavior changes were made in this migration commit.
- Behavior-relevant content (constraints, verification expectations, output templates) was preserved while syntax/formatting was normalized.
- Any post-migration behavior differences are expected to come from readability and parser-compatibility improvements, not policy changes.

## Per-File Matrix