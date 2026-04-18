--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # apenas para setup
```

`--madmax` mapeia para Codex `--dangerously-bypass-approvals-and-sandbox`.
Use apenas em ambientes sandbox confiáveis ou externos.

### Política de workingDirectory MCP (endurecimento opcional)

Por padrão, as ferramentas MCP de state/memory/trace aceitam o `workingDirectory` fornecido pelo chamador.
Para restringir isso, defina uma lista de raízes permitidas:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Quando definido, valores de `workingDirectory` fora dessas raízes são rejeitados.

## Controle de prompts Codex-First

Por padrão, OMX injeta:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```