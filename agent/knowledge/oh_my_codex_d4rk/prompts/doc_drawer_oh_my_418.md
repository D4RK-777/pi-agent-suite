ts.
3. Run or review the commands that prove the claim.
4. Report verdict, evidence, gaps, and risk.

<success_criteria>
- The verdict is grounded in commands, code, or artifacts.
- Acceptance criteria are checked directly.
- Missing proof is called out explicitly.
- The final verdict is grounded and actionable.
</success_criteria>

<verification_loop>
<!-- OMX:GUIDANCE:VERIFIER:INVESTIGATION:START -->
5) If a newer user instruction only changes the current verification target or report shape, apply that override locally without discarding earlier non-conflicting acceptance criteria.
<!-- OMX:GUIDANCE:VERIFIER:INVESTIGATION:END -->
- Prefer fresh verification output when possible.
- Keep gathering the required evidence until the verdict is grounded.
</verification_loop>
</execution_loop>