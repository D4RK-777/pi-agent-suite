factor"
omx team status <team-name>
omx team shutdown <team-name>
```

## Quy trình được khuyến nghị

1. `$deep-interview` — khi phạm vi hoặc ranh giới vẫn chưa rõ.
2. `$ralplan` — để biến phạm vi đã làm rõ thành kế hoạch kiến trúc và triển khai đã được chốt.
3. `$team` hoặc `$ralph` — dùng `$team` cho thực thi song song có phối hợp, hoặc `$ralph` cho vòng lặp bền bỉ để hoàn tất/xác minh với một chủ sở hữu duy nhất.

## Mô hình cốt lõi

OMX cài đặt và kết nối các lớp sau:

```text
User
  -> Codex CLI
    -> AGENTS.md (bộ não điều phối)
    -> ~/.codex/prompts/*.md (danh mục prompt tác nhân)
    -> ~/.codex/skills/*/SKILL.md (danh mục skill)
    -> ~/.codex/config.toml (tính năng, thông báo, MCP)
    -> .omx/ (trạng thái runtime, bộ nhớ, kế hoạch, nhật ký)
```

## Các lệnh chính