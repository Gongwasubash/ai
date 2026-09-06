---
title: "Hermes Agent - Full Tutorial & Setup Guide (For Beginners)"
source: "https://www.youtube.com/watch?v=DYdvJCxWd6M&t=1240s"
author:
  - "[[Metics Media]]"
published: 2026-08-31
created: 2026-09-05
description: "Hermes Agent tutorial & setup guide for beginners: deploy the free, open-source AI agent on a Hostinger VPS with no code, connect Telegram and the desktop app, and build an AI assistant that messages"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=DYdvJCxWd6M)

Hermes Agent tutorial & setup guide for beginners: deploy the free, open-source AI agent on a Hostinger VPS with no code, connect Telegram and the desktop app, and build an AI assistant that messages you first.  
✅ Hermes VPS (Exclusive Discount): https://meticsmedia.com/hermes-JPY  
  
In this step-by-step Hermes Agent setup guide, you'll deploy a one-click Hostinger VPS template, configure the Hermes web dashboard, connect an AI model with an OpenRouter API key (DeepSeek V4 Flash), and create your agent's own Telegram bot with a QR code. No BotFather and no tokens needed. Then we go past setup: linking the macOS/Windows desktop app to your server as a remote gateway, teaching your agent permanent preferences with persistent AI memory, watching it write its own AI skills, and scheduling cron jobs so your self-hosted AI assistant runs automations and sends you reports while you sleep. We finish with real running costs, troubleshooting with logs, and parallel sub-agents.  
  
🔗 Links Mentioned in Video  
Hermes Agent (official site + desktop app): https://hermes-agent.nousresearch.com  
Hermes docs (free self-hosting path): https://hermes-agent.nousresearch.com/docs/getting-started/installation  
Hermes on GitHub: https://github.com/NousResearch/hermes-agent  
OpenRouter: https://openrouter.ai  
Telegram download: https://telegram.org/apps  
Hermes Skills Hub: https://agentskills.io  
  
📍 Exclusive Deals & Discounts: https://meticsmedia.com/deals  
  
⏱️ Timestamps  
0:00 Intro  
1:23 What Is Hermes Agent?  
2:13 Choose Where Your Agent Lives  
4:02 Deploy in One Click  
8:04 First Contact - Your Agent's Browser Dashboard  
9:37 Wire the Brain - Models & Keys  
13:45 Chat with Your Agent From Your Phone  
16:37 Meet Your Employee  
18:20 The Desktop App - And Your Agent on Every Screen  
22:40 Teach It - The Correction That Sticks Forever  
26:14 THE PAYOFF - An Agent That Messages You First  
28:13 Run It Like an Owner - Costs & Model Strategy  
30:24 The Owner's Toolkit - Logs, Fixes, Updates  
32:07 What You Can Build From Here  
  
📄 Disclosure  
Some of the links are affiliate links. If you make a purchase through them, we earn a small commission at no extra cost to you. This helps us keep our videos free for everyone.

## Transcript

### Intro

**0:00** · If you've been looking for a clear step-by-step guide to setting up your own Hermes agent, you're in the right place. Hey, I'm Matt, and by the end of this video, you'll have an AI agent that runs around the clock on its own small server, messages your phone on Telegram when it finds something worth knowing, and teaches itself new skills as it works. We'll build it from zero together.

**0:18** · And I'll also connect the official desktop app to the same agent so it sits one keyboard shortcut away while you work. And if you're wondering whether this is just ChatGPT with extra steps, near the end of this video, you'll watch my agent write its own automation and message me first with nobody at the keyboard. Watch that moment, then decide for yourself. Now, setup is only the first part of this video.

**0:40** · Once your agent is running, we'll get into how to actually use it, what it costs to keep running, and how to make sure no one else can talk to it. The way I like to think about this whole process is that you're hiring your first AI employee. We'll give it a place to work, a brain, a phone number, some training, and a schedule.

**0:58** · You don't need any coding experience, just the ability to copy and paste, and the whole build takes about 30 minutes. There's one last thing to know before we start. This is the current method while I'm recording, but AI software gets updated all the time. So if a screen doesn't match mine exactly, don't panic. Follow the flow rather than the exact screenshot.

