tmux={{tmuxSession}} question={{question}}. 한국어로 사용자 응답 필요를 #omc-dev에 알리고 즉시 액션 아이템을 제시하세요."
   } |
   .notifications.openclaw.hooks["stop"] = {
     enabled: true,
     gateway: "local",
     instruction: "OMX hook=session-stop project={{projectName}} session={{sessionId}} tmux={{tmuxSession}}. 한국어로 중단 상태와 정리 액션을 SOUL.md 기준으로 전달하세요."
   } |
   .notifications.openclaw.hooks["session-end"] = {
     enabled: true,
     gateway: "local",
     instruction: "OMX hook=session-end project={{projectName}} session={{sessionId}} tmux={{tmuxSession}} reason={{reason}}. 한국어로 완료 요약을 1줄로 남기고 필요한 후속 조치를 안내하세요."
   }' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

Verification for this mode: