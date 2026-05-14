---
title: "I Gave Pi Access to Obsidian And I'm Not Looking Back"
source: "https://www.youtube.com/watch?v=JnQcPzjC6Vo"
author:
  - "[[DevOps Toolbox]]"
published: 2026-05-08
created: 2026-05-09
description: "Big thanks to Oracle AI for sponsoring this video! Check out their recent post on agents memory: https://fandf.co/4dd3HOw---Obsidian was always my favorite n..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=JnQcPzjC6Vo)

## Transcript

**0:00** · This recent Anre Karpathy post was a bit of a light bulb moment for me. It talks about the strong link between LLMs and knowledge base or in simple words AI and your second brain. It's a simple three layered cake. Taking notes, have a place to read them and then Q&amp;A on an ongoing basis. Simple but it gets complicated if you dive in. Agents don't really have a good place to put pieces of information that we will actually use later. Chat history is not only memory. It has some lessons learned, right? Some for the agent, sure, but some for you, the slave. I mean, the user.

**0:30** · Many people just ask it to create a summary MD file, but that's not a knowledge system. If you tell them to store information they gathered as MD files in a central place, just like you're asking them to store code in Git repos, you now have your own handwritten notes along with knowledge you've read as LLM responses, but never actually captured. It can now be stored in your second brain. Now, you can review this information with Obsidian.

**0:56** · By doing that, you're kind of treating it as your IDE. It's used to review and edit LLM text. See the connection? Now, you can start asking your second brain questions. And that is exactly why Obsidian's new CLI is so interesting.

**1:10** · And on top of that, I added another open source to bring this concept to life, but on god mode. Because the goal here isn't LinkedIn fluff. It's actually getting around my own personal second brain and using it. So, this video is not just Obsidian runs in the terminal.

**1:24** · Now, that's cool. Not the point. The point is Obsidian might be the perfect interface layer between you and your agents. And we're going to take it from this to well this a contextaware system.

**1:37** · Let me show you.

**1:44** · Let's first get the thing to try out before we dive deeper into what we can do, but more importantly, how to do it.

**1:50** · If you've upgraded Obsidian recently, you have noticed this. an Obsidian command line interface where you can pretty much do anything you like with Obsidian through the terminal.

**2:00** · Obviously, the point isn't regular note-taking, but rather scripting, automation, and integrating with tools.

**2:06** · You'd want the latest Obsidian installer downloaded and updated to the latest release. Next, head over to your settings or command comma for Mac users where you'll now see a command line interface activation on the bottom. This button is helpful, but I can tell you it doesn't always do the full job and you may head over excited to your terminal just to see obsidian command is not found. Not to worry, the CLI is now under the Obsidian app path, but an executable called Obsidian CLI, which you can sim to local bin. That's it. Pop it open.

**2:38** · Oh, and make sure Obsidians open at the same time to see the same vault welcoming you. It's not fancy. It does look like they've used Charm to build it. and it's a list of commands that you can find and use. You can start simple and create a daily note with thoughts, journaling, and tasks. If you use these, the syntax alone here already feels like it's not intuitive or userfriendly, if I may. You have to set some commands and add parameters like it's a curl request. Nevertheless, new note from the CLI.

**3:06** · You can read it directly and if you pop Obsidian, you'll see the same note waiting for you opened. You can keep appending content to your note like so. and the syntax would get translated to proper markdown like Obsidians to-do/done lists, but writing notes from the CLI is not very exciting. Sure, it's very helpful for the agent, which will soon connect, but let's talk about searching. If you search for something like meeting nodes and it finds a bunch, some not exactly what you'd expect from this kind of a search term. Here's why.

**3:37** · Before the CLI, your agent searches like this with GP, RIP GP, or even worse, just scanning files manually. That gives you raw matches, no structure, no ranking unless you built it. And of course, no awareness, nonobsidian semantics, so fast but dumb. With the CLI, instead of here are 200 lines that match Kubernetes, you get something closer to note titles, relevant matches. That means your agent can pick notes, not lines. Obsidian search isn't just text search.

