g Recommendation
**Suggested bump**: [MAJOR / MINOR / PATCH]
**Rationale**: [why]
</output_contract>

<anti_patterns>
- Missing breaking changes: Approving a parameter rename as non-breaking. Renaming a public API parameter is a breaking change that requires a major version bump.
- No migration path: Identifying a breaking change without telling callers how to update. Always provide migration guidance.
- Ignoring error contracts: Reviewing parameter types but skipping error documentation. Callers need to know what errors to expect.
- Internal focus: Reviewing implementation details instead of the public contract. Stay at the API surface.
- No history check: Reviewing API changes without understanding the previous shape. Always check git history.
</anti_patterns>