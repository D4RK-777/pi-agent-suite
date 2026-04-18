xpands into coordination-heavy lanes, hand off to `$team` and keep Ralph for verification continuity

### 4. **`$team`**
- **Input Artifact:** `.omx/specs/deep-interview-{slug}.md`
- **Invocation:** `$team <spec-path>`
- **Consumer Behavior:** Treat the spec as shared execution context for coordinated parallel work. Preserve the clarified intent, non-goals, decision boundaries, and acceptance criteria as common lane constraints.
- **Skipped / Already-Satisfied Stages:** Requirement clarification and early ambiguity reduction
- **Expected Output:** Coordinated multi-agent execution against the shared spec, with evidence that can later feed a Ralph verification pass when appropriate