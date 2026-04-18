oss-log traceability
- `{{tmuxSession}}` for direct tmux follow-up targeting

Include when relevant:

- `{{projectName}}`
- `{{question}}` (`ask-user-question`)
- `{{reason}}` (`session-end`)

### Structured instruction format

For production deployments, use a structured format that clawdbot agents can parse efficiently:

```
[event|exec]
project={{projectName}} session={{sessionId}} tmux={{tmuxSession}}
필드1: 값
필드2: 값
```

The `[event|exec]` prefix indicates this is an executable hook that requires agent action.
Korean field names (요약, 우선순위, 주의사항, 성과, 검증, 다음) provide consistent structure
for dev teams using Korean as their primary language.

### Verbosity strategy