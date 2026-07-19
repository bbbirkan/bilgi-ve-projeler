# Vault Rules

Use these rules when an agent is maintaining an Obsidian vault for a human.

## Folder Rules

- `01-Inbox`: temporary holding area for unprocessed or ambiguous captures.
- `02-Sources`: one note per durable source, such as an article, PDF, meeting, video, transcript, or pasted conversation.
- `03-Maps`: topic hubs and maps of content that help the user navigate.
- `04-Projects`: active outcomes with decisions, tasks, links, and status.
- `05-People`: people, companies, and collaborators.
- `_templates`: reusable note templates.

Do not create many top-level folders. If a new category appears, prefer a map note first.

## Naming Rules

- Use title case for durable notes: `Hermes Obsidian VPS Setup.md`.
- Prefix dates only when the date is part of the retrieval path: `2026-06-21 Telegram Capture Test.md`.
- Keep filenames readable. Avoid IDs unless the source already has one.
- Use singular entity names for people and companies.

## Tag Rules

Use tags for workflow and broad retrieval:

- `#inbox`
- `#source/web`
- `#source/pdf`
- `#source/telegram`
- `#project`
- `#person`
- `#needs-review`
- `#needs-verification`

Do not tag every noun. Prefer wikilinks for important concepts and entities.

## Link Rules

- Link durable concepts with `[[wikilinks]]`.
- Link source notes to extracted atomic notes.
- Link project notes to related sources and decisions.
- Add a note to a map only when the topic is likely to recur.
- Avoid orphan notes unless they are temporary inbox captures.

## Source Note Shape

```markdown
---
type: source
status: evergreen
created: YYYY-MM-DD
source: web
tags:
  - source/web
---

# Source Title

## Summary

Two to five bullets.

## Key Points

- Point with a link to any extracted note.

## Raw Capture

Paste or summarize the raw material when useful.

## Follow-Ups

- [ ] Question or next action.
```

## Atomic Note Shape

```markdown
---
type: note
status: evergreen
created: YYYY-MM-DD
source: source-note-title
tags: []
---

# One Clear Idea

Short explanation in the user's language.

## Why It Matters

- Practical implication.

## Links

- Source: [[Source Title]]
```

## Project Note Shape

```markdown
---
type: project
status: active
created: YYYY-MM-DD
tags:
  - project
---

# Project Name

## Outcome

What done means.

## Current State

- Decision
- Open question

## Linked Material

- [[Relevant Source]]

## Next Actions

- [ ] Concrete action
```

## Update Rules

When adding a new note:

1. Check whether an existing source, map, project, or person note should be updated instead.
2. Create a new note only when it has distinct retrieval value.
3. Add links in both directions when useful.
4. Keep a short change report for the user.

## What Not To Do

- Do not generate giant summaries that no one will read.
- Do not create fake links to notes that do not exist.
- Do not reorganize the entire vault without explicit permission.
- Do not add plugin-specific syntax unless the user already uses that plugin.
