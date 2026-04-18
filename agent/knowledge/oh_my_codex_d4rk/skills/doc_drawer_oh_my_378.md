egration tests"
omx team "ship end-to-end fix with verification"
```

### Team-first launch contract

`omx team ...` is now the canonical launch path for coordinated execution.
Team mode should carry its own parallel delivery + verification lanes without
requiring a separate linked Ralph launch up front.

- **Canonical launch:** use plain `omx team ...` / `$team ...` for coordinated workers.
- **Verification ownership:** keep one lane focused on tests, regression coverage, and evidence before shutdown.
- **Escalation:** start a separate `omx ralph ...` / `$ralph ...` only when a later manual follow-up still needs a persistent single-owner fix/verification loop.