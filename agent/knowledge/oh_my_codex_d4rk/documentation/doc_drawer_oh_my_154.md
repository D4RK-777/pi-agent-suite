NTS.md`) ile proje `./AGENTS.md` dosyasını birleştirir ve ardından çalışma zamanı kaplamasını ekler.
- Mevcut `AGENTS.md` dosyaları sessizce üzerine yazılmaz: etkileşimli TTY'de setup değiştirmeden önce sorar; etkileşimsiz çalıştırmada ise `--force` yoksa değiştirme atlanır (aktif oturum güvenlik kontrolleri hâlâ geçerlidir).
- `config.toml` güncellemeleri (her iki kapsam için):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - MCP sunucu girişleri (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- Kapsama özel `AGENTS.md`
- `.omx/` çalışma zamanı dizinleri ve HUD yapılandırması

## Ajanlar ve Skill'ler