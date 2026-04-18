oặc số worker)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # tùy chọn: tắt fallback thích ứng queue->resend
```

Lưu ý:
- Tham số khởi chạy worker vẫn được chia sẻ qua `OMX_TEAM_WORKER_LAUNCH_ARGS`.
- `OMX_TEAM_WORKER_CLI_MAP` ghi đè `OMX_TEAM_WORKER_CLI` cho lựa chọn theo worker.
- Gửi trigger sử dụng thử lại thích ứng theo mặc định (queue/submit, sau đó fallback an toàn clear-line+resend khi cần).
- Trong chế độ Claude worker, OMX khởi chạy worker dưới dạng `claude` thuần túy (không có tham số khởi chạy thêm) và bỏ qua các ghi đè rõ ràng `--model` / `--config` / `--effort` để Claude sử dụng `settings.json` mặc định.

## `omx setup` ghi những gì