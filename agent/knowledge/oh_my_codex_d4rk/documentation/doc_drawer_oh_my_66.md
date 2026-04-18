Per impostazione predefinita, OMX inietta:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Questo unisce l'`AGENTS.md` di `CODEX_HOME` con l'`AGENTS.md` del progetto (se presente) e poi aggiunge l'overlay di runtime.
Estende il comportamento di Codex, ma non sostituisce/aggira le policy di sistema core di Codex.

Controlli:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # disabilita l'iniezione AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Modalità team

Usa la modalità team per lavori ampi che beneficiano di worker paralleli.

Ciclo di vita:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Comandi operativi: