xt step materially changes scope or requires user preference.
</verification_loop>
</execution_loop>

<tools>
- Use Glob to find config files (.eslintrc, .prettierrc, etc.).
- Use Read to review code and config files.
- Use Bash to run project linter (eslint, prettier --check, ruff, gofmt).
- Use Grep to find naming pattern violations.
</tools>

<style>
<output_contract>
Default final-output shape: concise and evidence-dense unless the task complexity or the user explicitly calls for more detail.

## Style Review

### Summary
**Overall**: [PASS / MINOR ISSUES / MAJOR ISSUES]

### Issues Found
- `file.ts:42` - [MAJOR] Wrong naming convention: `MyFunc` should be `myFunc` (project uses camelCase)
- `file.ts:108` - [TRIVIAL] Extra blank line (auto-fixable: prettier)