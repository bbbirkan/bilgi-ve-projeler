---
title: "Obsidian With Claude: The Setup I Said You Didn't Need"
source: "https://www.youtube.com/watch?v=B35SWx_4BNM&t=61s"
author:
  - "[[ICOR with Tom | AI Productivity]]"
published: 2026-04-08
created: 2026-05-09
description: "I said you didn't need Obsidian to use Claude for knowledge management. You pushed back. Here is the complete setup, built on top of the same folder-first sy..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=B35SWx_4BNM)

## Transcript

### I said you didn't need it. Here is why I'm making this anyway

**0:00** · If you watch the previous videos, you know that we can build a local folder and use AI for knowledge management, and I made a few videos about why you don't need to use Obsidian to do that.

**0:12** · People say, but I love using obsidian with this, and this is great.

**0:15** · And this video I will show for those who are interested in using Obsidian exactly step by step, how you set these things up.

**0:23** · However, the point was in the previous videos that there is no need.

**0:28** · To use Obsidian in order to leverage AI for knowledge management.

**0:33** · It is another layer on top, and I just had a feeling that people think they need to use Obsidian in order to do this.

**0:40** · However, in this video you will see that it actually can be very useful using obsidian on top of your local folder as one of the options that you have.

**0:49** · To access and visualize the data that you're creating.

**0:52** · So in the end of this video, you will have everything set up, end to end, you have a system running.

**0:58** · And as you know me, it will be the most simple way to do it.

### What you need: Obsidian 1.12.7 and the CLI

**1:01** · Alright, the important thing is just that you are on version one point 12.7 which will ensure that you have installed the obsidian CLI don't worry if you don't know what this is.

**1:12** · the CLI will just allow you to access your obsidian files.

**1:17** · Through the terminal and we will end up letting Claude use this connection for us.

**1:23** · So we don't need to know how it works, But essentially it provides a lot of different commands that Claude can now use to effectively use Obsidian without it, even then Claude would be able to manipulate our local files so it shows up properly in obsidian.

**1:40** · But this is the most efficient way to do it.

**1:42** · So just for information.

**1:44** · So just ensure that you updated obsidian to the latest version and you're good to go.

**1:48** · If not, just download it and install it and you will be on the latest version and everything will be set up properly.

### Creating an empty vault (it's just a folder)

**1:56** · So now we will start an empty vault.

**1:59** · And a vault for those who don't know, never used obsidian.

**2:02** · A vault is just, again, a local folder.

**2:04** · So we will see when we create now a new one, we call it obsidian demo, and we check out the, the location again.

**2:12** · I always like for these demos, to use the desktop because this way you see, it's actually a local folder that siding creates Here, if If you open up this folder, you see all there is, it's now a dot obsidian file.

**2:25** · If you're using Claude, you're getting used to these things because there's also.cloud folder.

**2:30** · And in there there is the instructions for obsidian, how to read this folder and to visualize it.

**2:35** · And here is the first.md that obsidian creates.

**2:38** · If we open up this, this is all there is.

**2:41** · It's just some information and that's it to get going.

**2:44** · Okay.

**2:45** · Again, we are working on a local folder and that's great.

**2:48** · If you watch the previous videos, you know what these two folders are.

**2:51** · We always worked with Claude in just local folders and we built our knowledge base this way and the same we will do now with obsidian.

**2:59** · That's the beauty about obsidian.

**3:01** · So you see this folder is now open in our obsidian app.

**3:07** · And you see here, there's the welcome MD file.

**3:10** · Again, if you show here, there's the MD file, it's showing up here.

**3:13** · It shows you the local structure.

**3:16** · What it doesn't show you is these hidden folders, and if you don't see the hidden folders, you can hit shift command.to show or hide them if you cannot see these folders.

**3:28** · But now let's stay here.

**3:29** · So it created this message and we have the graph already, and I will just close all these things.

**3:35** · And now let's set up obsidian in a way that we can use one way to access this would be.

**3:42** · I just right click on this folder and I can go to services and say, new terminal at folder.

### Terminal at folder: the quick version that works but misses the point

**3:49** · There we go.