**4:07** · It understands your notes tags, the path in the vault, your font matter fields, the entries on top of your notes. And lastly, probably the most important bit of everything, understanding links. Now, if you actually want to read one of these findings, you'll be very disappointed to find this UIX was not made for you. I mean, you'd expect at the very least that the results are fed into a fuzzy list, but nope. Not even auto completion. When you do get the name right, literally provide the full name or path to use. You can view it directly or have it pop up in Obsidian.

**4:36** · One thing I keep noticing with AI tooling is that people reach for bigger models before fixing the surrounding system. If your agent has weak memory pool retrieval or no useful grounding, a larger model usually just gives you more expensive confusion. I was reading through Oracle's developer resources and two things stood up. One was getting more out of your smaller language models. The other was agent memory and why so many agents lose context once a task gets a bit longer.

**5:04** · That feels much closer to the real engineering problem than generic AI hype. If you're building internal tools, copilots, or automations, the real leverage usually comes from better context, better memory, and better data flow, not just swapping in a larger model and hoping for the best. If you want to dig into that side of the stack, Oracle has a developer resources page with articles, code, and examples worth browsing. link in the description. Thank me later. And now back to the video. Some commands just shorten the path for automation.

**5:32** · So if your tasks are built into daily nodes, and they should, we can talk about that another time. You can get them very quickly. Like so. These are daily tasks. If you just go tasks, well, you'll see every single task in your system. You can filter by file. You can actually get the ones that are done or in to-do or any status you've set.

**5:52** · A morning automation script can open the daily note, then add a to-do line to check your notes inbox, which is a critical step in the power method if you're following the second brain structure. And you could also tell your procedure to follow up on unresolved items. Now, this is where intent starts showing. You can find links and back links for notes, which basically gives you the mental model of a graph to work with, allowing an automation that collects data to search, but also forge knowledge. Hear me out.

**6:21** · Links are part of what makes note-taking in Obsidian, Notion, and other similar systems so good. You can use them to break down notes or simply link to other relevant written pieces. Implementing the PAR method in Obsidian or Notion relies heavily on these links. You link a resource to a project or an area and maybe another resource. You've made the connection because it makes sense. You can now hand over that information to your automation or AI or what have you.

**6:50** · When you ask the information, the context is not only bigger, it's smarter. When you create knowledge, bringing up the karpathy post again, you let the agent give you context. Starting to get it? There are some fun ones, too, like a random read node that you can have your personal assistant fetch for you every morning or just add it to the morning script. This is a real way to slowly recall old yet relevant notes over time. But if there's one thing that LLMs absolutely suck at is understanding visual concepts.

**7:19** · If you're debugging or building a plug-in or just want to fix workflows in Obsidian using an agent through the CLI, its API is exposing a screenshot that you can take on demand, exposing the full UI, open notes, tabs, menus, whether collapsed or expanded, adding context to the flow you're trying to achieve with an agent running underneath.

**7:39** · Now, if for whatever reason you are picking up notes on your own as a user through the terminal, I've recently shared a video around TV, a fuzzy searchable TUI where you can just pipe over your Obsidian files and enjoy a quick retrieval from the comfort of your terminal. My god, that was a nerdy sentence. I need to put that on a t-shirt. TV also has channels where you can configure the preview and different actions with key bindings. like you'd probably want a key to pop a note to neim and another to open it on Obsidian or other actions that you can take with the CLI like tagging, aliasing, etc.

**8:12** · More about TV in the video on the channel. Now, we've been dancing around the CLI. It's time to actually let the agent use it. Another video I recently made was around Pi, a LIN agent I've been falling in love with recently. So, I'll head over to its packages repo and grab PI Obsidian, a small extension that adds a skill for the Obsidian CLI. You can install it with pi install command or be me and let it figure out stuff on its own which is an incredibly inefficient token usage and just like that it's now on top of the CLI.

**8:39** · By the way, one of the beautiful things about Pi is its ability to change itself according to your needs. So earlier I asked it to teach itself about the Obsidian CLI. After installing the extension package, I actually asked it to compare the two solutions. And until it gives us the result, we can use Pi's on demand inline session to query my Obsidian Vault already. Now, mind you, this took 20 seconds, not ideal, but in my defense, I am running highest reasoning model here, which may force its hands trying to overkill a simple task.

