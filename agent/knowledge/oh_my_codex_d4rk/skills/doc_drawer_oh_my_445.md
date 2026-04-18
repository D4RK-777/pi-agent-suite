(accessibility tree) for structural understanding — it is far more token-efficient than screenshots.
- Use `browser_take_screenshot` only when visual verification is needed (Pass 1 baseline, Pass 4 comparison).
- Use `browser_evaluate` for DOM/style extraction — pass the scripts from this skill EXACTLY as written (do not modify them).
- If running within ralph, use `state_write` / `state_read` for web-clone state persistence between iterations.
- Skip Codex consultation for straightforward extraction; use it only if verification repeatedly fails on the same issue.
</Tool_Usage>

<State_Management>
Persist extraction and progress data so the pipeline can resume if interrupted.