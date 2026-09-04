---
title: "I taught Claude how to use Premiere Pro and it's INSANE."
source: "https://www.youtube.com/watch?v=Ohyo6-VO1jY&t=984s"
author:
  - "[[Jason Cooperson]]"
published: 2026-07-24
created: 2026-09-03
description: "🚀 Get the Plug n' Play Claude Video Editor Project Folder ⤵️https://www.skool.com/leveragelab/about🔗 HyperFrames (the free open-source toolkit Claude uses to make motion graphics) ⤵️https://gith"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Ohyo6-VO1jY)

🚀 Get the Plug n' Play Claude Video Editor Project Folder ⤵️  
https://www.skool.com/leveragelab/about  
  
🔗 HyperFrames (the free open-source toolkit Claude uses to make motion graphics) ⤵️  
https://github.com/heygen-com/hyperframes  
  
🔗 Premiere Pro MCP (the bridge that lets Claude control Premiere Pro) ⤵️  
https://github.com/hetpatel-11/Adobe\_Premiere\_Pro\_MCP  
  
Like, subscribe, and drop a comment if you want more honest AI builds like this!  
  
⏰ TIMESTAMPS  
  
0:00 Intro  
0:54 Project Overview  
5:24 Live Demo: The Rough Cut  
7:24 Live Demo: Motion Graphics  
12:18 Get it from my Skool  
13:29 Build It Yourself (Tutorial)  
15:40 Final Thoughts & The Future  
  
Follow me on other platforms  
📸 Instagram: https://www.instagram.com/jasoncooperson/  
🎞️ TikTok: https://www.tiktok.com/@jasoncooperson  
  
Summary ⤵️  
  
Every cut, transition, and motion graphic in this video was edited by Claude, inside Premiere Pro. I gave Claude control of my editor, it opened Premiere, cut all the raw footage, and edited this entire video. I'll let you be the judge of how well it did.  
  
The whole thing is just a folder of files on my computer: a Claude project with everything it needs to edit like me. Two core engines run it all. HyperFrames is a free GitHub repo that lets Claude generate motion graphics with HTML: it builds a web page, animates it, then records that animation as the graphic. The Premiere Pro MCP is the bridge that lets Claude actually drive Premiere: importing footage, cutting the timeline, adding transitions, all of it.  
  
Why not a video gen model like Higgsfield? I tried both. HTML graphics are cleaner, faster, and free. Higgsfield still wins for cinematic B-roll, but for motion graphics HyperFrames is 100% the way to go.  
  
