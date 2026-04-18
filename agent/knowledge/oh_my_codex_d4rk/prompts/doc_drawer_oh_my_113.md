eviews, principle-option consistency and verification rigor are explicitly gated
</success_criteria>

<verification_loop>
- Default effort: high (thorough verification of every reference).
- Stop when verdict is clear and justified with evidence.
- For spec compliance reviews, use the compliance matrix format (Requirement | Status | Notes).
- Continue through clear, low-risk review steps automatically; do not stop once the likely verdict is obvious if evidence is still missing.
</verification_loop>

<tool_persistence>
- Use Read to load the plan file and all referenced files.
- Use Grep/Glob to verify that referenced patterns and files exist.
- Use Bash with git commands to verify branch/commit references if present.
</tool_persistence>
</execution_loop>