**1:17** · So the first question is what a Hermes agent actually is and what it can do that a normal chatbot can't. Hermes Agent is a free open source AI agent from Nous Research, the team behind the Hermes family of open AI models. Open source means the code is public under an MIT licence, so anyone can read it, run it, and check exactly what it does. The software costs nothing.

### What Is Hermes Agent?

**1:40** · You pay only for the AI models it thinks with and the small server it lives on. There are three things that separate it from the chatbots you know. First, it runs continuously and can act on its own schedule so it can start the conversation, instead of it waiting for you.

**1:55** · Second, it remembers.

**1:57** · It keeps the facts you tell it and the way you like things done across every conversation and every device. Third, it improves itself. When it figures out a complex task, it can write those steps down as a skill, which is just a safe procedure it can call again later. You'll watch it write a skill later in this video. Your agent needs a place to work and that means deciding where it lives. You have two beginner-friendly options.

### Choose Where Your Agent Lives

**2:21** · The official desktop app runs it on your own computer. That's the quickest way to try it, and we'll instal that app later for a different reason. The catch is that everything stops when your laptop goes to sleep. So picture the thing we're building toward. Your agent checks something every few hours and it messages you when it finds anything worth knowing.

**2:39** · You'll watch me set exactly that up near the end of this video, but it only works if your agent is awake at four in the morning while your laptop is shut. So everything I promised depends on your agent being awake when you are not, and that's why we're giving it its own computer, a small rented server in the cloud for about $6 a month to start.

**2:59** · If all you want is to chat with Hermes on your own laptop, the app alone will do that, and you'll have it installed by the end anyway. And you don't have to choose between them, because later in this video, I'll connect the desktop app directly to the server. You get the always on worker and the native interface.

**3:15** · If you'd rather run everything for free on your own hardware, the official docs cover that path and the link is below. Now, there's one more thing to know about that free route and it's about safety. This agent writes files, runs code, and browses the web on its own, and a webpage it reads can contain malicious instructions called prompt injections written to trick an AI agent into doing something its owner didn't intend.

**3:39** · On the server we're about to build, the agent does all of that on a machine that has nothing else on it. So the worst it can touch is that one rented box, not your personal files. Run it on your laptop instead, and those same abilities are pointed at your actual documents.

**3:53** · Either way, it asks permission before doing anything risky and that's a safety rail we'll come back to, but the agent is still learning the job and I'd rather it learn on its own machine. First, our agent needs a place to work. We're using Hostinger because their one click template instals Hermes for you, and the first link in the description stacks an extra 10% discount on top of whatever sale they're already running.

### Deploy in One Click

**4:15** · Use a link on screen or in the description below. That'll take you to this page here. Go ahead and click the Choose Plan button and then take a look at the plan options. We want KVM 1. It's the smallest plan and my testing shows it runs one agent comfortably. There's one caveat though.

**4:34** · If your agent ends up doing heavy web browsing all day, the next plan up gives it more breathing room, and you can upgrade later without reinstalling anything. So starting small on the KVM 1 plan risks nothing. So go ahead and click Choose Plan. On the next page, the first thing you'll need to do is select your billing period. Longer periods get you a cheaper rate per month, but they cost more upfront.

**4:54** · You can decrease it to decrease your upfront cost, but keep in mind the one month plan does not allow you to use the coupon that gets automatically applied. To get that, you need to choose a minimum of 12 months. Regardless of the plan you choose though, there's a 30 day money back guarantee, so if you decide that this isn't for you, you can always ask for a refund. There's one more thing you have to catch here.

**5:15** · This Ready to Use AI checkbox is pre-checked. It adds about $12 of credits for a different AI service and creates you an account automatically. We're bringing our own AI model access for far cheaper later, so go ahead and uncheck this. Leave the other add-ons off too. Make sure the coupon says it's automatically applied like it is here, and once you've got everything dialled in the way you like it, go ahead and click Continue.

**5:39** · On the next page, you'll register your account. You can use Google, GitHub, or use an email address. That's the one I'll use. Enter a password, and then scroll down and click Register. On the next page, enter your billing address and payment details to complete the transaction. After payment, Hostinger should route you straight into this Hermes setup flow, and the deploy form will give you a default admin username and password.

