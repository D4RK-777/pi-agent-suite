e-dependent.

Delegates to the `security-reviewer` agent (THOROUGH tier) for deep security analysis:

1. **OWASP Top 10 Scan**
   - A01: Broken Access Control
   - A02: Cryptographic Failures
   - A03: Injection (SQL, NoSQL, Command, XSS)
   - A04: Insecure Design
   - A05: Security Misconfiguration
   - A06: Vulnerable and Outdated Components
   - A07: Identification and Authentication Failures
   - A08: Software and Data Integrity Failures
   - A09: Security Logging and Monitoring Failures
   - A10: Server-Side Request Forgery (SSRF)

2. **Secrets Detection**
   - Hardcoded API keys
   - Passwords in source code
   - Private keys in repo
   - Tokens and credentials
   - Connection strings with secrets