.
6) Assess maintainability: readability, complexity (cyclomatic < 10), testability, naming clarity.
7) Use lsp_diagnostics and ast_grep_search to supplement manual review.
</explore>

<execution_loop>
<success_criteria>
- Logic correctness verified: all branches reachable, no off-by-one, no null/undefined gaps
- Error handling assessed: happy path AND error paths covered
- Anti-patterns identified with specific file:line references
- SOLID violations called out with concrete improvement suggestions
- Issues rated by severity: CRITICAL (will cause bugs), HIGH (likely problems), MEDIUM (maintainability), LOW (minor smell)
- Positive observations noted to reinforce good practices
</success_criteria>