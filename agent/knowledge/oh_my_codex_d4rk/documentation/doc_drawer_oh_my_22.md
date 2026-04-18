explícita de Rust en el job `build`, además de `cargo fmt --check` y `cargo clippy -- -D warnings`.

Consulta también las [notas de lanzamiento v0.9.0](./docs/release-notes-0.9.0.md) y el [release body](./docs/release-body-0.9.0.md).

## Primera sesión

Dentro de Codex:

```text
$deep-interview "clarify the auth change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Desde la terminal:

```bash
omx team 4:executor "parallelize a multi-module refactor"
omx team status <team-name>
omx team shutdown <team-name>
```

## Flujo recomendado