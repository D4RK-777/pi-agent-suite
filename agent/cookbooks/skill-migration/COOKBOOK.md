# Skill Migration

## Purpose

Move an existing skill into the canonical `D4rkMynd` library without breaking downstream consumers.

## Use When

- a skill currently lives in a vendor folder
- a local package should become a wrapper around the shared root

## Steps

1. Read the existing skill and identify any vendor-specific assumptions.
2. Move the canonical body into `skills/<skill-name>/SKILL.md`.
3. Put packaging or tool-specific notes in `plugins/` or `adapters/`.
4. Register the skill in `manifests/skills.json`.
5. Re-link downstream folders instead of duplicating the content.

## Output

- canonical migrated skill
- updated manifest
- downstream wiring plan
