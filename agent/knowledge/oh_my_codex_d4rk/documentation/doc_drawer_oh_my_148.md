-bypass-approvals-and-sandbox` ile eşlenir.
Yalnızca güvenilir/harici sandbox ortamlarında kullanın.

### MCP workingDirectory politikası (isteğe bağlı sertleştirme)

Varsayılan olarak, MCP durum/bellek/trace araçları çağıranın sağladığı `workingDirectory` değerini kabul eder.
Bunu kısıtlamak için bir izin listesi belirleyin:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Ayarlandığında, bu kökler dışındaki `workingDirectory` değerleri reddedilir.

## Codex-First Prompt Kontrolü

Varsayılan olarak, OMX şunu enjekte eder:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```