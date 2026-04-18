yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # nur bei setup
```

`--madmax` entspricht Codex `--dangerously-bypass-approvals-and-sandbox`.
Nur in vertrauenswürdigen/externen Sandbox-Umgebungen verwenden.

### MCP workingDirectory-Richtlinie (optionale Härtung)

Standardmäßig akzeptieren MCP-Zustand/Speicher/Trace-Tools das vom Aufrufer bereitgestellte `workingDirectory`.
Um dies einzuschränken, setzen Sie eine Erlaubnisliste von Wurzelverzeichnissen:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Wenn gesetzt, werden `workingDirectory`-Werte außerhalb dieser Wurzeln abgelehnt.

## Codex-First Prompt-Steuerung

Standardmäßig injiziert OMX:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```