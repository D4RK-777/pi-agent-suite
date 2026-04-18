gateway timeout precedence: `gateways.<name>.timeout` > `OMX_OPENCLAW_COMMAND_TIMEOUT_MS` > `5000`.
> For `clawdbot agent` workflows, use `120000` (2 minutes) to avoid premature timeout.
>
> **Production best practices:**
> - Use `|| true` at the end of the command to prevent OMX hook failures from blocking sessions
> - Use `.jsonl` extension with append (`>>`) for structured log aggregation
> - Use `--reply-to 'channel:CHANNEL_ID'` format for reliable Discord delivery (preferred over aliases)

For Korean-first tmux follow-up operations in `#omc-dev`, see the dev guide section below.