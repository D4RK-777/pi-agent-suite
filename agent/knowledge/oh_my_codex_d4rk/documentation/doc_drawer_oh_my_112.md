ompts Codex-First

Por padrão, OMX injeta:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Isso combina o `AGENTS.md` de `CODEX_HOME` com o `AGENTS.md` do projeto (se existir) e depois adiciona o overlay de runtime.
Estende o comportamento do Codex, mas não substitui nem contorna as políticas centrais do sistema Codex.

Controles:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # desativar injeção de AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Modo equipe

Use o modo equipe para trabalhos amplos que se beneficiam de workers paralelos.

Ciclo de vida:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Comandos operacionais: