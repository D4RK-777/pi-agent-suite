mp directly into fixing or rewriting code.

## Good entry cases

Use `$analyze` when the problem is:

- ambiguous or causal
- evidence-heavy
- best answered by exploring competing explanations
- requires reading multiple files and reasoning across them

Examples:
- runtime bugs and regressions
- performance / latency / resource behavior
- architecture / premortem / postmortem analysis
- config / routing / orchestration behavior explanation
- dependency analysis or impact assessment
- "given this output, trace back the likely causes"

## Do not use when