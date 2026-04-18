o 'channel:1468539002985644084' --timeout 120 --json >>/tmp/omx-openclaw-agent.jsonl 2>&1 || true)",
          "timeout": 120000
        }
      },
      "hooks": {
        "session-start": {
          "enabled": true,
          "gateway": "local",
          "instruction": "[session-start|exec]\nproject={{projectName}} session={{sessionId}} tmux={{tmuxSession}}\n요약: 시작 맥락 1문장\n우선순위: 지금 할 일 1~2개\n주의사항: 리스크/의존성(없으면 없음)"
        },
        "session-idle": {
          "enabled": true,
          "gateway": "local",
          "instruction": "[session-idle|exec]\nsession={{sessionId}} tmux={{tmuxSession}}\n요약: idle 원인 1문장\n복구계획: 즉시 조치 1~2개\n의사결정: 사용자 입력 필요 여부"
        },
        "ask-user-question": {
          "enabled": true,
          "gateway": "local",