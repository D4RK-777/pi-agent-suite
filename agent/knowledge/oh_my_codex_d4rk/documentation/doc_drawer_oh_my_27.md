ion.md` para el flujo de trabajo completo de extensiones y el modelo de eventos.

## Flags de inicio

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # solo para setup
```

`--madmax` se mapea a Codex `--dangerously-bypass-approvals-and-sandbox`.
Úsalo solo en entornos sandbox de confianza o externos.

### Política de workingDirectory MCP (endurecimiento opcional)

Por defecto, las herramientas MCP de state/memory/trace aceptan el `workingDirectory` proporcionado por el llamador.
Para restringir esto, establece una lista de raíces permitidas:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Cuando se establece, los valores de `workingDirectory` fuera de estas raíces son rechazados.