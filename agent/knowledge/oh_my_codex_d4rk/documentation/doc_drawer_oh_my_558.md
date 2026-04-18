nts-overlay.ts` | Summarize active modes from scope-preferred mode files (session overrides root). |
| `src/cli/index.ts` (`status`/`cancel`) | Status and cancellation operate on scope-preferred mode files; cancellation does not mutate unrelated sessions. |

## Canonical PRD/progress sources

- Canonical PRD: `.omx/plans/prd-{slug}.md`
- Canonical progress ledger: `.omx/state/{scope}/ralph-progress.json`
- Legacy compatibility migration:
  - `.omx/prd.json` migrates one-way to canonical PRD markdown when no canonical PRD exists.
  - `.omx/progress.txt` migrates one-way to canonical `ralph-progress.json` when no canonical ledger exists.
  - Legacy files remain read-only compatibility artifacts for one release cycle.