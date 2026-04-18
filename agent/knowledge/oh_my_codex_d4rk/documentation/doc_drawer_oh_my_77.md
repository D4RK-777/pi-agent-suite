オーケストレーションレイヤー。

## v0.9.0 の新機能 — Spark Initiative

Spark Initiative は、OMX のネイティブ探索・検査経路を強化するリリースです。

- **`omx explore` ネイティブハーネス** — 読み取り専用のリポジトリ探索を Rust ベースのハーネスで高速かつ厳格に実行します。
- **`omx sparkshell`** — 長い出力の要約と tmux pane キャプチャを行う、オペレーター向けのネイティブ検査サーフェスです。
- **クロスプラットフォームのネイティブリリース資産** — `omx-explore-harness`、`omx-sparkshell`、`native-release-manifest.json` を中心とした hydration 経路がリリースパイプラインに組み込まれました。
- **強化された CI/CD** — `build` ジョブでの明示的な Rust toolchain セットアップ、`cargo fmt --check`、`cargo clippy -- -D warnings` を追加しました。

詳細は [v0.9.0 リリースノート](./docs/release-notes-0.9.0.md) と [リリース本文](./docs/release-body-0.9.0.md) を参照してください。

## 最初のセッション

Codex内部で：