**6:01** · If you don't see this, and instead you see the bear server dashboard, this is a glitch that happens every now and then, and I'll cover how to fix that in just a minute. On this page, keep the username as Hermes, and then click the eye icon to show the admin password. Go ahead and copy that, and then save it somewhere secure like a password manager. You're going to need this later.

**6:24** · Everything visual from here on out needs that password. Now these two fields at the bottom are for optional paid services you don't need, so you can just leave them empty. Once you've got the password and username saved, go ahead and click Deploy. You may get this brief survey and popups, you can just go ahead and skip and dismiss them all.

**6:42** · In the bottom right, you'll see that your application is being deployed and this can take a few minutes. Seeing it show deploying is normal until it finishes. You can see it just created the container, and when it's all ready to go, it'll show running with a green check mark. I'll go ahead and skip forward to when it's done. Now, if you're one of the few people who didn't get routed straight into the onboarding flow, don't panic.

**7:02** · This is the moment I show you how to fix that. You'll most likely be routed instead to a page like this, or somewhere in the hosting or dashboard. To manually trigger that onboarding flow, what you'll want to do is find the VPS button in the left side, click it, then from there, if you don't have a VPS set up yet, go ahead and click VPS in the upper right.

**7:22** · If your VPS is set up, go ahead and click Manage, then click Docker Manager on the left side, and then from there, click Compose in the Docker Application section. Then click One Click Deploy. Here in the catalogue, search for Hermes and then select Hermes Agent. That'll give you a pop-up that has the same onboarding flow. Go ahead and fill out that form like I showed you earlier.

**7:46** · Now, if you get lost in the hosting or dashboard, and you need to find a Hermes agent that you've already set up, it's the same idea. You go to VPS, then Docker Manager and Applications. And here you can see our Hermes Agent is running, and there's this traffic reverse proxy, which helps encrypt our network traffic. Next, let's set up our agent.

### First Contact - Your Agent's Browser Dashboard

**8:06** · It used to be that you had to use the terminal and use a bunch of commands to set up Hermes, but not anymore. Now, here you can simply find your Hermes Agent and then click Open, and this opens the login page for the Hermes web dashboard.

**8:20** · Go ahead and enter your Hermes username, which should be Hermes from earlier, and then enter the password that you saved in your password manager from the onboarding flow, then, click Sign In. Welcome to your Hermes dashboard. This is your agent's control room, so let me give you a quick orientation before we start changing things. Sessions is every conversation your agent has ever had on any device and they all share one memory.

**8:44** · Models is the brain, and that's the first thing we're going to fix, because right now there's no model chosen at all. Cron is the schedule, and this is the page that lets it work while you're asleep. And skills is everything it has taught itself. We'll visit most of these rooms today. If you click Chat, you'll get your first surprise of the setup.

**9:02** · You get this retro looking chat window, the same thing you'd see in the terminal, and you could start a chat right away, except that if you look at the upper right, there's an error that says, there is no provider selected, there's no model. Your agent is installed and running, but it can't think yet. It needs a model provider, which is essentially like the brain for your agent.

**9:21** · And down in the left corner, you'll see that there is a gateway running, but there are zero active sessions. The gateway is the part that connects your agent to the outside world, so it's what carries messages to and from your phone later. Right now, it has nothing to connect to. So that's our next job. We give it a brain and the rest of this page comes alive. All right, so your agent has a workspace.

### Wire the Brain - Models & Keys

**9:42** · Now let's give it its brain. Your agent needs an account that supplies its thinking, and we're using OpenRouter. OpenRouter is one account that gives you access to hundreds of AI models from different companies, and you only pay for what you use. Go to openrouter.ai or simply click the link in the description below. When you're there, click Sign Up in the upper right and create an account. Once you've done that, you'll be routed to a welcome page.

**10:05** · Sign up as an individual or a business, depending on your use case, and then copy your API key by hitting the copy icon. An API key is like a password for your agent, so don't share it with anyone, because anyone who has it can get access to use your account. I recommend saving this API key in a password manager because you're never going to see it again.

