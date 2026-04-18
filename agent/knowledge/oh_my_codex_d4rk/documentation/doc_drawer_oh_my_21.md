para [OpenAI Codex CLI](https://github.com/openai/codex).

## Novedades en v0.9.0 — Spark Initiative

Spark Initiative es la versión que refuerza la ruta nativa de exploración e inspección en OMX.

- **Harness nativo para `omx explore`** — ejecuta exploración de repositorio en modo solo lectura con una vía Rust más rápida y más estricta.
- **`omx sparkshell`** — superficie nativa para operadores, con resúmenes de salidas largas y captura explícita de paneles tmux.
- **Assets nativos multiplataforma** — la ruta de hidratación de `omx-explore-harness`, `omx-sparkshell` y `native-release-manifest.json` ya forma parte del pipeline de release.
- **CI/CD reforzado** — se añadió configuración explícita de Rust en el job `build`, además de `cargo fmt --check` y `cargo clippy -- -D warnings`.