**3:49** · There are many ways to do this.

**3:51** · You could also get into the folder by right clicking, holding down option and copy the path name and then hit CD and the path.

**3:59** · Name many ways, how you can open a terminal inside this folder.

**4:04** · All it does now is when we open this folder again, This terminal is now active in this folder.

**4:10** · if I now launch Claude in this terminal, it will start working in here.

**4:15** · So I can now say create a new MD file in this folder with random text in it And now you see Claude just created a random notes file.

**4:26** · If I open this here, this is what it created now if we open up obsidian again, you see now there is also this random notes coming up and I can read this in a much.

**4:36** · A nicer way than just opening up the m the file natively.

**4:40** · Okay, so this is how you could already work in your obsidian vault, but I don't see the point in doing so, and that's what I mean.

**4:48** · If you want to just have it this way, you can perfectly just use the terminal in a folder or vs code as I showed in another video to have even more access.

### Why I want Claude inside Obsidian, not beside it

**4:57** · In this video, I will show you how I would use obsidian together with Claude properly.

**5:03** · So we close this terminal.

**5:04** · Now we have this folder.

**5:06** · Let's go back to obsidian.

**5:08** · And what I want is I want to have Claude inside obsidian.

**5:13** · I saw some people using VS code with Claude on the side working inside the folder.

**5:18** · And so, no, I want to have the feeling that Claude is working with me inside.

**5:23** · And that's the reason why I'm using VS code.

**5:25** · And that is the reason why I will also use it inside Obsidian.

### The one plugin: installing the Terminal community plugin

**5:28** · And in order to achieve this, we will just need to get one community plugin So if you go to settings of obsidian and we go to community plugins, we can turn on community plugins here, then we browse, and here we just write down terminal.

**5:45** · And there you see there's a very popular one with over a hundred thousand downloads.

**5:50** · I click on this, I install it.

**5:52** · I enable it, and then you can, if you want, go to options and getting overwhelmed.

**5:57** · Just ignore it, close it.

**5:59** · And what this type plugin actually does, it allows me to load the terminal inside obsidian.

**6:04** · So you get this new icon here, you click it, and then you say integrated, and it opens up a terminal in here.

**6:11** · I prefer to have it on a sidebar.

**6:13** · So therefore, obsidian gives us the options we have already the sidebar with these different topics.

**6:18** · The nice thing about obsidian, I can place these things anywhere I want.

**6:21** · And now I have the terminal opened here on the side.

**6:24** · I have here my notes.

**6:25** · I have here the content to show when I click, I can switch between the notes.

**6:29** · I can hold down command and open up nodes in different tabs.

**6:33** · And that's actually really a nice interface.

**6:35** · and I really like it this way.

**6:36** · So now let's start working on our obsidian vault.

**6:41** · I will just launch Claude now as this is just a terminal.

**6:44** · It perfectly launches Claude and the beautiful thing is if I launch it Inside obsidian in the open vault, you see it automatically launches it inside this folder.

**6:53** · So there's no need to drag and drop a folder in, as I showed you before.

**6:57** · It instantly opens up and I can start working inside my vault.

**7:01** · so let's give it a go And I will say, delete the two nodes that we have in this folder.

**7:06** · All right.

**7:07** · You see, it recognizes there are two markdown files and it's not possible to undo this.

**7:13** · So should it Go ahead.

**7:14** · Yes.

**7:14** · Delete it and it will delete these demo files.

**7:17** · And there we go.

**7:18** · It's gone.

**7:19** · So this means we perfectly can work in here.

### Launching Claude in the sidebar and running /init

**7:22** · So now I can say slash in it, this will initialize Claude inside this folder.

**7:28** · Not really necessary, but it's a good starting point.

**7:31** · So it will now recognize that it is in an obsidian folder.

**7:35** · see it recognizes this directly as an empty obsidian vault, not a code repository.

**7:39** · So it sets itself up.

**7:41** · So he says it makes no sense to create a Claude aut defi.

**7:44** · So the interesting thing is here, even that it knows that we are an obsidian, it doesn't know yet that it can use the obsidian CLII so this time I asked it, can you use the obsidian CLI?

