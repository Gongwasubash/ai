---
title: "How To Build The ULTIMATE AI Second Brain for Hermes Agent"
source: "https://www.youtube.com/watch?v=wvYAuHfJRo0"
author:
  - "[[The AI Architects | Tom Crawshaw]]"
published: 2026-08-12
created: 2026-09-04
description: "Get your free 30 min AI Audit here 👉 http://theaiarchitects.com/yt/audit/hermes-second-brain📄 RESOURCES FROM THIS BUILD:Prompts → https://docs.google.com/document/d/17mwUm0gn-dyW7mxSZQNV2JzpR87X_"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=wvYAuHfJRo0)

Get your free 30 min AI Audit here 👉 http://theaiarchitects.com/yt/audit/hermes-second-brain  
  
📄 RESOURCES FROM THIS BUILD:  
Prompts → https://docs.google.com/document/d/17mwUm0gn-dyW7mxSZQNV2JzpR87X\_2Dn70piMYBRki4/edit?usp=sharing  
Obsidian → https://obsidian.md/  
  
🤖 Join the Mentorship & become AI Operator 👉 https://theaiarchitects.com/yt/mentorship/hermes-second-brain  
  
Hermes can already use tools and finish tasks. What it can't do is remember why your business does anything - that context is scattered across files, calls, notes and messages.  
  
A second brain fixes that. It turns the scattered stuff into a vault Hermes can search, so every task starts with the context it needs instead of a blank slate.  
  
In this video I build one from scratch with Obsidian and wire it into Hermes running on a VPS:  
  
→ Why a folder of plain text files beats a database, and how Hermes searches it without loading everything at once  
→ Creating the vault and letting Hermes set up its own structure with an agents.md file  
→ The ownership rule - what writes to raw, what writes to the wiki, and the nightly compile job that turns one into the other  
→ Identity and context rules, including the big one: if the vault has the answer, never answer from training data  
→ Routing rules so Hermes knows which folder a request belongs to  
→ Feeding it YouTube transcripts, books, sales pages and call transcripts, then distilling them into a usable wiki  
→ Turning the whole workflow into a reusable skill, and automating the daily dump  
  
The payoff is asking "what were the most common objections in the last 30 days?" and getting a real answer pulled from your own call transcripts - not a guess.  
  
If you've got Hermes running but it still feels generic, this is the layer that was missing.  
  
Subscribe for weekly AI automation breakdowns, and comment below on what you want me to build inside Hermes next.  
  
Follow me on X for Daily AI Insights: https://twitter.com/tomcrawshaw01  
  
⌛ Timestamps:  
00:00 Intro  
01:06 How the context layer works  
05:15 Running Hermes 24/7 on a Hostinger VPS  
06:23 Build: creating the Obsidian vault  
09:15 The ownership rule + nightly compile job  
11:46 Identity & context rules  
13:33 Routing rules  
15:30 Feeding it your YouTube transcripts  
17:43 Turning the workflow into a reusable skill  
21:07 Distilling raw notes into a usable wiki  
22:25 Automating the daily dump  
25:01 Outro  
  
📺 RELATED VIDEOS  
How to Run Hermes Agent 24/7 on a VPS Without Using Your Laptop (FULL TUTORIAL)  
https://www.youtube.com/watch?v=JQLWy96Ax5c  
  
How to Make Hermes Agent 10x More Powerful (Memory & Skills)  
https://www.youtube.com/watch?v=MFi3RUGzwtM  
  
#claudecode #aiautomation #aiagents #hermes #hermesagent

## Transcript

### Intro

**0:00** · If you want to turn your Hermes agent into a high-performing 24/7 AI employee that actually gets work done, you need to give it a second brain. You see, right now Hermes can already use tools and complete tasks, but the context behind your work is scattered across files, calls, notes, \[music\] and messages. A second brain fixes that.

**0:22** · It turns all of that scattered information into a system that Hermes can search and use. So, let me show you the easiest way to build your own second brain using Obsidian and connect it to Hermes so every task starts with the context it needs. Okay, before getting into the build today, give me 60 seconds because I need to make sure that you understand why a second brain is absolutely critical when it comes to using AI in your business.

**0:50** · Because a second brain is essentially a context layer. And the reason why you see people online maybe building some crazy stuff or seeing that they've automated a ton of different processes in their business, it doesn't just come from the building. It comes from developing a context layer, which is also what we're going to call a second brain in this video. And that includes a repository of all of the information that the AI needs to improve its outputs and actually build the things that you want.

