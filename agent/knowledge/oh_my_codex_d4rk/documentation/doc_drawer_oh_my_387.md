ed. |
| `templates/AGENTS.md` | 7 | 7 | Header/tone normalized; still intended as a template copy. |

### Unified Guidance Schema Follow-Up (AGENTS + Runtime/Worker Alignment)

- Added canonical schema document: `docs/guidance-schema.md`.
- Added explicit schema-contract sections to:
  - `AGENTS.md`
  - `templates/AGENTS.md`
- Normalized worker task guidance in `AGENTS.md` runtime worker overlay:
  - file path now uses `tasks/task-<id>.json`
  - API id rule now explicitly requires bare id `task_id: "<id>"` (never `"task-<id>"`).
- Marker contracts remain unchanged:
  - `<!-- OMX:RUNTIME:START --> ... <!-- OMX:RUNTIME:END -->`
  - `<!-- OMX:TEAM:WORKER:START --> ... <!-- OMX:TEAM:WORKER:END -->`