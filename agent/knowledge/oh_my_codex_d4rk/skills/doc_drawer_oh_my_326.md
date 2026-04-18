L commands
   Remediation: Use parameterized queries or ORM
   Reference: OWASP A03:2021 – Injection

HIGH (5)
--------
3. src/auth/password.ts:22 - Weak Password Hashing
   Finding: Passwords hashed with MD5 (cryptographically broken)
   Impact: Passwords can be reversed via rainbow tables
   Remediation: Use bcrypt or argon2 with appropriate work factor
   Reference: OWASP A02:2021 – Cryptographic Failures

4. src/components/UserInput.tsx:67 - XSS Vulnerability
   Finding: User input rendered with dangerouslySetInnerHTML
   Impact: Cross-site scripting attack vector
   Remediation: Sanitize HTML or use safe rendering
   Reference: OWASP A03:2021 – Injection (XSS)