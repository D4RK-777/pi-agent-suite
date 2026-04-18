g, diffs, tests, or diagnostics, keep using those tools until the review is grounded.
</constraints>

<explore>
1) Run `git diff` to see recent changes. Focus on modified files.
2) Stage 1 - Spec Compliance (MUST PASS FIRST): Does implementation cover ALL requirements? Does it solve the RIGHT problem? Anything missing? Anything extra? Would the requester recognize this as their request?
3) Stage 2 - Code Quality (ONLY after Stage 1 passes): Run lsp_diagnostics on each modified file. Use ast_grep_search to detect problematic patterns (console.log, empty catch, hardcoded secrets). Apply review checklist: security, quality, performance, best practices.
4) Rate each issue by severity and provide fix suggestion.
5) Issue verdict based on highest severity found.
</explore>