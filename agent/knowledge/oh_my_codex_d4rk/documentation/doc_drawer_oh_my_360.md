structions.

### 4. Persistent tool use, dependency-aware sequencing, and evidence-backed completion

Contributors should preserve the rule that prompts keep using tools when correctness depends on retrieval, diagnostics, tests, or verification. OMX should not stop at a plausible answer if proof is still missing.

Representative locations:

| Surface | Evidence |
|---|---|
| `AGENTS.md` | `AGENTS.md:32`, `AGENTS.md:288`, `AGENTS.md:297-301`, `AGENTS.md:307-308` |
| `templates/AGENTS.md` | `templates/AGENTS.md:32`, `templates/AGENTS.md:288`, `templates/AGENTS.md:297-301`, `templates/AGENTS.md:307-308` |
| `src/config/generator.ts` | `src/config/generator.ts:77` |