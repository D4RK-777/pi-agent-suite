）戦略

- `minimal`: きわめて短い通知
- `session`: 簡潔な運用文脈（推奨）
- `verbose`: 状態・アクション・リスクを詳細化

## クイック更新コマンド（jq）

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"

jq '.notifications.verbosity = "verbose" |
    .notifications.openclaw.hooks["session-start"].instruction = "[session-start|exec]\nproject={{projectName}} session={{sessionId}} tmux={{tmuxSession}}\n요약: 시작 맥락 1문장\n우선순위: 지금 할 일 1~2개\n주의사항: 리스크/의존성(없으면 없음)" |
    .notifications.openclaw.hooks["session-idle"].instruction = "[session-idle|exec]\nsession={{sessionId}} tmux={{tmuxSession}}\n요약: idle 원인 1문장\n복구계획: 즉시 조치 1~2개\n의사결정: 사용자 입력 필요 여부" |