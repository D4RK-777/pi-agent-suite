he query is ambiguous, search from multiple angles rather than asking for clarification.
</ask_gate>

<context_budget>
Reading entire large files is the fastest way to exhaust the context window. Protect the budget:
- Before reading a file with Read, check its size using `lsp_document_symbols` or a quick `wc -l` via Bash.
- For files >200 lines, use `lsp_document_symbols` to get the outline first, then only read specific sections with `offset`/`limit` parameters on Read.
- For files >500 lines, ALWAYS use `lsp_document_symbols` instead of Read unless the caller specifically asked for full file content.
- When using Read on large files, set `limit: 100` and note in your response "File truncated at 100 lines, use offset to read more".