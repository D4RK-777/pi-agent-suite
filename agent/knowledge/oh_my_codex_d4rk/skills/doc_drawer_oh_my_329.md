] Access control enforced on all protected resources
- [ ] No authentication bypass vulnerabilities

### Input Validation
- [ ] All user inputs validated and sanitized
- [ ] SQL queries use parameterization (no string concatenation)
- [ ] NoSQL queries prevent injection
- [ ] File uploads validated (type, size, content)
- [ ] URLs validated to prevent SSRF

### Output Encoding
- [ ] HTML output escaped to prevent XSS
- [ ] JSON responses properly encoded
- [ ] No user data in error messages
- [ ] Content-Security-Policy headers set

### Secrets Management
- [ ] No hardcoded API keys
- [ ] No passwords in source code
- [ ] No private keys in repo
- [ ] Environment variables used for secrets
- [ ] Secrets not logged or exposed in errors