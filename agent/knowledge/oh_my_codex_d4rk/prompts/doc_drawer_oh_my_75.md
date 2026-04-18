ource gathering, keep using those tools until the resolution is grounded.
</ask_gate>
</constraints>

<explore>
1) Detect project type from manifest files.
2) Collect ALL errors: run lsp_diagnostics_directory (preferred for TypeScript) or language-specific build command.
3) Categorize errors: type inference, missing definitions, import/export, configuration.
4) Fix each error with the minimal change: type annotation, null check, import fix, dependency addition.
5) Verify fix after each change: lsp_diagnostics on modified file.
6) Final verification: full build command exits 0.
</explore>