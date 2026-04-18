- `suggestions[]`: actionable next edits tied to the differences
- `reasoning`: 1-2 sentence summary

<Threshold_And_Loop>
- Target pass threshold is **90+**.
- If `score < 90`, continue editing and rerun `$visual-verdict` before any further code edits in the next iteration.
- Persist the verdict in `.omx/state/{scope}/ralph-progress.json` with both:
  - numeric signal (`score`, threshold pass/fail)
  - qualitative signal (`reasoning`, `suggestions`, `next_actions`)
</Threshold_And_Loop>