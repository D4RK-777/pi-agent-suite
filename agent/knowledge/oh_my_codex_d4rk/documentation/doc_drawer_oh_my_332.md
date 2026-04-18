struction`
- `notifications.openclaw.hooks["session-end"].instruction`

## Önerilen bağlam tokenları

- Her zaman: `{{sessionId}}`, `{{tmuxSession}}`
- Olaya göre: `{{projectName}}`, `{{question}}`, `{{reason}}`

## Ayrıntı (verbosity) stratejisi

- `minimal`: çok kısa bildirimler
- `session`: kısa operasyonel bağlam (önerilir)
- `verbose`: daha fazla durum/aksiyon/risk bağlamı

## Hızlı güncelleme komutu (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"