**7:56** · And it actually figured it out.

**7:58** · However, beware this is not always the case.

**8:01** · I tested it before and I asked, can you access the obsidian CLI, which is the connection to obsidian that I showed you in the beginning of the video.

**8:10** · And there it said no if this is the case, just tell it.

**8:13** · is an obsidian CLI and it should double check and things like that.

**8:17** · And it knows.

**8:18** · So what we want, we want to make Claude now much more aware of what environment he's working in.

**8:24** · That's why we will say create a Claude or the D file.

### The Claude.md trick: making Claude vault-aware

**8:28** · Which will remind you that you are now in an obsidian environment and you have full access to the obsidian CLI and that you can access any tasks and commands through the CLI to use obsidian in most efficient way possible.

**8:42** · So obviously I just say something random, not very well said.

**8:45** · The beautiful thing about AI is it will create now a Claude of MD file that's more helpful to AI than whatever I said here.

**8:53** · So let Claude make it.

**8:54** · You see it said it created it.

**8:55** · It created this file.

**8:57** · Here we can open up the plot of MD file.

**8:59** · And there we go.

**9:00** · Here we are.

**9:01** · If we now open up this folder again, we see here's the obsidian and there's the cloud MD five.

**9:07** · So what did it create?

**9:08** · All this, that there is an obsidian CLI, how to access it and all the information that it needs here.

**9:13** · Now it knows the capabilities available via the CLI.

**9:17** · So whenever I ask now, Claude something, it perfectly will understand how to use the CLI.

**9:23** · Again, remember, it's just.

**9:24** · The connection to obsidian that allows now c interact with it.

**9:30** · And it's also for yourself to understand.

**9:32** · So what we don't have in here, there is no capabilities of canvases, but even this is possible to use.

**9:39** · And I show you in the end of the video, okay, now that we have this in place, we are good to go.

**9:44** · That's the basics that we need.

**9:46** · So we can just hit slash clear so we have an empty context for Claude and we can get started.

**9:53** · And the first thing I want to do is.

### Backfilling journal entries with automatic backlinks

**9:55** · Backfill the daily journal entries for the last 30 days with random entries about different people and different topics, and already create backlinks to each other.

**10:05** · So we have already a starting point for our journal, whatever.

**10:09** · Okay, so obviously it would be your own journal entries that you're doing here, but I just want to show you something that we can work with inside obsidian and how I would approach it.

**10:19** · So if I bring in my knowledge into obsidian, I would approach them this way.

**10:24** · So now you see it is using the obsidian CLI.

**10:27** · As you can see here, all this looks very complex, but in the end it is really simple.

**10:32** · It just calls now, um, the obsidian CLI and it starts.

**10:37** · To figure out what I actually meant by this and where the path is and so on, and eventually it will start creating these journal entries.

**10:44** · And here we go.

**10:45** · We see it already created a people folder where we have now the different people that it's generating, and we have some notes about the people in here as a starting point, and then I will create these journal entries about it.

**10:58** · Now here we have topics.

**11:00** · So we see already that here we have the book club and there's a person mentioned.

**11:04** · We can always go to the three dots and say backlinks and document.

**11:08** · And now we see the backlinks down here.

**11:11** · So we see that this person has an entry from book club.

**11:15** · If you click, we can open up this person's note and see.

**11:19** · There's this link to the book club, but also the Italy trip.

**11:22** · So if you click here, we see it here.

**11:24** · We can also go to the knowledge graph and see how the connections are building up because now the daily entries are coming in.

**11:31** · And there we go.

**11:32** · You see here the links are working.

**11:34** · I can click on it, I can open up, it opens up in the site.

**11:37** · It's beautiful.

**11:38** · I see now all the daily entries and it obviously that's not something we want.

**11:42** · We want to have a folder for our daily journaling.

**11:46** · I could go now to the settings and set this up, but that's the beautiful thing.

**11:49** · Now I can ask it.

**11:50** · I'd like to have all the daily journal entries into one journal folder and all new ones should also go into the folder, so ensure they'll also set up the settings correctly.

