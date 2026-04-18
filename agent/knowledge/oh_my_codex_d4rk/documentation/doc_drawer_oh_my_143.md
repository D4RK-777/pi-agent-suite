om/openai/codex) için çok ajanlı orkestrasyon katmanı.

## v0.9.0'daki Yenilikler — Spark Initiative

Spark Initiative, OMX içindeki native keşif ve inceleme yolunu güçlendiren sürümdür.

- **`omx explore` için native harness** — salt okunur depo keşfini Rust tabanlı daha hızlı ve daha sıkı bir yol üzerinden çalıştırır.
- **`omx sparkshell`** — uzun çıktıları özetleyen ve açık tmux pane yakalama desteği veren operatör odaklı native inceleme yüzeyidir.
- **Çapraz platform native release varlıkları** — `omx-explore-harness`, `omx-sparkshell` ve `native-release-manifest.json` için hydration yolu artık release pipeline'ın parçasıdır.
- **Güçlendirilmiş CI/CD** — `build` job'ına açık Rust toolchain kurulumu ile birlikte `cargo fmt --check` ve `cargo clippy -- -D warnings` eklendi.