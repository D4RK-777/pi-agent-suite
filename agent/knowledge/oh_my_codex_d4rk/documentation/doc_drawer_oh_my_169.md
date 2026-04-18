` / `--config` / `--effort` để Claude sử dụng `settings.json` mặc định.

## `omx setup` ghi những gì

- `.omx/setup-scope.json` (phạm vi cài đặt được lưu trữ)
- Cài đặt phụ thuộc phạm vi:
  - `user`: `~/.codex/prompts/`, `~/.codex/skills/`, `~/.codex/config.toml`, `~/.omx/agents/`, `~/.codex/AGENTS.md`
  - `project`: `./.codex/prompts/`, `./.codex/skills/`, `./.codex/config.toml`, `./.omx/agents/`, `./AGENTS.md`
- Hành vi khởi chạy: nếu phạm vi được lưu trữ là `project`, khởi chạy `omx` tự động sử dụng `CODEX_HOME=./.codex` (trừ khi `CODEX_HOME` đã được đặt).
- Hướng dẫn khởi chạy sẽ kết hợp `~/.codex/AGENTS.md` (hoặc `CODEX_HOME/AGENTS.md` nếu đã ghi đè) với `./AGENTS.md` của dự án, rồi thêm lớp phủ runtime.