mento/verifica con un solo responsabile.

## Modello di base

OMX installa e collega questi livelli:

```text
User
  -> Codex CLI
    -> AGENTS.md (cervello dell'orchestrazione)
    -> ~/.codex/prompts/*.md (catalogo prompt degli agenti)
    -> ~/.codex/skills/*/SKILL.md (catalogo skill)
    -> ~/.codex/config.toml (funzionalità, notifiche, MCP)
    -> .omx/ (stato di esecuzione, memoria, piani, log)
```

## Comandi principali