ses like `#omc-dev` may fail if the bot doesn't have the channel cached.

Example instruction style:

```text
OMX 훅={{event}} 프로젝트={{projectName}} 세션={{sessionId}}.
반드시 한국어로 응답하세요.
OMX tmux 세션: {{tmuxSession}}.
SOUL.md 및 #omc-dev 맥락을 참고해 필요한 후속 액션이 있으면 즉시 안내하세요.
```

### 2) Track which OMX tmux session emitted the hook

- Include both `{{sessionId}}` and `{{tmuxSession}}` in every hook message.
- If `{{tmuxSession}}` is present, use that as the primary follow-up target.
- If missing, derive candidate tmux sessions from `sessionId` and current project path.

Quick checks:

```bash
tmux ls | grep '^omx-' || true
tmux list-panes -a -F '#{session_name}\t#{pane_id}\t#{pane_current_path}' | grep "$(basename "$PWD")" || true
```

### 3) SOUL.md + #omc-dev follow-up runbook