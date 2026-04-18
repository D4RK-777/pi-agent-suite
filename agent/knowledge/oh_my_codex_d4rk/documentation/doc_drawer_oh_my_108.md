lusão/verificação com um único responsável.

## Modelo central

OMX instala e conecta estas camadas:

```text
User
  -> Codex CLI
    -> AGENTS.md (cérebro de orquestração)
    -> ~/.codex/prompts/*.md (catálogo de prompts de agentes)
    -> ~/.codex/skills/*/SKILL.md (catálogo de skills)
    -> ~/.codex/config.toml (funcionalidades, notificações, MCP)
    -> .omx/ (estado de execução, memória, planos, logs)
```

## Comandos principais