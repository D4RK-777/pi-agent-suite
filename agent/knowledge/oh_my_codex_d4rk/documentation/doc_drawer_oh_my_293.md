매우 짧은 알림
- `session`: 간결한 운영 맥락 (권장)
- `verbose`: 상태/액션/리스크까지 확장

## 프로덕션 구성 모범 사례

### 명령 게이트웨이 설정

clawdbot agent를 사용하는 프로덕션 환경에서는 다음 설정을 권장합니다:

```json
{
  "notifications": {
    "openclaw": {
      "gateways": {
        "local": {
          "type": "command",
          "command": "(clawdbot agent --session-id omx-hooks --message {{instruction}} --thinking minimal --deliver --reply-channel discord --reply-to 'channel:1468539002985644084' --timeout 120 --json >>/tmp/omx-openclaw-agent.jsonl 2>&1 || true)",
          "timeout": 120000
        }
      }
    }
  }
}
```