zahl)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # optional: adaptiven Queue->Resend-Fallback deaktivieren
```

Hinweise:
- Worker-Startargumente werden weiterhin über `OMX_TEAM_WORKER_LAUNCH_ARGS` geteilt.
- `OMX_TEAM_WORKER_CLI_MAP` überschreibt `OMX_TEAM_WORKER_CLI` für Worker-spezifische Auswahl.
- Trigger-Übermittlung verwendet standardmäßig adaptive Wiederholungsversuche (Queue/Submit, dann sicherer Clear-Line+Resend-Fallback bei Bedarf).
- Im Claude-Worker-Modus startet OMX Worker als einfaches `claude` (keine zusätzlichen Startargumente) und ignoriert explizite `--model` / `--config` / `--effort`-Überschreibungen, sodass Claude die Standard-`settings.json` verwendet.

## Was `omx setup` schreibt