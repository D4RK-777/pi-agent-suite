오케스트레이션 레이어.

## v0.9.0 새로운 기능 — Spark Initiative

Spark Initiative는 OMX의 네이티브 탐색/검사 경로를 강화한 릴리스입니다.

- **`omx explore` 네이티브 하네스** — 읽기 전용 저장소 탐색을 Rust 기반 하네스로 더 빠르고 엄격하게 실행합니다.
- **`omx sparkshell`** — 긴 출력을 요약하고 tmux pane 캡처를 지원하는 운영자용 네이티브 검사 표면입니다.
- **크로스 플랫폼 네이티브 릴리스 자산** — `omx-explore-harness`, `omx-sparkshell`, `native-release-manifest.json` 기반 hydration 경로가 릴리스 파이프라인에 포함됩니다.
- **강화된 CI/CD** — `build` job의 명시적 Rust toolchain 설정, `cargo fmt --check`, `cargo clippy -- -D warnings`가 추가되었습니다.

자세한 내용은 [v0.9.0 릴리스 노트](./docs/release-notes-0.9.0.md) 및 [릴리스 본문](./docs/release-body-0.9.0.md)을 참고하세요.

## 첫 번째 세션

Codex 내부에서: