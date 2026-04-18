bhook forwarding), use a command gateway that invokes
`clawdbot agent` and delivers back to Discord.

Notes:
- Hook name mapping is intentional: notifications `session-stop` -> OpenClaw hook `stop`.
- OMX shell-escapes template substitutions for command gateways (including `{{instruction}}`).
- Keep `instruction` templates concise and avoid untrusted shell metacharacters.
- During troubleshooting, avoid swallowing command output; route it to a log file.
- Timeout precedence: `gateways.<name>.timeout` > `OMX_OPENCLAW_COMMAND_TIMEOUT_MS` > `5000`.
- For clawdbot agent workflows, set `gateways.<name>.timeout` to `120000` (recommended).
- For dev operations, enforce Korean output in all hook instructions.