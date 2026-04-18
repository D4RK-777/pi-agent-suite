ble. Do not assume LSP, ast-grep, MCP, web search, images, or structured Read/Glob tools exist here.
- Keep file/path arguments inside the current repository. Do not intentionally inspect `..` paths or unrelated absolute paths.
- This harness is for simple read-only repository lookup tasks after `omx explore` has already been selected; it is not the richer normal path.
- Prefer narrow, concrete lookup goals; if the ask is broad, multi-part, or needs synthesis beyond simple repository inspection, report the limitation so the caller can fall back to the richer normal path.
- Prefer `omx explore --prompt ...` for short one-off asks and `omx explore --prompt-file ...` when the brief is longer or reusable.