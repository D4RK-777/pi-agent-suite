# Knowledge Vault — Operating Manual

This vault follows the **Karpathy LLM Wiki** pattern grafted onto a thin PARA outer shell.
Claude Code is the maintainer; the user curates sources and makes decisions.

## Layer ownership

| Layer | Path | Owner | Claude may |
|-------|------|-------|-----------|
| 1. Raw sources | `raw/` | User | **read only** — never write, never edit |
| 2. Wiki | `wiki/` | LLM | read + write; maintained by ingest/query/lint ops |
| 3. PARA side-folders | `decisions/` `patterns/` `sessions/` | Mixed | read + write |
| 4. Vault config | `_config/` | User | read; propose edits, user approves |

**Safety rule 0:** Never write into `raw/`. It is the immutable source of truth.

---

## The three operations

When the user says "ingest", "query", or "lint", follow these exact steps.

### Ingest — `ingest raw/articles/some-file.md`

1. Read the target file verbatim.
2. Identify: key claims, named entities, concepts, comparisons.
3. Create `wiki/sources/summary-{slug}.md` (template below).
4. For each concept:
   - Exists at `wiki/concepts/{slug}.md` → append new source to frontmatter, add paragraph, bump `updated`.
   - Doesn't exist → create with Concept template.
5. Same for entities → `wiki/entities/{slug}.md`.
6. A vs B comparison → create/update `wiki/comparisons/{a}-vs-{b}.md`.
7. Append to `wiki/log.md`.
8. Update `wiki/index.md`.
9. Update `wiki/hot.md`.
10. Report: pages created, pages updated, contradictions surfaced.

### Query — any question

1. Read `wiki/hot.md` (already warm at session start).
2. Read `wiki/index.md` for relevant pages.
3. Pull and cite with wikilinks: `[[concept-slug]]` (sourced from `[[summary-xyz]]`).
4. If reusable and substantive → create `wiki/syntheses/{slug}.md` with `filed_from_query: true`.
5. Reusable code/design pattern → `patterns/{slug}.md` instead.
6. Architectural commitment → `decisions/YYYY-MM-DD-{slug}.md`.
7. Update `wiki/hot.md`.

### Lint — `lint the wiki`

1. Read every wiki page's frontmatter.
2. Report:
   - **Orphans** — pages with no inbound wikilinks from index or peers.
   - **Stale** — `confidence: low` or `updated` > 60 days ago.
   - **Contradictions** — two pages with opposite claims on same subject.
   - **Missing backlinks** — concept cites source but source doesn't cite concept.
   - **Index drift** — wiki files not listed in `wiki/index.md`.
3. Do NOT auto-fix. Produce a report for the user to triage.
4. Append lint summary to `wiki/log.md`.

---

## Frontmatter schemas

### Source page (`wiki/sources/summary-{slug}.md`)

```yaml
---
type: source
title: "Exact title of the source"
slug: "slug-for-wikilinking"
source_file: "../../raw/articles/original-file.md"
author: "Author Name or Unknown"
published: YYYY-MM-DD
ingested: YYYY-MM-DD
key_claims:
  - "Short claim 1"
  - "Short claim 2"
related:
  - "[[concept-x]]"
confidence: high | medium | low
---
```

### Concept page (`wiki/concepts/{slug}.md`)

```yaml
---
type: concept
title: "Concept Name"
aliases: ["alt name", "acronym"]
sources:
  - "[[summary-xyz]]"
related:
  - "[[concept-a]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high | medium | low
---
```

### Entity page (`wiki/entities/{slug}.md`)

```yaml
---
type: entity
title: "Entity Name"
entity_type: person | org | product | place
dob: YYYY-MM-DD          # disambiguates people with same name
sources:
  - "[[summary-xyz]]"
related:
  - "[[entity-b]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Decision page (`decisions/YYYY-MM-DD-{slug}.md`)

```yaml
---
type: decision
title: "Short decision title"
status: accepted | superseded | rejected
date: YYYY-MM-DD
supersedes: "decisions/YYYY-MM-DD-old.md"   # if applicable
related:
  - "[[pattern-a]]"
---
```

### Pattern page (`patterns/{slug}.md`)

```yaml
---
type: pattern
title: "Pattern Name"
language: typescript | python | bash | any
sources:
  - "[[summary-xyz]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Hot cache rules (`wiki/hot.md`)

- Keep the 10–15 most-recently-touched concepts here.
- Each entry: concept title, one-line summary, wikilink, last-updated date.
- Update on every ingest and query that touches a concept.
- On session start, read this silently to warm context — no need to announce it.

---

## Writing rules

- Always search before creating: `obsidian_search` for the concept name and aliases.
- If a page exists → append or refine. Do not duplicate.
- If creating new → add to `wiki/index.md` AND `wiki/log.md` in the same operation.
- Wikilinks format: `[[slug]]` — never use full paths.
- Never write into `raw/` under any circumstances.
