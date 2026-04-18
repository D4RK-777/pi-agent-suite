настройка Rust toolchain в job `build`, а также `cargo fmt --check` и `cargo clippy -- -D warnings`.

См. также [release notes v0.9.0](./docs/release-notes-0.9.0.md) и [release body](./docs/release-body-0.9.0.md).

## Первая сессия

Внутри Codex:

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Из терминала:

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## Рекомендуемый рабочий процесс