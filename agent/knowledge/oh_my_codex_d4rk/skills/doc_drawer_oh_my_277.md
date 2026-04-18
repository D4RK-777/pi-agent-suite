cation** (tiered):
   - <5 files, <100 lines with full tests: STANDARD tier minimum (architect role)
   - Standard changes: STANDARD tier (architect role)
   - >20 files or security/architectural changes: THOROUGH tier (architect role)
   - Ralph floor: always at least STANDARD, even for small changes
7.5 **Mandatory Deslop Pass**:
   - After Step 7 passes, run `oh-my-codex:ai-slop-cleaner` on **all files changed during the Ralph session**.
   - Scope the cleaner to **changed files only**; do not widen the pass beyond Ralph-owned edits.
   - Run the cleaner in **standard mode** (not `--review`).
   - If the prompt contains `--no-deslop`, skip Step 7.5 entirely and proceed with the most recent successful verification evidence.
7.6 **Regression Re-verification**: