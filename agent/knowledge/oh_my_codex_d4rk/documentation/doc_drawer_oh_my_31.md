rkers)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # opcional: desactivar fallback adaptativo queue->resend
```

Notas:
- Los argumentos de inicio de workers se comparten a través de `OMX_TEAM_WORKER_LAUNCH_ARGS`.
- `OMX_TEAM_WORKER_CLI_MAP` anula `OMX_TEAM_WORKER_CLI` para selección por worker.
- El envío de triggers usa reintentos adaptativos por defecto (queue/submit, luego fallback seguro clear-line+resend cuando es necesario).
- En modo Claude worker, OMX lanza workers como `claude` simple (sin argumentos de inicio extra) e ignora anulaciones explícitas de `--model` / `--config` / `--effort` para que Claude use el `settings.json` predeterminado.

## Qué escribe `omx setup`