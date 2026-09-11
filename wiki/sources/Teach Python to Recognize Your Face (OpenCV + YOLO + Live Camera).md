---
title: "Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)"
source_file: "Clippings/Teach Python to Recognize Your Face ?? (OpenCV + YOLO + Live Camera).md"
date_ingested: 2026-09-11
tags:
  - python
  - opencv
  - yolo
  - face-recognition
  - computer-vision
  - tutorial
---

# Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)

**Source:** YouTube video by [[Python Simplified]], 2026-08-26
**URL:** https://www.youtube.com/watch?v=Z2Ojl7m3JXk

## Summary

Step-by-step tutorial on building a real-time face recognition system using Python, OpenCV LBPH recognizer, and YOLO face detection. Train model on your own photos, recognize multiple faces in live camera, label familiar vs unknown faces. Everything runs locally.

## Key Takeaways

### Face Detection vs Recognition
- **Detection:** Finding a face in an image (previous tutorial)
- **Recognition:** Identifying WHO that face belongs to (this tutorial)

### Training Data Preparation
- Create folder structure: aces/Name1/, aces/Name2/
- ~20 photos per person, each with single face
- Photos should match camera conditions (lighting, angle, background)
- No need to crop faces manually (YOLO does this)

### YOLO Face Detection & Cropping
- Use YOLOv8 Medium Face model (download from GitHub)
- Extract face coordinates with .boxes.xyxy
- Convert coordinates to integers for pixel slicing
- Crop, grayscale, resize faces to 200x200 pixels

### OpenCV LBPH Face Recognizer
- Install opencv-contrib-python
- Use cv2.face.LBPHFaceRecognizer_create()
- Train with cropped faces and integer labels (0, 1, 2...)
- Save trained model as .yml file

### Multi-Person Training
- Create dictionary mapping labels to folders
- Iterate over dictionary to process each person
- Append faces and labels in parallel lists
- Convert labels to NumPy array for training

### Real-Time Recognition
- Load trained model with ace_recognizer.read()
- Process each video frame: detect → crop → grayscale → resize → predict
- Use ace_recognizer.predict() to get label + distance
- Map labels to names with dictionary
- Set max distance threshold (e.g., 70) to identify unknown faces

### Practical Tips
- Distance metric indicates confidence (small = good match)
- Adjust threshold based on testing
- Can improve with more training photos
- Works with multiple faces simultaneously

## Contradictions / Notes
- Builds on face detection tutorial; assumes basic OpenCV/YOLO knowledge
- Requires GPU for smooth real-time performance (optional but recommended)
- All processing local, no cloud APIs needed