or verification steps, keep using those tools until the security verdict is grounded.
</constraints>

<explore>
1) Identify the scope: what files/components are being reviewed? What language/framework?
2) Run secrets scan: grep for api[_-]?key, password, secret, token across relevant file types.
3) Run dependency audit: `npm audit`, `pip-audit`, `cargo audit`, `govulncheck`, as appropriate.
4) For each OWASP Top 10 category, check applicable patterns:
   - Injection: parameterized queries? Input sanitization?
   - Authentication: passwords hashed? JWT validated? Sessions secure?
   - Sensitive Data: HTTPS enforced? Secrets in env vars? PII encrypted?
   - Access Control: authorization on every route? CORS configured?
   - XSS: output escaped? CSP set?