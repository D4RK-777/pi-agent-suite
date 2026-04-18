t"
```

Cuando se establece, los valores de `workingDirectory` fuera de estas raíces son rechazados.

## Control de prompts Codex-First

Por defecto, OMX inyecta:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Esto combina el `AGENTS.md` de `CODEX_HOME` con el `AGENTS.md` del proyecto (si existe) y luego añade la superposición de runtime.
Extiende el comportamiento de Codex, pero no reemplaza ni elude las políticas centrales del sistema Codex.

Controles:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # desactivar inyección de AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Modo equipo

Usa el modo equipo para trabajo amplio que se beneficia de workers paralelos.

Ciclo de vida: