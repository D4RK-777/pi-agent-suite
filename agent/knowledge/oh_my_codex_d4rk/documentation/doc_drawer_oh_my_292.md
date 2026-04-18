n.it.md)


이 문서는 영문 본문 가이드의 **“Prompt tuning guide (concise + context-aware)”** 섹션을 한국어로 정리한 페이지입니다.

게이트웨이/훅/검증까지 포함한 전체 통합 문서는 [English guide](./openclaw-integration.md)를 참고하세요.

## 프롬프트 튜닝 (간결 + 컨텍스트 인식)

## 프롬프트 템플릿 수정 위치

- `notifications.openclaw.hooks["session-start"].instruction`
- `notifications.openclaw.hooks["session-idle"].instruction`
- `notifications.openclaw.hooks["ask-user-question"].instruction`
- `notifications.openclaw.hooks["stop"].instruction`
- `notifications.openclaw.hooks["session-end"].instruction`

## 권장 컨텍스트 토큰

- 항상 포함: `{{sessionId}}`, `{{tmuxSession}}`
- 이벤트별 선택: `{{projectName}}`, `{{question}}`, `{{reason}}`

## verbosity 전략

- `minimal`: 매우 짧은 알림
- `session`: 간결한 운영 맥락 (권장)
- `verbose`: 상태/액션/리스크까지 확장

## 프로덕션 구성 모범 사례

### 명령 게이트웨이 설정