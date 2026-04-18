ắt khi các tác vụ vẫn đang ở trạng thái `in_progress` trừ khi đang hủy bỏ.

### Team shutdown policy

Use `omx team shutdown <team-name>` after the team reaches a terminal state.
Team cleanup now follows one standalone path; legacy linked-Ralph shutdown handling is no longer a separate public workflow.

Chọn Worker CLI cho worker của đội:

```bash
OMX_TEAM_WORKER_CLI=auto    # mặc định; sử dụng claude khi worker --model chứa "claude"
OMX_TEAM_WORKER_CLI=codex   # ép buộc worker Codex CLI
OMX_TEAM_WORKER_CLI=claude  # ép buộc worker Claude CLI
OMX_TEAM_WORKER_CLI_MAP=codex,codex,claude,claude  # hỗn hợp CLI theo worker (độ dài=1 hoặc số worker)
OMX_TEAM_AUTO_INTERRUPT_RETRY=0  # tùy chọn: tắt fallback thích ứng queue->resend
```