### How the context layer works

**1:19** · Now, the reason why we're using Obsidian, it's essentially a tool that we can view and arrange and link different documents and files together. But don't let this overcomplicate things. At its most basic level, it's simply just a file viewer.

**1:36** · In fact, you don't necessarily even need Obsidian to make this work. Because at the end of the day, the files and folders are literally just on your computer. So, today we're going to collect all of the information that we have, so whether that's call transcripts, whether it's your accounts, whether it's YouTube transcripts, content scripts, whatever that is for your business. It could be SOPs, it could be candidate interviews, it could even be interviews with your own team asking them to walk through their own processes and tasks.

**2:04** · And that's a little bonus there for you because that's exactly what we do in our AI assessments. You need to hear things from the source, i.e. the people actually doing the tasks in your business to understand where the bottlenecks are and what that process actually looks like day-to-day because they might not be following the SOPs word for word, okay? So, we're not going to get into the interview process today.

**2:29** · But just know that all of those things can help you build in AI. It's going to give it the context layer so that you're not just spitting out AI slop like everybody else. And today we're going to build all of that using the incredible Hermes. And Hermes essentially is just a harness. Just like Claude Code is a harness, just like Codex is a harness.

**2:51** · All of these different types of harnesses have their own unique flavor and way of doing things. And you might be thinking, well, why is Hermes better than Claude Code? And I want to give you a solid reason. And Compozio put this post out on X last week and you could see they tested all of the different agent harnesses like Pi Agent, Open Code, Claude Code, Codex, and more importantly, Hermes. And we could see it putting through different tests. You could see Hermes got one of the highest completion rates, actually above Claude Code and Codex.

**3:20** · You could see the average cost per task was the cheapest with Hermes, whereas with Claude Code, it was more than like four or five times the price. And what this means is that Hermes is actually way more efficient with its tokens, whereas Claude Code might be having long internal dialogues with itself, which is going to eat up more tokens. Now, I don't know if that's because they want you to spend more with Claude Code, I don't know. But if you're like me, I'm on the subscription, right?

**3:48** · So, what this is saying is that we would get way more usage out of our subscription than actually using Claude code. You could see the run times here.

**3:56** · You see Hermes is one of the fastest agents, whereas Claude code is the slowest. And so, I thought this was really interesting. Now, I've not looked into the actual tasks they were doing in this test, but but this is just one of the reasons why I've started using Hermes and why I'm doing this tutorial for you here today. So, there are two parts to the second brain. We've got the archive. So, this is going to be all of your raw data. So, the transcripts, the documents, PDFs, whatever it is that you want to throw into that. And then, we're going to have a compiler. So, this is the wiki. So, you might have heard of the wiki.

**4:26** · It was an idea that Andrej Karpathy, who now works at Anthropic, he put this idea out earlier this year and it blew up because this was a way of taking all of your raw data and pulling out insights so that the AI doesn't have to search through all of your raw transcripts, it can actually just go to the wiki and find the key insights and the summaries that's actually going to help with whatever it is that you're working on and building. And the cool thing is you still have access to the archive, to all of the source material.

**4:56** · So, if you want to pull quotes from a transcript, for example, you can still do that with this system. So, the reason why having a wiki is important is that it's going to use less tokens. It doesn't have to search through all of your raw data to find the answer. So, these are all the files that we're going to set up and don't worry, I'm going to walk you through each of these in this video. I am using Hermes on a VPS. I do use Hostinger. They are the sponsor of today's video. It's up to you whether you want to use a VPS or not, but I'll just walk you through the benefit of why I use one. And the main reason is I can have it on Telegram here, right?

### Running Hermes 24/7 on a Hostinger VPS

**5:27** · And I can chat to it whenever I want. My laptop doesn't need to be open. And the cool thing is I can sync this to all of the files on my computer. So, I can build a second brain on my laptop, but I can access it through Telegram, through this VPS. And I can make edits, I can pull information and build things just using Telegram with Hermes. So, if you do want to grab this, you can get 10% off. You can head over to the link in the description below. You can grab a plan. I've got the KVM-2, and this is going to be good enough to get started.

**5:59** · It's going to give you way more memory for the money than like AWS, for example. And so, if you have a coupon code, which you do, it's going to be growthlab10.

