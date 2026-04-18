progress.json` including numeric + qualitative feedback.
   - Default pass threshold: `score >= 90`.
   - **URL-based cloning tasks**: When the task description contains a target URL (e.g., "clone https://example.com"), invoke `$web-clone` instead of `$visual-verdict`. The web-clone skill handles the full extraction → generation → verification pipeline and uses `$visual-verdict` internally for visual scoring.
6. **Verify completion with fresh evidence**:
   a. Identify what command proves the task is complete
   b. Run verification (test, build, lint)
   c. Read the output -- confirm it actually passed
   d. Check: zero pending/in_progress TODO items
7. **Architect verification** (tiered):
   - <5 files, <100 lines with full tests: STANDARD tier minimum (architect role)