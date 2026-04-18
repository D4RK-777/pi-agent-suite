rompt**
> I need to change auth in this brownfield app.

**Expected Phase 1 flow after this change**

1. **Preflight**
   - Assistant gathers codebase evidence first.
2. **Round 1**
   - Assistant: asks an evidence-backed confirmation question such as “I found token-refresh handling in `src/auth/session.ts`. Should this change follow that pattern or replace it?”
3. **Round 2**
   - User: says replace it because refresh loops hide the real failure.
   - Assistant: asks what evidence shows the loop is the root cause rather than a symptom.
4. **Round 3**
   - User: says refresh retries hide upstream 401 churn.
   - Assistant: asks what decision boundary OMX may take without confirmation if the fix requires touching both middleware and session storage.
5. **Round 4**