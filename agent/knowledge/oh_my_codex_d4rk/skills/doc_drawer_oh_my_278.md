d proceed with the most recent successful verification evidence.
7.6 **Regression Re-verification**:
   - After the deslop pass, re-run all tests/build/lint and read the output to confirm they still pass.
   - If post-deslop regression fails, roll back cleaner changes or fix and retry. Then rerun Step 7.5 and Step 7.6 until the regression is green.
   - Do not proceed to completion until post-deslop regression is green (unless `--no-deslop` explicitly skipped the deslop pass).
8. **On approval**: Run `/cancel` to cleanly exit and clean up all state files
9. **On rejection**: Fix the issues raised, then re-verify at the same tier
</Steps>