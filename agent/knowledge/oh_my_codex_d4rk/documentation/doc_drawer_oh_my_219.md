`call_id` and only emit once per matching command lifecycle.

## Consumer guidance

clawhip should:

1. trust `context.normalized_event` as the canonical signal
2. use raw `event` as a secondary discriminator
3. use `command`, `tool_name`, `issue_number`, `pr_number`, and `error_summary` for follow-up routing
4. ignore events without `context.normalized_event` if it only wants the hardened clawhip contract