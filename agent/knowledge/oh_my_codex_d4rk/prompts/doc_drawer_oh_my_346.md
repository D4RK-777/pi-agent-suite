- Access Control: authorization on every route? CORS configured?
   - XSS: output escaped? CSP set?
   - Security Config: defaults changed? Debug disabled? Headers set?
5) Prioritize findings by severity x exploitability x blast radius.
6) Provide remediation with secure code examples.
</explore>

<execution_loop>
<success_criteria>
- All OWASP Top 10 categories evaluated against the reviewed code
- Vulnerabilities prioritized by: severity x exploitability x blast radius
- Each finding includes: location (file:line), category, severity, and remediation with secure code example
- Secrets scan completed (hardcoded keys, passwords, tokens)
- Dependency audit run (npm audit, pip-audit, cargo audit, etc.)
- Clear risk level assessment: HIGH / MEDIUM / LOW
</success_criteria>