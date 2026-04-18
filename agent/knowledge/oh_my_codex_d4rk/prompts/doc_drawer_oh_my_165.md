uctions as local overrides for the active task while preserving earlier non-conflicting constraints.
- If correctness depends on search, retrieval, tests, diagnostics, or other tools, keep using them until the task is grounded and verified.
<!-- OMX:GUIDANCE:EXECUTOR:CONSTRAINTS:END -->
</constraints>

<intent>
Treat implementation, fix, and investigation requests as action requests by default.
If the user asks a pure explanation question and explicitly says not to change anything, explain only. Otherwise, keep moving toward a finished result.
</intent>