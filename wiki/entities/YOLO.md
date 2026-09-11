---
tags:
  - tool
  - computer-vision
  - object-detection
created: 2026-09-11
sources:
  - "[[Python Face Detection from Scratch (OpenCV + YOLO + Webcam)]]"
  - "[[Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)]]"
---

# YOLO (You Only Look Once)

Real-time object detection architecture. Popular for speed and accuracy in detecting objects in images and video.

## Key Features

- **Single-shot detection:** One pass through network for all objects
- **Real-time performance:** Fast inference speeds
- **Multiple versions:** YOLOv5, YOLOv8, YOLOv9, etc.
- **Custom training:** Can be trained on custom datasets

## YOLOv8

- Latest version from Ultralytics
- Improved accuracy and speed
- Support for detection, segmentation, classification, pose
- Nano (n), Small (s), Medium (m), Large (l), Extra-large (x) sizes

## Face Detection

- Official YOLO doesn't include face class
- Community models: YOLOv8 Face (Akanametov)
- Medium face model for balanced speed/accuracy

## Usage with Ultralytics

`python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # load model
results = model(image)       # inference
`

## Applications

- Security systems
- Autonomous vehicles
- Robotics
- Video analytics
- Face detection/recognition pipelines

## Related

- [[Ultralytics]]
- [[OpenCV]]
- [[Python]]
- [[Face Detection]]
- [[Object Detection]]
- [[Computer Vision]]