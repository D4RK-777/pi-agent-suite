ntime.
Mở rộng hành vi Codex, nhưng không thay thế/bỏ qua các chính sách hệ thống cốt lõi của Codex.

Điều khiển:

```bash
OMX_BYPASS_DEFAULT_SYSTEM_PROMPT=0 omx     # tắt tiêm AGENTS.md
OMX_MODEL_INSTRUCTIONS_FILE=/path/to/instructions.md omx
```

## Chế độ đội

Sử dụng chế độ đội cho công việc lớn được hưởng lợi từ worker song song.

Vòng đời:

```text
start -> assign scoped lanes -> monitor -> verify terminal tasks -> shutdown
```

Các lệnh vận hành:

```bash
omx team <args>
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

Quy tắc quan trọng: không tắt khi các tác vụ vẫn đang ở trạng thái `in_progress` trừ khi đang hủy bỏ.

### Team shutdown policy