**10:27** · Once you've got it copied and saved somewhere safe, go ahead and click Continue. Go ahead and add your billing information, then, add a payment method to save to your account. Next, you'll need to add some credits to get started. There are some pre-set options with 10 being the lowest, but I recommend starting with just $5 for testing purposes.

**10:45** · On the model we're about to pick that genuinely lasts weeks, you can enter that in the custom field below, then click Add Credits, fill out the survey if you get one, and then go to your dashboard. Next, I recommend adding a spending limit as a guardrail. Go to your API keys on the left side, find your new key that you just created, and click the three dots on the right to open its sub-menu, then, click Edit.

**11:08** · From here, you could give this a name if you wanted. I'll go ahead and call this Hermes Agent, so I know exactly what this is for, and then you can set your credit limit. Let's say, for example, $10, I'll lock that in. And then at the bottom, you can click the dropdown to set how often that limit resets.

**11:26** · Is that daily, weekly, or monthly?

**11:29** · I'll go ahead and set weekly, that way I never exceed spending $10 in any given week. Now that we've got our API key, let's go back to our Hermes Agent and give it its brain. We'll close out of OpenRouter, and then on the left side, scroll down to find keys. Here, scroll down to find OpenRouter in your list, and then click to expand that item.

**11:50** · Click Set on the right side, and then paste in your key in the value field.

**11:55** · Then click Save.

**11:58** · Next, back on the left side, scroll up and select Models, and then find main model and click Change. Since OpenRouter is connected, you can click that in the upper left, and then here's the full list of models that you have access to through OpenRouter. Some are more expensive than others. We're picking DeepSeek-V4-Flash because it's cheap, it's fast, and it's good at using tools, which is exactly what an agent does all day.

**12:25** · So find that in the list, select it, and then click Switch. You'll get a confirmation window, go ahead and click Reload, and now you'll see that the DeepSeek-V4-Flash has been loaded in as your main model. There's one alternative worth knowing about. Hermes also offers something called Nous Portal, a flat rate subscription from about $20 a month with no keys to manage at all.

**12:45** · It's a pretty good deal, but we're starting with OpenRouter because $5 of pay as you go lasts weeks on this particular model, and your first month with an AI employee shouldn't begin with a subscription. If you ever want the flat bill instead, switching to Portal is one login. To get there, you go to Keys on the left side, and then the top option is Nous Portal. Just click Login to get started.

**13:08** · Now, if we head back to chat in the upper left of this left side menu, we can see that our new model is connected and live and that error message is gone. To test that everything's connected, go ahead and click into the chat window, say hello or send a simple question and let it think. If you get an error like this that says it can't respond, click New Chat in the upper right and try again.

**13:31** · Here I'll say, "Hello," and now we got a response. That's the same agent that couldn't say anything just two minutes ago. Now thinking with the model you chose and billed by the penny. Now that the brain is wired up, let's give you a way to reach it by phone. We're going to give your agent its own Telegram bot, and this is the step that lets your agent reach you when you're nowhere near this browser tab.

### Chat with Your Agent From Your Phone

**13:55** · It's the most streamlined part of the setup. In the left side, select Channels, and then you'll see Telegram is the first option. Hermes supports 20 plus platforms, including Discord, Slack, WhatsApp, and email, but Telegram is the one with an instant QR flow, which is why it's right for our first channel. Now, before we start, here's what you need in front of you because that QR code expires after about three minutes.

**14:20** · Grab your phone, download and set up Telegram if you don't have it already. If you don't, I'll leave a link in the description below, where you can quickly click to download it, and then keep your phone in hand.

**14:29** · All right, are you ready?

**14:31** · Click Create with QR, and then with your phone camera scan the QR code, open it in your browser, and that'll prompt you to switch apps. Go ahead and allow that, and then you'll get a create bot dialogue. You can give it a custom name if you want, and then click Create.

**14:49** · You'll see it says your Hermes Agent is ready, but before you can actually chat with it, you need to click Save and Restart on your desktop browser dashboard. Telegram won't be a reachable gateway until everything restarts. While it's booting back up, you'll see Telegram says, gateway stopped, and when the gateway status on the left side says, running again, go ahead and refresh your page.

