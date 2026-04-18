urrent status

**Status:** the PRD/test-spec behavior is not implemented on the reviewed branch yet.

Current code still reflects the older guided-init flow:

- `omx autoresearch` with no args enters `guidedAutoresearchSetup()` and immediately asks for a raw evaluator command.
- bare `init` still routes into that same guided path instead of an explicit novice compatibility bridge.
- there is no autoresearch-specific intake module, no canonical `.omx/specs/deep-interview-autoresearch-{slug}.md` artifact, and no confirm/refine launch gate.
- launch still happens immediately after guided setup returns.
- README/help/contract docs still describe the thin-supervisor runtime, but not the new novice deep-interview intake surface from this PRD.

## Evidence observed