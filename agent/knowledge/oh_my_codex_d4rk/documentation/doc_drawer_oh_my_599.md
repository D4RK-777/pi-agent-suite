x team ralph ...` usage now fails with a clear deprecation error instead of being tolerated silently

This matches the intended product model: team can own coordinated execution and verification itself, while Ralph remains an independent persistence loop that a leader or separate worker may choose to run later.

## Why
The old team↔Ralph linkage had become bloated orchestration glue:
- bridge code between team and Ralph mode state
- linked lifecycle/profile branching
- notify-hook terminal sync behavior
- cleanup/shutdown special-casing
- extra tests and documentation for behavior that should be two separate tools

That coupling made the runtime harder to reason about without providing enough value to justify the complexity.