ización/verificación con un solo responsable.

## Modelo central

OMX instala y conecta estas capas:

```text
User
  -> Codex CLI
    -> AGENTS.md (cerebro de orquestación)
    -> ~/.codex/prompts/*.md (catálogo de prompts de agentes)
    -> ~/.codex/skills/*/SKILL.md (catálogo de skills)
    -> ~/.codex/config.toml (características, notificaciones, MCP)
    -> .omx/ (estado en ejecución, memoria, planes, registros)
```

## Comandos principales