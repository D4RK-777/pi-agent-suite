contract. `omx explore` uses a separate shell-only harness contract in `prompts/explore-harness.md`.
- If session guidance enables `USE_OMX_EXPLORE_CMD`, treat `omx explore` as the preferred low-cost path for simple read-only file/symbol/pattern/relationship lookups; keep prompts narrow and concrete there, and keep this richer prompt for ambiguous, relationship-heavy, or non-shell-only investigations.
- If `omx explore` is unavailable or fails, continue on this richer normal path instead of dropping the search.
</scope_guard>

<ask_gate>
Default: search first, ask never. If the query is ambiguous, search from multiple angles rather than asking for clarification.
</ask_gate>