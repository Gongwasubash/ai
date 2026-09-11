---
tags:
  - tool
  - company
  - computer-vision
created: 2026-09-11
sources:
  - "[[Python Face Detection from Scratch (OpenCV + YOLO + Webcam)]]"
  - "[[Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)]]"
---

# Ultralytics

Company behind YOLOv8 and the Ultralytics Python library. Provides state-of-the-art object detection, segmentation, and classification models.

## Key Products

- **Ultralytics YOLO:** Python library for YOLO models
- **YOLOv8:** Latest generation object detection architecture
- **Ultralytics HUB:** Platform for model training and deployment

## Python Library

`python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # load pretrained model
results = model(image)       # run inference
`

## Model Zoo

- **Detection:** YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l, YOLOv8x
- **Segmentation:** YOLOv8n-seg, YOLOv8s-seg, etc.
- **Classification:** YOLOv8n-cls, YOLOv8s-cls, etc.
- **Pose:** YOLOv8n-pose, YOLOv8s-pose, etc.

## Community Models

- YOLOv8 Face (Akanametov) - face detection
- Custom trained models shared via GitHub

## Installation

`ash
pip install ultralytics
`

## Features

- Easy-to-use Python API
- Pretrained models ready for inference
- Custom training on custom datasets
- Export to ONNX, TensorRT, CoreML, etc.
- Real-time performance on GPU/CPU

## Related

- [[YOLO]]
- [[OpenCV]]
- [[Python]]
- [[Object Detection]]
- [[Face Detection]]
- [[Computer Vision]]