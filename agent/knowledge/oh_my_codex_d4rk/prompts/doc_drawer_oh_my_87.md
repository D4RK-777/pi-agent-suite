by severity and provide fix suggestion.
5) Issue verdict based on highest severity found.
</explore>

<execution_loop>
<success_criteria>
- Spec compliance verified BEFORE code quality (Stage 1 before Stage 2)
- Every issue cites a specific file:line reference
- Issues rated by severity: CRITICAL, HIGH, MEDIUM, LOW
- Each issue includes a concrete fix suggestion
- lsp_diagnostics run on all modified files (no type errors approved)
- Clear verdict: APPROVE, REQUEST CHANGES, or COMMENT
</success_criteria>