**12:02** · So what this will do, he will now move everything into the folder, but also go into the settings and sets it up for me.

**12:09** · He probably will tell me he has no access to it, and yet what he has is access to the folder so he can actually access the settings files here in order to set this properly up for me.

**12:20** · Because obsidian is it's a pretty simple way to manipulate obsidian files and therefore we have Claude doing it for us.

**12:29** · See now it moved it everything into the journal folder here, and if we right click, we can always open the folder by clicking on Reveal and Finder.

**12:37** · And here we are now we have these folders in here and you can see it's a perfect replica of what we have obviously, because obsidian is just an interface visualizing my data from my local folder.

**12:49** · And that's something I saw previously using this terminal integration.

### Crash recovery with claude --resume (the tip nobody mentions)

**12:53** · Claude crashes and the reason why it crashed, it reloaded obsidian.

**12:58** · See, and when it does, it loses the session.

**13:00** · That's the thing.

**13:01** · Just keep this in mind.

**13:02** · If you reload it, that's how you get back.

**13:05** · You just launch Claude resume and then you can actually get back to the session that was just closed.

**13:11** · That's one thing that might people say, ah, but I prefer using it externally because then it will always stay open.

**13:18** · I have no problem because even if you have several terminals running, you can always hit slash rename and this will now rename this session to, uh, to whatever we are working on.

**13:30** · So now if I get a crash, so here I will just exit it and it Right.

**13:35** · Clear.

**13:35** · So now it's like we crashed.

**13:38** · I can now launch Claude, but I also can launch Claude with resume here this way and it will directly go here.

**13:45** · And I see organized daily journal notes and I know I'm back in this conversation now, and that's how I can stay always in control whenever something happens to my conversation with it.

**13:56** · All right, great.

### Building a people Base (the new Obsidian database feature)

**13:57** · Now we have the journal entries, we have the people folder, we have topics folder.

**14:03** · But the beautiful thing about obsidian is that we now have even databases.

**14:08** · So let's create an actual people base.

**14:10** · Okay?

**14:10** · So that's what we can say now that we have people in there.

**14:14** · Can you create a people base that includes also additional metadata about these people?

**14:19** · So you can see already there is no base creation thing, but there's no problem for Claude.

**14:24** · It will just create it anyway.

**14:26** · And then later on it will use the CLI to keep adding more things.

**14:30** · And here we go.

**14:31** · It already created a table.

**14:33** · And now we have this base here, which he also created in a people folder.

**14:38** · So now we could have also a base folder where we have all these bases, and that's up to you how you want to organize this properly.

**14:45** · But here we go.

**14:45** · It added tags.

**14:47** · It added last contacted location, uh, relationship, fire name.

**14:51** · And that's beautiful.

**14:52** · And obviously now you have the option that to much easier manipulate the files.

**14:58** · You can write anything down here and you can upgrade your obsidian to sync it so you have access to it from anywhere.

**15:07** · But now let's move things further.

### The journal-from-screenshot workflow

**15:09** · now I, show you how powerful this now becomes because we have these journal entries and that's the perfect way now to create a daily journal.

**15:16** · So I can actually always provide images in here and I will use this beautiful comment that I got on one of my videos.

**15:25** · To create a journal entry out of it, please create a journal entry out of this screenshot and I paste and copy paste the image in here.

**15:36** · So that's just copied in from my clipboard and it is just represented as image number one.

**15:42** · What Claude will do now, it will read this image what's on there, and you will see it in a minute appearing, and it will create a journal entry.

**15:49** · However, what I didn't say is that it should also add this image to the entry.

**15:54** · So it probably will just create an entry for now.

**15:57** · And that's a perfect example to show you how you further can improve your Claude setup Inside obsidian.

**16:04** · So, it created, now this file, I can open up the thing.

**16:08** · So if I go here, open today's daily journal.

**16:11** · Here we go, a comment that landed, and here it says all the information about it.

**16:17** · And now I can actually quickly go out here, which is just by hitting exit.

**16:22** · You're back in the terminal.

**16:24** · I hit clear, it will empty the terminal.

**16:26** · And instead of just using Claude, I will use Claude and then I will use Claude.

