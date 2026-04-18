_MODEL` (legacy alias: `OMX_SPARK_MODEL`) when 1+2 are absent and team `agentType` is low-complexity

Default-model rule:
- Do **not** assume a frontier or spark model from recency or model-family heuristics.
- Use `OMX_DEFAULT_FRONTIER_MODEL` for frontier-default guidance.
- Use `OMX_DEFAULT_SPARK_MODEL` for spark/low-complexity worker-default guidance.

Thinking-level rule (critical):
- **No model-name heuristic mapping.**
- Team runtime must **not** infer `model_reasoning_effort` from model-name substrings (e.g., `spark`, `high-capability`, `mini`).
- When the leader assigns teammate roles/tasks, OMX allocates **per-worker reasoning effort dynamically** from the resolved worker role (`low`, `medium`, `high`).