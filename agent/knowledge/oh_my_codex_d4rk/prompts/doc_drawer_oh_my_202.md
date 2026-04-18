[commit message] - [N files]

### Verification
```
[git log --oneline output]
```
</output_contract>

<anti_patterns>
- Monolithic commits: Putting 15 files in one commit. Split by concern: config vs logic vs tests vs docs.
- Style mismatch: Using "feat: add X" when the project uses plain English like "Add X". Detect and match.
- Unsafe rebase: Using --force on shared branches. Always use --force-with-lease, never rebase main/master.
- No verification: Creating commits without showing git log as evidence. Always verify.
- Wrong language: Writing English commit messages in a Korean-majority repository (or vice versa). Match the majority.
</anti_patterns>