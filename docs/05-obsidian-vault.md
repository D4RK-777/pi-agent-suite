# 05 — Obsidian Vault

How to use the Pi Agent Suite vault template for long-term structured knowledge management.

---

## Overview

The Obsidian vault component is **optional** but powerful. It gives your AI assistant a curated, human-reviewed knowledge base that persists across all conversations — separate from the fuzzy semantic memory of MemPalace.

**MemPalace vs. Obsidian vault:**

| | MemPalace | Obsidian Vault |
|---|---|---|
| Storage | ChromaDB vectors | Markdown files |
| Search | Semantic (fuzzy) | Text + wikilink graph |
| Maintainer | Auto (hooks) | LLM + human curation |
| Source of truth | No | **Yes** |
| Best for | Quick recall, session memory | Canonical knowledge, decisions |

**Rule:** When they conflict, the vault wins. MemPalace reflects what was said; the vault reflects what is true.

---

## Setting up the vault

### Step 1 — Create the vault directory

```bash
# Via installer
bash installer/install.sh --with-vault
# > Obsidian vault path (new directory will be created): ~/MyKnowledgeVault

# Or manually copy the template
cp -r vault-template/ ~/MyKnowledgeVault
```

### Step 2 — Open in Obsidian

1. Download Obsidian from obsidian.md
2. Open Obsidian → **Add vault** → select `~/MyKnowledgeVault`

### Step 3 — Install the Local REST API plugin

1. In Obsidian: Settings → Community plugins → Browse
2. Search for "Local REST API" by coddingtonbear
3. Install and enable it
4. Copy the API key from the plugin settings

### Step 4 — Install the MCP server for Claude Code

```bash
npm install -g obsidian-mcp-server

claude mcp add obsidian npx -- obsidian-mcp-server \
  --api-key "YOUR_API_KEY" \
  --vault "MyKnowledgeVault"
```

### Step 5 — Set environment variables

```bash
export OBSIDIAN_VAULT="$HOME/MyKnowledgeVault"
export OBSIDIAN_API_KEY="your-api-key"
export OBSIDIAN_VAULT_NAME="MyKnowledgeVault"
```

---

## Vault structure

```
MyKnowledgeVault/
├── raw/                           # Immutable source documents — Claude: READ ONLY
│   ├── articles/                  # Articles and papers
│   └── books/                     # Book excerpts
├── wiki/                          # Claude-maintained knowledge graph
│   ├── sources/                   # Summaries of raw docs
│   │   └── summary-{slug}.md
│   ├── concepts/                  # Atomic concept pages
│   │   └── {slug}.md
│   ├── entities/                  # People, orgs, products
│   │   └── {slug}.md
│   ├── comparisons/               # A-vs-B analysis pages
│   │   └── {a}-vs-{b}.md
│   ├── syntheses/                 # Cross-cutting analyses
│   │   └── {slug}.md
│   ├── index.md                   # Master index (auto-maintained)
│   ├── hot.md                     # 10-15 recently touched concepts
│   └── log.md                     # Append-only operation log
├── decisions/                     # Architectural commitments
│   └── YYYY-MM-DD-{slug}.md
├── patterns/                      # Reusable code patterns
│   └── {slug}.md
├── sessions/                      # Session notes
└── CLAUDE.md                      # Vault ops manual (read by Claude Code)
```

---

## The three operations

### Ingest

Tell Claude Code to ingest a document:
```
Ingest raw/articles/react-patterns.md
```

Claude will:
1. Read the document verbatim
2. Create `wiki/sources/summary-react-patterns.md`
3. Create or update concept pages for each key concept
4. Create entity pages for people/orgs mentioned
5. Create comparison pages if A-vs-B content found
6. Update `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`

### Query

Ask a question referencing the vault:
```
What does the vault say about JWT vs session cookie authentication?
```

Claude will:
1. Read `wiki/hot.md` (already warm)
2. Read relevant concept/comparison pages
3. Answer citing wikilinks: `[[jwt-auth]] (sourced from [[summary-auth-guide]])`
4. Optionally create a synthesis page if the answer is reusable

### Lint

Check the vault for quality issues:
```
Lint the wiki
```

Claude will report:
- **Orphans** — pages with no inbound links
- **Stale** — low-confidence or old pages
- **Contradictions** — conflicting claims across pages
- **Index drift** — files not listed in index.md

Lint does NOT auto-fix — it produces a report for you to triage.

---

## Page types and frontmatter

### Source page

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

### Concept page

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

### Decision page

```yaml
---
type: decision
title: "Short decision title"
status: accepted | superseded | rejected
date: YYYY-MM-DD
supersedes: "decisions/YYYY-MM-DD-old.md"
related:
  - "[[pattern-a]]"
---
```

### Pattern page

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

## Routing new knowledge

Not everything goes in `wiki/`. Use the right location:

| Type | Location |
|---|---|
| Reusable code/design pattern | `patterns/{slug}.md` |
| Architectural commitment | `decisions/YYYY-MM-DD-{slug}.md` |
| Atomic concept | `wiki/concepts/{slug}.md` |
| Cross-cutting analysis from query | `wiki/syntheses/{slug}.md` |
| Session notes | `sessions/` |
| Raw source documents | `raw/` (read-only) |

---

## Safety rules

- **Never write to `raw/`** — it is immutable. Claude Code is read-only there.
- **Search before creating** — `obsidian_search` for concept name and aliases first. If found, update; don't duplicate.
- **Always update index and log** — every write to `wiki/` must update `wiki/index.md` AND `wiki/log.md`.
- **Wikilinks format** — use `[[slug]]`, never full file paths.

---

## MCP tools available in Claude Code

After adding the obsidian-mcp-server:

| Tool | Description |
|---|---|
| `obsidian_search` | Full-text search across the vault |
| `obsidian_readFile` | Read a specific vault file |
| `obsidian_listFiles` | List files in a directory |
| `obsidian_appendContent` | Append to an existing file |
| `obsidian_createFile` | Create a new vault file |

These are used automatically by Claude Code when you ask vault-related questions.

---

## Integration with MemPalace

The two stores complement each other:

- **Mine vault into MemPalace** for faster recall:
  ```bash
  mempalace mine ~/MyKnowledgeVault/wiki/concepts/ --wing knowledge
  mempalace mine ~/MyKnowledgeVault/decisions/ --wing decisions
  mempalace mine ~/MyKnowledgeVault/patterns/ --wing code
  ```

- **When they conflict** — trust the vault. If a MemPalace drawer contradicts a wiki page, the page is the source of truth. Re-mine from the vault rather than overriding it.
