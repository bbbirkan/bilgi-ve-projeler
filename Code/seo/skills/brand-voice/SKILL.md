---
name: brand-voice
description: >
  Extract or build a brand voice profile that anchors consistent SEO content.
  Uses a "voice constant, tone flexes" model — voice is WHO the brand is
  (captured in a "We Are / We Are Not" identity table), tone is HOW it speaks
  in a given context (flexed via Formality, Energy, Technical Depth dimensions).
  Three modes — Extract (analyze existing content), Build (strategic questions),
  or Auto-Scrape (provide a URL). Analyzes content across 6 dimensions (tone,
  vocabulary, rhythm, structure, personality, POV), produces a voice profile
  with tone-by-context matrix and confidence scoring, calibrated for blog/SEO
  output. Use when onboarding a new brand, when content sounds generic, or when
  SEO articles need a consistent human voice. Writes: brand-voice.md.
---

# Brand Voice

Define a brand's voice so every piece of SEO content sounds like the same
person wrote it. Generic copy converts worse than copy with a distinct
voice — not because the words are different, but because the reader feels
like they're hearing from a person, not a content team.

This skill defines that voice. Either by extracting it from existing
content, building it from strategic questions, or auto-scraping a URL to
analyze a brand's public presence.

---

## Core Mental Model: Voice Constant, Tone Flexes

Every voice profile is built on one distinction:

**Voice** is WHO the brand is — personality, values, identity. It never
changes regardless of channel, audience, or content type. Voice is captured
in the "We Are / We Are Not" table: paired attributes that define what the
brand IS and the boundary it should never cross.

**Tone** is HOW the brand speaks in a given moment. It adapts to context
the way a person adjusts when speaking to a friend vs. a conference
audience vs. a support thread. Tone flexes along three dimensions:

| Dimension | What it controls |
|-----------|-----------------|
| **Formality** | How formal or casual the language is |
| **Energy** | How much enthusiasm, urgency, or dynamism |
| **Technical Depth** | How much domain expertise or jargon |

Voice stays constant across all content. Tone flexes by context. A blog
article and a landing page should sound like the same person — but that
person is allowed to adjust their delivery.

---

## Brand Context Integration

On every invocation, check for existing brand context in `./brand/`.

### Reads (if they exist)

If any brand context documents exist in `./brand/` — positioning docs, audience
profiles, competitor analyses, style guides, or any other brand materials — read
them and use them to inform the voice extraction. There is no required file schema.
The skill works with whatever the user provides.

### Writes

| File | What it contains |
|------|-----------------|
| brand-voice.md | The complete voice profile |

### Context Loading

1. Check whether `./brand/` exists.
2. If it exists, read all files present. Summarize what was found and how it will shape the profile.
3. If `./brand/` is empty or doesn't exist, proceed without brand context. The voice extraction works standalone.

---

## Iteration Detection

Before starting any mode, check whether `./brand/brand-voice.md` already
exists.

### If brand-voice.md EXISTS → Update Mode

Do not start from scratch. Instead:

1. Read the existing profile.
2. Present a summary of the current voice (summary, "We Are / We Are Not" table, tone spectrum).
3. Ask what to change:
   - Refine the tone (adjust the spectrum)
   - Update the identity table (add/change "We Are / We Are Not" rows)
   - Update vocabulary (add/remove words)
   - Add new content samples (re-extract)
   - Full rebuild (start from scratch)
   - Auto-scrape for fresh data
4. Process the chosen update. Before overwriting, show what changed and ask for confirmation.

### If brand-voice.md DOES NOT EXIST → Mode Selection

Proceed to mode selection below.

---

## Mode Selection

Ask the user which mode fits their situation:

1. **I have content I'm proud of** → Extract mode (paste it in)
2. **I'm starting fresh** → Build mode (strategic questions)
3. **I have content but want to evolve** → Build mode (with existing content as reference)
4. **Here's my URL** → Auto-Scrape mode (automated research)

If the user provides a URL in their initial message, skip mode selection
and go directly to Auto-Scrape.

---

## Mode 1: Extract

### What to Analyze

Request 3-5 pieces of content the brand considers representative:
- Website copy (especially About page, homepage)
- Emails they've sent
- Social posts that performed well
- Newsletter editions
- Blog posts they're proud of
- Video or podcast transcripts

### 6-Dimension Analysis

