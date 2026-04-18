ker)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # opzionale: disabilita il fallback adattivo queue->resend
```

Note:
- Gli argomenti di avvio dei worker sono ancora condivisi tramite `OMX_TEAM_WORKER_LAUNCH_ARGS`.
- `OMX_TEAM_WORKER_CLI_MAP` sovrascrive `OMX_TEAM_WORKER_CLI` per la selezione per singolo worker.
- L'invio dei trigger usa per impostazione predefinita tentativi adattivi (queue/submit, poi fallback sicuro clear-line+resend quando necessario).
- In modalità worker Claude, OMX avvia i worker come semplice `claude` (nessun argomento di avvio aggiuntivo) e ignora le sovrascritture esplicite `--model` / `--config` / `--effort` in modo che Claude usi il `settings.json` predefinito.

## Cosa scrive `omx setup`