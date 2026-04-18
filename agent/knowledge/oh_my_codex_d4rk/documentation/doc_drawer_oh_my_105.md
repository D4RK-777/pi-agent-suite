para [OpenAI Codex CLI](https://github.com/openai/codex).

## Novidades na v0.9.0 — Spark Initiative

Spark Initiative é a versão que fortalece o caminho nativo de exploração e inspeção no OMX.

- **Harness nativo para `omx explore`** — executa exploração de repositório somente leitura com uma via em Rust mais rápida e mais restrita.
- **`omx sparkshell`** — superfície nativa voltada ao operador, com resumos de saídas longas e captura explícita de painéis tmux.
- **Assets nativos multiplataforma** — o caminho de hidratação de `omx-explore-harness`, `omx-sparkshell` e `native-release-manifest.json` agora faz parte do pipeline de release.
- **CI/CD reforçado** — adiciona configuração explícita de Rust no job `build`, além de `cargo fmt --check` e `cargo clippy -- -D warnings`.