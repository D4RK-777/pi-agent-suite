для [OpenAI Codex CLI](https://github.com/openai/codex).

## Что нового в v0.9.0 — Spark Initiative

Spark Initiative — это релиз, усиливающий нативный путь исследования и инспекции в OMX.

- **Нативный harness для `omx explore`** — ускоряет и ужесточает read-only исследование репозитория через Rust-путь.
- **`omx sparkshell`** — нативная операторская поверхность для инспекции с краткими сводками длинного вывода и явным захватом tmux-pane.
- **Кроссплатформенные нативные release-артефакты** — путь hydration для `omx-explore-harness`, `omx-sparkshell` и `native-release-manifest.json` теперь входит в release pipeline.
- **Усиленный CI/CD** — добавлены явная настройка Rust toolchain в job `build`, а также `cargo fmt --check` и `cargo clippy -- -D warnings`.