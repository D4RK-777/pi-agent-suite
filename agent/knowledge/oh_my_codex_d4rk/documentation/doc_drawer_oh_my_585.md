e already supports worker roles, mixed CLIs, runtime state, and inspectable team lifecycle commands.

## Alternatives considered
- Keep the pattern implicit in docs only. This helps discovery, but still leaves users to translate plans into worker lanes manually.
- Fold everything into `autopilot`. Useful for default automation, but weaker for users who want direct control over planning, staffing, and verification.

## Additional context
Expected user outcome: a user runs `ralplan`, sees a plan that is already shaped for team execution, launches `team` with less guesswork, and uses `ralph` to keep the workflow honest until evidence-backed completion.