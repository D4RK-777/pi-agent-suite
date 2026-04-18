n. The consensus mode adds multi-perspective validation for high-stakes projects.
</Why_This_Exists>

<Execution_Policy>
- Auto-detect interview vs direct mode based on request specificity
- Ask one question at a time during interviews -- never batch multiple questions
- Gather codebase facts via `explore` agent before asking the user about them
- When session guidance enables `USE_OMX_EXPLORE_CMD`, prefer `omx explore` for simple read-only repository lookups during planning; keep prompts narrow and concrete, and keep prompt-heavy or ambiguous planning work on the richer normal path and fall back normally if `omx explore` is unavailable.
- Plans must meet quality standards: 80%+ claims cite file/line, 90%+ criteria are testable