Everything else in the project is my specific stuff: an assets folder with my sound effects, plus all the skills, workflows, presets, and editing styles baked in so it runs together smoothly. If you want to download the entire pre-built project (the one I've been building for the past couple months), it's inside my Skool community (first link above). If you don't want to pay, totally fine: I show you how to build it yourself for free in this video.  
  
You don't need to know how to keyframe or master the technical side of editing anymore. You need good creative ideas, and then you prompt.  
  
What I cover ⤵️  
  
\- The Claude video editor project: what it is and everything inside the folder  
\- HyperFrames: the free repo that lets Claude generate motion graphics with HTML  
\- The Premiere Pro MCP: how Claude actually controls Premiere Pro  
\- Live demo: Claude turning raw footage into a rough cut  
\- Live demo: Claude creating a motion graphic from a single prompt  
\- The full tutorial to build the whole system yourself for free  
\- Why HTML graphics beat video gen models like Higgsfield for motion graphics  
\- What this means for video editors and the future of content creation  
  
If you're into using AI to build stuff that actually makes you money and saves you time, not just tips and tutorials, come learn how to build automations like this with me. I run a community of high-level builders with 2 group calls a week, plug-and-play systems, and a full Claude Code course (including this exact video editor project, my Content OS, and the finance system from my last video). First link down below. 👇

## Transcript

### Intro

**0:00** · what you're watching right now. Every cut, \[music\] every transition, and every graphic was done by Claude within Premiere Pro.

**0:09** · Claude opened up Premiere Pro, cut together all of the footage, generated all of the graphics, and actually edited this entire video. And I'll let you be the judge of how well it did. But, honestly guys, I think that this is just the beginning. I think that this is the future of where video editing is \[music\] headed.

**0:27** · I believe that you don't need to know how to do key frames, you don't need to know what an adjustment layer is anymore, you don't need to know any of the technical aspects of things because that is being essentially replaced by AI, and now we can just focus on the creative aspects of \[music\] creating content. And again, guys, I just want to remind you that everything you've seen so far has been edited using the exact system that I'm about to show you in this video right now. So, without further ado, let's get into the tutorial. \[music\] All right, guys. So, before we get into the nitty-gritty of the video, I'm going to quickly go over an overview of this entire project.

### Project Overview

**0:59** · Now, if you want to skip this part, you totally can. You can skip to the demo, or you can skip to the tutorial section if you just want to get it straight into it. Okay, so basically, what this project is that I've been working on and how I actually edited the intro that you just saw was with this project folder.

**1:16** · It's pretty much just a Claude project that lives on my computer. So, it's a folder of files. You can see all these files, and that is how it's able to edit videos. I had to custom build a lot of this stuff. You can see this is what it looks like on my computer, and this is what it looks like when you're in a Claude chat. Now, it's really built upon two core engines here. We have Hyper Frames, and we have the Premiere Pro MCP. So, Hyper Frames is how it's actually able to generate the motion graphics. And then the Premiere Pro MCP is how we connect up the Claude app to our Premiere Pro.

**1:47** · Basically, how I edited the intro of this video is I'm just prompting. I'm literally just talking in a Claude chat. I'm like, "Hey, create a visual of this." For example, I want to have a movie director on the left-hand side. Claude has like a cape and he's flying and there's lights on him, right? You describe literally whatever it is that you want and Claude will use hyper frames to build out the actual motion graphic and then use the Premiere Pro MCP to put it actually inside Premiere. Now, there's a couple of other tools and installations you need.

**2:13** · Whisper X is the transcription tool that we're using to transcribe videos so that we can know how to cut them and where to cut them. So, both of these free open source repos will be linked down in the description below.

**2:26** · Now, let me explain how hyper frames works. So, you're like, "Ah, how does it generate these motion graphics, right?

**2:31** · Are you generating the video or are you actually building the actual motion graphics, right?" And what it's actually doing is actually building the motion graphics and you can think of it like this. You know, Claude is really good at building websites, right? We already know that. It's really good at web design and coding and a lot of the times we're just using HTML, which is a coding language, a website building coding language, uh to create, you know, things like websites. And so, if I click here and if I go to this website, you can see it's animated, right? All of these animations and everything here.

**3:01** · When I scroll, it gets larger, blah blah blah. These things fade in, they dissolve in.

**3:06** · There's all these animations right here.

**3:07** · And so, that is how Claude is actually creating these motion graphics for me.

**3:12** · It's just kind of building a HTML website that does that and has that animation and then it's screen recording the website to then capture that animation, turn it into a video, and then, you know, put it in your Premiere Pro timeline or whichever editing software you're using. Now, MCPs. How do we give Claude control over Premiere Pro? This is also pretty easy.

**3:30** · It's pretty much just that GitHub repo that I mentioned before that has all the code and all the tools necessary and it basically serves as this little connector right here so you can, you know, plug Claude into Premiere and now you can say things like, "Oh, hey, like apply a transform effect and then like do all these key frames." And I'm like, "Damn, that actually looks good. Let's make it slightly less intense, right?"

**3:54** · So, it's going to actually go into Premiere and put all the key frames in there. I would like to also mention that this also works with DaVinci Resolve Studio. Okay, it has to be the paid studio version, and it also works with Final Cut Pro. However, there has not been a CapCut one published yet. So, to sum it up, really, this whole system is pretty much just a folder of files on your computer, and it can generate motion graphics, it can control Premiere Pro, or whatever other editing apps you need.

**4:21** · And my specific folder has a bunch of pre-built prompts, presets, and tools that are already coded in there, and it's a lot of the work is already done.

**4:30** · It's already a full fully built-out system, uh so that you don't need to do all that work. You can think of it like an app, except Claude is the app. So, with all of that out of the way, I want to talk about now the two different ways that you can go about building this for yourself. Now, if you want, you can just get the paid version. It's inside my school community, like I mentioned. I already built out all of this for you, and it comes plug and play, you know, works right out of the box, and you also get the support of being inside my school community. So, I have group calls, I can help you make it work.

**5:00** · That'll be the first link in the description. So, if you don't want to pay for it, that's totally fine. I'm going to show you how to build this for free right now in this video. You can definitely use the YouTube transcript, so take the transcript of this video, use that, kind of like plug it into Claude, and it'll help you build this as we go. Next, I'm going to do a live demo, so you can actually see it in action, what that looks like, and then after that, we will get into the tutorial, the step-by-step of how you can build this. I'll see you there. All right, guys. So, now I'm going to do a live demo of the Claude video editor in action, so you guys can see it actually run.

### Live Demo: The Rough Cut

**5:32** · So, basically, what we're going to do is do a rough cut for the overview section of this video, which is the section that you just watched. So, what I'm going to do is go in Finder and select my raw footage. I think the raw footage is about like 9 minutes long.

**5:47** · So, we're going to command option C to copy the file path. I'm going to paste in the file path, so it knows where to find it. Or, you can simply say, "Hey, find the footage in my downloads folder." And then I'm going to give off a prompt, something like this. "Hey, I need you to do a rough cut for this raw footage. It's part of the Claude Premiere project. Just put it in the timeline right after the intro section.

**6:11** · And I also want you to cut it pretty hard. So, I really want you to cut out everything that's not like absolutely essential. So, cut it as much as you can. Only really keep the essential parts and just throw it in the Premiere timeline. Go now." Okay, boom. So, that's literally all I needed to say.

**6:31** · And now I'm just going to let it run and come back when it's done. My guess is it'll probably take about 10 minutes.

**6:48** · All right, guys. So, that just finished and it took about 15 minutes. I think it spent a little bit of extra time like verifying a couple things. It did a pretty good rough cut. So, it took it from a 10-minute long clip to a 4-minute long total thing. And it also applied some amplify and hard limiter preset thing that I have, so it already took care of the audio, too, which is very, very nice.

**7:12** · And that's pretty much the rough cut done. Now, I don't need to really touch it at all. I can, of course, verify though and make any extra changes that I want to here if I want to drag some clips or adjust some things here, which is super, super nice in terms of flexibility. Okay, now I'm going to show you a quick demo of how we generate graphics. So, as an example, I'm going to be trying to recreate this little graphic here of Mars, Earth. We can open up Claude and what we're going to do here is say, "Hey, I I I you to create a graphic.

### Live Demo: Motion Graphics

**7:40** · So, for the background, it's going to be like uh off-white, a little warmer grid background, and it needs to be like grungy and and textured. Uh and it needs to also be animated, too. So, maybe we can have like two different frames that it kind of goes back and forth between to give it the animated look.

**8:01** · So, that's for the background. So, for the animation, we're going to have Mars, the planet, pop uh it's going to rise up to the center, and then the text is going to appear above it that says Mars, and then it's immediately going to slide to the left, and then Earth is going to slide in like slide in from the right, and then the text is going to pop pop above it that says Earth. And both of those need to be like actual images of the actual planets. I mean, I guess I can give you the PNGs, but I don't know.

**8:30** · Just see if you can go and find those yourself. If not, it's fine. I'll give them to you. But, immediately after that, Earth is going to slide out to the right again, and then Mars is going to come back to center, get a little bit bigger, and under it, we're going to show I think it's -153° C, and it needs to be in like a digital um alarm clock font. I mean, obviously, I could keep going, but I think for now, just for the purpose of this demo, I'm just going to show that.

**8:58** · One more thing is I'm going to say, "Also, there should be a slight shadow behind each planet object, of course. And obviously, you know, everything should be textured as much as you can with halftone or grunge.

**9:15** · Definitely for the background, it should be paper feel. And then for the frame rate, we'll go with 8 FPS." So, that's super important because that gives it that sort of feel and style and look to it. And one more thing I want to say here is, "And so, when you're done with this, just throw it in the graphics demo sequence, so that I can view it." Okay, boom. So, we're going to send off that prompt. I'm going to see how it does.

**9:35** · And we'll see how long it takes. I'm going to start a timer. So, I'm going to come back when this is done. Okay, boom.

**9:41** · That just finished up and it took a total of about 16 minutes and 45 seconds. And let's check it out. Mind you, I haven't done anything to it. I haven't watched it even yet. I just want to see just straight up how it looks out right out of the gate.

**10:04** · Boom. Pretty cool, right? Pretty good, I'd say. I mean, if I want to tweak it further, I can. I would say that's already pretty good to go. So, one more little extra cherry on top is that I'll put this adjustment layer over on top of it that I already have, so I can just copy and paste that in. I'm going to move this over on top. Do like that.

**10:25** · Okay, honestly, I think the grain is a little bit too much. So, I'm going to tone that down to maybe just 30%. Yeah, bump that contrast up.

**10:35** · Turn down the exposure. Okay, again, let's just re-render everything.

**10:43** · All right.

**10:45** · Dude, that's pretty good. I don't know, man. That's pretty good. Yeah, I mean, if I want to make any extra little changes to it, I totally can. And I can essentially, if I want to change anything, I can just prompt whatever changes I need and it will do it pretty perfectly. But, I'd say honestly, this is good to go right off the bat. Like, there's really not much changes I would want to make besides maybe making the -153°C like a little bit smaller. But, honestly, I mean, it's pretty much a perfect copy.

**11:12** · Like, the the YouTube viewer like isn't going to notice the small little extra details.

**11:19** · Like, this is already like good as is, right? It gets the job done. It even pulled the pictures of Earth and Mars, which is like pretty damn cool, right?

**11:27** · And it cut them out perfectly. This looks amazing. This is pretty much first try. So, that's how you do the graphics.

**11:33** · And that was basically just the entire process that I used to craft, you know, the entire intro of this YouTube video.

**11:40** · I just literally just prompted it and told it what I wanted it to do and it was able to build it for me.

**11:45** · And honestly, guys, this would have taken like hours and hours. I don't even know how to do this on my own. A, it does it autonomously, so I can literally just scroll my phone or do or work on whatever else I want to work on while this is going. B, it does it way faster than if I were to do it myself. I would have had to go into After Effects, do all the keyframes and all that I don't even know how to do that, right? So, I would say this is a massive, massive time save and effort save to get really high-quality looking graphics.

**12:11** · So, that's how you create graphics and that's what I did to make the entire intro of this YouTube video. So, guys, if you want, you can join my school, first link down in the description below, and go to the classroom, go here, and just download the project folder.

### Get it from my Skool

**12:29** · And inside of that project folder, I have everything already pre-built out for you. So, if you look in here, it's going to have all the skills like these.

**12:38** · It's going to have all the hyper frame stuff already installed. It's going to have the Premiere Pro MCP already installed and all of the graphics uh presets and everything and all the knowledge and time that I took to build out this entire system is already all going to be in there pretty much ready to go right out of the box. Not only do you get the files and everything pre-built, but you also get all of the other assets, projects, workflows, automations that I have inside my school community, everything to do from content creation to even just the basics of cloud code and learning how to do that, to finance.

**13:06** · And there's group calls twice a week, so if you run into any issues, you can come talk to me in person. I'll help you solve it or I'll help you get it installed and you can post in the community if you run into any issues and I respond to these every single day with a full loom video. But, anyways, guys, with that shameless plug out of the way, let me get into the free way to do this. So, let's actually go through the tutorial of building this for free. Okay, so the first step is to go in finder, go wherever you keep all of your Claude projects, create a new folder.

### Build It Yourself (Tutorial)

**13:35** · I'm going to name this video editor demo build, okay? And just make sure you have that new folder, and then go here in Claude, click open folder. We are going to go in our projects, and we are going to open that new blank folder that we just created. And now what I would do is take the transcript of this YouTube video and literally just paste in the transcript, and then enter a few lines.

**14:01** · So, paste the transcript of this YouTube video, right? The one that you're watching right now, because then it'll it just has everything about how to build this. And then just say, "Help me" No, not even help me.

**14:15** · "Build all of this. Do not stop until you're done. Go now."

**14:22** · Make sure bypass permissions is on, and then just let that run. That's probably going to get the scaffolding probably like 60% of the way there. That's pretty much what I would do to build this yourself. From there, you just kind of have to prompt back and forth until you get it doing what you need. Obviously, you can copy and paste both of the links to the GitHub repos and paste them in here. Or, if you're on, for example, DaVinci Resolve, you can search for the DaVinci Resolve MCP and copy and paste this one.

**14:53** · Or, if you're on Final Cut Pro, you can do the same.

**14:57** · Final Cut Pro MCP, and then copy and paste this one in there to get it working with your specific application, whatever you have. But honestly, guys, to build it yourself for free, that's really that's really all there is to it. I mean, if you just paste in the transcript of this YouTube video, Claude will pretty much have all of the knowledge it needs to build out this entire thing. It just will be missing all of the signature editing style and presets and common gotchas and all of the infrastructure that I spent time weeks crafting custom building.

**15:28** · And it obviously will take it'll probably take you I'd say two to five hours to get it working like fully fully well. So again guys, if you just want something that works right out of the box, join my school community first link down in the description.

### Final Thoughts & The Future

**15:41** · Okay, now I'm just going to give you some final notes and thoughts about this whole project. So let's zoom out on a larger picture grand grand scheme of things. What is this really mean for video editors and content creators?

**15:53** · Well, if you're a video editor, then I definitely think that you should be using AI to power up your workflow because this is going to help you work faster and better, right? If you're a content creator and you're looking to quote-unquote replace a video editor, I think this will definitely help. Here is the biggest concept that I want to stress about this entire project. Claude video editor does not replace creativity. Okay?

**16:18** · The only reason that the intro of this video that you watched was so good was because I came up with the ideas of what to do for the graphics, right? I prompted it and said, "Hey, let's do a flying arrow that like flies around and then it hits this and then there's like an image of this, right?" That takes creativity. If you say, "All right, Claude, edit this video for me. Make it good." It's just not going to do it that well, right?

**16:45** · I had to go and actually research, "Okay, you know, eight frames per second, halftone grunge texture, paper animations, paper rip animations, Vox style, putting grain overlay." You know, all these creative things that add to the style of the video. And so what this project really means for video editors and content creators is that it it's replacing the execution.

**17:11** · The one plus one technical aspects of video editing, right? No longer do you need to know how to do keyframes or know how to apply effects or do the technical things of coding or building the actual motion graphics and stuff like that because that's the code part of it, right?

**17:28** · So, it can do anything that you want it to do, but you have to actually have the creativity to come up with the ideas.

**17:37** · What this means is that we, as content creators and video editors, we are no longer limited by technical knowledge, right? Now, if I want to create a motion graphic, I can create literally whatever motion graphic I want in any style that I want. All that the The only limiting factor now is my creativity and my ability to prompt well. And actually, here's a really good comparison, okay?

**18:04** · It's like software engineers. So, people that know how to code and know how to build websites and apps are much better at vibe coding than people who don't because they actually know the ins and outs and the the high-level creative aspects of building an app, right? A software engineer who is very skilled is going to be able to prompt AI and build a better app than someone who doesn't.

**18:33** · Just the same way that if you are a content creator already or a really good video editor already, you're probably going to be able to use this project a lot more effectively than someone who doesn't because you already have the skills and the creativity and the knowledge of how to video editor edit. This is just cutting the time and effort that it takes to, like I said before, bring your ideas to life. Now, can you use it to outsource and replace your own creativity?

**19:01** · Sure, if you're just not a very creative person, then you I guess you could just be like, "Hey, Claude, edit this video for me."

**19:08** · It'll do an okay job. It'll do some graphics that are kind of basic, kind of like, "Meh." The worst thing to do, guys, and I see people get frustrated with this a lot. They're like, "Well, it didn't It didn't do a good job." No. You are lazy. And you didn't come up with any ideas, and you're trying to outsource creativity to the AI, which is the worst thing that AI is good for. AI is good at the technical one-plus-one busy work stuff. That's what it should be used for, not creativity.

**19:36** · Your ideas are the highest leverage that you have left. All the AI is doing is giving you the power to, if you have an idea, boom, it's done. So, that's how you should look at this project. It's not replacing your creativity, it's replacing the busy work of actually taking your idea and bringing it to life on the screen. So, that's my final thoughts and how you should look at this, and how you should look at AI in general. I'm going to plug my school one more time. Would love to see you in here.

**20:07** · If you're a content creator or video editor, you don't want to get replaced by AI, and you want to learn about this stuff, and you want to learn how to leverage it to create more content, create better content, scale your business, then definitely join the school community. There's also a classroom, there's Claude Code for Dummies, so if you're just getting started with AI or Claude, then this will have you covered. I have an entire content system, I have a finance system, I have the video editor, along with a bunch of extra miscellaneous stuff. And like I said, there's group calls twice a week.

**20:33** · I'm literally about to hop on one right after this video in like 2 hours and speak live to all the community members. And honestly, guys, not that many people join, so you can get one-on-one time with me. If you join the community, I will help you and coach you one-on-one, or just give you whatever my two cents on whatever you're working on, right? So, would love to see you in here. That's going to conclude this video. I hope you guys got value out of it. I will see you in the next one.

**20:57** · Peace.