**9:10** · Regardless, the note is opened, and Pi realized it had done a better job itself by wrapping around the CLI, so it kept its own thing and removed the extension. the CLI in our tool belts and the agents. You can script around it, pipe results to your favorite toes and enjoy notes through the terminal, but we've mentioned tokens usage a lot earlier. Both the fact that the CLI should improve the consumption, but also the quality of usage. Just scanning files is fine, but not extremely efficient. The CLI improves capturing notes and improves the results.

**9:38** · But if we take a quick look again at Karpath's previous LLM post, we're now at stage three, Q&amp;A. We want to query the knowledge base and maximize both docking usage and quality of results. Someone actually went ahead and built it. Graphy graph graphi is a knowledge graph for coding assistance. And I'm pretty sure this was designed for code repos. So you can improve the questions on top of these like how the authors implemented where's the data layer and so on.

**10:06** · It uses tree sitter and every context it can find to build a graph that should reduce up to 70 times token usage. Now that graph made me think of this immediately. So I thought what the hell let's run it run on my notes fold pex install graphifi with two Y's and you can start working. If you run install it'll create a claude skill and instructions but I'm not a cloud fan.

**10:29** · It comes with installations for Gemini cursor codeex open code ader if someone still uses that copilot vs code claw her even AWS has attempt at an IDE kira hero is here long list no pi if I pick open code and check the instructions they added a reference to graphifi out directory and a request to check the graph report and index then update when necessary if you're a pi user someone took care of that for you and there's a graphifi pi package ready that adds roughly the same workflow to pi.

**11:01** · It'll use the same outpat remind the agent to traverse it before any search etc. Pi installed. Give it a minute and we're good to go. We now have graphifi and a matching skill because the extension ships with both. You can use the command from pi or a generic skill command. If you let it run with no instructions, it'll just print the commands itself and other options. But we want actual work.

**11:26** · Let's build a graph mister. And after a minute, get this. It actually stopped itself because it's past the intended size. Like I mentioned, this was made to provide answers to relatively small repos with a bunch of files in the system. I'm forcing its hand into something massive. So, let's do the entire vault, and I'll try to show you the result in hopes my Mac doesn't start smoking. Over 5 minutes later, we've got a report, a JSON, wiki index, and other stuff. The report, while a bit much to go into, looks for what's described as god nodes, the nodes with most edges.

**11:59** · most well connected. It also lists surprising connections like launching a course note that I have is semantically similar to what's devops. Then there are tags and many other indexes cohesion calculations of found notes. But here's the fun part. Graph HTML opens this. And while it's beautiful, I don't think you'll learn anything by just watching it. What you can however do now is run explain a topic and the system would yield connections for that context. This is basically a reasoning layer that checks the graph and adds a touch of context.

**12:31** · If you want proper answers to questions, you can query things like everything I know about Kubernetes.

**12:36** · You'll get all the relevant nodes ready to compile a response. When you finally actually do it from the agent, you'll get the response you're looking for, properly structured for review, references, and everything you like.

**12:48** · Lastly, while I'm not one to get excited about benchmarks, surely not from the tool we're benchmarking, Graphifi comes with its own internal benchmarking tool that tries to analyze reduction of tokens per query based on the index and the graph it's generated. In our case, not the 70x promised, but again, this is a knowledge base, not a repository. You be the judge. At this point, you might ask, why not use one of the million AI note-taking tools that promise to organize your life, summarize your meetings, write your emails, and probably raise your kids if you upload enough PDFs?

**13:18** · But I don't want another place. I want the place I already used to become scriptable. That's a very different thing. Obsidian doesn't force agents world view on me. It doesn't say, "Here's your AI workspace. Here's your AI memories. Here's your AI graph that only exists inside our subscription." It just says, "Here are your markdown files." That's powerful because markdown is boring and boring wins. Boring means portable. It means diffable. It means I can use git and I can edit in nearly.

**13:46** · And if Obsidian disappears tomorrow, I still have my notes. Lastly, I must say this does not make Obsidian a magical second brain that thinks for it. You can't outsource thinking yet. If you don't compile notes and read them, this isn't knowledge. Not only it's not cemented in your brain, it doesn't even get there. A large graph is great, but that's just a fancy way to waste even more token. And if you want the human side of this workflow, the Obsidian and Neovim setup is still one of my favorite videos I've ever made. If you want the agent side, watch Open Code or Pi videos next. Thank you for watching.

**14:16** · I'll see you on the next