) |
   .notifications.openclaw.hooks["session-start"] = {
     enabled: true,
     gateway: "local",
     instruction: "OMX hook=session-start project={{projectName}} session={{sessionId}} tmux={{tmuxSession}}. 한국어로 상태를 공유하고 SOUL.md를 참고해 필요한 후속 조치를 #omc-dev에 안내하세요."
   } |
   .notifications.openclaw.hooks["session-idle"] = {
     enabled: true,
     gateway: "local",
     instruction: "OMX hook=session-idle project={{projectName}} session={{sessionId}} tmux={{tmuxSession}}. 한국어로 idle 상황을 간단히 공유하고 진행중인 작업 팔로업을 안내하세요."
   } |
   .notifications.openclaw.hooks["ask-user-question"] = {
     enabled: true,
     gateway: "local",
     instruction: "OMX hook=ask-user-question session={{sessionId}} tmux={{tmuxSession}} question={{question}}. 한국어로 사용자 응답 필요를 #omc-dev에 알리고 즉시 액션 아이템을 제시하세요."
   } |