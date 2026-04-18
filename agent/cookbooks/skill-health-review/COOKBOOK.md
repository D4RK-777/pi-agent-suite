# Skill Health Review

## Purpose

Review the shared library on a recurring basis so stale, duplicate, or missing capabilities are found before drift sets in.

## Use When

- the shared skill library needs a periodic review
- a repo keeps solving the same problem outside shared core
- the team wants to evaluate whether a new skill should exist

## Steps

1. Inventory the current shared skills and the downstream consumers that depend on them.
2. Identify duplicate guidance living in vendor folders or project repos.
3. Separate reusable patterns from repo-specific context.
4. Recommend one of three outcomes: keep as-is, improve an existing skill, or add a new canonical skill.
5. Update manifests and migration notes for any approved change.
6. Record follow-up items for adapters, packaging, or downstream relinking.

## Output

- health summary of the shared library
- recommended adds, merges, or removals
- explicit note on what should remain project-local
