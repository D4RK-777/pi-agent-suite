-harness`, `omx-sparkshell` e `native-release-manifest.json` ora fa parte della pipeline di release.
- **CI/CD rafforzato** — aggiunge la configurazione esplicita della toolchain Rust nel job `build`, oltre a `cargo fmt --check` e `cargo clippy -- -D warnings`.

Vedi anche le [note di rilascio v0.9.0](./docs/release-notes-0.9.0.md) e il [testo della release](./docs/release-body-0.9.0.md).

## Prima sessione

All'interno di Codex:

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Dal terminale:

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```