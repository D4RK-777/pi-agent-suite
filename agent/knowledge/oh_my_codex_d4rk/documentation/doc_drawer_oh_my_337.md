truction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Token ngữ cảnh khuyến nghị

- Luôn có: `{{sessionId}}`, `{{tmuxSession}}`
- Theo sự kiện: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Chiến lược mức độ chi tiết (verbosity)

- `minimal`: thông báo rất ngắn
- `session`: ngữ cảnh vận hành ngắn gọn (khuyến nghị)
- `verbose`: nhiều ngữ cảnh hơn về trạng thái/hành động/rủi ro

## Lệnh cập nhật nhanh (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"