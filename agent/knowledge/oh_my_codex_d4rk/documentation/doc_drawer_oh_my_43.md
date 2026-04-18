on/vérification avec un seul responsable.

## Modèle de base

OMX installe et connecte ces couches :

```text
User
  -> Codex CLI
    -> AGENTS.md (cerveau d'orchestration)
    -> ~/.codex/prompts/*.md (catalogue de prompts d'agents)
    -> ~/.codex/skills/*/SKILL.md (catalogue de skills)
    -> ~/.codex/config.toml (fonctionnalités, notifications, MCP)
    -> .omx/ (état d'exécution, mémoire, plans, journaux)
```

## Commandes principales