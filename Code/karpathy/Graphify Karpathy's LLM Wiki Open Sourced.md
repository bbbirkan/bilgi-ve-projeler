---
title: "Graphify: Karpathy's LLM Wiki Open Sourced"
source: "https://www.youtube.com/watch?v=zR5tyP4Onkc"
author:
  - "[[DevsKingdom]]"
published: 2026-04-13
created: 2026-05-09
description: "Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and gener..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=zR5tyP4Onkc)

## Transcript

**0:06** · Hello guys, welcome to another video. In today's tutorial, we're going to introduce a very interesting topic. It is called LM Wiki from Karpathy. So, Karpathy is one of the Open AI founders.

**0:19** · So, he wrote this paper or this short short article to discuss one problem. So, because when you actually talk to a LM, so one thing is that the information is temporary. So, once you start over, then the LM will basically retrieve a fresh new information.

**0:43** · The other thing is that the information is very scattered. So, it's not really persistent. It's here and there and some of them are in the files, some of them are in the videos, some of them are in the PDFs, images.

**0:59** · So, it is very hard to retrieve the next time. So, once you, for example, wrote something in Notion, wrote something in piece of paper, it's very easy to forget after a while or even just after a few days.

**1:15** · So, the idea of this Wiki is that you want to build a persistent storage for knowledge.

**1:24** · That means the knowledge can compound.

**1:27** · So, it will not be scattered everywhere. Instead, it collects everything together every day and rebuilds every day once you talk to the LM.

**1:40** · So, that next time the LM remembers everything that you did and it collects all the information, all the resources you have from a specific location, then it will start compounding the knowledge.

**1:56** · So, it's like session management, but more of a persistent session management.

**2:01** · So, so it will always be there. So, once you want it, you can even retrieve the things that you did or the thoughts that you had years ago. And this is very powerful because think about this. So, if you have something that you did maybe a few years ago and you don't remember it, but you just keep it as a diary or

**2:26** · you just keep on adding things to it and a few years later, so \[snorts\] you don't remember this, but the storage does and the system still kept everything that you did and LM kept building the information in a very structured way.

**2:46** · So, years later, you still can query everything so that it can help you to understand what you did, why you did it and what's the outcome, why you shouldn't do it, why you should do it, such things like that. So, it's a very interesting idea and so a lot of people have already implemented this. So, also in this tutorial, we're going to show you what are the best repos you can look at and how to try them out.

**3:16** · So, that being said, let's get started.

**3:21** · If you look at the core idea, what Karpathy said is that LM is rediscovering knowledge from scratch on every question. So, there's no accumulation, which means there's no compounding. So, ask a subtle question that requires synthesizing five documents and the LM has to find and piece together the relevant fragments every time. So, nothing is built up.

**3:47** · Notebook, LM, ChatGPT, file uploads.

**3:50** · So, the idea is different. Instead of just retrieving from raw documents at query time, the LM incrementally builds and maintains that a persistent Wiki.

**4:01** · So, that's why it's called LM Wiki, a structured, interlinked collection of markdown files that sits between you and the raw sources. So, we're going to show that what does that mean to raw sources and also the interlinked collection of markdown files.

**4:18** · So, basically, this is the idea. So, build a Wiki that is persistent, compounding artifacts. The cross-references are already there and the predictions have already been flagged. So, the synthesis already reflects everything you have read.

**4:36** · The Wiki keeps getting richer with every resource you add and every question you ask. So, super powerful. And so, what this is good for is for personal, for research, for reading a book, for business, teams and also competitive analysis, due diligence and trip planning and course notes, so on and so forth.

**4:59** · So, you can see there are a lot of people actually commented on this and they show up their examples. Feel free to check them out.

**5:05** · It's very good projects. So, there are particularly two things, two projects that actually got very a lot of attention. So, one of them is called Graphify.

**5:18** · So, this project actually got almost 25k in 1 week. So, right after Karpathy released the project and this GitHub repo got very popular. And it's very simple. It implemented everything that Karpathy talked about and also they give up examples. And if you look at the Graphify folder, you can see basically that's all it is. Very simple.

