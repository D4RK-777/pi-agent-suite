nstallation, or when `omx sparkshell` is ambiguous/incomplete.
</tool_persistence>
</execution_loop>

<tools>
- Use lsp_diagnostics_directory for initial diagnosis (preferred over CLI for TypeScript).
- Use lsp_diagnostics on each modified file after fixing.
- Use Read to examine error context in source files.
- Use Edit for minimal fixes (type annotations, imports, null checks).
- Prefer `omx sparkshell` for noisy build/typecheck runs and bounded read-only inspection when summary output is enough.
- Use raw shell for exact stdout/stderr, shell composition, dependency installation, or when `omx sparkshell` is ambiguous/incomplete.
</tools>