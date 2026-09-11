---
tags:
  - entity
  - tool
  - computer-vision
created: 2026-09-11
sources:
  - "[[Teach Python to Recognize Your Face (OpenCV + YOLO + Live Camera)]]"
---

# OpenCV LBPH Face Recognizer

OpenCV's Local Binary Patterns Histograms (LBPH) face recognizer — a classical machine learning model for face recognition that runs entirely locally.

## How It Works

1. **Detect faces** using YOLOv8n-face or Haar cascades
2. **Crop and resize** detected face regions to a standard size
3. **Extract LBPH features** — texture descriptors computed from local binary patterns in pixel neighborhoods
4. **Train the recognizer** on labeled face images (one label per person)
5. **Predict** — given a new face, output a label + confidence score

## Key Properties

- **Local**: no cloud API, no internet required after training
- **Fast**: runs in real-time on CPU (no GPU needed for recognition)
- **Lightweight**: trained model is small (KB, not GB)
- **Deterministic**: same input → same output (no LLM randomness)

## Use Cases

- Smart door locks / access control
- Attendance systems
- Photo organization (auto-tag people)
- Security monitoring

## Limitations

- Needs 10-20+ photos per person for reliable recognition
- Sensitive to lighting, angle, and expression changes
- No deep learning — less robust than ArcFace/Dlib for challenging conditions
- Confidence threshold must be tuned per deployment

## Related

- [[OpenCV]] — parent library
- [[YOLO]] — face detection backbone
- [[Python Simplified]] — tutorial source