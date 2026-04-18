olo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # solo per setup
```

`--madmax` corrisponde a Codex `--dangerously-bypass-approvals-and-sandbox`.
Utilizzare solo in ambienti sandbox fidati/esterni.

### Policy MCP workingDirectory (hardening opzionale)

Per impostazione predefinita, gli strumenti MCP stato/memoria/trace accettano il `workingDirectory` fornito dal chiamante.
Per limitare questo, imposta una lista di directory root consentite:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Quando impostato, i valori `workingDirectory` al di fuori di queste root vengono rifiutati.

## Controllo Codex-First dei prompt

Per impostazione predefinita, OMX inietta:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```