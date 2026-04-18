s|validate|test (quy trình mở rộng plugin)
omx hud ...        # --watch|--json|--preset
omx help
```

## Mở rộng Hooks (Bề mặt bổ sung)

OMX hiện bao gồm `omx hooks` cho scaffolding và xác thực plugin.

- `omx tmux-hook` vẫn được hỗ trợ và không thay đổi.
- `omx hooks` là bổ sung và không thay thế quy trình tmux-hook.
- Tệp plugin nằm tại `.omx/hooks/*.mjs`.
- Plugin tắt theo mặc định; kích hoạt bằng `OMX_HOOK_PLUGINS=1`.

Xem `docs/hooks-extension.md` cho quy trình mở rộng đầy đủ và mô hình sự kiện.

## Cờ khởi chạy

```bash
--yolo
--high
--xhigh
--madmax
--force
--dry-run
--verbose
--scope <user|project>  # chỉ dành cho setup
```

`--madmax` ánh xạ đến Codex `--dangerously-bypass-approvals-and-sandbox`.
Chỉ sử dụng trong môi trường sandbox tin cậy hoặc bên ngoài.