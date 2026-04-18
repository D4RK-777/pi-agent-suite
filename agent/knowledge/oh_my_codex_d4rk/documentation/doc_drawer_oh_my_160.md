ho [OpenAI Codex CLI](https://github.com/openai/codex).

## Điểm mới trong v0.9.0 — Spark Initiative

Spark Initiative là bản phát hành tăng cường đường đi native cho khám phá và kiểm tra trong OMX.

- **Native harness cho `omx explore`** — chạy khám phá kho mã chỉ đọc nhanh hơn và chặt chẽ hơn bằng harness Rust.
- **`omx sparkshell`** — bề mặt kiểm tra native cho operator, hỗ trợ tóm tắt đầu ra dài và chụp tmux pane.
- **Tài sản phát hành native đa nền tảng** — đường hydration cho `omx-explore-harness`, `omx-sparkshell` và `native-release-manifest.json` nay đã nằm trong pipeline phát hành.
- **CI/CD được tăng cường** — thêm thiết lập Rust toolchain tường minh cho `build` job cùng với `cargo fmt --check` và `cargo clippy -- -D warnings`.