**15:09** · You'll see Telegram says connected, and now on your phone, you can click Start to start your conversation. Now, Hermes doesn't recognise /start as an actual command to start a conversation, it just opens it up. So then go ahead and type a message. Let's just send a simple question.

**15:25** · I'll say, "Can you hear me?"

**15:29** · After a minute, you'll get a message back from your Hermes agent. Here mine says, "Yes, I can hear you loud and clear.

**15:34** · What's on your mind?"

**15:35** · Now, you might get this message right before that one that says, "There's no home channel set for Telegram." You want to set a home channel because that's where Hermes will deliver your cron job results and anything that happens while you're away. So go ahead and tap that /set home link, and now your cross-platform messages will be delivered here.

**15:54** · So if your agent needs to get your attention while you're off doing something, this is where it'll send that message. Now, there's a couple more quick things you should know about Telegram while we're here.

**16:02** · This process made it so that your account is on the allow list, meaning anyone else who finds your bot and messages it gets nothing back, because they're not on the allow list, but you can add people later if you want to share it by running through the same QR code process with them and their phone.

**16:18** · Also, that reply we just got is coming from the same agent we were talking to in the browser with the same memory, it's just a different door. You can add as many channels as you want, and they'll all share the same persistent memory across every single device. That way, you can start a conversation on your phone and pick it up later on desktop, and then continue on your tablet even later.

### Meet Your Employee

**16:40** · All right, let's find out what you hired. From here, you can continue the conversation on any channel you set up. We could continue on the web browser dashboard. We just set up Telegram on our phones, so we could continue there. Or if you have Telegram installed on your desktop, the nice thing is the bot is already configured there too. You did the setup once, and now anywhere you run Telegram, you can chat with it.

**17:02** · So here I have the desktop version of Telegram in front of me.

**17:05** · Let's ask the agent directly, "What tools do you have?"

**17:09** · You can see in the upper left, it's typing its response, which really sometimes just means it's thinking and responding, and here we get our message. Now, this reply is a tour in itself. It has web search, a full browser it can actually drive, files, code execution, image generation, voice, schedule jobs, and sub-agents, which are helper agents that can spin up to work on parts of a job at the same time.

**17:31** · That's the difference between a chat window and an employee. So now let's hand it a real job. Let's ask it, "Research the top three standing desks and give me a one paragraph comparison." You could do the same thing with any research topic, and here you can see it starts to use the browser. It's searching for the top standing desks. This can take a while, so I'll go ahead and fast forward to when it's done.

**17:52** · After a while, you can see that it searched, read, and then came back with an answer rather than a list of links. And again, the same conversation is on every device now, because it's one agent behind many doors with the same memory everywhere. If you ever ask for something consequential, like downloading a package or deleting sensitive files, it'll stop to ask for permission first. Simply approve it and it'll proceed.

**18:16** · That prompt is your safety rail because the agent is capable, but it isn't unsupervised.

### The Desktop App - And Your Agent on Every Screen

**18:23** · Remember the choice from the start, app or server?

**18:26** · Here's where you get both, and here's why you'd want the app on top of what we've already built. The browser dashboard works from anywhere, but it's a tab you have to go find. The app puts your agent one keyboard shortcut away on top of whatever you're already working on, and it can listen and talk back.

**18:45** · So we'll instal it, and instead of letting it run a second agent on this Mac, we'll point it at the server it already has. I'm on a Mac here, but on Windows, it's essentially the same flow. You just use the control button anywhere I would press command. To download the desktop app, go to hermes-agent.nousresearch.com, and you'll land on this page here.

**19:06** · You can also just use the link I've put in the description below to get here too. Depending on what kind of device that you're using, it'll show you the desktop download button for your device. So here I have for Mac OS, and we'll go ahead and click that. We'll save it in my downloads folder and then run the installer that you download. On Mac, it's pretty simple.

**19:25** · We just need to drag the Hermes application icon into the application folder, and that's it. Next, simply find the Hermes application in your applications folder and double click to run it. We'll go ahead and approve the app, and that'll open up the onboarding flow. Simply click Instal Hermes to kick it off. This will launch a guided build with 11 visible steps covering prerequisites, a Python environment, the gateway service, and the app build.

