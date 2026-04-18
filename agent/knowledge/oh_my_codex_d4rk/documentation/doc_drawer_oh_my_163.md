thông báo, MCP)
    -> .omx/ (trạng thái runtime, bộ nhớ, kế hoạch, nhật ký)
```

## Các lệnh chính

```bash
omx                # Khởi chạy Codex (+ HUD trong tmux khi có sẵn)
omx setup          # Cài đặt prompt/skill/config theo phạm vi + .omx của dự án + AGENTS.md theo phạm vi
omx doctor         # Chẩn đoán cài đặt/runtime
omx doctor --team  # Chẩn đoán Team/swarm
omx team ...       # Khởi động/trạng thái/tiếp tục/tắt worker tmux của đội
omx status         # Hiển thị các chế độ đang hoạt động
omx cancel         # Hủy các chế độ thực thi đang hoạt động
omx reasoning <mode> # low|medium|high|xhigh
omx tmux-hook ...  # init|status|validate|test
omx hooks ...      # init|status|validate|test (quy trình mở rộng plugin)
omx hud ...        # --watch|--json|--preset
omx help
```