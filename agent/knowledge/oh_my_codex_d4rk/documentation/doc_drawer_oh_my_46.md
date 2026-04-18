igh
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # uniquement pour setup
```

`--madmax` correspond à Codex `--dangerously-bypass-approvals-and-sandbox`.
À utiliser uniquement dans des environnements sandbox de confiance/externes.

### Politique MCP workingDirectory (durcissement optionnel)

Par défaut, les outils MCP état/mémoire/trace acceptent le `workingDirectory` fourni par l'appelant.
Pour restreindre cela, définissez une liste d'autorisation de racines :

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Lorsque défini, les valeurs `workingDirectory` en dehors de ces racines sont rejetées.

## Contrôle Codex-First des prompts

Par défaut, OMX injecte :

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```