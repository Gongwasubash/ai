---
title: "How to Generate UNLIMITED AI Pictures Inside Claude"
source: "https://www.youtube.com/watch?v=4BBgP3gD8Gg&t=705s"
author:
  - "[[AsapGuide]]"
published: 2026-09-10
created: 2026-09-11
description: "ðŸ‘‰  In this video, I will show you how to generate AI images inside Claude by connecting it to Cloudflare Workers AI through a custom MCP connector, since Claude does not come with a built in image mo"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=4BBgP3gD8Gg)

ðŸ‘‰ In this video, I will show you how to generate AI images inside Claude by connecting it to Cloudflare Workers AI through a custom MCP connector, since Claude does not come with a built in image model like ChatGPT or Gemini. This setup gives you access to an image model called Flux and lets you send prompts straight from your Claude chat without paying for an API key or running anything locally on your computer. If you keep running into limits with other AI image tools or just want a simple way to add image generation to Claude, this method solves that problem with a daily allowance of ten thousand neurons that resets every day.  
  
â¤ï¸ Subscribe: https://www.youtube.com/@asapguide?sub\_confirmation=1  
  
Code in the pinned comment :)

## Transcript

**0:01** Â· So, can you generate a picture via cloud? Well, unlike Chhat, Gibbbit and Gemini, cloud does not have a built-in image model. So, you cannot create a traditional image in cloud. And right now, Antropic is not developing any image model. So, that's very unfortunate. And the closest thing that you can do in cloud when it comes to generating visuals is by creating a sort of SVG a picture which is basically just a bunch of codes and that is not a traditional image.

**0:32** Â· This is not the same as creating a picture using Gemini nor banana or chart GBT. But with something called MCP you can bring the capability of image generation from somewhere else into cloud. So this is just one example that I have added into my club account and this is actually not my first time talking about this very topic.

**1:00** Â· Previously I have published some videos about how you can uh bring an image generation feature into cloud. But basically uh you have to use an API key and yeah you have to pay for that API key or you can also just use a local model via cloud cover that's also an option but what if you don't have a BV computer but also you don't have to pay for an API key to generate that image.

**1:29** Â· Well uh that is exactly what I'm about to show you in this video. So I will show you how you can build an image generation MCP tool in cloth but you don't have to pay uh for any subscription or API key and it is not running locally on your computer instead we are going to use the help of Cloudflare.

**1:53** Â· So this is a really really big company and uh they actually offers uh many services for free including running open-source AI model. Actually not just open source there are many models that are available on Cloudflare that you can use for free. Uh they're giving you 10,000 credits every day again for free. And this is not like just some promotional event or anything.

**2:22** Â· it it's basically the way it is for years. So it is not uh something that only happens once a year. No, I think you can use the service uh for years down the line and it is also quite reliable. So I'm going to show you the step-by-step process to set up uh that connection between Cloudflare to cloud and eventually you should be able to uh send a message, send a prompt to cloud to generate a picture like this example.

**2:52** Â· So let's get started. First of course you have to uh navigate to Cloudflare and then you can create a free account and you can log into your account go to the dashboard.

**3:05** Â· So here we want to utilize something called workers. So just navigate to a menu called compute and then click workers and pages.

**3:17** Â· Okay. So just click create application and uh you can just click start with hello world. That's fine.

**3:25** Â· Okay. So here is you you can you can name the workers. Let's say I'm going to call this one cloudflare. Oh, sorry about that.

**3:35** Â· Cloudflare image. Actually not cloudflare. Actually it is cloudflare. Uh you know what Cloudflare Cloud uh image generation that is quite a mouthful name but that should be fine and after that you can just click deploy but just wait for a few seconds for it to be deployed and then later we need to do some setup in here.

**4:01** Â· Okay. So this is the workers the AI workers that we are going to use. Now uh you have to navigate to bindings. Okay, navigate to the bindings menu. Click add binding and you want to click add binding again.

**4:18** Â· Oh, sorry about that. I forgot about that step. Uh let's go back. Uh you have to navigate to workers AI first. I'm sorry about that. So you have to open workers AI and then click add binding.

**4:28** Â· Sorry about that. And let's call this one uh how about image AI.

**4:37** Â· underscore AI. So, let's give it that name for the variable and then click add binding.

**4:45** Â· So, we're just creating a worker AI.

**4:49** Â· Okay, looks good. Now, uh the next thing that we need to do is uh this is for authentication later. So, just navigate to settings and then go to uh click add variable.

**5:03** Â· So let's call this one mcp secret and the value could be the name or sorry the password that we will use later in the mcp authentication in cloud. So you you can use any password. Let's say I'm going to use password 1 2 3. Obviously you don't want to use something like that. You want to use something that is more uh secure. But this is just one example. And don't forget to check secret and then click add one variable and deploy.

**5:34** Â· And again remember the password because we are going to use it again later on the next setup on cloud.

**5:41** Â· Okay. Just click add one and just wait for it to finish to be fully deployed.

**5:47** Â· Uh okay. Do you want to remember password? No thanks. Okay. Now next thing that we need to do is we have to click the edit code button.

**5:58** Â· I'll just wait for this editor to open.

