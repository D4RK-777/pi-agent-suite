# Review Checklists

Per-domain checklists for code review — frontend, backend, security, performance.

---

## 1. Frontend Review Checklist

### Structure
- [ ] Components are under 200 lines
- [ ] No monolithic components (split at logical boundaries)
- [ ] Props are typed, no `any`
- [ ] No prop drilling (use Context or composition for deep trees)
- [ ] Component names are descriptive and PascalCase

### State
- [ ] State is as local as possible
- [ ] No unnecessary state (derive from props when possible)
- [ ] Loading, empty, and error states are handled
- [ ] No race conditions in async state updates

### Styling
- [ ] No hardcoded colors (use design tokens)
- [ ] No hardcoded spacing (use spacing scale)
- [ ] Responsive at 320px, 768px, 1024px
- [ ] Dark mode supported (test with `.dark` class)

### Accessibility
- [ ] All interactive elements are keyboard-accessible
- [ ] Form inputs have labels
- [ ] Images have alt text
- [ ] Color contrast meets WCAG 2.1 AA
- [ ] Focus states are visible

### Performance
- [ ] No unnecessary re-renders (check with React DevTools)
- [ ] Large lists are virtualized
- [ ] Images are lazy-loaded
- [ ] No blocking scripts in render path

---

## 2. Backend Review Checklist

### API Design
- [ ] Endpoints follow REST conventions
- [ ] Request/response shapes are documented
- [ ] Pagination is implemented for list endpoints
- [ ] Error responses use standardized format
- [ ] Status codes are correct (200, 201, 400, 401, 403, 404, 409, 429, 500)

### Validation
- [ ] All input is validated with Zod schemas
- [ ] No raw user input reaches database
- [ ] File uploads are validated (type, size, path)
- [ ] Output is sanitized before sending to client

### Database
- [ ] Queries use parameterized inputs (no SQL injection)
- [ ] N+1 queries are avoided
- [ ] Indexes exist for WHERE and JOIN columns
- [ ] Transactions wrap multi-table writes
- [ ] Migrations are backward-compatible

### Error Handling
- [ ] All errors are caught and logged
- [ ] No stack traces in production responses
- [ ] Error messages are user-friendly
- [ ] Trace IDs for support debugging

---

## 3. Security Review Checklist

### Authentication
- [ ] Passwords are hashed with argon2/bcrypt
- [ ] Session tokens are rotated
- [ ] Rate limiting on auth endpoints
- [ ] MFA supported for sensitive operations

### Authorization
- [ ] Ownership checks on all resource access
- [ ] Role checks on all protected endpoints
- [ ] No IDOR vulnerabilities
- [ ] Admin routes are protected

### Input/Output
- [ ] No XSS vectors (sanitize HTML output)
- [ ] No SQL injection (parameterized queries)
- [ ] No path traversal (sanitize file paths)
- [ ] No SSRF (validate outbound URLs)

### Data Protection
- [ ] Sensitive data is encrypted at rest
- [ ] Secrets are not logged
- [ ] API keys are not exposed to client
- [ ] PII is handled per compliance requirements

### Headers
- [ ] Content-Security-Policy set
- [ ] Strict-Transport-Security set
- [ ] X-Content-Type-Options: nosniff
- [ ] X-Frame-Options: DENY

---

## 4. Performance Review Checklist

### Response Time
- [ ] p95 latency < 200ms for API endpoints
- [ ] Database queries < 50ms
- [ ] No N+1 query patterns
- [ ] Caching implemented for expensive operations

### Bundle Size
- [ ] No unnecessary dependencies
- [ ] Code splitting implemented for routes
- [ ] Images optimized (WebP, responsive sizes)
- [ ] No duplicate packages in lockfile

### Rendering
- [ ] Server components where possible
- [ ] Client components only when necessary
- [ ] No blocking render in critical path
- [ ] Suspense boundaries for async content

### Caching
- [ ] HTTP cache headers set appropriately
- [ ] CDN caching configured for static assets
- [ ] Stale-while-revalidate for non-critical data
- [ ] Cache invalidation strategy documented

---

## 5. Testing Review Checklist

### Coverage
- [ ] P0 paths have tests
- [ ] New behavior has tests
- [ ] Edge cases are covered
- [ ] Error paths are tested

### Quality
- [ ] Tests are readable and maintainable
- [ ] No flaky tests (no arbitrary timeouts)
- [ ] Test names describe behavior
- [ ] Mocks are reset between tests

---

## Review Severity Classification

| Severity | Meaning | Action |
|---|---|---|
| **Blocker** | Bug, security issue, data loss | Must fix before merge |
| **Major** | Performance issue, missing error handling | Should fix before merge |
| **Minor** | Code style, naming, organization | Can fix in follow-up |
| **Nit** | Preference, optional improvement | Optional |

### Blocker Examples
- SQL injection vulnerability
- Missing authentication check
- Data corruption risk
- Unhandled promise rejection

### Major Examples
- N+1 query pattern
- Missing error boundary
- No loading state
- Hardcoded secrets

### Minor Examples
- Inconsistent naming
- Missing JSDoc
- Component could be split
- Magic number without comment

### Nit Examples
- Prefer `const` over `let`
- Alphabetize imports
- Extra blank line
- Prefer arrow function
