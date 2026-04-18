# PR Draft: Deprecate `omx team ralph` and keep team standalone

## Target branch
`dev`

## Title
Deprecate `omx team ralph` and remove linked team↔Ralph lifecycle machinery

## Summary
This PR removes the built-in linked `omx team ralph` workflow and restores a clean separation between `team` and `ralph`.

After this change:
- `omx team ...` / `$team ...` is the only supported team launch path
- `omx ralph ...` / `$ralph ...` remains available as a separate, explicit follow-up
- team no longer creates, syncs, or depends on linked Ralph state
- legacy `omx team ralph ...` usage now fails with a clear deprecation error instead of being tolerated silently