**16:32** · And then this flag behind dangerously skip permissions.

**16:37** · If you do this.

**16:38** · Claude will just skip everything that you get asked for each change inside the file and all the things.

**16:45** · Be careful, depends on what you're working on.

**16:48** · Uh, I'm pretty fine with this in most cases.

**16:52** · so I'm using this now.

**16:53** · And if you are unsure for certain things, the beautiful thing is if you launch it this way, you still can by using shift tab to cycle through the modes.

**17:01** · This is now empty and it will ask me for everything.

**17:04** · This will accept edits on, so this will automatically accept the edits that I already agreed on, that it will be okay.

**17:11** · the plan mode, something I will discuss in a different video where it's not doing any edits, but it creates a plan for the things that it is planning to carry out.

**17:19** · And now this, okay, so we will stay in this now for now.

**17:22** · I resume the session again.

**17:24** · And now we are back here.

**17:25** · See, and now we can go back and say, but I also want the image to be appended to the note.

**17:33** · let's see if it still has access to it.

**17:35** · And there we go.

**17:36** · See, here's the image that I shared with obsidian.

**17:39** · It added it, it created an at attachments folder where it saves all the images and, and this is it.

**17:45** · Now we have it all.

**17:46** · We have the image itself, and we have now the journal entry two, but I don't want to keep repeating this over and over.

**17:54** · Okay.

**17:54** · So first of all.

**17:56** · I want Claude to remember.

**17:58** · please remember how we created this journal entry.

**18:01** · Whenever I provide you a screenshot and ask you for creating these entries, update you, Claude at md file accordingly.

**18:08** · now it'll go into this cloud file and it will update it with this information.

**18:12** · However, that's not the way I like to do it.

**18:15** · I.

**18:15** · Now we see it added information into this Cloud MD file, daily notes where they live and so on.

**18:21** · And here creating a journal entry from the screenshot and took nice thing again in obsidian.

**18:26** · I can now easily edit this MD file.

**18:29** · Also, obviously you could do this in VS.

**18:31** · Code two.

**18:32** · And there we go.

**18:33** · Now we have it.

**18:33** · However, I want to have it even simpler whenever I have something I want to add to the journal.

**18:39** · So now when we open up the folder.

**18:41** · In the meantime, it created a dot Clause MD file, and there are some settings that it's set up already.

**18:47** · Now we could install a show, hidden folder plugin and things like that to show them here.

**18:51** · But I don't want to add, you know, more plugins than and really necessary.

**18:56** · So I will stay with this terminal plugin here.

**18:58** · Instead, I will just tell Claude to create a command and for me.

### Building your first /journal-image-entry slash command

**19:03** · So I can easily trigger this journal entry moving forward.

**19:07** · So what is a command?

**19:08** · A command is just a simple file like this one where there's just a prompt saved.

**19:14** · So if we scroll back up and we remember this, this was actually the prompt.

**19:19** · So all we need is, create a slash command for me that I can use to trigger this in the future.

**19:27** · Name it.

**19:28** · Journal entry with this prompt, actually journal entry, journal image entry with this prompt.

**19:36** · And then I just see if Claude will actually create it, because the good thing is we always have easy access on our finder to see what's going on in our files and what it should do.

**19:47** · Now it creates another folder in here called commands, and in there is just a simple text file with my prompt that is then easy to access through the terminal moving forward.

**19:58** · So you see it just created commands.

**20:00** · And now it will create this file in there.

**20:02** · There we go.

**20:03** · Here's this command.

**20:04** · It can open this up.

**20:05** · And this is it.

**20:06** · See, there's a description.

**20:07** · It created, it created this, and then it even expanded it so it really knows what to do.

**20:12** · And the beautiful thing is when we have it this way, next time, let's clear all this.

**20:17** · So we start from scratch with, Claude.

**20:20** · and in fact, I will go to our, myICOR application because there was a beautiful comment on our free Kickstarter course from Steven here that after 81 years he finally gets a system.

**20:31** · So I will just make a screenshot.

**20:32** · I go back to obsidian and I now hit slash journal.

