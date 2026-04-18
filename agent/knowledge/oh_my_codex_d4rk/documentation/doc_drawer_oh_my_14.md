nn überschrieben) mit dem Projekt-`./AGENTS.md` und hängen anschließend die Runtime-Überlagerung an.
- Vorhandene `AGENTS.md`-Dateien werden nie stillschweigend überschrieben: Interaktive TTY-Läufe fragen vor dem Ersetzen, nicht-interaktive Läufe überspringen das Ersetzen ohne `--force` (aktive Sitzungs-Sicherheitsprüfungen gelten weiterhin).
- `config.toml`-Aktualisierungen (für beide Bereiche):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCP-Server-Einträge (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- Bereichsspezifische `AGENTS.md`
- `.omx/`-Laufzeitverzeichnisse und HUD-Konfiguration

## Agenten und Skills