Analyze every piece across these dimensions:

**1. Tone Patterns**
- Formal ↔ Casual (contractions, slang, sentence fragments)
- Serious ↔ Playful (humor, lightness, gravity)
- Reserved ↔ Bold (hedging vs. strong claims, confidence)
- Distant ↔ Intimate (we/they vs. I/you, personal stories)

**2. Vocabulary Patterns**
- Industry jargon level (heavy, light, translated)
- Signature words or phrases they repeat
- Words they avoid
- Profanity or edgy language tolerance
- Formal words vs. everyday words

**3. Rhythm Patterns**
- Average sentence length
- Paragraph length
- Mix of short punchy vs. longer flowing
- Fragment usage
- List usage

**4. Structural Patterns**
- Opening style (story, question, bold statement)
- Transition style (smooth, abrupt, conversational)
- Closing style (CTA, summary, open loop)
- Header and formatting preferences

**5. Personality Signals**
- Confidence level (self-deprecating vs. authoritative)
- Stance (teacher, peer, rebel, guide, insider)
- Polish level (raw vs. polished)
- Optimism vs. realism
- Reference and example style

**6. POV Patterns**
- First person (I vs. we)
- Reader address (you, folks, friends, readers)
- Direct address vs. general statements

### Synthesis: From Dimensions to Identity

After the 6-dimension analysis, synthesize findings into the "We Are / We
Are Not" table. This is the critical translation step — moving from
observed patterns to an actionable identity anchor.

For each strong pattern found:
1. Name the voice attribute it reveals (e.g., "Bold" from low hedging + strong claims)
2. Define what it means in practice (the "We Are" column)
3. Define the boundary — the overextension to avoid (the "We Are Not" column)
4. Note which content pieces provided evidence

Target 4-7 rows. Each row should be supported by evidence from at least
one content piece. Assign confidence per row:
- **High** — Pattern appears consistently across 3+ pieces
- **Medium** — Pattern appears in 1-2 pieces
- **Low** — Inferred from a single signal or absence

Then proceed to building the full voice profile (template below) and the
Voice Test Loop.

For detailed scoring rubrics, see
[Voice Extraction Patterns](references/voice-extraction-patterns.md).

---

## Mode 2: Build

### Strategic Questions

Ask these in natural conversation, not as a checklist. Group by theme:

**Identity (who you are):**
1. What are 3-5 words that describe your personality?
2. What do you stand for? What's your core belief about your industry?
3. What's your background? What shaped how you see things?
4. What makes you genuinely different from others in your space?
5. What are you explicitly NOT? What should you never sound like?

