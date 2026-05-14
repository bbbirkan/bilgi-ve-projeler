---
title: "This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)"
source: "https://www.youtube.com/watch?v=WNru_PFycT8&t=71s"
author:
  - "[[Better Stack]]"
published: 2026-04-29
created: 2026-05-09
description: "If you’re using AI coding tools like Claude Code or Cursor on anything bigger than a small project, you’ve probably run into the same problem: massive token ..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WNru_PFycT8)

## Transcript

### Why AI Coding Tools Break on Real Projects (Token Problem)

**0:00** · This might be one of the most insane ways to bring your code base to life. If you're using Claude code or cursor on a real project, you'd think the hard part is writing code. Well, it's not. The hard part is just understanding your own repo. You ask one question and your AI is burning through your tokens just to figure out what's going on. It's slow, it's expensive, and half the time still wrong. What if instead of sending your whole project every time, you gave the AI a map of it? That's exactly what Graphy does. And it can cut token usage by over 70%.

**0:31** · Let me show you how all this works.

**0:39** · Right now, your AI sees your project like this, just a pile of files. There's no real connections, there's no structure, there's no memory. So, every time you ask a question, it has to relearn everything from scratch. That's why answers feel close, but not quite right. And yeah, this is exactly what Carpathy pointed out when the raw folder problem. Graphy showed up right after that. It's more of a memory layer. If you enjoy coding tools and tips like this, be sure to subscribe. We have videos coming out all the time. All right, now let me show you.

### The Hidden Cost of AI Coding: Tokens, Context, and Hallucinations

### Live Demo: Turn Any Repo Into a Knowledge Graph (Graphify)

**1:11** · I've got a small repo here, code, docs, and diagram. Now, normally I'd have to explain all this to AI every time.

**1:20** · Instead, I run one command, Graphy, right here. Give it a second. Now, look at this. After Claude executes Graphy, this isn't just files anymore, it's an actual graph. Everything is connected. I can click and dissect actually what's going on and what is linked together to just here within the HTML file that it generated. Then, instead of asking AI to read everything again, I can now ask it, "What connects off to the API layer?"

**1:50** · And now it answers using relationships, using the MD file that it generated with this call. It's not guesses, it's relationships. And here's the part that surprised me. Before this, around 14,000 tokens, okay, however many were used.

**2:04** · After this, after it executes the first time, we drop that down to maybe a couple hundred. Same question, completely different cost. All because of this generated map. So, what is this actually doing? Graphy is basically like Google Maps for your code base. Instead of raw text, you get nodes and connections. Under it all, it uses tree-sitters to understand the structure, then an LLM to extract the meaning. Then, it can group everything into clusters and it's not just code.

### What Is Graphify? (AI Knowledge Graph for Codebases Explained)

**2:32** · It reads PDFs, diagrams, even audio and video. All locally, nothing leaves the machine. What you get from this is simple. We get a visual graph, a written report, and a knowledge base we can actually explore. This visual graph is huge for a lot of us as we can see how things connect. Now, here's where this changes how AI coding usually works.

### How Graphify Works (Tree-sitter, LLMs, Graph Clustering)

**2:57** · Most tools use rag, which basically means find similar chunks of text. Well, Graphy doesn't do that. It builds real relationships. This function calls that one. This module depends on that. This idea came from this document. And it even tells you how confident it is. So, instead of this looks related, we get something like this is actually connected in an actual visual representation of what is connected. And the biggest difference here, it remembers too since it generated us that MD file, it can look back on.

### Graphify vs RAG: Why Similarity Search Fails for Code

**3:28** · We're not starting from zero every time. It updates only what's changed, so your AI finally has context that sticks. All right, now I actually thought all this was pretty sweet. But what are the good and the bad things here? And now, first up to the plate, the efficiency compounds. Every question gets cheaper, and because it connects code, docs, diagrams, you start finding relationships you didn't even know existed. That's huge for onboarding for these messy projects that we get dumped into. That's great.

### Graphify Pros: Token Savings, Multi-Modal Support, Better Reasoning

**3:59** · Now, the drawbacks to all this are this. The first run can be slow and cost tokens, especially with a lot of documents. After that, it's cached, but yeah, that first hit is real. It's also early, so long-term support is still unknown. And small thing, when you install this, it's Graphy with two Ys, not one. So, check your spelling on that. The relationships aren't always perfect, but it labels them clearly, extracted, inferred, and biguous, so you know what you can actually trust.

### Graphify Cons: First Run Cost, Accuracy Limits, Early Stage

**4:29** · And if your repo is tiny, this is going to be somewhat of an overkill. So, is it worth it? I mean, yeah, if you're using AI on anything real, this is cool. It's I thought it was worth it. Because your biggest problem isn't running the code, it's actually understanding it across files, across time, across context. And that's exactly what this fixes. The token savings alone make it worth trying, but the bigger win is this. Your AI stops guessing and starts reasoning. If you're working solo, doing research, or have all these big systems, this is a serious upgrade.

### Is Graphify Worth It for Developers?

### Final Thoughts

**5:01** · If you're just working on smaller scripts, this is probably just an overkill, so you don't really need to try it. But most have to try this, this is going to be an awesome tool. If you enjoy coding tools and tips to speed up your workflow, be sure to subscribe to the Better Stack channel. We'll see you in another video.