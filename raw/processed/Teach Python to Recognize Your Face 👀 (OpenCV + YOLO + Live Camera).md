---
title: "Teach Python to Recognize Your Face ðŸ‘€ (OpenCV + YOLO + Live Camera)"
source: "https://www.youtube.com/watch?v=Z2Ojl7m3JXk&t=1683s"
author:
  - "[[Python Simplified]]"
published: 2026-08-26
created: 2026-09-11
description: "Detecting a face is one thing. Knowing WHO that face belongs to is a whole different level of skill! ðŸ’ª In this step-by-step Python tutorial, weâ€™ll teach our computer to recognize specific people in"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Z2Ojl7m3JXk)

Detecting a face is one thing. Knowing WHO that face belongs to is a whole different level of skill! ðŸ’ª  
In this step-by-step Python tutorial, weâ€™ll teach our computer to recognize specific people in a live camera feed using our own photos, Python, OpenCV and YOLO ðŸðŸ’»  
  
â­ This video is brought to you by HubSpot! Check out their FREE AI Agents Cheat Sheet comparing different AI agent tools:  
https://clickhubspot.com/86c13b  
  
Big thanks to HubSpot for sponsoring this video and providing the guide for free! ðŸ™Œ  
  
The best part is everything runs locally â€” no cloud face-recognition service, no paid API, and all your training photos stay on your computer.  
  
All you need is roughly 20 photos, a webcam and some basic Python skills. By the end of this video, you will have the foundation of your own security system, labeling familiar faces with their names in real-time, and unfamiliar faces with "Unknown".  
  
If you watched my recent Face Detection tutorial - you already have a solid background. If you haven't - don't worry! I'll go over everything here as well (previous tutorial link is below in case you'd like to dive deeper ðŸ‘‡).  
  
ðŸ“š What you'll learn ðŸ“š  
  
\- Prepare face-recognition training photos  
\- Detect and crop faces with YOLO  
\- Process faces with OpenCV (grayscale + resize)  
\- Train an OpenCV LBPH face recognition model on your own photos  
\- Save and load the trained model  
\- Recognize multiple faces in real time with a webcam  
\- Map predicted labels to real names  
\- Use recognition distance to identify unfamiliar faces as Unknown  
  
ðŸ› ï¸ Tools Used ðŸ› ï¸  
  
\- Python  
\- OpenCV  
\- Ultralytics YOLO  
\- YOLOv8 Face  
\- OpenCV LBPH Face Recognizer  
\- NumPy  
\- Jupyter Lab  
\- CUDA (Optional)  
  
ðŸ“¹ Tutorials Mentioned In This Video ðŸ“¹  
  
â­ Detect Faces with Python (OpenCV + YOLO ):  
https://youtu.be/GhAC0xBIepQ  
  
â­ Simple Machine Learning with Scikit-Learn:  
https://youtu.be/-IvNzmrcyUM  
  
ðŸ’» Source Code ðŸ’»  
  
Check out the full notebook on GitHub:  
https://github.com/MariyaSha/FaceRecognition  
  
Check out the pinned comment for the full list of resources & installation instructions! ðŸ“Œ  
The model download link and full environment setup is there!!  
  
â¬‡ï¸ IMPORTS â¬‡ï¸  
  
import os  
import cv2  
import numpy as np  
from ultralytics import YOLO  
from IPython.display import display  
from PIL import Image  
  
ðŸ‘¾ HORRIFIC IMAGE DISPLAY COMMAND ðŸ‘¾  
Image.fromarray(photo\[:, :, ::-1\])  
  
ðŸ˜€ LBPH FACE RECOGNIZER COMMAND ðŸ˜€  
face\_recognizer = cv2.face.LBPHFaceRecognizer\_create()  
  
âœï¸ PUT TEXT PLACEHOLDERS COMMAND âœï¸  
cv2.putText(image, text, (x, y), font, font\_size, color, thickness)  
  
