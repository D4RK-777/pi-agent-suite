# Bug Triage

## Purpose

Handle broken behavior methodically without looping.

## Use When

- the user reports a bug
- a failure repeats after attempted fixes

## Steps

1. Re-state the failing behavior precisely.
2. Find the likely owning files or runtime surface.
3. Attempt the first strategy and track strikes by strategy.
4. Pivot using `adaptive-error-recovery` when the same pattern repeats.
5. End with either a fix, a narrowed root cause, or a clean escalation.

## Output

- failure summary
- root cause or best current hypothesis
- next concrete action