**5:44** · It's a skill with all the different Python files and it supports different IDEs like Atom, Claw, Codox, Copilot, Draw and also Open Code, Tray and also Windows. So, very \[snorts\] simple project, very effective. So, that's the beauty of it and it's not heavy. You can just do a pip install as they mentioned in here.

**6:05** · Very simple, just do a pip install.

**6:07** · So, pip install Graphify, Graphify install. That's it. And then you install the skills with the with your favorite IDE, which is like Claw Code and Codox and Open Code. So, one command line, it's ready to go. So, right installed it. So, let's go to the Visual Studio Code. As you can see, we already launched everything. So, in the Claw Code, so simply put all the files inside one folder. We created actually three test folders. So, just put a raw folder.

**6:39** · You can name it anyone anything you want, but since Karpathy said to put in the raw folder, we put everything in the raw folder and it's just resources. You can put anything in it and doesn't have to be a Python file. It doesn't have to be a markdown file. You can put any resource.

**6:57** · The goal is to optimize everything in a structured way. So, you can create a structured memory system or structured Wiki for LM. So, you can retrieve later on. So, if you be able to create something in a random like a random folder and just CD the Claw Code to it, so you can see basically the Claw Code is already CDed to this test two folder.

**7:21** · So, basically, this is a working folder and then you can see there's a raw file already wrong test. So, this test is to show the relationship of a different markdown files. So, for example, the first one is "Attention is All You Need". So, this is very old article way before the GPT came out. And there's abstract, there's key innovations, basically self-attention mechanism, multi-head attention, positional encoding and encoder-decoder structure.

**7:48** · So, basically, this is the article and someone wrote it and long long time ago. And BERT explained, so this basically explained the BERT, the bidirectional contacts, masked language modeling, next sentence prediction and fine-tuning or or four downstream tasks. So, there's another one, which is the scaled dot product attention. So, basically, this is explained what is the dot product attention. And from the paper, we call our particular attention scaled dot production product attention.

**8:20** · There's a architecture board. So, this can be image or PDF or videos, but this to make it simple, we just put a TXT file. So, it just basically the notes on the famous Transformer diagram, the architecture diagram. The left is a encoder text stack, the right side is a decoder stack. The multi-head attention is in both and basically, this is the architecture select architecture image.

**8:44** · And when you run this Graphify to this folder, so for example, you run the command, basically, first will build a folder Graphify out. So, you just run this Graphify.raw. So, because we're actually in the test two folder, you have to point where to run this command, run this skill. So, we put all the files in the raw folder, so you run that in the raw folder.

**9:16** · So, you can see the skill is loaded.

**9:18** · It's called Graphify. And uh the basically first have to install basically the Python files, which I saw.

**9:24** · And after that, uh you basically starting to build this folder, which is Graphify out. So, in this folder, uh the output folder, there's a couple of files that are very important.

**9:34** · Actually, all the files are important, but because we're actually using the open source LM, so so this cost.json is not relevant. So, it's probably just all zeros. And for the manifest, it basically just tell you all the raw files. So, the important three files are graph report, graph.html and graph.json.

**9:55** · So, the graph report is a summary of the output. So, if you look at the graph report, so it's basically a final release of the Suricata contacts, which understand the entire resources that you give it.

**10:14** · So, you can see there's a corpus check, there's a summary, there's community hubs. So, basically the extraction comes first. So, the first extract all the different entities from the resources. You have all the resources in the raw folder, extract the entities, then it builds the relationships of those entities.

**10:36** · And lastly, it will form the communities. For example, there are different communities. The first community is the architecture, which is the probably the transformer architecture file. Then you have this pre-trained BERT, also another community is the attention mechanism, which is probably the paper and also in decoder encoder stacks, which is the this one, scale dot product attention.

**11:01** · So, \[snorts\] so probably it's the other one, but basically they um sort of like understand everything in this raw folder.

