r
   Remediation: Sanitize HTML or use safe rendering
   Reference: OWASP A03:2021 – Injection (XSS)

5. src/api/upload.ts:34 - Path Traversal Vulnerability
   Finding: User-controlled filename used without validation
   Impact: Attacker can read/write arbitrary files
   Remediation: Validate and sanitize filenames, use allowlist
   Reference: OWASP A01:2021 – Broken Access Control

...

MEDIUM (8)
----------
...

LOW (12)
--------
...

DEPENDENCY VULNERABILITIES
--------------------------
Found 3 vulnerabilities via npm audit:

CRITICAL: axios@0.21.0 - Server-Side Request Forgery (CVE-2021-3749)
  Installed: axios@0.21.0
  Fix: npm install axios@0.21.2

HIGH: lodash@4.17.19 - Prototype Pollution (CVE-2020-8203)
  Installed: lodash@4.17.19
  Fix: npm install lodash@4.17.21

...