**6:03** Â· Okay. Uh, is this the latest? Oh, it's not the latest.

**6:09** Â· Okay. I have to click the latest because that's the only one that we can edit.

**6:13** Â· So, just click here and then click the latest or anything that is active. And after that, uh, you we need to edit uh this worker.js code. And this is the code that I'm going to use. You can get this code in the description down below and perhaps I'll put it in the maybe in the description or perhaps in a link which later you can visit and then get this code. So I'll just copy it. Let's go back to worker.js. I will just select all of it.

**6:44** Â· Delete and I'll just paste that content the code. Uh unable to read. Okay, sorry about that. I guess I'll just use Ctrl N and V. That should be fine. and click deploy. Just wait for a few seconds. There you go. So, it has been deployed. Now, let's move on to the next step. And this is actually quite easy. So, uh you you want to copy this URL. Okay, you want to copy this. Just copy and then you can open cloth.ai.

**7:23** Â· And we have to create a custom MCP. So click your profile, go to settings, connectors, and then in the connectors, click add. So let's call this one cloudflare uh cloud uh image generation.

**7:42** Â· That's quite a mouthful name. And you can just paste that workers URL. But don't forget to add MCP at the end. So just add that three letters MCP towards the end and then click continue and here we are going to add request headers. So I'm going to select it to be authorization and the value is the password that we have created earlier in the cloud flare worker settings.

**8:10** Â· So remember that uh I mentioned that you have to remember the password because we have to enter it again and at the time the password was oh I forgot to mention something here. So yeah you have to enter enter your password but you have to enter the keyword bearer first before the password. For example my password was password 1 2 3. Okay but I have to enter this error.

**8:39** Â· So this is the keyword that you need to enter before the password. So just make sure that you include that particular word.

**8:53** Â· Anyway, I'll just copy it and let's paste that to the value and click add.

**9:02** Â· Okay. Do you want to save the password?

**9:05** Â· No. Thanks. Now you can click connect and just wait for it to be connected.

**9:12** Â· And there you go. It is available and it should be ready to use. I'm going to close this window.

**9:19** Â· Now, uh we can refresh the page. I just want to make sure that we have the newer version. Now, if you click the plus button in the connector section, you can see that the Cloudflare cloud image generation is available. Uh just make sure that it is enabled and you can use some prompts to test the capability. So, let's go with this one. I think I'm going to generate a realistic picture of a cat driving a motorcycle in a cinematic angle and I want the aspect ratio to be 16 by9.

**9:54** Â· Okay, let's go with that pro and yeah the uh script that we use it it is it does support a customizable aspect ratio. So that is info that you can enter and just send a message. just wait for a few seconds up to a few minutes depending on the prompt. But it usually can start generating the image in less than 20 seconds. So it will check my prompt.

**10:19** Â· It will analyze that if it will require some tools and if it is able to detect that then it will call the workers that we just built in Cloudflare and then it will pass that message.

**10:32** Â· Actually it will improve the prompt first. Okay, there's this permission.

**10:37** Â· Just click always allow.

**10:40** Â· So, it won't ask us again.

**10:44** Â· And yep, now as you can see, it is actually improving my prompt. That's really nice. So, hopefully we can get the result very very soon. And by the way, in the script, I was using a model called flux to clean 4B. You can use anything else. There are plenty of models available in the Cloudflare workers AI, but I intentionally go with this model because it is fast and also very very cheap. Remember, we have a limit of 10,000 credits. They call it 10,000 neurons every day.

**11:16** Â· And with with this model, you can generate hundreds of images a day. But you can use a more capable model like the 9 billion variation of this model, but it will be more expensive. And again, there are some other models that you could try and explore later. Anyway, let's go back to cloth. And there you go. So, we got this image of a cat riding a motorcycle. So, yeah, it does work.

**11:44** Â· And as you can see, I literally made this video without any cut just to show you that it is quite a smooth sailing process. Now, there is one thing here that you need to know about this system. The model itself can edit an image but because of the fact that we are using MCP uh the image that we upload to cloud uh won't be passed via MCP to Cloudflare.

**12:12** Â· So Cloudflare cannot see the image that we just provided to cloud. And yeah there are some other ways we can uh navigate around that problem but honestly it's just so complicated. I think if you want to use uh an image model for image editing, I don't think you want to go with this way.

**12:33** Â· I think this method is really just a way to generate have some assets that later you can use for your projects in cloud or at the very least this is a proof of concept that you can access the capabilities of some other AI models from cloudflare for free inside of cloud and it is going to enhance some extra capabilities of cloud AI. So yeah, that's basically one free way to uh generate an image via cloud.

**13:06** Â· And by the way, in case you're wondering about how many credits that you have left on your cloud uh Cloudflare account, then you can actually navigate to the AI menu and then workers AI and then right here you you can see how many neurons that you use today. And again, it will reset every day and you have the quota of 10,000 neurons or let's say 10,000 credits every day, which is very very generous. So, I guess that's it. I hope you learned something from this video.

**13:39** Â· And if there is anything that uh you want to ask, you can ask that in the comment down below. And if anything, if you want to see some really cool tutorials like this, then you can subscribe to this channel. And I'll see you on my next video. Have a great day.