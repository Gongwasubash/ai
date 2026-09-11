---
tags:
  - tool
  - computer-vision
  - python
created: 2026-09-11
sources:
  - "[[Python Face Detection from Scratch (OpenCV + YOLO + Webcam)]]"
  - "[[Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)]]"
---

# OpenCV

Open Source Computer Vision Library. Popular Python library for image and video processing, computer vision, and machine learning.

## Key Features

- **Image/Video I/O:** Read, write, display images and video streams
- **Image Processing:** Transformations, filtering, color space conversion
- **Object Detection:** Haar cascades, DNN module
- **Face Recognition:** LBPH, Eigen, Fisher face recognizers
- **Camera Calibration:** Undistortion, stereo vision

## Python Usage

- Import as import cv2
- Install via pip install opencv-python
- For face recognition: pip install opencv-contrib-python

## Common Functions

- cv2.imread() / cv2.imshow() - Image display
- cv2.VideoCapture() - Camera/video capture
- cv2.cvtColor() - Color conversion (e.g., BGR to grayscale)
- cv2.resize() - Resize images
- cv2.rectangle() / cv2.putText() - Draw on images

## Integration

- Works with YOLO for object detection
- Used with NumPy for array operations
- JupyterLab for interactive development

## Related

- [[Python]]
- [[YOLO]]
- [[Ultralytics]]
- [[Face Detection]]
- [[Face Recognition]]
- [[OpenCV LBPH Face Recognizer]]
- [[Computer Vision]]