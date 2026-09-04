# LLM Wiki — Schema

This document tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow.

## Architecture

Three layers:

1. **raw/** — Immutable source documents. The LLM reads from them but never modifies them. This is the source of truth.
2. **wiki/** — LLM-generated markdown files. The LLM owns this layer entirely. It creates, updates, cross-references, and maintains consistency.
3. **AGENTS.md** — This file. The schema. Co-evolved over time as workflows are refined.

## Directory Structure

```
second brain/
├── raw/                    # Source documents (LLM reads, never writes)
│   └── assets/             # Images and attachments
├── wiki/                   # LLM-maintained knowledge base
│   ├── index.md            # Content-oriented catalog of all pages
│   ├── log.md              # Chronological append-only activity record
│   ├── sources/            # Summary pages for ingested sources
│   ├── entities/           # Pages for people, organizations, tools
│   ├── concepts/           # Pages for theories, methods, patterns
│   └── analyses/           # Comparisons, syntheses, explorations
├── crm/                    # Contact records (person pages + index)
├── journal/                # Journal entries (conversation logs + index)
└── AGENTS.md               # This file (the schema)
```

## Wiki Page Conventions

- Every page uses `[[wikilinks]]` for cross-references.
- Entity and concept pages include YAML frontmatter: `tags`, `created`, `sources`.
- Source summary pages include: `title`, `source_file`, `date_ingested`, `tags`.
- When new sources contradict existing claims, flag it on the relevant page and note it in the contradiction section.

## Operations

### Ingest

When a new source is added to `raw/`:

1. Read the source.
2. Discuss key takeaways with the user.
3. Write a summary page in `wiki/sources/`.
4. Crosslink any wiki pages generated or updated to the original source page.
5. Create or update relevant entity pages in `wiki/entities/`.
6. Create or update relevant concept pages in `wiki/concepts/`.
7. Update `wiki/index.md` with the new page.
8. Append an entry to `wiki/log.md`.
9. Move the source file from the root raw/ directory to `raw/processed/`. Prefer ingesting one at a time, until user explicitly asks for batch processing.

A single source may touch 10-15 wiki pages.

### Query

When the user asks a question:

1. Read `wiki/index.md` to find relevant pages.
2. Read those pages.
3. Synthesize an answer with citations.
4. If the answer is valuable, file it back into `wiki/analyses/` as a new page.

### Lint

Periodically health-check the wiki:

1. Look for contradictions between pages.
2. Identify stale claims superseded by newer sources.
3. Find orphan pages with no inbound links.
4. Find important concepts mentioned but lacking their own page.
5. Find missing cross-references.
6. Identify data gaps that could be filled with a web search.
7. Append a summary entry to `wiki/log.md`.

### CRM

When the user provides information about a person for the CRM:

1. If the person already has a page in `crm/`, update it with the new details.
2. If not, create a new page named after the person in `crm/`.
3. Include: name, contact details, where/how you met, things you know about them, and any other details provided.
4. Update `crm/index.md` with the person listed in alphabetical order and a short bio.
5. Append an entry to `wiki/log.md`.

### Journal

When the user starts a chat with "journal":

1. The entire conversation becomes a new markdown file in `journal/`.
2. Filename format: `YYYY-MM-DD Title.md` (decide a short title based on content).
3. Create or update `journal/index.md` with the entry linked and a short summary.
4. Append the journal entry title and short summary to `wiki/log.md`.
5. Responses to journal entries should be grounded in wiki content — read the index and relevant pages before responding, the same way you do for queries.

## Log Format

Each entry in `wiki/log.md` starts with a consistent prefix for unix-tool parsing:

```
## [YYYY-MM-DD] ingest | Title
## [YYYY-MM-DD] query | Question text
## [YYYY-MM-DD] lint | Health check summary
## [YYYY-MM-DD] journal | Entry title
```

Example: `grep "^## \[" wiki/log.md | tail -5` gives the last 5 entries.
