# Heavy / Manual Stress Lane: `omx-explore` and `omx-sparkshell`

Date: **2026-03-11**
Scope: opt-in/manual stress scenarios that complement the deterministic CI lane in:
- `npm run test:explore`
- `npm run test:sparkshell`

This document covers the heavy/manual scenarios intentionally excluded from default CI because they depend on noisy operator environments, repeated invocation, or judgment-based evidence review.

## Preconditions

From the repository root:

```bash
npm run build:full
```

`npm run build:full` covers the TypeScript build plus the packaged explore harness and sparkshell native binary. Use `npm run build:explore` separately only if you specifically want the debug cargo build path during local investigation.