ðŸ–¥ï¸ IMAGE FACE DETECTION CODE @ MINUTE 05:25ðŸ–¥ï¸  
\`\`\`  
folder = "faces/Mariya"  
files = os.listdir(folder)  
  
face\_model = YOLO("yolov8m-face.pt")  
  
for file in files:  
photo = cv2.imread(folder + "/" + file)  
  
face\_result = face\_model(photo, verbose=False)  
processed\_image = face\_result\[0\].plot()  
  
Image.fromarray(photo\[:, :, ::-1\])  
\`\`\`  
  
ðŸ–¥ï¸ VIDEO FACE DETECTION CODE @ MINUTE 20:18ðŸ–¥ï¸  
\`\`\`  
cap = cv2.VideoCapture(2)  
  
face\_model = YOLO("yolov8m-face.pt")  
  
while cv2.waitKey(1) != ord("x"):  
\_, frame = cap.read()  
  
face\_result = face\_model(frame, verbose=False)  
processed\_feed = face\_result\[0\].plot()  
  
cv2.imshow("my window", processed\_feed)  
  
cv2.waitKey(5000)  
cap.release()  
\`\`\`  
  
â° Timestamps â°  
  
00:00 - Face Detection vs Face Recognition  
01:11 - Prepare Face Recognition Training Photos  
03:22 - Set Up Jupyter Notebook  
05:29 - YOLO Face Detection & Cropping  
12:18 - OpenCV LBPH Face Recognition  
12:54 - Prepare Faces for Recognition  
14:53 - Train a Face Recognition Model  
16:30 - Save the Trained Face Recognition Model  
17:33 - Train Face Recognition on Multiple People  
20:19 - Real-Time Face Recognition with Webcam  
23:45 - Predict Faces in Real Time  
27:31 - Recognize Multiple Faces  
28:23 - Convert Labels Into Names  
28:47 - Detect Unknown Faces  
31:43 - Final Real-Time Face Recognition Demo  
32:05 - Thanks for Watching!  
  
ðŸ”Ž Topics Covered ðŸ”Ž  
  
Python face recognition  
OpenCV face recognition  
YOLO face detection  
LBPH face recognition  
Real-time face recognition  
Webcam face recognition  
Computer vision with Python  
Face recognition security system  
  
#Python #OpenCV #YOLO #FaceRecognition #ComputerVision

## Transcript

### Face Detection vs Face Recognition

**0:00** Â· It's one thing to detect a face, but recognizing Mariya, Jason and all your favorite people from just a few pictures.

**0:10** Â· That's a whole new level of skill, and that's exactly what we'll do today.

**0:14** Â· We will teach our computer to recognize specific faces in live camera feeds, using your own photos, your own code, and without sending anything to the cloud or spending any money.

**0:28** Â· All you need is OpenCV, YOLO and about 20 pictures and boom!

**0:33** Â· You got yourself a smart security system.

**0:36** Â· So if you watched my recent face detection video then you already know the basics.

**0:41** Â· If you haven't.

**0:42** Â· Don't worry, I'll explain everything here as well.

**0:45** Â· So homework is canceled by the end of this video.

**0:48** Â· Your camera will know exactly who you're hanging out with, which is a little creepy, so we will make sure we do it safely.

**0:57** Â· Finally, this video is brought to you by HubSpot.

**1:00** Â· We will talk about them more shortly.

**1:01** Â· So if you're ready, let's roll.

### Prepare Face Recognition Training Photos

**1:11** Â· Let's start with the photos that our system will learn.

**1:13** Â· You can of course download my photos from GitHub, but for this project it is better to use your own photos, photos of yourself and anyone who can physically be with you.

**1:23** Â· When you test this system.

**1:24** Â· So yeah, you can play one of my videos on your phone and show it to the camera, but it's much better to have somebody with you in the same room.

**1:32** Â· And it's a pretty cool project, so I'm sure they'll enjoy it.

**1:35** Â· Also very important to mention, since everything, including the models, lives on your computer, you're not sharing these photos with anyone.

**1:44** Â· You're not uploading them to some cloud provider or some, you know, third party app. Great.

**1:49** Â· So at the root of our project, we have a folder named faces.

**1:53** Â· And inside it every person gets their own folder where we dump a whole bunch of pictures I have mine.

**2:01** Â· There you go.

**2:02** Â· And I have Mario's who will join me when it's time to do the testing.

**2:06** Â· And the idea is the more folders we add over here, then the more faces our system will recognize.

**2:13** Â· Now we do have some rules.

**2:15** Â· Each picture can only have one face, and it must belong to the right person.

**2:21** Â· To make sure the photos reflect what the camera is going to see.

**2:26** Â· So if the camera is pointing at my green screen setup with controlled lighting, then that's the type of photos we provide.

**2:33** Â· If it's a security camera that moves from side to side, running at different times of day under different weather conditions, then you will need a much bigger gallery with a lot more variety.

**2:43** Â· And three we don't really care about the size of the face or how much of the body appears in the photo, because the first thing we'll do in our code is find the face and crop it automatically.

**2:54** Â· So when I say just dump a bunch of photos there, I actually mean it. And beautiful!

**2:59** Â· Once our folders are ready, we will move on with training and we will do so with the detection environment that we've set up in the previous video running on GPU.

**3:09** Â· In my case, I left all the instructions in the comments so you can set it up exactly as me.

**3:15** Â· If you don't have a CUDA-compatible GPU, you can still set it up.

**3:19** Â· It will still work.

**3:19** Â· It's just going to be a little bit slower.

### Set Up Jupyter Notebook

**3:22** Â· So let's create a new Jupyter notebook at the root of our project, right?

**3:26** Â· Besides our faces folder.

**3:28** Â· And again, check out the pinned comment if you don't know how.

**3:31** Â· This is very easy.

**3:33** Â· I've also included all the imports in the description.

**3:35** Â· You can just copy them and paste them like so.

**3:38** Â· On my end.

**3:39** Â· I will also run them as a separate cell just so I don't have to worry about it later.

**3:44** Â· Now, to keep things simple, we are going to start with training on only one person.

**3:49** Â· Once we get that to work, we will then extend it to multiple people.

**3:53** Â· So first we need the folder where our photos live.

**3:57** Â· In my case, folder equals faces/Mariya and then we will list all the files in this folder with os.listdir, to which we will pass our folder.

**4:12** Â· And this will return all our images back.

**4:17** Â· Great.

**4:17** Â· So now let's assign it to files.

**4:20** Â· And then let's load each of those files as an image with OpenCV, which is the computer vision library we are using in this project.

**4:30** Â· So down below for file in files we will load them with cv2.imread as in image read, passing it the path to each file which is folder slash file and this one we can assign to photo.

**4:52** Â· How do we know if it worked?

**4:54** Â· Well, we will just copy this absolutely horrific line of code from the description.

**5:00** Â· Okay, I apologize in advance.

**5:02** Â· We will paste it outside of the for loop and if everything worked properly then it will display the very last image we've loaded.

**5:12** Â· This one should match the last image you have in your gallery.

**5:15** Â· So if we open it.

**5:16** Â· Yep, have the exact same stupid face.

**5:19** Â· Perfect.

**5:20** Â· So now that all our images are loaded, let's find the face in them and let's crop it.

**5:25** Â· Since we already know how to do it, I will quickly explain it to the new folks.

### YOLO Face Detection & Cropping

**5:29** Â· We simply download a model named YOLOv8 Medium Face.

**5:35** Â· We do it from GitHub.

**5:37** Â· The link is in the pinned comment.

**5:38** Â· All you do is scroll down and you click it.

**5:42** Â· You then save this model right next to our notebook right over here and we load it into our code.

**5:50** Â· Then we pass our photos into this model one at a time.

**5:55** Â· It automatically finds faces in them and it returns their exact location along with some other stuff.

**6:01** Â· Now, so far we only cared about processing the original image or drawing a blue box around faces and then displaying the results.

**6:10** Â· So if we now quickly display this processed image with our horrific command from earlier, we then see a blue box right on top of the original photo that says face.

**6:24** Â· That's exactly what we did in the previous video for this workflow.

**6:28** Â· We don't really need the full image.

**6:30** Â· We only need whatever lives inside this blue box.

**6:33** Â· Okay, so instead of plotting the process image, let's quickly see what else we can do.

**6:39** Â· So right above, we will just comment out our last line of code and instead of it okay, we will quickly print the face result in the index of zero just to see what else lives inside.

**6:55** Â· And okay, if we scroll up, the first thing we see is exactly what we're looking for boxes.

**7:02** Â· So let's add dot boxes to the very end of our expression to take another dive, okay.

**7:09** Â· And see what else is there.

**7:11** Â· And now we get a whole bunch of settings back.

**7:14** Â· And it's kind of hard to tell what they actually mean.

**7:17** Â· The only setting I'm comfortable with is this xyxy, because it seems to me like a bunch of coordinates.

**7:24** Â· So let's quickly add it to the end of our expression right after boxes, and let's give it another print.

**7:31** Â· And okay, we get four numbers back.

**7:34** Â· And these two they must be x1 and x2, the left and the right.

**7:39** Â· And these two must be y1 and y2, which is the top and bottom.

**7:45** Â· And from these four points we actually draw our box.

**7:49** Â· Great.

**7:49** Â· So this means we can unpack this expression okay into left top right and bottom.

**7:59** Â· Hopefully I got the order right okay.

**8:02** Â· This is x1 x2 y1 y2. Perfect.

**8:06** Â· But we actually need to be careful here because as you can see we're not getting one set of coordinates back.

**8:13** Â· This is a nested structure.

**8:15** Â· And that's because there could be a few faces in each photo.

**8:18** Â· So even though we know for sure that our photos only have one face, our code is not aware of it.

**8:25** Â· It keeps looking for multiple faces.

**8:27** Â· So to ignore it, we will just focus on the first and only item of this structure, and only now our expression unpacks properly.

**8:38** Â· Okay, so let's give it a quick indent because it happens inside the for loop and outside of it.

**8:43** Â· And then once we have these lovely coordinates we can then slice our photo accordingly.

**8:48** Â· So we will type photo in the index of top to bottom left to right.

**8:55** Â· And then we will assign this new expression to face because that's exactly what we get when we slice our photo to this box.

**9:03** Â· But there's actually one more thing to be careful here, because even if we focus on the first item of the list, this item stores fractions, okay.

**9:13** Â· It doesn't store whole numbers.

**9:15** Â· So when we are trying to slice a photo that's made out of pixels, there is no such thing as 233.6 pixels.

**9:24** Â· There's only 233 and 234.

**9:29** Â· There's nothing in between.

**9:30** Â· So before we are even attempting to slice, we need to convert these floating point numbers into integers.

**9:37** Â· For this, we will add the int method at the very end of our long coordinates expression.

**9:44** Â· Hopefully my head doesn't block it.

**9:46** Â· And now if everything worked properly okay, when we try to display our face in our horrific command then it should work.

**9:55** Â· Okay. Fingers crossed.

**9:56** Â· Let's give it a quick run and Bam!

**10:00** Â· We see my stupid face return back to us.

**10:04** Â· But there's one more thing left to do.

**10:06** Â· And it's storing these faces because right now we are catching them.

**10:09** Â· But we don't do anything with those faces.

**10:12** Â· They just go nowhere.

**10:13** Â· So then, right above our for loop, we will create an empty list called faces.

**10:20** Â· And then at the bottom of our for loop.

**10:24** Â· Oh, what did I do?

**10:26** Â· I accidentally ran this cell. Sorry, guys.

**10:29** Â· Okay, at the bottom of our for loop, we will append each of our faces into this empty list with faces dot append, to which we will pass each individual face.

**10:41** Â· And now to make sure it worked instead of the very last phase, let's go ahead and display faces in the index of zero, which is the very first face.

**10:52** Â· Let's give it another run.

**10:53** Â· And okay, we no longer get the stupid face, but a much more refined one.

**10:58** Â· Yay! We can officially move on now.

**11:01** Â· So far our AI model only has one job find the face.

**11:06** Â· But the more complicated our project gets and the more tasks we give it, the less we actually want to hold its hand at every step of the process.

**11:17** Â· Just figure it out and call me when you're done.

**11:20** Â· That's exactly what AI agents are here for.

**11:22** Â· And if you've been wondering which ones are actually worth trying, I think you will really enjoy HubSpot's free AI Agents Cheat Sheet.

**11:30** Â· It compares seven different AI agent tools, shows you what each of them is actually good for, how easy it is to set them up, what it costs, and if it fits the kind of work you want to automate.

**11:43** Â· And each tool comes with copy and paste prompts for real workflows, so you can just grab one and go.

**11:49** Â· There's also a very important tip here that I want to highlight.

**11:53** Â· Start with the simplest version of your task and get one thing working well before adding complexity, which is exactly what we're doing in this tutorial, so check out the full guide using the link in the description.

**12:05** Â· It is completely free.

**12:07** Â· Thanks so much to HubSpot for sponsoring this video, and let's teach our model who these faces actually belong to.

### OpenCV LBPH Face Recognition

**12:18** Â· For this we will load a face recognizer that is already built into OpenCV.

**12:23** Â· Just copy this command.

**12:26** Â· Oh from the description.

**12:28** Â· Otherwise it's a lot of typing.

**12:30** Â· It is called the Local Binary Patterns Histogram face recognizer and we will feed our cropped faces into it.

**12:39** Â· You will need to pip install opencv-contrib-python.

**12:43** Â· So go ahead and collapse your notebook, install it from the terminal and only then go back.

**12:48** Â· If you don't run it then you will get an error.

**12:51** Â· Now for this type of face recognizer, we need our images in grayscale and matching in size.

### Prepare Faces for Recognition

**12:58** Â· So right before we append them into our list, we will go ahead and call cv2.cvtColor, passing it our colorful face and converting it with cv2.COLOR\_BGR2GRAY.

**13:21** Â· We can then reassign it back to face, overwriting the original photo with a great version.

**13:28** Â· Additionally, right below we will see cv2.resize, passing it our gray face and then resizing it into a size of 200 pixels by 200 pixels.

**13:45** Â· And then once again we will assign it back to face.

**13:49** Â· We can now give it another print below.

**13:52** Â· Just make sure you remove this horrific part okay from our image display command, because now we don't need to worry about color dimensions.

**14:01** Â· We only have one because the image is great.

**14:03** Â· Okay, so now when we give this cell a run beautiful.

**14:08** Â· That's exactly what our recognizer expects to us.

**14:12** Â· It looks a bit distorted.

**14:13** Â· It's kind of wide okay.

**14:16** Â· But for computers, this is perfect.

**14:19** Â· And I'm so sorry to interrupt you guys, but if you enjoy this video and if you find it helpful, please consider clicking on the like button, the Hype button, or leaving me a very nice comment.

**14:29** Â· Anything that will help the algorithm will be highly appreciated.

**14:33** Â· And let's go back to the video.

**14:36** Â· So now that our faces are processed and then appended in a list of faces, we can now feed them into our face recognizer.

**14:45** Â· So let's quickly copy the name of our model.

**14:48** Â· And then right below, right after our for loop ends, we will go ahead and call face\_recognizer.train and we will of course pass it our list of faces.

### Train a Face Recognition Model

**15:01** Â· But that's not all.

**15:03** Â· We can't just send our models a bunch of faces without telling it who these faces belong to.

**15:09** Â· So right above our empty list, you know, at least initially a faces, we will need an empty list of labels.

**15:17** Â· And these labels, they will tell our model that this face belongs to Mariya and that face belongs to Mario.

**15:25** Â· So both of these lists, they have to be at a perfect, orderly sequence now to make it happen.

**15:32** Â· In the very end of our for loop, right after we append each of our faces, we will also append each of our labels.

**15:39** Â· We will do so with labels dot append, and we will pass it the name of the person that this face belongs to.

**15:49** Â· But here's the thing.

**15:50** Â· We can't just use an actual name.

**15:53** Â· Our model doesn't know any letters, it only knows numbers.

**15:57** Â· So instead of saying that all those photos belong to Mariya, they will say that all those photos belong to class zero.

**16:05** Â· Okay, that way, class zero always represents Mariya.

**16:10** Â· And then later on when we are dealing with multiple people, then class one will always represent Mario, class two will always represent neo, and so on and so on.

**16:20** Â· Great.

**16:20** Â· So then in our training command, right next to our faces, we will also include our labels.

**16:27** Â· And then finally, once the training is complete, we will just save the results with face\_recognizer.write.

### Save the Trained Face Recognition Model

**16:35** Â· Right, okay.

**16:36** Â· And we will call our special result file face\_recognizer.yml.

**16:43** Â· Great.

**16:44** Â· So now let's give this cell a quick run and we get an error.

**16:49** Â· And that's because our labels are not a NumPy array, okay.

**16:53** Â· Well that's an easy fix.

**16:55** Â· So right at the top of our code let's do it.

**16:58** Â· In the first cell we will import numpy as np.

**17:02** Â· And after we run it then back in our train function, we will wrap our labels in a NumPy array.

**17:12** Â· Like so.

**17:13** Â· And now when we rerun this cell, everything should work like a charm.

**17:18** Â· Let's open our file system and boom!

**17:21** Â· Our training is officially complete and we have a new face recognizer YAML in our file system. Yay!

**17:30** Â· Okay, so how do we take this code and get it to recognize multiple people and not just Mariya?

### Train Face Recognition on Multiple People

**17:36** Â· I slightly rearranged the variables so I can explain it better, but it's the exact same code from earlier.

**17:42** Â· So right now our code only knows about one folder, and since all the photos in this folder belong to Mariya, we gave all of them the exact same label of zero.

**17:55** Â· But now we want to add Mario and set his label to one.

**17:59** Â· So let's try to hit two birds with one stone.

**18:02** Â· Let's create a dictionary of folders where we will set the key of zero to store faces/Mariya and the key of one to store faces slash Mario.

**18:19** Â· So now we know where to get those photos and who they belong to.

**18:23** Â· And then right below we will load all these photos with for label folder in folders.items().

**18:36** Â· That's how we iterate over a dictionary the first time with label zero and folder faces/Mariya, and the second time with label one and the folder of faces slash Mario.

**18:49** Â· Okay, so that way inside this new loop, we can use the exact same commands to find all the files as well as anything that comes after without any changes.

**19:01** Â· So the only thing we do is indent our files and our old for loop.

**19:08** Â· Okay, with tab.

**19:11** Â· And now we are nesting it inside this new loop that we iterate over a dictionary.

**19:16** Â· We still use the same variables okay files and folder, even though they represent different people one at a time.

**19:26** Â· So then finally, okay, at the very end of the loop, instead of appending zero time and time again, zero only represents Mariya, we will now append the actual label that we pull directly from our dictionary.

**19:42** Â· Okay, either 0 or 1 depending on the actual person okay.

**19:47** Â· And that's it.

**19:48** Â· If we now we run this code okay.

**19:51** Â· Let's do it.

**19:53** Â· Our model will now recognize two faces and not just one.

**19:57** Â· If we pull out our file system and we wait until our face recognizer refreshes.

**20:04** Â· Okay, there we go.

**20:05** Â· Four seconds ago, we saved a fresh version with two classes and not just one.

**20:10** Â· Now we can of course, automate it even further, especially if we're dealing with tens of people.

**20:15** Â· Okay, so check out my GitHub if you want to know how.

### Real-Time Face Recognition with Webcam

**20:19** Â· Okay, so how do we take what our face recognizer learned.

**20:23** Â· And we plug it into a camera feed.

**20:25** Â· Now we already know how to detect a face in a video.

**20:29** Â· We did it together in the previous tutorial.

**20:32** Â· We simply capture the feed from our sorry, the feed from our camera.

**20:37** Â· It's usually our webcam or some kind of a USB camera.

**20:40** Â· In my case, I am grabbing the footage from my DJI Osmo Pocket that lives at index two two on my computer.

**20:49** Â· On your computer, it could live at index 0 or 1 or some other number.

**20:54** Â· So just play with these numbers and you will find it, you know, eventually.

**20:58** Â· Then we open a video stream that keeps playing until we press the X key on our keyboard.

**21:05** Â· And then we take each frame, you know, from the video stream, and we then feed it into our face model.

**21:14** Â· Okay.

**21:14** Â· So we pull it from the video and we pass it through the model getting processed feed in return.

**21:22** Â· Okay.

**21:22** Â· And then we display this process stream this processed feed with a blue box, you know, around a face.

**21:30** Â· So if we give this code a click run.

**21:36** Â· This is exactly where our previous video ended.

**21:40** Â· Face successfully detected.

**21:42** Â· But this is just a face.

**21:43** Â· Now to recognize who this face belongs to.

**21:46** Â· As you may guess, we will need our OpenCV face recognizer once again.

**21:51** Â· So let's quickly collapse it and let's copy our face recognizer from the previous cell, okay?

**22:00** Â· And we will initialize it right below our face model.

**22:03** Â· But this is not the model we trained.

**22:06** Â· If we want to load the version that is already familiar with Mariya and Mario, we will simply type okay, face\_recognizer.read and we will pass it the name of the file that we just saved with our results.

**22:21** Â· Okay, face\_recognizer.yml.

**22:25** Â· And this is the model we trained.

**22:28** Â· So what exactly are we supposed to do with this model.

**22:32** Â· Well similar to what we've done for we will take the coordinates of this face box from earlier.

**22:38** Â· We will crop them, gray them out and resize them.

**22:41** Â· But instead of using it for training, we will use them for prediction, meaning the model will take everything it learned and it will guess who this new anonymous face belongs to.

**22:53** Â· So we are no longer telling the model that this face belongs to Mariya.

**22:57** Â· We now get the model to tell it to us.

**23:00** Â· Okay, for this, we'll go ahead and copy all our transformation commands from earlier.

**23:06** Â· Starting from the coordinates and ending with the resizing.

**23:09** Â· We will paste them right before we show our feed.

**23:15** Â· Okay. Fixing the indentation.

**23:17** Â· And we will rename photo to frame because right now we are no longer dealing with a folder of photos.

**23:24** Â· This is no longer our training stage, but we are dealing with a real stream coming from the camera through this very complex pipeline.

**23:32** Â· And then we are cropping any kind of face from the stream.

**23:36** Â· So after we detect the face box, after we crop it, after we we color it, and after we resize it, we can then officially call face\_recognizer.predict passing it our face.

### Predict Faces in Real Time

**23:54** Â· Okay.

**23:55** Â· Basically asking the model who is this?

**23:59** Â· Now the cool part is that the model doesn't just tell us who it is.

**24:03** Â· It also tells us how closely this face matches the person.

**24:07** Â· So when we unpack our prediction okay, it actually gives us back the predicted label.

**24:12** Â· So let's call it pred label okay as well as the distance.

**24:19** Â· So if the distance is small then the face looks exactly like the person.

**24:24** Â· If the distance is big then the person is not doing too well.

**24:30** Â· He has seen better days.

**24:31** Â· Okay, but how do we actually know if it worked?

**24:36** Â· Well, we can just put this predicted label on top of our camera feed, right?

**24:41** Â· So at the bottom of our for loop we will go ahead and add some text with cv2.putText.

**24:49** Â· And then we will fill in all these placeholders with actual values.

**24:53** Â· Let me just quickly separate them into a few lines because my head is going to, you know, cover a lot of them.

**25:01** Â· Now the image we are putting the text on is of course, our processed feed, the one that we display later.

**25:08** Â· The text we want to put on this feed is our pred label.

**25:12** Â· Okay. The one we got from the model.

**25:14** Â· The best guess that the model made and we will wrap it in a string.

**25:20** Â· Okay.

**25:20** Â· Because as I mentioned earlier, the model is dealing with numbers, not letters.

**25:26** Â· We will then place it on the left side of our blue box.

**25:29** Â· Okay, so left and we will also place it at the bottom of our blue box actually slightly below it.

**25:36** Â· So bottom plus 20 pixels okay.

**25:40** Â· And then we will use font number zero.

**25:43** Â· We will use the font size of 0.8 the color of white.

**25:48** Â· So 255 by 255 by 255 okay.

**25:52** Â· And finally the thickness of two.

**25:54** Â· And then hopefully when we give this cell a quick run okay.

**26:00** Â· No hope is gone.

**26:01** Â· Okay.

**26:01** Â· We get an error something that has to do with the origin.

**26:05** Â· Now if you're a graph enthusiast, which I am sure many of you are okay, you've probably heard of the origin of the coordinate system, point (0,0).

**26:16** Â· Okay.

**26:17** Â· So this label probably tells us that it has to do with coordinates.

**26:22** Â· Okay.

**26:22** Â· The left and bottom coordinates.

**26:24** Â· That already gave us a hard time before. Okay.

**26:27** Â· Since we previously converted them to integer.

**26:30** Â· Let's try to do it again okay.

**26:32** Â· Integer and integer okay.

**26:35** Â· And hopefully this solves it.

**26:37** Â· Let's give it another run and boom.

**26:41** Â· We now see label zero right under my chin.

**26:45** Â· And we already know it means Maria.

**26:47** Â· But we are not done yet.

**26:49** Â· Because if now I ask Mario to join me.

**26:52** Â· Okay Mario, we are not done yet because only one of our faces will go through the recognition process.

**26:59** Â· Okay, I have index.

**27:01** Â· Oh, it kind of works because if I hide my face, he's being recognized.

**27:06** Â· If I don't, I'm being recognized.

**27:07** Â· Okay, so it's one only one person at a time.

**27:10** Â· It happens because that's exactly what we wanted earlier when we focused on the only box of xyxy.

**27:18** Â· Okay.

**27:19** Â· Back at the time, we specifically told the model to ignore multiple faces and only focus on one.

**27:26** Â· It made a lot of sense when all the I was involved, but now there's a few of us, so let's fix it.

### Recognize Multiple Faces

**27:31** Â· So right above our coordinates, we will go ahead and fetch multiple face boxes with for box in face\_result\[0\].boxes.xyxy.

**27:43** Â· Okay, we will indent everything below it.

**27:48** Â· Okay, up until our weight key which we will not touch.

**27:51** Â· Okay.

**27:51** Â· And then we will replace face\_result\[0\].boxes.xyxy in the index of zero with our new iteration variable of box.

**28:02** Â· Okay.

**28:03** Â· And now if we run our code then each and every face box is sent through the face recognizer separately.

**28:10** Â· You can tell it now because it's just me alone.

**28:13** Â· We call Mario once again, and now my box has zero and Mario's box has one.

**28:18** Â· So we fixed all the issues and.

### Convert Labels Into Names

**28:23** Â· Finally, since people have names and not numbers, let's map the class labels to the class names.

**28:30** Â· So we will create a dictionary named names, and we will map the key of zero to Mariya as well as the key of one two.

**28:41** Â· Mario.

**28:42** Â· Just like we did with our labels, we will also need to set a maximum distance, something that separates familiar faces from strangers.

### Detect Unknown Faces

**28:53** Â· So let's just say that our max distance is 70.

**28:56** Â· Now if you're looking for the absolute sweet spot, you will need some learning.

**29:01** Â· You would have to test a whole bunch of numbers like we did in my scikit learn tutorial.

**29:05** Â· I just randomly picked 70, but you can always adjust it on your end.

**29:09** Â· And same goes for our model training parameters.

**29:13** Â· We basically it's basically a naked model.

**29:16** Â· We didn't change it at all.

**29:18** Â· We didn't customize it, but people usually do on our end.

**29:22** Â· It just happens to work.

**29:23** Â· But it can always work better.

**29:25** Â· We're going to keep it for the next time.

**29:26** Â· Okay, so once we have our names, dictionary and our maximum distance right before we put our text, okay, right over here, we're going to check if the distance is greater than the max distance.

**29:43** Â· Then in this case we are not confident enough in the identity of the person in the box okay.

**29:50** Â· So we'll set the name to Unknown.

**29:54** Â· Otherwise we will set it to whichever name the label that the model returned to us okay belongs to.

**30:04** Â· We will do so with name equals names okay.

**30:08** Â· To which we will pass our predicted label.

**30:12** Â· Okay so names is our new dictionary okay.

**30:16** Â· And then our predicted label can only be 0 or 1 I hope I explained it clearly okay.

**30:24** Â· So then right below when we put our text text we no longer put our predicted label, but we put the name we just derived from it or unknown.

**30:34** Â· Okay, now if you'd like to be extra informed, we can also print the string version of the distance that we also receive from the model, and we can put some kind of a separator in between.

**30:47** Â· Okay, let's say this straight line I don't know what it's called, but now when we rerun this cell am indeed recognized as Mariya, but with a too long of a number.

**31:00** Â· Okay, so let's quickly collapse it.

**31:02** Â· And now let's convert our distance into an integer before we convert it into a string.

**31:09** Â· And hopefully the number will be a bit smaller in terms of decimal points.

**31:15** Â· And okay, I am recognized as Mariya with about 60-something distance.

**31:22** Â· When I start covering my face, it is now 80 something distance well above our max distance threshold and therefore I am unknown.

**31:32** Â· So now when my fingers go down slowly, slowly that I'm suddenly Mariya again.

**31:38** Â· Amazing.

**31:39** Â· So now let me quickly call Mario and let's see how this thing affects it too.

### Final Real-Time Face Recognition Demo

**31:43** Â· And congratulations!

**31:44** Â· Our facial recognition system is officially complete.

**31:47** Â· It mostly recognizes Mario and myself.

**31:50** Â· I mean, most of the time.

**31:51** Â· Sometimes I'm unknown because I'm talking okay, but you can improve it by providing a little bit more photos.

**31:56** Â· You can improve it by changing some of the training parameters, but for the most part it works really well.

**32:02** Â· So congratulations and yay!

### Thanks for Watching!

**32:05** Â· And thank you so much for watching!

**32:07** Â· If you found this video helpful, please share it with the world and don't forget to leave it a huge thumbs up and all kinds of comments.

**32:15** Â· Now, if you'd like to see more videos of this kind, you can always subscribe to my channel and turn on the notification bell.

**32:22** Â· I'll see you soon in an awesome tutorial.

**32:25** Â· So in the meantime, I.