x-openclaw-agent.jsonl 2>&1 || true)",
          "timeout": 120000
        }
      }
    }
  }
}
```

**주요 설정 설명:**
- `|| true`: clawdbot 실패 시 OMX 세션이 차단되지 않도록 합니다
- `>>/tmp/omx-openclaw-agent.jsonl`: 구조화된 JSONL 로그를 append 모드로 기록합니다
- `--reply-to 'channel:CHANNEL_ID'`: 채널 별칭 대신 ID를 사용하여 안정적인 전달을 보장합니다
- `timeout: 120000`: 2분 타임아웃으로 clawdbot agent 작업이 완료될 시간을 확보합니다

### 로그 확인 명령어

```bash
# JSONL 로그에서 최근 항목 확인
tail -n 120 /tmp/omx-openclaw-agent.jsonl | jq -s '.[] | {timestamp: (.timestamp // .time), status: (.status // .error // "ok")}'

# 오류 검색
rg '"error"|"failed"|"timeout"' /tmp/omx-openclaw-agent.jsonl | tail -20
```

## 빠른 업데이트 명령어 (jq)

```bash
CONFIG_FILE="$HOME/.codex/.omx-config.json"