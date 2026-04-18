module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## Önerilen iş akışı

1. `$deep-interview` — kapsam veya sınırlar hâlâ net değilse.
2. `$ralplan` — netleşen kapsamı onaylanmış bir mimari ve uygulama planına dönüştürmek için.
3. `$team` veya `$ralph` — koordineli paralel yürütme için `$team`, tek sahipli kalıcı tamamlama/doğrulama döngüsü için `$ralph` kullanın.

## Temel Model

OMX şu katmanları kurar ve bağlar:

```text
User
  -> Codex CLI
    -> AGENTS.md (orkestrasyon beyni)
    -> ~/.codex/prompts/*.md (ajan prompt kataloğu)
    -> ~/.codex/skills/*/SKILL.md (skill kataloğu)
    -> ~/.codex/config.toml (özellikler, bildirimler, MCP)
    -> .omx/ (çalışma zamanı durumu, bellek, planlar, günlükler)
```

## Ana Komutlar