---
title: "Python Face Detection from Scratch (OpenCV  + YOLO + Webcam)"
source: "https://www.youtube.com/watch?v=GhAC0xBIepQ"
author:
  - "[[Python Simplified]]"
published: 2026-07-24
created: 2026-09-11
description: "Face detection has been watching you for years. Every time you unlock your phone, walk through an airport, or enter a store with security cameras, a computer is trying to find your face. ðŸ‘€ Today, it'"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=GhAC0xBIepQ)

Face detection has been watching you for years. Every time you unlock your phone, walk through an airport, or enter a store with security cameras, a computer is trying to find your face. ðŸ‘€ Today, it's your turn! Instead of being detected, you'll become the detector ðŸ’ªðŸ’ªðŸ’ª  
  
â­ This video is brought to you by HubSpot! Check out their FREE AI Coding Showdown comparing OpenAI Codex and Claude Code:  
https://clickhubspot.com/06f823  
  
Big thanks to HubSpot for sponsoring this video and providing the guide for free! ðŸ™Œ  
  
In this beginner-friendly tutorial, we'll build a real-time face detection system from scratch using Python, OpenCV, and YOLO. Along the way, you'll learn how to detect many other objects in images and real-time video streams. We'll even combine multiple YOLO AI models to detect different things all at once! ðŸ¤©  
  
ðŸš¨important note for people who are new to this channel, and never watched my videos before ðŸš¨  
\- Windows is better than WSL for this specific workflow.  
\- Native Linux is better than Windows for everything. This workflow included.  
  
Hope it helps! ðŸ«¡  
  
ðŸš¨If you're here for FACE RECOGNITION and not DETECTION - check out this tutorial of mine:  
â­ Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera):  
https://youtu.be/Z2Ojl7m3JXk  
  
ðŸ“š What you'll learn ðŸ“š  
  
\- How OpenCV reads images and video streams from different cameras  
\- Installing and using Ultralytics YOLO  
\- Detecting faces and objects in real time  
\- Setting up and using community-trained YOLO models  
\- Running multiple YOLO models on the same image or video feed  
\- Running your YOLO workflows on GPU for maximum performance  
  
ðŸ› ï¸ Tools Used ðŸ› ï¸  
  
\- Python  
\- OpenCV  
\- Ultralytics YOLO  
\- JupyterLab  
\- Miniconda (Windows)  
\- CUDA (Optional)  
  
â° Timestamps â°  
  
01:15 - Install Miniconda, OpenCV & YOLO on Windows  
03:06 - Load and Display Images with OpenCV  
05:03 - Detect Objects in Images with YOLO  
07:45 - Install a Community YOLO Face Detection Model  
10:43 - Combine Multiple YOLO Models on the Same Image  
12:40 - Read Live Webcam Video with OpenCV  
14:50 - Real-Time Face Detection with YOLO  
17:42 - Run YOLO on GPU with CUDA  
20:08 - Final Face Detection Demo  
20:43 - Thanks for Watching!  
  
ðŸŽ¥ Related Videos From the Tutorial ðŸŽ¥  
  
â­ Full Guide to Anaconda:  
https://youtu.be/MUZtVEDKXsk  
  
â­ CUDA Simply Explained:  
https://youtu.be/r9IqwpMR9TE  
  
ðŸ’» Source Code & Resources ðŸ’»  
  
Check out the pinned comment! ðŸ“Œ  
You'll find everything you need there, including:  
  
\- Demo images used in this tutorial  
\- Miniconda installation  
\- YOLO-Face model  
\- PyTorch CUDA installation  
\- GitHub repository  
  
ðŸ“ Summary ðŸ“  
  
Learn how to build a real-time face detection system in Python from scratch using OpenCV and YOLO. This tutorial covers computer vision, object detection, webcam processing, community-trained YOLO models, CUDA GPU acceleration, and combining multiple AI models into a single workflow.  
  
#Python #OpenCV #YOLO #ComputerVision #AI

## Transcript

**0:00** Â· Face detection is everywhere.

**0:02** Â· It unlocks our phones, replaces our passports, and allows drones to trace us in a crowd full of people.

**0:09** Â· It's kind of scary, I know, but that's exactly why we should join the party and learn how to do it ourselves with Python.

**0:17** Â· So today we're going to use OpenCV with a model named YOLO to detect faces both in images and in live video feeds.

