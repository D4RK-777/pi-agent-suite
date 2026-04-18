gerously-bypass-approvals-and-sandbox`.
Chỉ sử dụng trong môi trường sandbox tin cậy hoặc bên ngoài.

### Chính sách workingDirectory MCP (tăng cường tùy chọn)

Theo mặc định, các công cụ MCP state/memory/trace chấp nhận `workingDirectory` do người gọi cung cấp.
Để hạn chế điều này, đặt danh sách gốc được phép:

```bash
export OMX_MCP_WORKDIR_ROOTS="/path/to/project:/path/to/another-root"
```

Khi được đặt, các giá trị `workingDirectory` ngoài các gốc này sẽ bị từ chối.

## Kiểm soát Prompt Codex-First

Theo mặc định, OMX tiêm:

```text
-c model_instructions_file="<cwd>/AGENTS.md"
```

Điều này kết hợp `AGENTS.md` trong `CODEX_HOME` với `AGENTS.md` của dự án (nếu có), rồi thêm lớp phủ runtime.
Mở rộng hành vi Codex, nhưng không thay thế/bỏ qua các chính sách hệ thống cốt lõi của Codex.