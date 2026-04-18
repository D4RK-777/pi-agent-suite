Varsayılan olarak, OMX şunu enjekte eder:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Bu, `CODEX_HOME` içindeki `AGENTS.md` ile proje `AGENTS.md` dosyasını (varsa) birleştirir ve ardından çalışma zamanı kaplamasını ekler.
Codex davranışını genişletir, ancak Codex çekirdek sistem politikalarını değiştirmez/atlamaz.

Kontroller:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # AGENTS.md enjeksiyonunu devre dışı bırak
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Takım Modu

Paralel çalışanlardan fayda sağlayan geniş kapsamlı işler için takım modunu kullanın.

Yaşam döngüsü:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Operasyonel komutlar: