across 3+ iterations, report it as a potential fundamental problem
</Escalation_And_Stop_Conditions>

<Final_Checklist>
- [ ] All requirements from the original task are met (no scope reduction)
- [ ] Zero pending or in_progress TODO items
- [ ] Fresh test run output shows all tests pass
- [ ] Fresh build output shows success
- [ ] lsp_diagnostics shows 0 errors on affected files
- [ ] Architect verification passed (STANDARD tier minimum)
- [ ] ai-slop-cleaner pass completed on changed files (or --no-deslop specified)
- [ ] Post-deslop regression tests pass
- [ ] `/cancel` run for clean state cleanup
</Final_Checklist>

<Advanced>
## PRD Mode (Optional)

When the user provides the `--prd` flag, initialize a Product Requirements Document before starting the ralph loop.