**0:25** Â· It is super accurate and at the same time staring easy to build.

**0:29** Â· Now the best part is, even though we focus on face detection, this workflow can detect almost anything cars, cats, drones, and even specific people that you can teach the model to recognize.

**0:42** Â· So this project gives you a solid foundation for building things like smart security systems, robotics, and interactive games.

**0:50** Â· You don't need a fancy computer to make it work.

**0:53** Â· Even a system with a tiny, tiny brain is good enough.

**0:56** Â· But as you know me, at the end of the video we will also see how to run it on GPU.

**1:01** Â· And finally, this video is brought to you by hotspot.

**1:04** Â· We will talk about them more shortly, so if you're ready, let's roll.

**1:14** Â· Now. First things first, let's make sure we have the right setup for this.

### Install Miniconda, OpenCV & YOLO on Windows

**1:19** Â· You're not going to believe it, but we will actually use windows.

**1:22** Â· It is better optimized for reading a live camera feed and handling OpenCV in general.

**1:28** Â· So we'll go ahead and install Miniconda.

**1:31** Â· It will just click on this windows 64 installation.

**1:35** Â· We will then follow the wizard instructions.

**1:38** Â· And once we are done, we will find it in the start menu as Anaconda Prompt.

**1:44** Â· I have a detailed tutorial about it if you're new to this.

**1:47** Â· Next we will create a new working environment with Conda create dash n.

**1:53** Â· We will call it detection env and we will install Python 3.1 in it.

**2:01** Â· We will then activate it by copying this command.

**2:05** Â· And then we will pip install OpenCV dash Python which is my favorite computer vision library.

**2:13** Â· I use it very often and we will also install Ultra Litex, which is where YOLO our AI model lives.

**2:23** Â· And finally we will install Jupyter, which is the coding interface we will use for this project.

**2:30** Â· And let's give it a quick run.

**2:32** Â· Then we will navigate to a project folder on our file system, where we saved a bunch of demo images.

**2:38** Â· In my case, I called it Face Detection.

**2:41** Â· It's right over here.

**2:43** Â· You can of course download the exact same images as me.

**2:46** Â· All the instructions are in the pinned comment.

**2:48** Â· So then back in our terminal we will navigate to this folder with CD change directory followed by face detection.

**2:57** Â· Then from our project folder we will run our Jupyter notebook with JupyterLab.

### Load and Display Images with OpenCV

**3:06** Â· So in a new notebook, the first thing we'll do is import OpenCV with import cv2.

**3:13** Â· And yes, when we installed it we called it opencv-python.

**3:17** Â· But when we import it, it suddenly cv2 Tada!

**3:22** Â· Then we will load one of our demo images with cv2 read as in image read, to which we will pass one of our demo images in my case demo dot jpg and we will assign it to photo.

**3:40** Â· Now to display it in a new window we will call cv2.im show as in image show.

**3:49** Â· We will call this window my window and we will display our photo inside of it.

**3:56** Â· Now we will pop this window for precisely five seconds with cv2 dot wait key in camel case, to which we will pass 5000 milliseconds.

**4:09** Â· And once these 5000 milliseconds are over okay, we will then cv2 dot destroy all windows.

**4:19** Â· And I'm so sorry to interrupt you guys, but if you enjoyed this video and if you find it helpful, please consider clicking on the like button, the high button, or leaving me a very nice comment or anything that can help with the algorithm.

**4:34** Â· Any help will be highly appreciated.

**4:37** Â· And let's go back to the video.

**4:39** Â· Finally, and this one is optional.

**4:41** Â· If you have a giant monitor like I do, let's make sure the window pops in the section that I'm recording.

**4:47** Â· We will do so right below.

**4:48** Â· Image show with cv2 dot move window, specifically the one we called my window, and we will place it at the x coordinate of 1800 and the y coordinate of 200 pixels.

### Detect Objects in Images with YOLO

**5:06** Â· So when we give this cell a quick run with control enter our image is displayed as expected, and we are officially ready to detect faces in it.

**5:17** Â· Now in this project, we are intentionally writing every line of code because that's the best way to learn.

**5:23** Â· But let's be honest, most of us have an AI coding assistant open in another tab, and once I am done guiding you through this project, it will probably help you take it even further.

**5:34** Â· The only challenge is there are so many coding assistants now that it's hard to tell which one actually fits your workflow.

