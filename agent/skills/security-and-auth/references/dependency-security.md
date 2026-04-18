# Dependency Security

Audit patterns, supply chain attacks, lockfile verification, CVE response.

---

## 1. Dependency Audit

### Automated Audit in CI

```yaml
# .github/workflows/security.yml
name: Security Audit
on:
  push:
    paths:
      - "package.json"
      - "package-lock.json"
  schedule:
    - cron: "0 6 * * 1" # Every Monday at 6am

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm audit --audit-level=moderate
        continue-on-error: true
      - run: npx audit-ci --moderate
```

### Pre-Commit Audit Hook

```json
// package.json
{
  "scripts": {
    "audit": "npm audit --audit-level=moderate",
    "audit:fix": "npm audit fix",
    "audit:force": "npm audit fix --force"
  }
}
```

### Audit Response Workflow

```
1. npm audit → Identify vulnerabilities
2. Categorize by severity:
   - Critical: Fix immediately, block deployment
   - High: Fix within 24 hours
   - Moderate: Fix within 1 week
   - Low: Fix in next maintenance window
3. npm audit fix → Auto-fix compatible updates
4. For remaining: manually update packages
5. Test thoroughly after updates
6. Deploy and monitor
```

---

## 2. Supply Chain Attack Prevention

### Lockfile Verification

```bash
# Always commit lockfile
git add package-lock.json  # npm
git add yarn.lock          # yarn
git add pnpm-lock.yaml     # pnpm

# Verify lockfile integrity
npm ci  # Fails if lockfile doesn't match package.json
```

### Pin Dependencies

```json
// BAD: Wide version ranges — could pull in malicious updates
{
  "dependencies": {
    "lodash": "^4.17.21",
    "express": "*"
  }
}

// GOOD: Exact versions
{
  "dependencies": {
    "lodash": "4.17.21",
    "express": "4.18.2"
  }
}

// BETTER: Exact versions with Renovate/Dependabot for updates
{
  "dependencies": {
    "lodash": "4.17.21"
  }
}
// renovate.json config handles updates via PRs with changelogs
```

### Verify Package Integrity

```bash
# Check for typosquatting (similar names to popular packages)
npx npm-audit typosquat

# Verify package signatures (npm v9+)
npm install --verify-signatures

# Check package before installing
npm view <package-name> --json | jq '.author, .maintainers, .repository'
```

### Red Flags in Dependencies

```
❌ Package created recently (< 6 months)
❌ Very few downloads (< 100/week)
❌ Single maintainer, no organization
❌ Sudden major version change without changelog
❌ Unusual permissions in package.json (postinstall scripts)
❌ Obfuscated code in node_modules
❌ Network requests in postinstall scripts
❌ Package name similar to popular package (typosquatting)
```

---

## 3. CVE Response Process

### Monitoring

```bash
# Automated daily check
npx audit-ci --moderate

# GitHub Dependabot alerts
# Settings → Security & analysis → Dependabot alerts: Enable

# Snyk for deeper scanning
npx snyk test
```

### Response Playbook

```
1. Assess severity (CVSS score)
   - Critical (9.0-10.0): Immediate action
   - High (7.0-8.9): Action within 24h
   - Medium (4.0-6.9): Action within 1 week
   - Low (0.1-3.9): Next maintenance window

2. Check if your app is actually affected
   - Is the vulnerable function used?
   - Is the attack vector reachable?

3. Find the fix
   - npm audit fix (automatic)
   - Update to patched version
   - Apply workaround if no fix available

4. Test the fix
   - Run test suite
   - Manual smoke test of affected area

5. Deploy and monitor
   - Deploy to staging first
   - Monitor error rates
   - Deploy to production
```

---

## 4. Secure Dependency Patterns

### Safe Package Installation

```bash
# GOOD: Install with integrity verification
npm install lodash@4.17.21

# GOOD: Use npm shrinkwrap for production
npm shrinkwrap

# BAD: Install from untrusted sources
npm install git://github.com/unknown/lodash.git
```

### Postinstall Script Audit

```json
// package.json — review all postinstall scripts
{
  "scripts": {
    "postinstall": "echo 'Review this script!'"
  }
}

// Check what postinstall scripts do
grep -r "postinstall" node_modules/*/package.json
```

### Subresource Integrity (SRI)

```html
<!-- For CDN dependencies -->
<script
  src="https://cdn.example.com/react-18.2.0.min.js"
  integrity="sha384-..."
  crossorigin="anonymous"
></script>
```

---

## Dependency Security Checklist

- [ ] Lockfile committed to version control
- [ ] CI runs `npm audit` on every PR
- [ ] Dependabot/Renovate enabled for automated updates
- [ ] No `*` version ranges in package.json
- [ ] Postinstall scripts reviewed
- [ ] Critical CVEs fixed within 24 hours
- [ ] High CVEs fixed within 1 week
- [ ] Production dependencies pinned to exact versions
- [ ] No unused dependencies (`npm prune`)
- [ ] Regular dependency review (monthly)