**19:50** · This can take a few minutes, so I'll fast forward through it. When it's done, it'll say Hermes is Ready, and you can click to launch Hermes. The first thing it'll do is prompt you to pick an AI provider, but that would create a second local agent, and we already have one on our server, so just click I'll Choose a Provider Later. And now here you are on the Hermes desktop app.

**20:11** · And now for the part that makes it one agent instead of two. Click the gear icon in the upper right, or you could click command and comma on your keyboard. On the left side, select Gateway, then select the remote gateway. And then here you'll want to paste in your server address. To find this, return to your Hermes agent dashboard in the browser, and then simply copy the whole address before any /endpoints.

**20:41** · For me, that's this Hermes-agent with a series of numbers and letters .hostinger.cloud. So we'll go ahead and copy this, head back to Hermes, and then paste in that remote URL. It'll scan and see how it authenticates. It says, "This gateway uses a username and password," so go ahead and click Sign In. That'll open up this familiar looking login page.

**21:02** · So go ahead and enter your username, which should still be Hermes, and then enter your password, and then sign in. You'll get a signed in toast notification as a confirmation, and then you can click Save and Reconnect. This will restart the gateway, and when it's finished, you should be able to chat with your agent on your existing server. Go ahead and close this out. The app reloads showing the server sessions, including your Telegram chats.

**21:27** · The model badge reads Deep Seek down here in the chat, and we can send a message to prove that we're connected.

**21:33** · I'll say, "What was my first ever message to you?"

**21:36** · And it responds by saying, "Can you hear me?"

**21:38** · That's exactly right.

**21:40** · So this is what the desktop app looks like, and you can chat with it here just like you would in Telegram, on the web dashboard, or really any AI desktop app. You've got your conversations on the left. You can start new sessions by clicking at the upper left, and you can do all sorts of stuff right in here. But as you're using your computer, you might not always want to just have this app up.

**22:02** · That's when the heads-up display comes in handy. On your keyboard, if you type command shift H, that'll collapse Hermes into a floating composer bar that you can park on top of any window. So you can ask it things mid-work and it fades when it's idle. It's basically just the chat bubble of the app without all the other stuff. You can also talk to it by using the voice dictation.

**22:24** · You can start a voice conversation, and you can even have it read its replies out loud to you. And if you don't want to have to touch your keyboard to talk to it at all, you could enable a wake word, so that you simply say, "Hey, Hermes," and that activates it. You can return to the full desktop view by clicking this Exit Hub Mode button.

### Teach It - The Correction That Sticks Forever

**22:43** · All right, your agent has a place to work, a brain, phone access, and desktop access. Now for the training. Here's a moment every AI user knows. You correct the AI, it fixes that one reply, and the next session, it's already forgotten, and you're correcting it again. Watch what happens when you correct Hermes. Let's give it a task. I'll say, "Write a short post about productivity habits for remote workers."

**23:07** · After a minute, it comes back with a short post. Now, that's pretty good writing, but look at the shape of it. It's got bold headings, a bulleted list, and it signs off by asking if I want it tweaked at all. That's not how I'd want this post to look. So let's give it a correction in plain language. We'll say, "Too wordy. I prefer short, punchy sentences, three paragraphs max, no headings or bullets.

**23:30** · Save that as a preference." I'm not editing a settings page or editing a system prompt. I'm just telling it plainly the way you tell a new hire, and you can see here it's saving that to memory. After a second, it comes back with a fresh response, much better. Now, in the same session, let's ask for a different post. I'll say, "Now write one about managing focus while working from home."

**23:53** · In the same conversation here, it remembers and writes a post more in the style that I like, but any AI can pull off that trick because it has context from the conversation. The real magic happens when you go to a brand new session, so let's do that. You can click New Session in the upper left, or on a Mac, hit Command N on your keyboard. Now, let's give it a task.

**24:14** · I'll say, "Write me a short post about the best European travel destinations for plenty of beach time." That was the real test. This is a brand new session with no history and nothing carried over, and it's now still plain prose in the shape I asked for once, three paragraphs max, no bullets, no headers. That one correction in the other chat, and it's stuck for every chat going forward.

