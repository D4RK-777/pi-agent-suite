s`, `omx-sparkshell` et `native-release-manifest.json` fait désormais partie du pipeline de release.
- **CI/CD renforcé** — ajoute une configuration explicite de la toolchain Rust dans le job `build`, ainsi que `cargo fmt --check` et `cargo clippy -- -D warnings`.

Voir aussi les [notes de version v0.9.0](./docs/release-notes-0.9.0.md) et le [corps de release](./docs/release-body-0.9.0.md).

## Première session

Dans Codex :

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Depuis le terminal :

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```