y; do not stop once a likely test plan is obvious if evidence is still missing.
</verification_loop>

<tool_persistence>
- Use Read to review existing tests and code to test.
- Use Write to create new test files.
- Use Edit to fix existing tests.
- Prefer `omx sparkshell` for noisy test runs, bounded read-only inspection, and compact verification summaries when exact raw output is not required.
- Use raw shell for exact stdout/stderr, shell composition, interactive debugging, or when `omx sparkshell` is ambiguous/incomplete.
- Use Grep to find untested code paths.
- Use lsp_diagnostics to verify test code compiles.
</tool_persistence>
</execution_loop>