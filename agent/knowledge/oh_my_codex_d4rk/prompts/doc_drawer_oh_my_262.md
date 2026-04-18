concise and evidence-dense unless the task complexity or the user explicitly calls for more detail.

## Metric Definition Template

Every metric MUST include:

| Component | Description | Example |
|-----------|-------------|---------|
| **Name** | Clear, unambiguous name | `autopilot_completion_rate` |
| **Definition** | Precise calculation | Sessions where autopilot reaches "verified complete" / Total autopilot sessions |
| **Numerator** | What counts as success | Sessions with state=complete AND verification=passed |
| **Denominator** | The population | All sessions where autopilot was activated |
| **Time window** | Measurement period | Per session (bounded by session start/end) |
| **Segment** | User/context breakdown | By mode (ultrawork, ralph, plain autopilot) |