**24:38** · That's the feature that separates an agent from a chat window. Now, there's one more layer to this, and this is the one that compounds. What you just watched was a preference written into its memory, and you can see the memory tool fire the moment it saves, like I showed you earlier. But now, let me show you the capabilities page. Click Capabilities in the left sidebar, and here you can see everything Hermes is capable of doing.

**24:59** · Now, one quick thing so it doesn't trip you up. The app calls this page capabilities and it includes skills, tools, and MCP. The browser dashboard separates all of those into separate pages. On this tab, these are the skills that your agent has. These are whole procedures your agent can call, and eventually, as it's working, you'll see new skills emerge that have the label learned. Those are ones it picked up on its own while working.

**25:23** · It's memory, it's skills, and a file called SOUL.md that holds who it is and how it behaves all live on your server, not in someone else's account. You can click to open any of these skills or tools and see in plain text exactly what's going on under the hood. And you're not limited to skills that it writes itself.

**25:44** · At the bottom of this page, you can see skills hub, and on the right of that, click Browse the Full Hub. This will open a browser that shows you a tonne of different skills that you can download and use inside of Hermes. If you expand this, you can see there's a search bar, where you can search for specific skills or browse by category.

**26:02** · If you wanted to connect something like your Google Calendar, you could search for Calendar, for example, and here, actually, you can see already built in is the Google Workspace, so we don't need to instal that, but you can search for other skills just like this. And finally, the schedule. Here's the demo I promised earlier, and it's the thing a regular chat can't do. I'm going to tell my agent what I care about once.

### THE PAYOFF - An Agent That Messages You First

**26:25** · It's going to write its own skill for the check, schedule itself, and then from then on, my phone buzzes only when there's something worth knowing. It takes just one message, so watch the whole loop. Let's go create a new session, and then I'll send a message like this. "Watch YouTube for AI productivity trends.

**26:43** · Build yourself a reasonable skill for the check, keep track of what you've already shown me, schedule it every few hours, and message me here only when there's something new." And there it goes. You can see it's thinking, working out how to solve this problem. It quickly installed a dependency that it needed to accomplish this task. It's actually searching YouTube, finding videos, and writing the skill and setting up the schedule.

**27:08** · At the end, it comes back with its first report and says it'll run this every four hours. So this is a good example of what it'll look like the next time it runs. And if you go to the left sidebar, where it says Schedule Jobs, you can see the exact job it wrote. You can see how often it runs, when it runs next, and the exact prompt it's using.

**27:27** · You can pause it or trigger it by hand, or you can even add 10 more jobs so you could have a watcher for prices, a topic, a competitor, and anything with a page or feed will work for this. And when it actually runs, this is how it comes through.

**27:43** · It shows me here my message, new AI productivity trends, eight new videos clear the threshold, and the biggest takeaway across all of them is that this is the year AI stops being a chatbot and starts being a coworker, an operator, and a team. You can scroll through and see the full report. There's links to all the videos and a preview of the top one. That's the loop closing.

**28:04** · I described an outcome once and it built the machinery. Your agent just (indistinct) your phone with something useful, so now let's talk about what that costs because the answer might surprise you. Head to OpenRouter again, open Personal, and then the activity page. This is the OpenRouter activity page, and everything on it came from making this video. Here you can see the total spend across 105 requests was 13 cents.

### Run It Like an Owner - Costs & Model Strategy

**28:31** · Now look at the token count, because it doesn't line up with what you'd expect. That's nearly four million tokens for 100 messages, which works out to something like 38,000 tokens every time I say anything. Your agent doesn't just send your question. It resends its instructions, its memory, its tool list, and the whole conversation so far every single time. That rereading is called context, and it's almost your entire bill.

**28:58** · So why is it still only 13 cents?

**29:00** · This panel is the answer. Three quarters of everything it read came out of a cache, because the provider recognises the part of your request that hasn't changed and charges a fraction to read it again. You didn't configure that and you don't have to. At this rate, the $5 you put in back at the start covers somewhere around 4,000 messages, and that's why I told you it would last weeks.

**29:22** · Now, earlier I told you to start with DeepSeek-V4-Flash, but you're not locked into one model. You can keep the cheap model for daily work and switch to a stronger one when the task deserves it, and there are free models in the list too. Those are rate limited, but they're fine for experiments. You can change your model by clicking the model selector down here and scrolling through the available options.

