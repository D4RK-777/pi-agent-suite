LI

**Prompt**
> I want to build a task management CLI.

**Expected Phase 1 flow after this change**

1. **Round 1**
   - Assistant: asks why the user wants the CLI and what failure in the current workflow triggered the request.
2. **Round 2**
   - User: explains they keep forgetting ad-hoc tasks across repos.
   - Assistant: follows the same seam and asks which assumption makes a CLI better than a calendar/reminder flow.
3. **Round 3**
   - User: says they need repo-local context and quick capture.
   - Assistant: asks what should stay explicitly out of scope for the first version.
4. **Round 4**
   - User: says no sync, no multi-user, no GUI.
   - Assistant: asks which tradeoff is unacceptable if fast capture conflicts with strict task structure.