**6:08** · If you apply that, you're going to get 10% off. And yeah, you can select the duration. So, that's totally up to you. Hermes comes automatically deployed on your VPS. So, anyway, let's crack on with the actual build. So, this is what we're going to be covering today. So, let's get stuck in. This is what Obsidian's going to look like when you open it up on your computer. And I'm going to create a second brain in Obsidian from scratch using Hermes, so you can follow along with me. You can pause it, whatever you want to do. But, the first thing you need to do is create a new vault. So, we're just going to create, we're going to name it, we're going to call it Hermes brain for me. I'm going to pick a location.

### Build: creating the Obsidian vault

**6:41** · We're going to add this into the AI operator OS, and let's just click click create. That's going to open up your Obsidian folder here. Obviously, there's nothing in here, just this file.

**6:53** · And we're going to get started. So, one thing real quick, you might be thinking, "Well, what's the difference between memory and a second brain?" Well, inside of Hermes, there is a memory.md file, and that can contain only so much information. Okay? And there are different memory systems like I have a QMD memory search function. So, that indexes everything inside of my AI operator OS folder. That then makes everything searchable. But, the cool thing about having a second brain is that you're going to have the raw data and the insights that are then going to both be searchable as well.

**7:23** · Now, having a memory system is essentially for me like a backup, because I might not put every single thing inside of my second brain system. So, if you want to recall a previous conversation or something that we created in a different folder, then that memory system that I have becomes very important. But, that's not the topic of today's video. If you want me to create one about the QMB system, then you can let me know in the comments below. Now, I already have Hermes set up. If you don't have Hermes set up, whether it's on a VPS or your local desktop, then you need to make sure that you've got that set up.

**7:53** · I do have a video on my YouTube channel going through the entire setup with a VPS specifically so that you can connect to the files on your computer using Tailscale, which is what I'm doing here.

**8:03** · But, you don't need to do that. You can set all of this up on your desktop if you wish. Hermes even has a desktop app, which you can see here. So, you've got different ways of accessing it. Now, I also did a video on memory and skills for Hermes. So, that video is on my channel as well if you want to check that out. It will be in the description.

**8:21** · So, let's get into the build. I'm going to connect here to Tailscale. So, the way this works is by SSHing into my computer. So, I just need to log in here. I log in with GitHub, and it's just a one-click authorization, and then boom, Hermes is going to have access to all of the files and folders on my computer. Okay, so we can see that's connected. I'm going to put a prompt in next, which I'm going to include in a document in the description below. It's super simple. We're just going to tell it to set up the second brain at a specific path, which I'm going to copy from my finder window.

**8:51** · So, if I come into here and find Hermes brain one, you see the bottom, we right-click, we go copy the path name. I'm going to pop that in there. That's the path name that we want. And you can see we've got the raw folder, we've got the wiki, we've got the digest, the identity.md, the projects.md, and the tasks.md. These are all crucial files to the operation of your second brain. And we've got a description here to write the agents.md file at the vault root explaining the ownership rule.

### The ownership rule + nightly compile job

**9:20** · You can see and the only thing that writes to the raw and the identity.md and the nightly compile jobs is the only thing that writes to the wiki. So, what we're going to set up, if you haven't guessed already, is we're going to set up a nightly run so that anything that gets added into the raw folder is going to then get compiled overnight. All right, so we're not going to use up our usage during the day when we're busy and we're working using our subscription. We're actually going to set Hermes to run this overnight when we don't need our usage window.

**9:49** · It's also writing the code in D file and this whole structure is going to work really nicely together. So, let's send that off and see what it gives us.

**9:59** · Okay, so Hermes has set all of that up and we can double-check by going into Obsidian and seeing, "Okay, so we've got these folders. Uh we've got the agents that I'm D filing, got the Claude MD file, got the identity." So, we need to fill all of this out, okay? So, for you, you want to customize this to your own business and use cases. One of the things that you can do is add a prompt interview you to extract all of the information that it needs. Now, this might take a little while, but it's definitely worth investing the time up front to give it as much context about you and your business as possible.

**10:27** · Now, I'm going to put a prompt in here and it's going to be in the document as well, so you can copy and paste this.

