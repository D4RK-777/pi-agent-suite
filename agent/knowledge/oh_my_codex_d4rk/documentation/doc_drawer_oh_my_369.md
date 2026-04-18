list for prompt changes

Before opening a PR that changes prompt text, confirm all of the following:

1. **Preserve the four core behaviors.** Your change should keep or strengthen compact output, low-risk follow-through, scoped overrides, and grounded tool use/verification.
2. **Keep role-specific wording role-specific.** The phrasing can differ by role, but the behavior should stay semantically aligned.
3. **Update scenario examples when behavior changes.** If you change how prompts handle `continue`, `make a PR`, or `merge if CI green`, update the prompt examples and the related tests.