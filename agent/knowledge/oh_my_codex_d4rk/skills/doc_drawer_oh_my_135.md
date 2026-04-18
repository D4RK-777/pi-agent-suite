ut` to `120000` (recommended).
- For dev operations, enforce Korean output in all hook instructions.
- Include both `session={{sessionId}}` and `tmux={{tmuxSession}}` in hook text for traceability.
- If follow-up is needed, explicitly instruct clawdbot to consult `SOUL.md` and continue in `#omc-dev`.
- **Error handling**: Append `|| true` to prevent OMX hook failures from blocking the session.
- **JSONL logging**: Use `.jsonl` extension and append (`>>`) for structured log aggregation.
- **Reply target format**: Use `--reply-to 'channel:CHANNEL_ID'` for reliability (preferred over channel aliases).

Example (targeting `#omc-dev` with production-tested settings):