**10:33** · I'm not going to answer these questions cuz I'm going to ask Hermes to just answer them for me cuz he's got all the information about me, but if you don't have anything set up, then you can answer the questions. If you do like me, you already have folders and files, then maybe you could just ask Hermes to answer these questions for you, so you can start populating the second brain.

**10:51** · So, while that's working, you might be wondering, "Well, what model am I using?" Now, I've got my Hermes agent here connected to my Chat GPT subscription. So, in this case, it is using Codex, but you can plug in any of the other LLMs that you want. And the research that I showed you earlier, that was testing the different harnesses. And as you can see, that was using the Chimney K3 model. So, they used the same model across all of these different harnesses. But, there's no right and wrong way here. You can connect up your Claude Code subscription, Codex subscription.

**11:21** · If you want to use some of the open-source models, you can hook up Open Router, but you will be paying for your usage in that case. Okay, so you can see it's answered a a of these questions for me. It's asked me some things to add in as well. So, I'm going to put in this next prompt. And this next prompt is going to save it to the memory and update the second brain. So, this prompt again will also be in the document in the description below. So, you can see it says, "Before answering anything about my work, read identity.md and context rule.md as well from the vault."

### Identity & context rules

**11:51** · So, we could see the context rule.md file doesn't actually exist, but that's what we're going to do in this next step. So, the memory now says all of this stuff here and it's updated with my information. So, I'll show you that in a second. Let's just put this next prompt in. We're going to create the context rule.md file in my vault root.

**12:10** · And it's going to reference it from the agents.md file as read first. So, these are the steps we're going to include.

**12:16** · Read identity.md and projects.md before answering anything and pull only the notes that match the question and follow their links one hop out and cite every note that you used by name. If the vault has the answer, never answer from training data. If the vault does not have it, say so plainly. Okay, so each answer and piece of context that it's going to pull is going to be referenced from the vault. Okay, so all our files are updated. You can see the file sizes verified.

**12:42** · I did have to ask it to put all of the information that it pulled from the questions and answers into the wiki. So, if we go into Obsidian, we see they've got the context rules filled out, got identity filled out, projects filled out, tasks, some open loops, things like this. agents.md file, this is going to get filled out. And again, I'm going to give you the introductory setup. This is something you'll want to work on continuously. Cuz the more that you add to it and the more that you improve your system, the better it's going to get. And how do you test that?

**13:14** · Well, you have to use and build things pulling from this context. If it's not giving you the outputs that you want, let's say you're creating a script for your YouTube video or an Instagram reel, then you're going to need to add more examples and references that you can then distill into a formulas and things like this. So next, we need to create some routing rules, or if you're American, routing.

### Routing rules

**13:40** · So we're going to put that into the agents.md file. So every time it's going to read the agents.md file and it's going to figure out where to route the request and task. Are we going to route to accounts? Are we going to route to content creation or call recordings?

**13:56** · This kind of stuff. So let's go over to Telegram. We're going to pop this prompt in. I'm going to give you this in the document as well. We're going to add a routing table. So for each kind of work I do, list which files to read, what to skip, and which skill to use. Okay, this is very important so it doesn't go doesn't have to search through everything in your wiki. It's going to route to the specific area that's relevant for the task you're working on.

**14:18** · Does that make sense? So let's see what happens. Okay, so let's see what's been changed. So in my agents.md file, we've added the routes router line at the top.

**14:28** · That's a bit of a weird one to say. And it's added a routing table. So let's take a look at what that looks like. So we've got the router.md file and you can see it's created a folder map of what's in each of the folders and where to look and what kind of work routes to what kind of folder or md file. So you can see in the agents.md file, we've got the routing table in here as well. This isn't essential part of your setup to optimize your token efficiency.

**14:52** · Also just to make it easy for yourself, especially if you want to add stuff to these folders or pull stuff or you want to copy and paste it a script from a specific folder. You want to see where that script has been dropped. Okay, next we need to turn on capture mode. So I'm going to pop in this prompt here so that every time I send a voice note or a message, it's basically going to add that to the raw folder. It's not going to title it, it's not going to tag it, it's not going to do anything else.

**15:19** · That's what the nightly run is going to figure out. Okay, so the raw capture is set up. So, let's try this out. So, here's something that you can do. If you want to extract a bunch of information from YouTube videos where they that's on your own channel or somebody else's, you can just pop the channel URL in. And I'm going to put a voice note in saying, "Hey, I want you to grab the transcripts from the most recent top five videos on the YouTube channel. This is my channel and I need to pull the raw transcripts and put them in the raw folder for processing."

