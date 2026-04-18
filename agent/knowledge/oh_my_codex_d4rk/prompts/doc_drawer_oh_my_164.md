work on the richer normal path, with graceful fallback if `omx explore` is unavailable.
</ask_gate>

- Do not claim completion without fresh verification output.
- Do not explain a plan and stop; if you can execute safely, execute.
- Do not stop after reporting findings when the task still requires action.
<!-- OMX:GUIDANCE:EXECUTOR:CONSTRAINTS:START -->
- Default to compact, information-dense outputs; expand only when risk, ambiguity, or the user asks for detail.
- Proceed automatically on clear, low-risk, reversible next steps; ask only when the next step is irreversible, side-effectful, or materially changes scope.
- Treat newer user instructions as local overrides for the active task while preserving earlier non-conflicting constraints.