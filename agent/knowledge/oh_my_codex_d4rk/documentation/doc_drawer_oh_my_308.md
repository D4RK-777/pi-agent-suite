}}",
      "events": ["session-end"],
      "instruction": "OMX event {{event}} for {{projectPath}}"
    }
  }
}
```

These aliases are normalized by OMX into internal OpenClaw gateway mappings.

## Option C: Clawdbot agent-command workflow (recommended for dev)

Use this when you want OMX hook events to trigger **agent turns** (not plain
message/webhook forwarding), e.g. for `#omc-dev`.

> Shell safety: template variables (for example `{{instruction}}`) are interpolated into the
> command string. Keep templates simple and avoid shell metacharacters in user-derived content.
> For troubleshooting, temporarily remove output redirection and inspect command output.
>
> Command gateway timeout precedence: `gateways.<name>.timeout` > `OMX_OPENCLAW_COMMAND_TIMEOUT_MS` > `5000`.