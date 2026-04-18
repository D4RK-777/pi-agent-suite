reason={{reason}}\n성과: 완료 결과 1~2문장\n검증: 확인/테스트 결과\n다음: 후속 액션 1~2개"
        }
      }
    }
  }
}
```

## Dev Guide: OpenClaw + Clawdbot Agent (Korean follow-up mode)

Use this profile when `#omc-dev` should receive OpenClaw notifications as
**actual clawdbot agent turns**, with proactive follow-up behavior.

### 1) Force Korean output in hook instructions

- Write all hook instructions in Korean.
- Explicitly require Korean in each instruction template.
- **Prefer `--reply-to 'channel:CHANNEL_ID'` format** over channel aliases for reliability.
  - Example: `--reply-to 'channel:1468539002985644084'` (for #omc-dev)
  - Channel aliases like `#omc-dev` may fail if the bot doesn't have the channel cached.

Example instruction style: