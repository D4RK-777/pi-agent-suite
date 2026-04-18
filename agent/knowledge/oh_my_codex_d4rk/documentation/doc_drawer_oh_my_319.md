ys.<name>.timeout` (recommend `120000` for clawdbot agent) or set `OMX_OPENCLAW_COMMAND_TIMEOUT_MS`.
- **Hook failures blocking sessions**: ensure command ends with `|| true` to prevent OMX from waiting on clawdbot failures.
- **Missing logs**: use `.jsonl` extension with append (`>>`) for persistent structured logging.
- **Discord delivery failures**: use `--reply-to 'channel:CHANNEL_ID'` format instead of channel aliases.