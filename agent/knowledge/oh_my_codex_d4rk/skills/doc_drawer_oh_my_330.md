s in repo
- [ ] Environment variables used for secrets
- [ ] Secrets not logged or exposed in errors

### Cryptography
- [ ] Strong algorithms used (AES-256, RSA-2048+)
- [ ] Proper key management
- [ ] Random number generation cryptographically secure
- [ ] TLS/HTTPS enforced for sensitive data

### Dependencies
- [ ] No known vulnerabilities in dependencies
- [ ] Dependencies up to date
- [ ] No CRITICAL or HIGH CVEs
- [ ] Dependency sources verified

## Severity Definitions

**CRITICAL** - Exploitable vulnerability with severe impact (data breach, RCE, credential theft)
**HIGH** - Vulnerability requiring specific conditions but serious impact
**MEDIUM** - Security weakness with limited impact or difficult exploitation
**LOW** - Best practice violation or minor security concern