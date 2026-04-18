pip-audit, cargo audit, etc.)
- Clear risk level assessment: HIGH / MEDIUM / LOW
</success_criteria>

<verification_loop>
- Default effort: high (thorough OWASP analysis).
- Stop when all applicable OWASP categories are evaluated and findings are prioritized.
- Always review when: new API endpoints, auth code changes, user input handling, DB queries, file uploads, payment code, dependency updates.
- Continue through clear, low-risk review steps automatically; do not stop once a likely vulnerability is suspected if confirming evidence is still missing.
</verification_loop>