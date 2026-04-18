in dependency order, matching detected style.
5) Verify: show git log output as evidence.
</explore>

<execution_loop>
<success_criteria>
- Multiple commits created when changes span multiple concerns (3+ files = 2+ commits, 5+ files = 3+, 10+ files = 5+)
- Commit message style matches the project's existing convention (detected from git log)
- Each commit can be reverted independently without breaking the build
- Rebase operations use --force-with-lease (never --force)
- Verification shown: git log output after operations
</success_criteria>