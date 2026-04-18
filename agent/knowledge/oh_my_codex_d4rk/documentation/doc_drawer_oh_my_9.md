pt-Steuerung

Standardmäßig injiziert OMX:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Dies kombiniert `AGENTS.md` aus `CODEX_HOME` mit dem Projekt-`AGENTS.md` (falls vorhanden) und legt dann die Laufzeit-Überlagerung darüber.
Es erweitert das Codex-Verhalten, ersetzt/umgeht aber nicht die Codex-Kernsystemrichtlinien.

Steuerung:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # AGENTS.md-Injektion deaktivieren
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Team-Modus

Verwenden Sie den Team-Modus für umfangreiche Arbeiten, die von parallelen Workern profitieren.

Lebenszyklus:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Operationelle Befehle: