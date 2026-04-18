nner.md:118-126` |
| `prompts/verifier.md` | `prompts/verifier.md:38`, `prompts/verifier.md:91-99` |
| contract tests | `src/hooks/__tests__/prompt-guidance-contract.test.ts:34-36`, `src/hooks/__tests__/prompt-guidance-wave-two.test.ts:27-30`, `src/hooks/__tests__/prompt-guidance-catalog.test.ts:35-39` |

Example prompt text:

> - Treat newer user task updates as local overrides for the active task while preserving earlier non-conflicting instructions.
>
> 4. If a newer user message updates only the current step or output shape, apply that override locally without discarding earlier non-conflicting instructions.

### 4. Persistent tool use, dependency-aware sequencing, and evidence-backed completion