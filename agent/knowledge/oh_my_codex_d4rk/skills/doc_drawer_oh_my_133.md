ser-question"]
   }' "$CONFIG_FILE" > "$CONFIG_FILE.tmp" && mv "$CONFIG_FILE.tmp" "$CONFIG_FILE"
```

> Activation gate: OpenClaw-backed dispatch is active only when `OMX_OPENCLAW=1`.
> For command gateways, also require `OMX_OPENCLAW_COMMAND=1`.
> Optional timeout env override: `OMX_OPENCLAW_COMMAND_TIMEOUT_MS` (ms).

### 4b-1) OpenClaw + Clawdbot Agent Workflow (recommended for dev)

If the user explicitly asks to route hook notifications through **clawdbot agent turns**
(not direct message/webhook forwarding), use a command gateway that invokes
`clawdbot agent` and delivers back to Discord.