---
title: "Graphify: Instant Knowledge Graph for Claude Code/Antigravity (FREE)"
source: "https://www.youtube.com/watch?v=BkHps04qGgc&t=74s"
author:
  - "[[FuturMinds]]"
published: 2026-04-15
created: 2026-05-09
description: "Claude Code / Antigravity + Graphify = Instant Knowledge Graphhttps://github.com/safishamsi/graphifyFor business enquiries: ai@futurminds.com🔗 My Resources:..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=BkHps04qGgc)

## Transcript

### Why Claude Code Reads Your Files Every Session

**0:00** · Let's say you're working on a project in Claude Code. You have just opened a new session and you want to understand the codebase before building something new. So you ask a question. What does browser-use do? Give me a one-line summary of each major component. It's a very simple question. And now watch what happens. Before it answers a single word, it reads the project readme to figure out what kind of project this even is. It goes through multiple files. It builds a mental model from scratch. Reading through your codebase file by file, and every one of those reads costs money.

**0:30** · And the answer you get is only as good as what Claude managed to find in those reads. Now, here's the issue. If you close that session and open a new one tomorrow, Claude starts from zero again. No memory of what it read, no map of how the files are connected.

**0:46** · Every session, it rebuilds the same understanding from scratch. It burns the same tokens, makes the same searches, re-reads the same files every time. There's a tool that fixes this. It's called Graphify.

**0:58** · It reads your project once, builds a knowledge graph of how everything connects, and Claude reads that graph at the start of every session.

**1:06** · Instead of re-reading your files. Let me show you how it works — and then I'll show you the actual numbers from running ten questions in two identical sessions.

### What Graphify Does for Claude Code

**1:14** · Here's the simplest way to understand what just happened. So you can think of a Claude session as a new hire that shows up on their first day.

**1:21** · They have never seen the project, and they have to read through everything before answering a single question. And every new session means a new hire.

**1:29** · Graphify builds the senior colleague — someone who already has the map, who already knows where the decision logic lives, which components talk to each other, and which five components are the hub that everything routes through. You build that map once, and Claude reads it at the start of every session automatically. And that's the whole idea.

**1:47** · And it's not just for code. It also works for research papers, meeting recordings, strategy documents, or any kind of mixed content.

**1:55** · I'll come back to that, but first let me show you exactly how it works under the hood. This tool shipped 48 hours after Andrej Karpathy, co-founder of OpenAI, described exactly what it should do. Currently, it has almost 25,000 stars. There are three passes, and that's the whole system. First pass analyzes the code structure. If your folder has Python, TypeScript, Go, Rust, or anything with real syntax, Graphify runs a code parser across every file. It reads every class, every function, every import, every call.

### Graphify Architecture: 3 Passes Explained

**2:27** · This runs entirely on your machine. No external API calls are made, no tokens are used. It extracts hard facts — this function calls that one, this class imports this module. Facts, not guesses.

**2:39** · Second pass analyzes the audio and video.

**2:43** · If you've got meeting recordings, tutorials, or YouTube URLs, Graphify transcribes them locally using Faster-Whisper, which is also free. Third pass: it scans everything else — markdown, PDFs, images, readme files, docs, et cetera. Claude sub-agents run in parallel, extract concepts and relationships and figure out what things mean and how they connect with each other. Pass three is the only part that touches Claude's API and it only runs once. After that, every session reads the cached graph for free. Everything merges into one graph.

**3:17** · An algorithm groups related concepts into neighborhoods.

**3:21** · You can think of them as departments. Every time you open a new conversation or session, before Claude reads a single file, that hook fires and Claude reads a summary of the entire graph. Then it makes two or three targeted reads instead of fifteen. And that's where the savings come from.

### Real Token Savings Test: 10 Questions

**3:37** · Now, does this actually save tokens? I ran ten questions in two identical sessions to find out. Same project, same ten questions, asked in the same order. The session on the left is not using Graphify, the one on the right is using Graphify. Let me run all ten questions.

**3:59** · Now, if we check the context usage in both of these sessions, the session without Graphify is using 120,000 tokens and the one using Graphify is using 113,000 tokens. So it's not a big difference, probably less than 8%.

**4:16** · However, if you look at the questions and their replies, I think the quality of responses in the session using Graphify is better than the one which is not. So if you look at this question, both of these found that there are three phases. But on the left it simply mentions these three functions as phases.

**4:34** · But on the right it has explained phase one in detail, and similarly phase two and phase three it has also added details about loop detection and replanning, et cetera.

**4:46** · If we look at Graphify's GitHub repository, you will see these worked examples where they're claiming that they achieved 71.5x reduction. So why did our sessions look more like 7 to 8% reduction? I'll explain exactly what that benchmark actually measures and when the big savings are. But first, let's see how to set it up.

