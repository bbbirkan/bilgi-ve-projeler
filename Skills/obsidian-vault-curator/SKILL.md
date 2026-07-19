---
name: obsidian-vault-curator
description: Organize raw captures, PDFs, links, meeting notes, Telegram dumps, and project notes into an Obsidian vault using Markdown, wikilinks, tags, source notes, maps of content, and inbox triage. Use when an agent needs to maintain a self-organizing second brain rather than control the Obsidian app.
---

# Obsidian Vault Curator

## Overview

Maintain an Obsidian vault as a clean, linked Markdown knowledge base. The user should be able to dump raw material; the agent should file, link, tag, summarize, and update indexes.

## Default Vault Map

Use this structure unless the user already has a strong vault convention:

- `01-Inbox`: unprocessed captures and uncertain notes.
- `02-Sources`: durable notes for links, PDFs, transcripts, conversations, and imported docs.
- `03-Maps`: maps of content, indexes, and topic hubs.
- `04-Projects`: active outcomes, plans, briefs, and deliverables.
- `05-People`: people, collaborators, companies, and relationship notes.
- `_templates`: note templates copied by the agent.

Starter files are in `assets/vault-starter`.

## Workflow

1. Identify the input type:
   - Raw idea
   - Link or article
   - PDF or document
   - Transcript or conversation
   - Project update
   - Person/company note
2. Preserve the source:
   - Create or update a source note in `02-Sources` when the capture references external material.
   - Keep a short "Raw capture" section when the source is messy or personal.
3. Extract useful notes:
   - Split dense captures into atomic notes only when each note has standalone value.
   - Link atomic notes back to the source note.
4. File the note:
   - Use `01-Inbox` only when classification is uncertain.
   - Use project folders for active deliverables.
   - Use maps when a topic is recurring.
5. Add links and tags:
   - Use `[[wikilinks]]` for durable entities and ideas.
   - Use tags for workflow/status, not every keyword.
6. Update indexes:
   - Update `00-Home.md` only for major maps/projects.
   - Update the relevant map in `03-Maps` for repeated topics.
7. Report what changed:
   - List created notes.
   - List updated notes.
   - Mention unresolved questions.

## Note Quality Rules

- Write Markdown that works in Obsidian without plugins.
- Prefer clear titles over clever titles.
- Use YAML frontmatter only when it helps later retrieval.
- Use concise summaries; do not turn the vault into a duplicate of the full source.
- Do not invent facts from inaccessible sources.
- Mark uncertain statements with `Needs verification`.
- Do not store secrets unless the user explicitly asks and accepts the risk.

## Standard Frontmatter

Use this shape when creating new durable notes:

```yaml
---
type: source | note | project | person | map
status: inbox | active | evergreen | archived
created: YYYY-MM-DD
source: telegram | web | pdf | conversation | manual
tags:
  - inbox
---
```

## Resources

- Read `references/vault-rules.md` before reorganizing an existing vault or creating many notes.
- Copy `assets/vault-starter` when bootstrapping a new vault.
- Use the templates in `_templates` for consistent output.

## Completion Criteria

Finish when the raw capture is represented by useful Markdown, relevant notes are linked, tags are meaningful, and the user can find the material from a map, project note, or home index.
