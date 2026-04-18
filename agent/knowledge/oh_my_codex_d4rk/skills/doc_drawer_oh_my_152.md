explore` is unavailable.
- Always run a preflight context intake before the first interview question
- Reduce user effort: ask only the highest-leverage unresolved question, and never ask the user for codebase facts that can be discovered directly
- For brownfield work, prefer evidence-backed confirmation questions such as "I found X in Y. Should this change follow that pattern?"
- In Codex CLI, prefer `request_user_input` when available; if unavailable, fall back to concise plain-text one-question turns
- Re-score ambiguity after each answer and show progress transparently
- Do not hand off to execution while ambiguity remains above threshold unless user explicitly opts to proceed with warning