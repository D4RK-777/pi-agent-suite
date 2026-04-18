---
name: security-first-pass
description: >-
  Use when a repo, app, or change needs a lightweight security sweep before a deeper review.
  Triggers on "quick security scan", "first-pass security review", "find obvious secrets",
  "dependency or config smell check", "scan this project for risky patterns", or when security
  needs a fast recon pass before full threat modeling or manual review.
trigger: quick security scan, first-pass review, secret scan
tags:
  - security
  - scanning
  - secrets
  - audit
  - first-pass
---

# Security First Pass

## Purpose

Use this skill for a lightweight automated first pass over a codebase or change set before doing
deeper security analysis.

This skill is intentionally opinionated and shallow. It is meant to catch obvious secrets,
dangerous calls, missing hygiene, and risky configuration patterns quickly so the security lane can
focus deeper effort where it matters.

## When to Use

- A project needs a fast initial security scan
- You want a secrets pass before a deeper review
- A repo should be triaged for obvious risky patterns
- Security needs a starting point before a manual audit

## Rules

- Treat this as reconnaissance, not final security sign-off.
- Escalate serious findings into `security-and-auth` or a deeper review.
- Prefer the bundled scripts over ad hoc regex hunting when repeating this task.
- Keep false positives visible but distinguish them from confirmed issues.

## Workflow

1. Run the project scanner.
2. Run the secrets-focused scanner when secret hygiene matters.
3. Group findings by severity and type.
4. Escalate high-risk items into a proper manual review.

## Commands

```powershell
python scripts/scan_project.py C:\path\to\repo
python scripts/scan_project.py C:\path\to\repo --format json
python scripts/scan_secrets.py C:\path\to\repo
python scripts/scan_secrets.py C:\path\to\repo --format json
```

## References

- `references/vulnerability-patterns.md`
- `references/secrets-patterns.md`

## Expected Output

- quick first-pass security findings
- obvious secret exposures
- high-risk files or directories for deeper manual review
