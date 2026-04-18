# Ralph State Contract (Frozen)

## Canonical Ralph state schema

Ralph runtime state is stored at `.omx/state/{scope}/ralph-state.json` and MUST use this schema:

- `active: boolean` **(required)**
- `iteration: number` **(required while active)**
- `max_iterations: number` **(required while active)**
- `current_phase: string` **(required while active)**
- `started_at: ISO8601 string` **(required while active)**
- `completed_at?: ISO8601 string`
- Optional linkage fields: `linked_ultrawork`, `linked_ecomode`, `linked_mode`

Ralph remains a standalone mode. Other workflows may start Ralph later as an
explicit follow-up, but there is no built-in `omx team ralph ...` linked launch
path anymore.