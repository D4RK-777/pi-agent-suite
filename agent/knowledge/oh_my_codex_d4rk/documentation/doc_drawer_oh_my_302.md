"
        },
        "ask-user-question": {
          "enabled": true,
          "gateway": "local",
          "instruction": "[ask-user-question|exec]\nsession={{sessionId}} tmux={{tmuxSession}} question={{question}}\n핵심질문: 필요한 답변 1문장\n영향: 미응답 시 영향 1문장\n권장응답: 가장 빠른 답변 형태"
        },
        "stop": {
          "enabled": true,
          "gateway": "local",
          "instruction": "[session-stop|exec]\nsession={{sessionId}} tmux={{tmuxSession}}\n요약: 중단 사유\n현재상태: 저장/미완료 항목\n재개: 첫 액션 1개"
        },
        "session-end": {
          "enabled": true,
          "gateway": "local",
          "instruction": "[session-end|exec]\nproject={{projectName}} session={{sessionId}} tmux={{tmuxSession}} reason={{reason}}\n성과: 완료 결과 1~2문장\n검증: 확인/테스트 결과\n다음: 후속 액션 1~2개"
        }
      }
    }
  }
}
```