### How to Install Graphify Step by Step

**5:06** · You can scroll down to the install section, then copy this command, go to your project, open a terminal, paste and run.

**5:14** · If you are on Windows you will see this error. It's because double ampersand is not recognized. So you can simply run each of these commands separately.

**5:23** · First, let's run pip install graphifyy — double y. It's complete.

**5:26** · Now let's run graphify install. And this is now ready. By the way, if you are using other platforms like Codex, Opencode, et cetera — you can copy the corresponding command from here and replace the graphify install with it. Once that is done, we want our Claude Code to use Graphify in every session without us asking to do it. And to set it up we need to run this command: graphify claude install. And it is done. Now we can start a new Claude session and run Graphify.

**5:59** · So this is a new session. Now let's run slash graphify.

**6:02** · Alright, so it has found a corpus of 357 code files, 53 docs and seven images.

**6:11** · There is a threshold of 200 files in one go, so it's asking us to select subdirectories for which we want to create the graph.

**6:18** · Let's select browser-use and examples.

### Graph Output and How to Update It

**6:24** · Okay, so it took around 12 minutes to complete and here's what we get. There's a new directory called graphify-out.

**6:32** · It contains GRAPH\_REPORT.md. It has identified 4,041 nodes, 20,900 edges and 185 communities. We also get this graph dot HTML and if you open it in a browser, this is what you're going to see.

**6:46** · On the right hand side we have the list of communities that it has identified and by default all of these are selected. So you can deselect any of these by clicking on that community. Each dot in this graph is a concept, a class, a function, a documented idea — and each line is a relationship between two dots or two concepts. The colors are neighborhoods, and the bigger the dot, the more things connect to it. Now, building this entire graph was really cheap and we just need to build it once and then Claude has access to this entire graph.

**7:18** · It can easily understand how things are connected so that it can selectively read those relevant docs instead of blindly going through a large number of docs. Now, when you're working on your project, you're of course making changes, adding new files, making code changes, et cetera. And you want to keep that graph in sync. To do that there are a couple of options. One is you can simply run graphify update. And it will automatically identify what changed from the previous run and update your graph.

**7:46** · Or you can run graphify hook install, and this will wire up git hooks. The graph rebuilds automatically if there is a new commit or when you switch your branch, and it has been set up successfully.

### Real-World Impact + 71x Claim Debunked

**7:59** · Now here's what this actually means for your day to day. Every time you open a new Claude session on any project where you have run Graphify, that graph report gets read first automatically.

**8:10** · You don't type anything special, you don't run a command — you just ask a question and Claude already has the map. The seventy-one times claim.

**8:18** · Here's what it actually measures. The benchmark took a 52-file corpus — three repos, five papers and four images. The naive approach: loading all 52 files directly into Claude's context at once — that costs around 123,000 tokens. Whereas Graphify's approach is to first read that graph file and only go through the relevant neighborhoods in the graph, and it consumed only 1,700 tokens per query. And that ratio is 71.5 times.

**8:47** · But here's the thing: nobody works by pasting 52 files into a Claude conversation. In real Claude Code sessions, you will probably tag your folder and start asking questions. You will never tag a large number of files because you wouldn't know where to look. So that 71 times benchmark is comparing against a workflow most people don't actually use.

**9:08** · So this number doesn't really make sense. Your savings will be considerable if you're working on mixed projects that contain code plus docs, or if you are working on long sessions, or if you have large projects. If your project has more files, Claude would otherwise search through more files, but with the graph it can reduce that search. So what Graphify actually gives you in Claude Code is fewer wrong-direction file reads, better answers from the first message, and savings that grow with session length. This isn't only for code projects.

### Graphify for Research, Content, and Business Folders

**9:40** · I ran Graphify on a folder of YouTube scripts, transcripts and research notes.

**9:44** · There was no Python or JavaScript, just Markdown and text files.

**9:48** · And I asked questions like what topics I have covered most and what's missing in my content on this subject, et cetera. And it answered using the graph, not by reading every file. And it's the same idea for research folders.

**10:00** · You can point it to a stack of PDFs or papers and Claude can start making connections across all of them. You can have just one connected map for all of your meeting recordings, strategy docs and client files.

**10:12** · And the short version is: if Claude keeps reading the same things over and over in your sessions, Graphify is worth running. So if you're using this for a research vault or business planning folder, it's definitely worth it.

**10:24** · I hope you found the video useful, and I would love to know your thoughts and experience on this. Don't forget to like the video and subscribe to the channel and I'll see you in the next one.