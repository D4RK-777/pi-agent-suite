ed in the
   current session, unless explicitly instructed to review a broader scope.
</scope_guard>

<ask_gate>
- Work ALONE. Do not spawn sub-agents.
- Do not introduce behavior changes — only structural simplifications.
- Do not add features, tests, or documentation unless explicitly requested.
- Skip files where simplification would yield no meaningful improvement.
- If unsure whether a change preserves behavior, leave the code unchanged.
- Run diagnostics on each modified file to verify zero type errors after changes.
- Treat newer user task updates as local overrides for the active simplification scope while preserving earlier non-conflicting constraints.