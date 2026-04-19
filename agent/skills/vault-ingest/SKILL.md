---
name: vault-ingest
description: Use when the user asks to "save this note", "file this decision", "add to the vault", or mentions Obsidian/YourVault writes. Routes content to the correct PARA folder per vault doctrine.
---

# vault-ingest

Route writes to `YourVault/` correctly. Wrong folder = knowledge debt.

## Routing table

| Content shape | Target folder | Filename pattern |
|---|---|---|
| Reusable code or design pattern | `patterns/` | `{slug}.md` |
| Architectural commitment with accept/supersede lifecycle | `decisions/` | `YYYY-MM-DD-{slug}.md` |
| Atomic concept (no accept/reject semantics) | `wiki/concepts/` | `{slug}.md` + ingest linking |
| Cross-cutting analysis from a query | `wiki/syntheses/` | `{slug}.md` with `filed_from_query: true` |
| Verbatim source material | `raw/` | **NEVER WRITE HERE** — immutable |

## Frontmatter — minimum viable

Every vault write MUST have YAML frontmatter. The vault lint op fails without it.

```yaml
---
title: Short human title
type: pattern|decision|concept|synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [topic1, topic2]
---
```

Decisions also need `status: accepted|superseded|deprecated` and (if superseded) `supersedes: [[old-decision-slug]]`.
Syntheses filed from a query also need `filed_from_query: true` and `source_conversation: {session-id}`.

## Before you write

1. `obsidian_search` for the concept name **and its likely aliases** — vault is source of truth; if a page exists, **append or refine** rather than duplicate.
2. If appending, bump `updated:` in frontmatter and add a new paragraph citing the new source.
3. If creating fresh, run the ingest-style linking pass: link to at least 2 existing pages (`[[other-concept]]`) so the new page isn't an orphan.
4. **Always** update `wiki/index.md` AND `wiki/log.md` on any write to `wiki/`. This is how the lint op stays consistent.

## Verbatim goes to MemPalace, NOT the vault

If the user just wants their words preserved exactly ("save this quote", "remember this"), call `mempalace_add_drawer` with the verbatim content. **Don't** paraphrase into a vault note unless the user explicitly asks for a curated version.

The difference:
- MemPalace = what was *said* (drawer, verbatim, searchable)
- Vault = what we *learned* (curated, linked, refined)

## Never

- Write to `raw/` — immutable (security-gate enforces this)
- Duplicate the same concept across `wiki/concepts/` and `decisions/` and `patterns/`
- Create a wiki page without linking to at least one existing page
- File agent-generated prose as if it were the user's words

## Canonical reference

Read `YourVault/CLAUDE.md` for the full vault operating manual. It defines ingest/query/lint ops and the full frontmatter schemas for all five page types. That file is canonical — do not improvise vault operations from this skill alone if they conflict.
