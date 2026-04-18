kılmalarını yok sayar, böylece Claude varsayılan `settings.json` kullanır.

## `omx setup` Ne Yazar

- `.omx/setup-scope.json` (kalıcı kurulum kapsamı)
- Kapsama bağlı kurulumlar:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Başlatma davranışı: kalıcı kapsam `project` ise, `omx` başlatma otomatik olarak `CODEX_HOME=./.codex` kullanır (`CODEX_HOME` zaten ayarlanmadıysa).
- Başlatma talimatları `~/.codex/AGENTS.md` (veya geçersiz kılındıysa `CODEX_HOME/AGENTS.md`) ile proje `./AGENTS.md` dosyasını birleştirir ve ardından çalışma zamanı kaplamasını ekler.