### Feeding it your YouTube transcripts

**15:52** · So, let's come back and see what happens. So, the cool thing with Hermes is that he's got a bunch of built-in skills where he's going to be able to grab the transcripts from these videos without me having to install any additional tools.

**16:08** · Okay, boom. So, that is done. And in fact, one of the things that you could do is you could grab the transcript of this video put into Hermes and say, "Set this up." And probably get you pretty close. So, it's pulled all of my recent five videos and the transcripts. We've not done anything with those yet. They are in the raw folder as we could see in Obsidian. You see just pulled the the timestamped transcripts.

**16:29** · So, let's manually compile everything in the raw folder. You can see I've got this prompt here. Read everything in the raw folder. File each item where it belongs. And we're going to see what happens.

**16:41** · It's also going to link the pages together. So, linking related pages. So, when your AI agent comes in to pull information and it reads through one of your MD files and that's linked to another, it's going to go and check out the other file to see if there is additional context in there that could be useful for your request or whatever it is that you're trying to build. Okay, boom. So, we are done and you could see all of the files that it's touched here and updated. So, we've got the identity.md file which has been updated, projects.md file, tasks.

**17:12** · And it's created a bunch of clean wiki pages that we could take a look at in Obsidian here. See, these are our raw transcripts. We've got the Wiki here.

**17:22** · So, a core code business automation use cases. All right, I pulled this from one of my videos. Who needs agent memory, right, from my last video. And you can see it's got related pages and the source notes as well. So, I think this is a pretty cool way of collecting information and synthesizing it into stuff that is actually useful. So, now we can actually turn this into a skill.

### Turning the workflow into a reusable skill

**17:46** · So, we can use the /learn feature, which actually is probably only available on the desktop app. So, I'm just going to tell it what to do instead. Hey, so can you turn what we've just done into a skill? So, we're talking about the processing of the raw data into these updated files and everything that you've updated and created in the last run. Can you create it into a skill so I can run it whenever I want to digest the information in the raw folder?

**18:15** · Boom. \[snorts\] Okay, just like that, the skill has been created. So, this is the raw digest.

**18:21** · We've got an overview of what it covers here. It's just exactly what I've done in the previous prompt. See, you might be thinking, "Well, Tom, I've got all of these different departments in my business. I've got marketing. I've got finance. I've got my clients." Don't worry, we're going to expand the system that we've just created now. And this is going to be completely tailored to your own business, right? But I'm going to show you what I'm going to do for mine.

**18:42** · So, I've got this prompt. Again, it's going to be in the document below as well. And inside the Wiki, create a folder for each part of my business.

**18:49** · We've got finance, marketing, operations. I'm going to put clients here as well. And then you can add in any of the departments that you want.

**18:57** · Like I could put in maybe offers, which are, you know, it kind of goes into marketing, but yeah, you can choose whichever ones you want. You can always change this. Now, the cool thing is you could delete your entire Wiki and just regenerate it from all of your raw information. That's the cool part. So, don't delete the raw files cuz they're usable. You can regenerate the wiki from those, but that's where everything's going to be stashed and overnight, which is what we're going to set up in a second, it's going to do the processing every single day.

**19:27** · So, that anything that goes in your raw folder will get processed using this skill overnight.

**19:35** · So, you then have the context ready to go. So, you can see we're giving each folder an agents.md file, which is going to tell Claude Code or whatever harness it is that you're using, it's going to tell it what's in that folder and how to work with that information. We're going to rewrite the router.md file. This is important cuz we're adding additional directions and files and folders into our second brain. Now, if you're going to add new files and folders, then you'll want to make sure to go through this process and update the other files inside of your second brain.

**20:06** · Now, if you want to see something while that's loading, what I've set up inside of one of my folders is a copywriting wiki. So, I've got all my source material here as you can see on the on the left-hand side under my copywriting folder, and I have the wiki. So, this has been insanely valuable for me to help hone how I write copy with AI. And you can see we've got books, concepts, papers, VSL, advertorials. And so, you can see in the books, it's got like summaries of all of these really high-quality direct response books.

**20:37** · So, that whenever I'm writing copy in my skills, it's going to reference and check the wiki for information that that matches whatever it is that I'm creating. This is absolutely killer, and you could set this up for writing like Instagram scripts. You could set this up for any area of your business. You just have to collect enough information to distill that into a wiki here.

