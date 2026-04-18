p mit einer verantwortlichen Instanz.

## Kernmodell

OMX installiert und verbindet diese Schichten:

```text
User
  -> Codex CLI
    -> AGENTS.md (Orchestrierungs-Gehirn)
    -> ~/.codex/prompts/*.md (Agenten-Prompt-Katalog)
    -> ~/.codex/skills/*/SKILL.md (Skill-Katalog)
    -> ~/.codex/config.toml (Features, Benachrichtigungen, MCP)
    -> .omx/ (Laufzeitzustand, Speicher, Pläne, Protokolle)
```

## Hauptbefehle