**5:40** Â· If that's something you've been wondering about, I think you will really enjoy HubSpot Pre Coding Showdown.

**5:46** Â· It compares OpenAI, Codex and Claude code by having both assistants build the same project.

**5:52** Â· But instead of trying to crown one universal winner, this guide compares them side by side on things like speed setup, learning curve, and real world usability.

**6:02** Â· It also gives you a practical framework for deciding when to use each, and if you want to go even further, there are ten copy and paste prompts so you can test both tools yourself.

**6:13** Â· What's really cool here is that this guide is based on Matt Wolf's work.

**6:17** Â· Matt is not only a friend of mine, but he's also one of my favorite people to follow for practical AI news and insights.

**6:24** Â· In fact, I've been a guest on The Next Way, the podcast behind this guy, so this is extra exciting for me now.

**6:30** Â· Personally, my favorite part is the collection of copy and paste prompts.

**6:34** Â· You can just run them yourself instead of looking at benchmarks.

**6:38** Â· The best way to know if a tool is right for you is to actually try it.

**6:41** Â· And these prompts, they make it really quick and easy.

**6:44** Â· So if you want to finally settle the Codex versus Claudia bait, check out how spots AI Coding Showdown.

**6:50** Â· Right now it is completely free and you will find the link in the description down below.

**6:55** Â· A huge thanks to HubSpot for sponsoring this video.

**6:58** Â· And now let's get back to building our face detector.

**7:05** Â· For this, we will need an AI model in our case YOLO.

**7:09** Â· As in you only look once.

**7:12** Â· So let's go ahead and download it with from ultra Litex.

**7:18** Â· We will import YOLO in all caps and then right below we will assign model to YOLO, to which we will pass the name of the specific model version that we would like to download.

**7:32** Â· In our case, yolov8n.pt, as in yolo in the version of eight nano, a very, very small one.

**7:43** Â· And then into this model right below our photo, we will pass our photo photo and we will assign it to result.

### Install a Community YOLO Face Detection Model

**7:56** Â· Now, if we quickly comment out the rest of our code and we only print the result, oh, there you go.

**8:05** Â· If we scroll up, then we'll see the names of the 79 classes that our model detects.

**8:12** Â· We have things like person, cat, bicycle, and so on.

**8:17** Â· What we don't have here is a face, which means that this automatic download is not going to work and we will solve it right away.

**8:25** Â· But nevertheless, if we want to quickly detect who is the person and who is the cat in our photo, then we will delete our print statement.

**8:33** Â· We will uncomment everything else.

**8:35** Â· And then instead of displaying our photo as we did before, we will display the result in the index of zero dot plot, which is a nice shortcut to the processed image.

**8:48** Â· So if we give it a run, then we successfully detect who is the cat and who is the person.

**8:55** Â· Similarly, we can run another image, let's say demo one, where we detect a person, a bicycle, and a bunch of cars.

**9:04** Â· Or let's say demo two, where we detect an entire kitchen.

**9:10** Â· Okay.

**9:10** Â· And if you're curious what all these numbers mean, let's quickly stop on demo four and let's give us a bit more wiggle room.

**9:20** Â· There you go.

**9:21** Â· And we see that YOLO is 85% confident that this is a laptop.

**9:26** Â· It is 76% confident that this is a cup and 79% confident that this is a mouse.

**9:34** Â· Now, when it comes to detecting faces, there is no official version of YOLO that can do that.

**9:39** Â· But there is a great community version that you can find on GitHub.

**9:42** Â· The link is in the print comment and make sure you give it a star if you end up using it.

**9:47** Â· So a huge shout out to Akanametov for sharing it with the world and let's quickly find YOLOv8 face.

**9:55** Â· Okay, let's scroll down and there you go.

**9:57** Â· YOLOv8 Medium face okay, this one is not nano is going to be bigger.

**10:03** Â· We will click it and we will go ahead and save it inside our project folder.

**10:08** Â· And we will also copy the name.

**10:11** Â· Come on.

**10:12** Â· There you go.

**10:14** Â· And then back in our notebook we will create a new variable named Face Model.

**10:20** Â· And we will assign it to YOLO once again, but this time passing it the file name we just copied.

**10:28** Â· So now we have both the regular model and the face model inside our code.

**10:34** Â· If we only want to detect faces, then instead of passing our photo to the model, we will pass it to the face model.

### Combine Multiple YOLO Models on the Same Image

