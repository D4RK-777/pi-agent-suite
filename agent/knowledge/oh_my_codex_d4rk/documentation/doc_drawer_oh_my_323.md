ão/risco

## Comando rápido de atualização (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"

jq '.notifications.verbosity = "verbose" |
    .notifications.openclaw.hooks["session-start"].instruction = "[session-start|exec]\nproject={{projectName}} session={{sessionId}} tmux={{tmuxSession}}\n요약: 시작 맥락 1문장\n우선순위: 지금 할 일 1~2개\n주의사항: 리스크/의존성(없으면 없음)" |
    .notifications.openclaw.hooks["session-idle"].instruction = "[session-idle|exec]\nsession={{sessionId}} tmux={{tmuxSession}}\n요약: idle 원인 1문장\n복구계획: 즉시 조치 1~2개\n의사결정: 사용자 입력 필요 여부" |
    .notifications.openclaw.hooks["ask-user-question"].instruction = "[ask-user-question|exec]\nsession={{sessionId}} tmux={{tmuxSession}} question={{question}}\n핵심질문: 필요한 답변 1문장\n영향: 미응답 시 영향 1문장\n권장응답: 가장 빠른 답변 형태" |