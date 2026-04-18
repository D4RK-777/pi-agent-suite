penai/codex) 的多智能体编排层。

## v0.9.0 新特性 — Spark Initiative

Spark Initiative 是一次强化 OMX 原生探索与检查路径的版本发布。

- **`omx explore` 原生 harness** —— 通过 Rust 原生 harness 更快、更严格地执行只读仓库探索。
- **`omx sparkshell`** —— 面向操作者的原生检查界面，支持长输出摘要与 tmux pane 捕获。
- **跨平台原生发布资产** —— `omx-explore-harness`、`omx-sparkshell` 与 `native-release-manifest.json` 的 hydration 路径现已纳入发布流水线。
- **增强的 CI/CD** —— 为 `build` job 增加显式 Rust toolchain 设置，并加入 `cargo fmt --check` 与 `cargo clippy -- -D warnings`。

详情请参阅 [v0.9.0 发布说明](./docs/release-notes-0.9.0.md) 和 [发布正文](./docs/release-body-0.9.0.md)。

## 首次会话

在 Codex 内部：

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

从终端：