**20:58** · So, this is just one side use case that I've created an entire wiki for, and this is essentially a a second brain where we take concepts from raw transcripts and in this case books and sales pages and courses and we distill down the usable information.

### Distilling raw notes into a usable wiki

**21:18** · Okay, so what we can do is we can rerun this skill here and we can have Hermes re-categorize and sort things according to these different departments. Okay, so that's run and it's moved some of the pages. So we've got marketing moves into finance operations and into offers. Okay, so how do you go about setting up the automation that's going to run this skill every single day and night. So we pop in this prompt down here at the bottom every night 3:00 a.m. Uh let's do Malaysian time. That's where I'm at.

**21:49** · You run a compile against this and we want to grab the path name and at 7:00 a.m.

**21:57** · write the brief. So it's going to send me a five-bullet brief of what's actually happened and we're just going to add make sure to run the compile skill. All right, it was actually called this skill. Okay? So because I use VPS, this can run 24/7. So overnight it's going to be able to tap into my usage that I'm not using with my max subscription plan either on Codex or on Cloud Code and he's going to do all of this for me.

**22:24** · So during the day if I want to just dump stuff into the raw folder, maybe I can sync up my call transcripts, maybe I could put in my transcripts for my YouTube videos, all of this stuff.

### Automating the daily dump

**22:35** · And maybe maybe you could even set up a skill in Cloud Code so that at the end of every day it summarizes all of your sessions and then puts that into the raw folder. So these are just some of the additional more like advanced modifications that you can do thinking about how can I get more information into that raw folder so that that information can then be categorized and used on anything that I'm working on in the future. You can also build skills into this whole framework. You can have different folders that trigger certain skills.

**23:03** · So, for example, if I wanted to, let's say, create let's say 10 different Instagram carousels, like the images, based on, let's say, a call that I had with somebody. So, what can happen is I could create an automation that would add the calls, the transcripts, into the raw folder, and then that gets added into marketing. And when it does get added into, let's say, the let's say I have a carousels folder.

**23:25** · And in there, the agents.txt file says, "Whenever the call transcript gets added, we're going to pull out 10 different ideas for carousels, and we're going to create those images." And that could all be a skill inside of that folder, if that makes sense. So, there's a lot of different additional stuff you can do here.

**23:45** · These are just kind of the base level to get started. And it's really up to you and your own creativity and processes that you follow every day. Maybe at the end of the month, you just dump all of your bank exports into the raw folder, and it spits out nice reports, right?

**24:00** · Maybe you have a skill in that accounts folder, in the finance folder, so that when every time that folder gets updated with new information, it then adds that to a a dashboard that you've got created, for example. Okay, so you can see in Telegram, the scheduled job has been set up that's going to run every single day. And so, that's all I need to do. Now, it's up to you to actually build this and implement this into your own workflows and your own systems. You can also access this folder because this is on my local device, on my laptop, I can access this using Quad Code on my local device, as well.

**24:32** · And so, just think about the possibilities here, you know, you're loading your call transcripts, they then get processed, and then maybe you want to create a training for your sales guys, and so you ask, "What were the most common objection in the last 30 days?" And you'll be able to pull that from the wiki because it'll have pulled that information out from your call transcripts. So, this is building Hermes, so let me know what else you want me to do with Hermes. Drop me a message, and if there's anything else that you want me to build inside of Hermes, let me know and we can nail that in the next video.

### Outro

**25:01** · All right, so that is the complete second brain build. But this is just one system. Every business has different work eating up time and the hard part is usually not finding another \[music\] AI tool, it's knowing what is actually worth building first. And that's why I created a free 30-minute \[music\] AI audit. On the call, you show me how your business works and I'll give you the number one ROI opportunity in your business \[music\] and give you a clear road map for what to build next.

**25:28** · And if it makes sense, I'll let you know how we can work together \[music\] to build that number one system live on a call. So you actually leave with a running agent instead of just a plan. Now, if that sounds useful and helpful for you where you're at in your business right now, make sure to click the link below and \[music\] you can book your free 30-minute AI audit call with myself today. And if you want to build the exact second brain in this video, my hosting \[music\] link is down there, too. And you can use the code growth up 10 for an extra 10% off.

**26:02** · Anyway, thanks for watching. I'll see you in the next one.