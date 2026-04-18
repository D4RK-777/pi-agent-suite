tier="THOROUGH",
  prompt="SECURITY REVIEW TASK

Conduct comprehensive security audit of codebase.

Scope: [specific files or entire codebase]

Security Checklist:
1. OWASP Top 10 scan
2. Hardcoded secrets detection
3. Input validation review
4. Authentication/authorization review
5. Dependency vulnerability scan (npm audit)

Output: Security review report with:
- Summary of findings by severity (CRITICAL, HIGH, MEDIUM, LOW)
- Specific file:line locations
- CVE references where applicable
- Remediation guidance for each issue
- Overall security posture assessment"
)
```

## External Model Consultation (Preferred)

The security-reviewer agent SHOULD consult Codex for cross-validation.