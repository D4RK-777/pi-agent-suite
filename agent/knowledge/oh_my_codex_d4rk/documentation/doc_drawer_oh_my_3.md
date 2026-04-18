e-harness`, `omx-sparkshell` und `native-release-manifest.json` ist jetzt Teil der Release-Pipeline.
- **Gehärtetes CI/CD** — ergänzt ein explizites Rust-Toolchain-Setup im `build`-Job sowie `cargo fmt --check` und `cargo clippy -- -D warnings`.

Siehe auch die [Release Notes zu v0.9.0](./docs/release-notes-0.9.0.md) und den [Release-Text](./docs/release-body-0.9.0.md).

## Erste Sitzung

Innerhalb von Codex:

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Vom Terminal:

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## Empfohlener Workflow