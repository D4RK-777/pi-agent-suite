`merge if CI green`, and you reply `Should I check CI?` instead of checking it.
</scenario_handling>

<lore_commits>
When committing code, follow the Lore commit protocol:
- Intent line first: describe *why*, not *what* (the diff shows what).
- Add git trailers after a blank line for decision context:
  - `Constraint:` — external forces that shaped the decision
  - `Rejected: <alternative> | <reason>` — dead ends future agents shouldn't revisit
  - `Directive:` — warnings for future modifiers ("do not X without Y")
  - `Confidence:` — low/medium/high
  - `Scope-risk:` — narrow/moderate/broad
  - `Tested:` / `Not-tested:` — verification coverage and gaps
- Use only the trailers that add value; all are optional.