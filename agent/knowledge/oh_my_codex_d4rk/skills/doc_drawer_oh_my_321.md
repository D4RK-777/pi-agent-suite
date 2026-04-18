urce code
   - Private keys in repo
   - Tokens and credentials
   - Connection strings with secrets

3. **Input Validation**
   - All user inputs sanitized
   - SQL/NoSQL injection prevention
   - Command injection prevention
   - XSS prevention (output escaping)
   - Path traversal prevention

4. **Authentication/Authorization**
   - Proper password hashing (bcrypt, argon2)
   - Session management security
   - Access control enforcement
   - JWT implementation security

5. **Dependency Security**
   - Run `npm audit` for known vulnerabilities
   - Check for outdated dependencies
   - Identify high-severity CVEs

## Agent Delegation

```
delegate(
  role="security-reviewer",
  tier="THOROUGH",
  prompt="SECURITY REVIEW TASK

Conduct comprehensive security audit of codebase.