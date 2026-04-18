penai/codex) 的多智能體編排層。

## v0.9.0 新功能 — Spark Initiative

Spark Initiative 是一個強化 OMX 原生探索與檢查路徑的版本發布。

- **`omx explore` 原生 harness** —— 以 Rust 原生 harness 更快且更嚴格地執行唯讀儲存庫探索。
- **`omx sparkshell`** —— 面向操作員的原生檢查介面，支援長輸出摘要與 tmux pane 擷取。
- **跨平台原生釋出資產** —— `omx-explore-harness`、`omx-sparkshell` 與 `native-release-manifest.json` 的 hydration 路徑已納入釋出流程。
- **強化的 CI/CD** —— 在 `build` job 中加入明確的 Rust toolchain 設定，並新增 `cargo fmt --check` 與 `cargo clippy -- -D warnings`。

詳細內容請參閱 [v0.9.0 版本說明](./docs/release-notes-0.9.0.md) 與 [釋出正文](./docs/release-body-0.9.0.md)。

## 首次會話

在 Codex 內部：

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

從終端機：