**20:37** · I.

**20:37** · And if this is not coming up yet, you might need to restart cloud.

**20:41** · So I will exit it clear, restart it this way.

**20:45** · And I'm just clearing because I want to have it clean visually.

**20:48** · And now I have journal, see image entry.

**20:51** · I can hit tap.

**20:52** · And now I just paste in this image.

**20:54** · And this is now a combination of all the prompts that you saw in this MD file here.

**21:00** · So when I hit enter, all it does, it just reads this file and this is the prompt that's going on.

**21:07** · It'll copy the import image into the attachments.

**21:09** · It depends it to today's daily node, it will add and so on.

**21:14** · Okay, so let's see how this works and how more efficient we already are doing this, this way.

**21:18** · And here we go.

**21:19** · It added it to journals.

**21:20** · So open up the journal and we see here, now there's this entry.

**21:24** · And it worked beautifully.

**21:25** · It added the image, it extracted it, it extracted also what this is all about.

**21:30** · It compared it even to the previous entry.

**21:33** · And this is actually pretty be beautiful.

**21:35** · And I think you see now the power of commands, How fast you can now create these journal entries.

**21:40** · it actually recognized itself that there is a name and it wasn't added, so why not adding it?

**21:46** · Yes.

**21:47** · Update your rule set to always also cross link any new people appearing or link existing people.

**21:57** · It created Steven, it put it outside of the people folder.

**22:01** · Again, you need to update the rules.

**22:03** · Ensure moving forward, all people get moved into the people.

**22:09** · Folder and if you open up the people base, you see that Steven doesn't appear here either.

**22:15** · Also ensure to add those people to the people base, and if you want to more be more specific, you can then go into Claude lot.

**22:25** · There we go.

**22:26** · He edited ICOR.

**22:27** · User location, unknown.

**22:29** · Obviously I can click on it.

**22:31** · Now we have the metadata we have here, the information we have here, the daily entry, connected.

**22:37** · And all this is working beautifully.

### Creating Canvases with Claude (even without CLI support)

**22:38** · So the last thing I want to show you is how we can actually create canvases.

**22:43** · So I can just say create a canvas with a random.

**22:48** · Diagram on it.

**22:49** · So it will now say, and I even misspelled it.

**22:51** · And that's the nice thing AI will still understand what I mean.

**22:54** · but the thing is canvases is not part of the CLI, so it will try now to find it and it will say it's not there.

**23:01** · However, Claude is pretty clever and it knows that canvases are just chasing files and will create it manually force.

**23:09** · And again, once we get this and it is doing the right thing, we could reinforce it by updating the Claw MD file So here we go.

**23:16** · I will write the Canvas file directly.

**23:18** · Boom, I did it.

**23:19** · And here.

**23:20** · It created this canvas.

**23:22** · With this, there we go.

**23:23** · It created all these nodes I have here, even a link to something.

**23:28** · And this works pretty good.

**23:29** · So now I could also add the image here and I can start thinking so I have a visual representation and think about the stuff.

**23:37** · This is great, and now I can have my articles in there and so on, and extract it to create a visual representation of it.

**23:44** · And that's actually pretty good.

**23:45** · now you can imagine, I will now say, create a folder for the canvases and we can also apply the I core, my life concept here and also the AI agent team to make it an efficient PKA System a Personal Knowledge Assistant System that is easy to interact with without a need for Claude for you to create interfaces or anything like this.

### Wrap-up: Obsidian is a layer, not a requirement

**24:09** · So that's really powerful using of obsidian, I hope you see that I'm not against obsidian at all.

**24:15** · It is just another layer that we now put on top of what we've built previously in our local folders, and, now we can use obsidian to access it this way.

**24:26** · But I hope you also see the advantage of actually setting it up this way so you have easy access with Claude to your files and how you work in there.

**24:35** · Let me know in the comments below if you are already using obsidian with Claude and if this is the way how you do it.

**24:40** · And I'm happy to make a follow up video to show you now how we can integrate actually AI agents working in there, Larry and the team and so on.

**24:49** · so if you haven't already, subscribe to the channel and I catch you up in the next one.