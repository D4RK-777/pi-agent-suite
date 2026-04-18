. **Run long operations in background**: Builds, installs, test suites use `run_in_background: true`
5. **Visual task gate (when screenshot/reference images are present)**:
   - Run `$visual-verdict` **before every next edit**.
   - Require structured JSON output: `score`, `verdict`, `category_match`, `differences[]`, `suggestions[]`, `reasoning`.
   - Persist verdict to `.omx/state/{scope}/ralph-progress.json` including numeric + qualitative feedback.
   - Default pass threshold: `score >= 90`.