operties** | Key-value pairs | `{ mode: string, source: "explicit" | "auto", session_id: string }` |
| **Example payload** | Concrete instance | `{ mode: "autopilot", source: "explicit", session_id: "abc-123" }` |
| **Volume estimate** | Expected frequency | ~50-200 events/day |

## Experiment Measurement Checklist

| Step | Question |
|------|----------|
| **Hypothesis** | What change do we expect? In which metric? |
| **Primary metric** | What's the ONE metric that decides success? |
| **Guardrail metrics** | What must NOT get worse? |
| **Sample size** | How many units per variant for 80% power? |
| **MDE** | What's the minimum detectable effect worth acting on? |
| **Duration** | How long must the test run? (accounting for weekly cycles) |