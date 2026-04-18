` (hoặc `CODEX_HOME/AGENTS.md` nếu đã ghi đè) với `./AGENTS.md` của dự án, rồi thêm lớp phủ runtime.
- Các tệp `AGENTS.md` hiện có sẽ không bao giờ bị ghi đè âm thầm: ở TTY tương tác, setup hỏi trước khi thay thế; ở chế độ không tương tác, việc thay thế sẽ bị bỏ qua trừ khi dùng `--force` (kiểm tra an toàn phiên hoạt động vẫn áp dụng).
- Cập nhật `config.toml` (cho cả hai phạm vi):
  - `notify = ["node", "..."]`
  - `model_reasoning_effort = "high"`
  - `developer_instructions = "..."`
  - `[features] multi_agent = true, child_agents_md = true`
  - Mục máy chủ MCP (`omx_state`, `omx_memory`, `omx_code_intel`, `omx_trace`)
  - `[tui] status_line`
- `AGENTS.md` theo phạm vi
- Thư mục `.omx/` runtime và cấu hình HUD

## Tác nhân và skill