**10:43** Â· And now if we rerun our code, then we only detect a face.

**10:49** Â· However, if we want to detect cat people and faces, we will scroll up and we will assign the result to the model.

**10:59** Â· And down below we will assign the face result to the face model, and we are basically passing the same image to both of these models separately.

**11:13** Â· And then right below we will create a new variable named cat person, assigning it to the processed results that we displayed earlier will just copy the expression and paste it.

**11:27** Â· And then similarly down below we will copy this line of code.

**11:32** Â· But we will plot the face results, which means that we will rename cat person to face.

**11:40** Â· Okay, but how exactly do we combine these two?

**11:44** Â· Well, this is actually the easy part.

**11:46** Â· All we do is we pass image equals cat person inside the plot method of our face results.

**11:54** Â· So instead of using the original photo that we have over here as a base image, we are using the photo where we already detected the cat and the person.

**12:07** Â· And then on top of these existing objects, we also add a square around the face.

**12:14** Â· So technically this last line of code doesn't really return a face, but a cat person face.

**12:23** Â· And that's exactly what we will display inside my window.

**12:28** Â· So now when we rerun this code, bam!

**12:32** Â· We have the face, the cat and the person, and we have both models working on the same image.

### Read Live Webcam Video with OpenCV

**12:40** Â· Okay, but how do we translate this code from images to video?

**12:44** Â· Well, first let's load the video feed from our camera.

**12:48** Â· For this, in a brand new cell, we will create a video capture object which cv2 dot video capture in upper camel case.

**12:58** Â· And in most cases your integrated camera will be at index zero, as in the camera that lives inside your laptop.

**13:07** Â· In my case, because I'm using my DJI pocket Osmo as a webcam.

**13:12** Â· I'm going to go for index two.

**13:15** Â· Just play with these numbers until you find the right one.

**13:17** Â· Okay.

**13:18** Â· Then we usually assign it to cap as in - capture. Next.

**13:24** Â· To start our live video feed, we will need a while loop that will keep looping until we press the X key on the keyboard, or any kind of key you'd like.

**13:35** Â· So while cv2 wait key is not equal to ordinal x, then we will display our live video feed continuously.

**13:48** Â· Also, we will pass a millisecond into our weight key, meaning each video frame will be displayed for one millisecond before moving on to the next one.

**13:59** Â· So the bigger this number, the longer each frame will be displayed and the slower the video will be.

**14:06** Â· Ultimately.

**14:07** Â· Next we will read our video capture with capped read, and this expression unpacks into two values.

**14:16** Â· The first one we don't really care about, so we will store it as an underscore.

**14:21** Â· The second one, this is the video frame that we will display which is very important.

**14:26** Â· So we'll store it as frame.

**14:29** Â· Ha. We're basically the frame is a static image and many, many frames displayed one after the other.

**14:37** Â· They make up our video feed. Great.

**14:40** Â· So now let's display everything in the same way that we displayed our images.

**14:44** Â· So in our cell above we will copy everything starting from show down to the very bottom.

### Real-Time Face Detection with YOLO

**14:51** Â· And we will paste it in our new cell where Im show and move window.

**14:57** Â· Stay inside the loop and then weight key and destroy.

**15:01** Â· All windows will be outside of it.

**15:04** Â· And also, as you may guess, instead of the cat person face, we will display each frame one at a time.

**15:11** Â· And finally, right before we destroy all the windows, we will close our connection with the camera with kept release.

**15:19** Â· So when we run this cell, then we officially display the live feed from my camera.

**15:27** Â· Hi. Hello.

**15:30** Â· And. Yeah.

**15:31** Â· And once we hit X, then everything collapses.

**15:35** Â· Beautiful.

**15:37** Â· Now, to detect faces and objects in our live video feed, we will copy both models from the previous cell.

**15:44** Â· There you go.

**15:44** Â· And we will paste them right above our loop.

**15:48** Â· Also, we will copy the results along with their combinations and we will paste them right below our capture.

**15:57** Â· Read okay, fixing the indentation.

**15:59** Â· And then instead of processing our photo, we will process our frame and it will do so both for the regular model and for the face model.

**16:10** Â· So then at the very end inside our image show, we will not display the frame like we displayed at earlier, but we will display the cat person face processed feed.

**16:22** Â· Okay, so now when we run this cell okay, we see both the face and the person.

**16:28** Â· We also see a font, but we also see a lot of print statements, a lot of unnecessary things happening in the background.