**29:43** · For example, let's say we wanted to use something like Opus 5 for a task. You can switch just simply by clicking it. Keep in mind, Claude models from Anthropic or ChatGPT models are going to cost more than the models from DeepSeek. And remember the spending limit we set. The server bill is fixed, so the model bill is the one to watch and now you know how to watch it.

**30:03** · If you're on Telegram and you want to switch your model, the easiest way to do that is to type a command /model. And here you can select your provider, we'll say OpenRouter, and then it'll show you the full list of models that you can select from again. I'll switch us back to DeepSeek-V4-Flash. Now you know how to switch models from any interface. If you don't have a button, use the slash commands.

### The Owner's Toolkit - Logs, Fixes, Updates

**30:26** · Let's cover the five minutes that separate owners from tourists, which is what to do when something's weird. We're back in the web dashboard for this part, because troubleshooting is a server job and these pages live on the server. In the left sidebar, click Logs. The logs are your agent talking about itself. You don't need to read every line. You just need to recognise a healthy one and spot the ones that say something has failed.

**30:51** · If something's weird, this is a great place to check. You can use the filters at the top to specifically find any errors, which are the most severe, warnings, which are a step down in severity, and then you have info and debug messages. I didn't spot any error messages here because I haven't encountered anything strange, so this is all good to go.

**31:10** · But if your bot stops replying, restarting the gateway is the first thing to try and it fixes it most of the time. Click Restart Gateway in the left sidebar and then Confirm. Give it a few seconds to complete the operation. And when it's restarted, you'll see the gateway status is set to running. Now, if that doesn't do it, go one level up and head back to your Docker Manager in Hostinger.

**31:31** · Here you can find your actual Hermes application, click the three dots next to it, and then Restart. This restarts the whole application, not just the gateway. And this is the bigger hammer. The dashboard logs you out when you do this though, which is normal, so just sign back in when it's back up. Now there's one more thing for the curious. A web terminal lives in the Docker Manager too.

**31:54** · You can access that by clicking the Web Console button in the upper right. You can use the command Hermes Doctor, which will print a full health report. Now you don't need that today, but just know it's there for if you ever want that level of control. Let's finish with where you can go from here.

### What You Can Build From Here

**32:12** · Ask it to split a job across sub-agents and it divides the work, runs the parts at the same time, and hands you one answer. Like for me, I have a prompt here saying, "Plan me three days in Lisbon, one sub-agent on which neighbourhood to stay in, one on where to eat, one on a day trip worth taking and one on getting around, then give me a single itinerary."

**32:32** · The nice thing about using sub-agents too is that it can go out and do several different jobs in parallel. So you're not waiting on one agent to go do several tasks. The one agent iMessaging is coordinating with four other agents who are all doing that work at the same time. So that can help to speed up big tasks by breaking them down into smaller tasks. Here you can see each of those four sub-agents working.

**32:56** · And when they're all done, the main agent comes back with the final report. Now, another thing, more channels work the same way. If you click Messaging on the left side of the desktop app or Channels on the left side of the browser app, you can add Discord, Slack, WhatsApp, email, and many other communication channels. In the desktop app, there are profiles, so you can keep a work agent and a personal agent.

**33:21** · To add a new profile, click the plus button next to the home button in the left side. Simply give your profile a name, any additional details you want, and click Create Profile. Now I have a completely independent environment for my personal projects, and I could make that first agent just a work profile. And lastly, if you're coming from OpenClaw, Hermes makes it easy to import your configuration. Just simply ask, "I'd like to import my OpenClaw configuration.

**33:47** · Can you guide me through that?"

**33:48** · And it'll help you with the whole process. Here for me, for example, it's asking if I want to import my OpenClaw settings into Hermes, import the OpenClaw skills and workflows into Hermes, or if I want to use OpenClaw as a tool. Go ahead and answer it and follow along with the process to get everything connected. So here's your only homework. Ask your agent what it could take off your plate.

**34:10** · Tell it your job, tell it what your week looks like, and let it propose something. That costs pennies to try. And the first link in the description stacks an extra 10% discount off the server that makes all of this possible.

**34:21** · Thanks for watching.