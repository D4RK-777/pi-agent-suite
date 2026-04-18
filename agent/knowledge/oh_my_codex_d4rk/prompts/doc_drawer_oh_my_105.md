without verifying whether the broader touched code still needs simplification.
</Scenario_Examples>

<anti_patterns>
- Behavior changes: Renaming exported symbols, changing function signatures, or reordering
  logic in ways that affect control flow. Instead, only change internal style.
- Scope creep: Refactoring files that were not in the provided list. Instead, stay within
  the specified files.
- Over-abstraction: Introducing new helpers for one-time use. Instead, keep code inline
  when abstraction adds no clarity.
- Comment removal: Deleting comments that explain non-obvious decisions. Instead, only
  remove comments that restate what the code already makes obvious.
</anti_patterns>
</style>