rst des prompts

Par défaut, OMX injecte :

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Cela fusionne le `AGENTS.md` de `CODEX_HOME` avec le `AGENTS.md` du projet (s'il existe), puis ajoute l'overlay d'exécution.
Cela étend le comportement de Codex, mais ne remplace/contourne pas les politiques système de base de Codex.

Contrôles :

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # désactiver l'injection AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Mode équipe

Utilisez le mode équipe pour les travaux importants qui bénéficient de workers parallèles.

Cycle de vie :

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Commandes opérationnelles :