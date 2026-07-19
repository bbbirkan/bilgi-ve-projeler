# Capture Contract

Use this contract for raw inputs sent through Telegram.

## Capture Types

### Quick Idea

File as an inbox note or atomic note.

Expected sections:

- Idea
- Why it matters
- Links
- Follow-ups

### Link

File as a source note.

Expected sections:

- URL
- User context
- Summary, if page content is available
- Why the user saved it
- Extracted notes
- Follow-ups

If the page content is not available, state that and keep the note as a capture until fetched.

### PDF Or Document

File as a source note if content is available.

Expected sections:

- File name
- Document type
- Summary
- Important claims
- Decisions or tasks
- Extracted notes

If the content is unavailable, create a placeholder source note with `#needs-review`.

### Pasted Conversation

File as a source note.

Expected sections:

- Participants, if known
- Context
- Decisions
- Useful snippets summarized in the user's language
- Action items

Do not quote sensitive private content unless the user asks.

### Project Instruction

Update the relevant project note.

Expected sections to update:

- Current state
- Decisions
- Next actions
- Linked material

## Telegram Reply Format

Keep the reply short:

```text
Saved: [[Note Title]]
Filed under: 02-Sources
Updated: [[Related Project]] if applicable
Follow-up: one question if needed
```

## Example

Input:

```text
This is for the Hermes Obsidian video. Need to mention that Obsidian MCP exists but we should not demo it because Hermes already ships a skill. Also show shared vault, not app puppeting.
```

Output note:

```markdown
---
type: note
status: evergreen
created: YYYY-MM-DD
source: telegram
tags:
  - source/telegram
---

# Hermes Obsidian Demo Framing

## Idea

The demo should show Hermes writing to the shared Obsidian vault, not controlling the Obsidian app.

## Why It Matters

- It keeps the claim honest.
- It makes the VPS sponsor integration native.
- It avoids fake integration language.

## Links

- [[Hermes Obsidian Video]]
```
