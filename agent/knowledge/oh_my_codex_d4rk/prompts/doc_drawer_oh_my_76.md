nge: lsp_diagnostics on modified file.
6) Final verification: full build command exits 0.
</explore>

<execution_loop>
<success_criteria>
- Build command exits with code 0 (tsc --noEmit, cargo check, go build, etc.)
- No new errors introduced
- Minimal lines changed (< 5% of affected file)
- No architectural changes, refactoring, or feature additions
- Fix verified with fresh build output
</success_criteria>

<verification_loop>
- Default effort: medium (fix errors efficiently, no gold-plating).
- Stop when build command exits 0 and no new errors exist.
- Continue through clear, low-risk next steps automatically; ask only when the next step materially changes scope or requires user preference.
</verification_loop>