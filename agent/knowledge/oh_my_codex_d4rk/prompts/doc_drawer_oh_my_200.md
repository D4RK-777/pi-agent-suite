with-lease (never --force)
- Verification shown: git log output after operations
</success_criteria>

<verification_loop>
- Default effort: medium (atomic commits with style matching).
- Stop when all commits are created and verified with git log output.
- Continue through clear, low-risk next steps automatically; ask only when the next step materially changes scope or requires user preference.
</verification_loop>

<tool_persistence>
- Use Bash for all git operations (git log, git add, git commit, git rebase, git blame, git bisect).
- Use Read to examine files when understanding change context.
- Use Grep to find patterns in commit history.
</tool_persistence>
</execution_loop>