**11:13** · So, um then what it will do is basically put everything together as a report. All right, so after everything is generated, it put it as a report. So, go through this report the resources, how the resources are structured. All right, so base they also have interesting sections called surprising connections. So, this something that you probably didn't know but just looking at the files. So, this is something that you probably is hidden inside the contacts, but they understand it through the graphify process.

**11:44** · So, now you understand what are the entities, what are the connections, which is like the relationships between the entities. Then you have different communities, also hyperedges. So, the communities one is core transformer architecture, community also community zero, community one is BERT and pre-training and then also the community two is attention mechanism and also last one is probably the

**12:14** · the last one is the encoder decoder stacks, yeah. So, that's the one.

**12:19** · So, basically this is the final report for understanding this round. And then you have this graph HTML, which is super cool. So, graph HTML, if you copy and paste it, you can see that the very visual way how it works. All right, so you have four communities, they're interconnected together, the relationship are built together.

**12:41** · So, so like for the red one means red community, so the scale dot product attention, the transformer architecture diagram and also there's a transformer architecture and this last one is basically the BERT one, the BERT pre-training of deep bidirectional transformers. So, it's very clear for the different entities, the communities and also the relations between different communities. Very clear, so nice graph, nice visual and it just takes a few minutes to generate everything. So, this is keep on compounding. After you put more files in this raw folder, it's going to keep on involving over time.

**13:15** · So, super cool.

**13:18** · And so let's take another example. So, so basically this is the graph report, which is the final report and also graph HTML, which is the visual.

**13:32** · The graph JSON is probably something that you definitely want. So, the graph JSON, this is the part you use the query for.

**13:41** · So, if you eventually build a graph for everything, for every knowledge, every resource, then the store the structure inside this graph JSON and it involves updates over time automatically. So, if you see this one and you can run query against it. So, for example, in this readme, they also said you can run the JSON with it.

**14:04** · So, the JSON file the graph JSON, so we can just loop through the wiki. So, you can see there's a graph query and show the off file and basically they put in the graph. This is the JSON that represents that graph. So, you can just do the graph query to run the query, ask questions against this graph, which is what built over time. So, so that's how it works.

**14:34** · In this repo, they also provide a lot of examples you can try out. So, the first one probably shouldn't go to the worked.

**14:41** · So, this also kind of similar to what Kapathy talked about in his wiki alarm article. So, you can just go to this uh example.

**14:51** · So, you can try this example, which is a reproducible example and then there's a lot of other coder files and you can just run the graphify.raw for this folder, then you should be able to generate something that you just saw.

**15:05** · So, it's very \[snorts\] simple but it's very effective. And so there are examples in the worked and there's HTTPX, there's Kapathy repos, there's mixed mixed corpus. So, there's a lot of things you can try but they follow the same structure, a raw folder with raw resources and also the other documentations here. So, it's very nice. It supports different IDEs just by simply install which platform you want.

**15:30** · So, and so last but not least, if you want to try a more heavier version, so this is a very simple graphify, it's very simple version, very light, very effective. But if you want to try another version, which is heavier but more complicated version, so in the comment you can search for something called call agent. So, so this guy actually created a project called call agent with GitHub most like 40K stars. That's a heavier solution and you can see there's a lot of people are actually downloaded that version.

**16:00** · And so if you look at the installation, it's very easy also.

**16:07** · So, I think it's just one command line.

**16:10** · So, there's one command for Linux and also one command line for Windows.

**16:15** · So, it's very simple, we can try that out but we're not going to cover that in this wiki in this video.

**16:21** · So, you can see basically it acts very similar to what we just saw as a markdown and clock code version and there's a document browsing. So, they basically added a UI to it and then they also come up with this visualization.

**16:35** · Very nice. So, but it's heavier, so we're not going to cover that in this video.

**16:39** · So, but that's it. Hopefully this helpful and if you do like this video, please subscribe, like or comment if you have any questions. Thank you so much for supporting channel and see you in the next one.