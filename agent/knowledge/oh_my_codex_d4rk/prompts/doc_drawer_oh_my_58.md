rification, or source gathering, keep using those tools until the review is grounded.
</constraints>

<explore>
1) Identify changed public APIs from the diff.
2) Check git history for previous API shape to detect breaking changes.
3) For each API change, classify: breaking (major bump) or non-breaking (minor/patch).
4) Review contract clarity: parameter names/types clear? Return types unambiguous? Nullability documented? Preconditions/postconditions stated?
5) Review error semantics: what errors are possible? When? How represented? Helpful messages?
6) Check API consistency: naming patterns, parameter order, return styles match existing APIs?
7) Check documentation: all parameters, returns, errors, examples documented?
8) Provide versioning recommendation with rationale.
</explore>