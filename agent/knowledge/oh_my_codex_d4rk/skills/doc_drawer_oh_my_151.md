gue; stay on the same thread until one layer deeper, one assumption clearer, or one boundary tighter
- Before crystallizing, complete at least one explicit pressure pass that revisits an earlier answer with a deeper, assumption-focused, or tradeoff-focused follow-up
- Gather codebase facts via `explore` before asking user about internals
- When session guidance enables `USE_OMX_EXPLORE_CMD`, prefer `omx explore` for simple read-only brownfield fact gathering; keep prompts narrow and concrete, and keep ambiguous or non-shell-only investigation on the richer normal path and fall back normally if `omx explore` is unavailable.
- Always run a preflight context intake before the first interview question