**16:36** Â· Okay, so let's get rid of them.

**16:37** Â· And the way to do so is to pass into each of our models and argument of verbose and set it to false.

**16:46** Â· Okay.

**16:46** Â· We will do so both for the model and the face model.

**16:50** Â· And now when we rerun everything okay, we no longer get the print statements, but everything runs super, super slowly.

**16:59** Â· And it kind of makes sense because we are running a very heavy workflow with two large models.

**17:06** Â· One of them is a medium okay, not a nano.

**17:09** Â· We are running both of them on CPU, so one way to make it run smoother is to just collapse everything and only pick one of our models.

**17:18** Â· Okay, disregarding the second one, let's say we don't want this face model.

**17:23** Â· Let's get rid of it and let's only display the cat person and not the cat person face.

**17:29** Â· So now when we rerun this cell, everything will run much smoother.

**17:34** Â· I can bring up all kinds of objects, but it will not detect my face.

**17:38** Â· Or we can just run the whole thing on GPU.

### Run YOLO on GPU with CUDA

**17:42** Â· Okay, both of the models and it will run smoothly and nicely and properly.

**17:48** Â· So if you happen to have a Cuda based GPU, let's collapse our notebook in the terminal with Ctrl C, and let's check our version of Cuda with Nvidia SMI.

**18:00** Â· Okay, we will scroll up.

**18:02** Â· We will find it right over here.

**18:05** Â· Then based on that, we will assemble the right installation command in the PyTorch documentation.

**18:11** Â· Check out the pinned comment for the link.

**18:13** Â· So we will go for stable windows pip Python and in my case Cuda 13.

**18:20** Â· We will then copy. Okay.

**18:23** Â· And we will paste the command that was generated inside our terminal okay.

**18:29** Â· We'll do so in a new line.

**18:31** Â· But don't you dare running it okay let's engineer it first because windows is always problematic with GPU stuff.

**18:40** Â· This is why I usually use WSL.

**18:42** Â· But today we don't really have a choice, so we need to adjust things.

**18:46** Â· Specifically, we will delete this index URL section okay.

**18:51** Â· And then we will change install to uninstall okay.

**18:56** Â· And we will change pip three to pip.

**18:59** Â· And then we will go ahead and give it a run okay.

**19:03** Â· And only after we will paste the actual command which is copied.

**19:07** Â· And again we will pip it instead of pip three it okay.

**19:13** Â· And now when we run it PyTorch is officially installed on windows and we can open our notebook once again with JupyterLab.

**19:23** Â· We will of course open our untitled notebook from earlier.

**19:26** Â· Okay, we will copy the import commands from the first cell, pasting them in the second cell, because that's the only cell we'll be running right now.

**19:36** Â· We no longer need the first one.

**19:37** Â· And make sure that everything that we commented before is now on commented.

**19:41** Â· So cat person, face and face results.

**19:44** Â· Okay, and now to send our workflow into our GPU, the only thing we need to add is for both our models.

**19:51** Â· We will wrap them with a two method, passing them a string of Cuda.

**19:58** Â· Okay, and we will do so both for the model and for the face model.

**20:02** Â· And now when we rerun our program for the very last time okay.

### Final Face Detection Demo

**20:08** Â· Now everything will run super smoothly.

**20:11** Â· There you go.

**20:12** Â· Here is my cell phone.

**20:14** Â· Here's a cup of wine.

**20:16** Â· Apparently it's coffee, I swear.

**20:20** Â· And okay, I just happen to have a cat handy.

**20:25** Â· I brought him just in case, but once in a while he's recognized as a dog.

**20:29** Â· Maybe if you show the camera your beautiful face.

**20:32** Â· There you go.

**20:34** Â· He doesn't detect you at all.

**20:36** Â· And sometimes it detects a face.

**20:39** Â· Oh. You show cute. Okay.

**20:41** Â· Thank you so much for modeling, Neel.

**20:42** Â· And thank you so much for watching.

### Thanks for Watching!

**20:45** Â· If you found this video helpful, please share it with the world and don't forget to leave it a huge thumbs up and all kinds of comments.

**20:52** Â· Now, if you'd like to see more videos of this kind, you can always subscribe to my channel and turn on the notification bell.

**20:59** Â· I'll see you soon in an awesome tutorial.

**21:02** Â· So in the meantime. Bye bye.