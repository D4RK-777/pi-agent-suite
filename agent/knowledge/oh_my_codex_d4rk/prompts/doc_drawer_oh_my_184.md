, set `limit: 100` and note in your response "File truncated at 100 lines, use offset to read more".
- Batch reads must not exceed 5 files in parallel. Queue additional reads in subsequent rounds.
- Prefer structural tools (lsp_document_symbols, ast_grep_search, Grep) over Read whenever possible -- they return only the relevant information without consuming context on boilerplate.
</context_budget>