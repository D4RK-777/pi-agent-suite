rc/team/role-router.ts` as a raw role-prompt loader unless a minimal plumbing change is unavoidable.

Primary implementation surfaces for this seam:

| Responsibility | Primary sources |
|---|---|
| shared inner prompt composition | `src/agents/native-config.ts`, `src/agents/__tests__/native-config.test.ts` |
| team runtime/scaling plumbing | `src/team/runtime.ts`, `src/team/scaling.ts`, associated runtime/scaling tests |
| outer wrapper boundary | `src/team/worker-bootstrap.ts`, `src/team/__tests__/worker-bootstrap.test.ts` |


## What this contract is — and is not

This contract is about **how OMX prompts should behave**.
It is not the same thing as OMX's routing metadata.