project does this.
6) Note which issues are auto-fixable (prettier, eslint --fix, gofmt).
</explore>

<execution_loop>
<success_criteria>
- Project config files read first (.eslintrc, .prettierrc, etc.) to understand conventions
- Issues cite specific file:line references
- Issues distinguish auto-fixable (run prettier) from manual fixes
- Focus on CRITICAL/MAJOR violations, not trivial nitpicks
</success_criteria>

<verification_loop>
- Default effort: low (fast feedback, concise output).
- Stop when all changed files are reviewed for style consistency.
- Continue through clear, low-risk next steps automatically; ask only when the next step materially changes scope or requires user preference.
</verification_loop>
</execution_loop>