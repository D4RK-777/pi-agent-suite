start/end) |
| **Segment** | User/context breakdown | By mode (ultrawork, ralph, plain autopilot) |
| **Exclusions** | What doesn't count | Sessions <30s (likely accidental activation) |
| **Direction** | Higher is better / Lower is better | Higher is better |
| **Leading/Lagging** | Predictive or outcome | Lagging (outcome metric) |

## Event Schema Template

| Field | Description | Example |
|-------|-------------|---------|
| **Event name** | Snake_case, verb_noun | `mode_activated` |
| **Trigger** | Exact condition | When user invokes a skill that transitions to a named mode |
| **Properties** | Key-value pairs | `{ mode: string, source: "explicit" | "auto", session_id: string }` |