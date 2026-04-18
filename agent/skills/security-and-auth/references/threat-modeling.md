# Threat Modeling

STRIDE methodology, trust boundary mapping, attack surface analysis.

---

## 1. STRIDE Threat Model

### What Is STRIDE?

STRIDE is a systematic way to identify security threats across 6 categories:

| Category | What It Means | Example |
|---|---|---|
| **S**poofing | Pretending to be someone else | Stolen session token |
| **T**ampering | Modifying data unauthorized | Changing order total in request |
| **R**epudiation | Denying an action occurred | "I didn't make that transaction" |
| **I**nformation Disclosure | Exposing data to unauthorized party | API returns user passwords |
| **D**enial of Service | Making system unavailable | Flooding login endpoint |
| **E**levation of Privilege | Gaining higher access than intended | User accessing admin routes |

### STRIDE Analysis Template

```markdown
## Component: User Authentication

| Threat | How It Could Happen | Mitigation | Status |
|---|---|---|---|
| Spoofing | Attacker steals session token | HttpOnly cookies, short expiry | ✅ Mitigated |
| Tampering | Attacker modifies JWT payload | JWT signature verification | ✅ Mitigated |
| Repudiation | User denies logging in | Audit log with timestamps | ✅ Mitigated |
| Info Disclosure | Error message reveals user exists | Generic error messages | ✅ Mitigated |
| DoS | Brute force login attempts | Rate limiting, account lockout | ✅ Mitigated |
| Elevation | User changes role in JWT | Server-side role verification | ✅ Mitigated |
```

---

## 2. Trust Boundary Mapping

### What Are Trust Boundaries?

Trust boundaries are where data crosses from one trust level to another. Every boundary is a potential attack surface.

### Common Trust Boundaries

```
┌─────────────────────────────────────────────┐
│                 UNTRUSTED                    │
│  ┌───────────┐    ┌───────────────────┐     │
│  │  Browser   │    │  Third-party API  │     │
│  │  (User)    │    │  (Stripe, etc.)   │     │
│  └─────┬─────┘    └────────┬──────────┘     │
│        │                   │                │
│  ┌─────▼───────────────────▼──────────┐     │
│  │         TRUST BOUNDARY             │     │
│  │    (API Gateway / Middleware)      │     │
│  └─────────────────┬─────────────────┘     │
│                    │                        │
│  ┌─────────────────▼─────────────────┐     │
│  │           SEMI-TRUSTED             │     │
│  │     (Application Server)           │     │
│  └─────────────────┬─────────────────┘     │
│                    │                        │
│  ┌─────────────────▼─────────────────┐     │
│  │         TRUST BOUNDARY             │     │
│  │      (ORM / Query Builder)         │     │
│  └─────────────────┬─────────────────┘     │
│                    │                        │
│  ┌─────────────────▼─────────────────┐     │
│  │            TRUSTED                 │     │
│  │        (Database)                  │     │
│  └───────────────────────────────────┘     │
└─────────────────────────────────────────────┘
```

### Boundary Checklist

For EVERY trust boundary, verify:

```
Boundary: Browser → API
- [ ] Input validation (Zod schemas)
- [ ] Authentication required
- [ ] Rate limiting in place
- [ ] CORS configured correctly
- [ ] Security headers set

Boundary: API → Database
- [ ] Parameterized queries (no SQL injection)
- [ ] Least-privilege DB user
- [ ] Row-level access control
- [ ] Audit logging enabled

Boundary: API → Third-Party
- [ ] Domain allowlist for SSRF prevention
- [ ] API keys stored securely
- [ ] Response data validated before use
- [ ] Timeouts configured
```

---

## 3. Attack Surface Analysis

### Mapping the Attack Surface

```
Application: E-Commerce Platform

External Entry Points:
1. Web UI (React frontend)
2. REST API (/api/*)
3. Webhook endpoints (/api/webhooks/*)
4. Static file serving (/public/*)

Internal Entry Points:
5. Admin panel (/admin/*)
6. Database (direct access)
7. Background jobs (cron, queues)

Data Stores:
8. PostgreSQL (users, orders, products)
9. Redis (sessions, cache, rate limits)
10. File storage (product images, receipts)

Third-Party Integrations:
11. Stripe (payments)
12. Resend (emails)
13. AWS S3 (file storage)
```

### Risk Prioritization

```
Risk = Likelihood × Impact

| Attack Vector | Likelihood | Impact | Risk | Priority |
|---|---|---|---|---|
| SQL Injection via API | Low (ORM) | Critical | Medium | P2 |
| Stolen session token | Medium | High | High | P1 |
| Brute force login | High | Medium | High | P1 |
| SSRF via webhook | Low | Critical | Medium | P2 |
| XSS via user content | Medium | High | High | P1 |
| Dependency vulnerability | Medium | High | High | P1 |
| IDOR on order details | Medium | High | High | P1 |
| DoS on login endpoint | Low | Medium | Low | P3 |
```

---

## 4. Threat Model Documentation

### Template

```markdown
# Threat Model: [Component/Feature]

## Overview
- Component: User authentication and session management
- Last reviewed: 2024-01-15
- Reviewer: Security team

## Data Flow
1. User submits credentials → API validates → DB checks → Session created
2. Session token stored in HttpOnly cookie
3. Token verified on each API request
4. Token expires after 15 minutes, refreshable for 7 days

## Trust Boundaries
1. Browser → API (authentication required)
2. API → Database (parameterized queries)
3. API → Redis (session storage)

## Threats (STRIDE)
[See STRIDE table above]

## Mitigations
- [List all security controls]

## Residual Risks
- Session token theft via XSS (mitigated by HttpOnly, but XSS still possible)
- Refresh token replay if database is compromised (mitigated by hashing)

## Recommendations
1. Add Content-Security-Policy headers to prevent XSS
2. Implement device fingerprinting for session binding
3. Add anomaly detection for login location/time
```

---

## 5. Security Review Questions

For every new feature, ask:

### Authentication
- Who can access this feature?
- How do we verify their identity?
- What happens if authentication fails?

### Authorization
- What data can this user access?
- Can they access other users' data?
- What actions are they allowed to perform?

### Input
- What data comes from outside the system?
- Is it validated before use?
- Can it contain malicious content?

### Output
- What data leaves the system?
- Does it include sensitive information?
- Is it logged anywhere?

### Dependencies
- What external services does this feature use?
- What happens if they're compromised?
- What happens if they're unavailable?

### State
- What state does this feature maintain?
- Can it be corrupted or lost?
- Is there an audit trail?

---

## Threat Modeling Quick Reference

| Question | If Yes → |
|---|---|
| Can an unauthenticated user access this? | Add authentication |
| Can a user access another user's data? | Add ownership check |
| Can user input reach the database unsanitized? | Add validation |
| Can user input reach the browser unsanitized? | Add sanitization |
| Can this endpoint be called rapidly? | Add rate limiting |
| Does this log sensitive data? | Redact before logging |
| Does this depend on an external service? | Add timeout + fallback |
| Can this action be denied to anyone? | Add DoS protection |
