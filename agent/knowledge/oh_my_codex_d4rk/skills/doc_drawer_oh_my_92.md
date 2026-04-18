(MUST)

When cancellation targets Ralph state in a scope, completion requires all of the following:

1. Ralph state is terminal in that same scope: `active=false`, `current_phase='cancelled'` (or linked terminal phase), and `completed_at` is set.
2. Linked Ultrawork/Ecomode in the same scope is also terminal/non-active.
4. Unrelated sessions are untouched.

## Force Clear All

Use `--force` or `--all` when you need to erase every session plus legacy artifacts, e.g., to reset the workspace entirely.

```
/cancel --force
```

```
/cancel --all
```