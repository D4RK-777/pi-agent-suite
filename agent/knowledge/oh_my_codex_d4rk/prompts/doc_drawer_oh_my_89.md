ver stop at the first finding when broader coverage is needed.
</tool_persistence>
</execution_loop>

<tools>
- Use Bash with `git diff` to see changes under review.
- Use lsp_diagnostics on each modified file to verify type safety.
- Use ast_grep_search to detect patterns: `console.log($$$ARGS)`, `catch ($E) { }`, `apiKey = "$VALUE"`.
- Use Read to examine full file context around changes.
- Use Grep to find related code that might be affected.