**Audience (who you're talking to):**
6. Who are you talking to? Be specific.
7. What tone resonates with them? What do they respond to?
8. What would make them trust you? What would turn them off?

**Positioning (where you stand):**
9. Are you the expert, the peer, the rebel, the guide, the insider?
10. Where do you sit on accessible ↔ exclusive?
11. Where do you sit on approachable ↔ authoritative?

**Aspiration (who you admire):**
12. Name 2-3 brands or people whose voice you admire. What specifically do you like?
13. What do you explicitly NOT want to sound like?

**Practical (specific preferences):**
14. Any words or phrases that are signature to you?
15. Any words or phrases you hate or want to avoid?
16. How do you feel about humor? Profanity? Hot takes?

### Build Process

From the answers:
1. Synthesize into the "We Are / We Are Not" table — each row derived from answers, especially questions 1-5 and 12-13
2. Define tone spectrum — where they land on each of the 5 dimensions
3. Build the tone-by-context matrix — how tone flexes for blog/SEO, email, social, landing pages
4. Set vocabulary rules — words to use, words to avoid
5. Establish rhythm — sentence/paragraph patterns
6. Create examples — sample phrases that embody the voice, annotated with which "We Are" attributes they demonstrate
7. Define boundaries — what's off-brand (from the "We Are Not" column)
8. Assign confidence — Build mode is typically High confidence since the user stated preferences directly

If the brand has strong style or terminology preferences (Oxford comma,
product name capitalization, jargon rules), see
[Voice & Style Guide](references/voice-and-style-guide.md).

After building, proceed to the Voice Test Loop.

---

## Mode 3: Auto-Scrape

Auto-Scrape requires web search capability. If unavailable, fall back
gracefully to Extract or Build mode.

### Process

**Step 1: Gather content** from the provided URL:
- Homepage copy
- About page
- Recent blog posts (2-3)
- LinkedIn bio and posts (search `site:{domain} linkedin.com`)
- Twitter/X bio and tweets (search `site:{domain} twitter.com`)
- Any podcast appearances, interviews, guest posts

Report what was found and total word count before proceeding. Flag source
quality:
- **Rich** (>2,000 words across 3+ sources) — enough for High confidence extraction
- **Moderate** (500-2,000 words) — Medium confidence; supplement with questions
- **Thin** (<500 words) — Low confidence; fall back to supplementary questions

**Step 2: Feed into Extract** — run the full 6-dimension analysis on all
gathered content. Synthesize into the "We Are / We Are Not" table with
confidence ratings per row based on source quality.

**Step 3: Ask supplementary questions** to fill gaps the scrape can't
answer:
1. Is there anything about your current voice you want to change?
2. Any words or phrases you love or hate that might not show up in public content?
3. Who do you admire voice-wise?
4. What should you explicitly never sound like?

Merge supplementary answers with the extraction — user-stated preferences
override inferred patterns and upgrade confidence to High. Produce the
final profile. Then proceed to the Voice Test Loop.

### Insufficient Content

If scraping yields fewer than 500 words, fall back gracefully:
- Show what was found and what's missing
- Offer to supplement with pasted content (Extract) or strategic questions (Build)

---

## Tone-by-Context Matrix

After defining voice constants and the tone spectrum, build the context
matrix — how tone flexes for different content types across three
dimensions (Formality, Energy, Technical Depth).

### Default Matrix (starting point — adapt per brand)

| Context | Formality | Energy | Technical Depth | Key Principle |
|---------|-----------|--------|-----------------|---------------|
| Blog/SEO article | Medium | Medium | Medium-High | Teach, don't lecture |
| Email newsletter | Medium | Medium-High | Low-Medium | Personal, value-forward |
| LinkedIn | Medium-High | Medium | Medium | Professional insight |
| Twitter/X | Low-Medium | High | Low | Brevity and personality |
| Landing page | Medium | High | Low-Medium | Benefits, not features |

Adapt based on the brand's tone spectrum. A bold, casual brand shifts
toward lower formality and higher energy. A reserved, technical brand
shifts the other way.

For level definitions and enforcement guidance, see
[Voice & Style Guide](references/voice-and-style-guide.md).

---

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **High** | 3+ corroborating sources OR explicit user statement |
| **Medium** | 1-2 sources OR inferred from patterns |
| **Low** | Single source OR assumption from indirect evidence |

Score each major section of the profile. User-stated preferences always
count as High. For Medium/Low sections, note what would raise confidence.

---

## Voice Profile Output

This is the template for `brand-voice.md`. Every profile should cover
these sections. Adapt detail level to what the extraction or build
reveals — not every field needs to be exhaustive, but every section
should be present.

```markdown
# {Brand/Person Name} — Voice Profile

> Last updated: {YYYY-MM-DD}

## Voice Summary

{2-3 sentences capturing the essence. What does this voice FEEL like?}

## We Are / We Are Not

The brand identity anchor. Voice stays constant across all content.

| We Are | We Are Not |
|--------|------------|
| **{Attribute 1}** — {what this means in practice} | **{Counter 1}** — {the boundary we don't cross} |
| **{Attribute 2}** — {what this means in practice} | **{Counter 2}** — {the boundary we don't cross} |
| **{Attribute 3}** — {what this means in practice} | **{Counter 3}** — {the boundary we don't cross} |
| **{Attribute 4}** — {what this means in practice} | **{Counter 4}** — {the boundary we don't cross} |

{4-7 rows. Each row should be defensible from the extraction or build.}

## Tone Spectrum

| Dimension | Position | Notes |
|-----------|----------|-------|
| Formal ↔ Casual | {position} | {specifics} |
| Serious ↔ Playful | {position} | {specifics} |
| Reserved ↔ Bold | {position} | {specifics} |
| Simple ↔ Sophisticated | {position} | {specifics} |
| Warm ↔ Direct | {position} | {specifics} |

## Tone-by-Context Matrix

Voice stays constant. Tone flexes by context across three dimensions:

| Context | Formality | Energy | Technical Depth | Key Principle |
|---------|-----------|--------|-----------------|---------------|
| Blog/SEO article | {level} | {level} | {level} | {principle} |
| Email newsletter | {level} | {level} | {level} | {principle} |
| LinkedIn | {level} | {level} | {level} | {principle} |
| Twitter/X | {level} | {level} | {level} | {principle} |
| Landing page | {level} | {level} | {level} | {principle} |

## Vocabulary

**Words/phrases to USE:**
- {word/phrase} — {why/when}

**Words/phrases to AVOID:**
- {word/phrase} — {why}

**Jargon level:** {Heavy / Moderate / Light / Translated}
**Profanity:** {Yes / Occasional / Never}

## Rhythm & Structure

**Sentences:** {length and style patterns}
**Paragraphs:** {length patterns}
**Openings:** {how they start pieces}
**Formatting:** {headers, lists, bold, emoji preferences}

## POV & Address

**First person:** {I / We / Mix}
**Reader address:** {You / Direct name / Folks / etc.}
**Relationship stance:** {Teacher / Peer / Guide / Insider / Rebel}

## Blog/SEO Calibration

How the base voice adapts specifically for long-form search content:

- **Depth:** {how personality carries at 1,500-2,500 words}
- **Structure:** {headers, lists, section patterns for scannability}
- **Jargon handling:** {no jargon without explanation; translate for search}
- **Rhythm at length:** {how to maintain voice over longer pieces}
- **Personality balance:** {voice present but not performing — teaching, not entertaining}
- **Typical lengths:** {standard posts 1,500-2,500 words; pillar content up to 4,000}

## Example Phrases

**On-brand (sounds like us):**
- "{example}" — *Voice: {which "We Are" attributes are active}*
- "{example}" — *Voice: {which "We Are" attributes are active}*
- "{example}" — *Voice: {which "We Are" attributes are active}*

**Off-brand (doesn't sound like us):**
- "{example}" — *Crosses: {which "We Are Not" boundary}. Better: "{fix}"*
- "{example}" — *Crosses: {which "We Are Not" boundary}. Better: "{fix}"*
- "{example}" — *Crosses: {which "We Are Not" boundary}. Better: "{fix}"*

## Do's and Don'ts

**DO:**
- {specific guidance}
- {specific guidance}
- {specific guidance}

**DON'T:**
- {specific guidance}
- {specific guidance}
- {specific guidance}

## Confidence Notes

- **Strong (High):** {list sections with solid evidence}
- **Inferred (Medium):** {list sections + what would strengthen them}
- **Assumed (Low):** {list sections + recommendations to validate}
```

---

## Voice Test Loop

After generating the profile from any mode, validate before saving.

### Generate 3 SEO-Calibrated Samples

Using the voice profile, write three samples tuned for blog/SEO content:

1. **Blog intro paragraph** — the first 3-4 sentences of an SEO article.
   Demonstrates the opening style, hook, and tone.
2. **Explanatory section** — a mid-article section teaching a concept.
   Shows how the voice handles depth and instruction.
3. **CTA/closing** — the final paragraph with call to action. Shows how
   the voice handles urgency and next steps.

Annotate each sample: note which "We Are" attributes are active and what
tone settings (Formality/Energy/Technical Depth) are applied. This helps
the user see enforcement in action and give targeted feedback.

### Collect Feedback

Present the samples and ask: does this sound like you?

- **Yes, nails it** → save the profile
- **Close but needs adjustment** → ask what feels off (tone? vocabulary?
  rhythm? identity?), adjust the profile, regenerate samples, re-test
- **Not quite right** → ask for an example of what sounds right, or offer
  to switch modes. Re-extract or rebuild the off sections.

### Iteration Limit

After 3 rounds without confirmation, offer:
- Save current version (can always re-run to refine)
- One more round with specific fixes
- Start over with a different mode

---

## File Output Protocol

After the voice test loop passes:

1. Create `./brand/` directory if it doesn't exist.
2. Write the complete voice profile to `./brand/brand-voice.md`.
3. If overwriting an existing file: read the existing file, show what
   changed, and confirm before saving.

---

## References

Load when needed:

- [Voice Extraction Patterns](references/voice-extraction-patterns.md) — Scoring rubrics for the 6 extraction dimensions, corpus requirements, cross-platform consistency
- [Voice & Style Guide](references/voice-and-style-guide.md) — Tone flex definitions, enforcement procedure, style rules, before/after examples
