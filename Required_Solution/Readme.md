# Hand Gesture Recognition System

A modular Python project to capture webcam video, detect hand landmarks using MediaPipe, and recognize simple gestures to trigger commands.

---

## 📑 Table of Contents

- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 📖 About

This project demonstrates real-time hand gesture recognition with Python, OpenCV, and MediaPipe.  
It can recognize:
- **STOP**: All fingers extended
- **MOVE BACKWARD**: All fingers folded
- **MOVE FORWARD**: Index and middle fingers extended

These gestures can be extended to control external systems (robots, UI navigation, etc).

---

## ✨ Features

✅ Live video capture from webcam  
✅ Hand landmarks detection and visualization  
✅ Real-time gesture classification  
✅ Modular, clean Python code  
✅ Easily extensible with more gestures

---

## ✅ Prerequisites

Before installing, ensure you have:

- **Python 3.7+**
- **pip**

Recommended Python version: **3.8 or later**

---

## ⚙️ Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2️⃣ (Optional) Create a virtual environment
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
3️⃣ Install dependencies
```bash
pip install opencv-python mediapipe

```
## 🗂️ Project Structure

├── video_capture.py # Webcam video capture logic
├── display_service.py # Landmark and text drawing utilities
├── gesture_recognizer.py # Gesture recognition logic
└── README.md # Project documentation

## 🛠️ How It Works

### `video_capture.py`

- `VideoCaptureService` initializes the webcam and reads frames.
- Frames are horizontally flipped for a mirror-like view.

---

### `display_service.py`

- `DisplayService` contains:
  - `draw_landmarks()` to overlay hand skeleton.
  - `draw_text()` to display labels (e.g., detected gesture).

---

### `gesture_recognizer.py`

- `GestureRecognizer` classifies gestures by comparing fingertip and PIP (proximal interphalangeal joint) landmark Y coordinates.

**Gesture Logic:**

| Gesture        | Condition                                                         |
|----------------|-------------------------------------------------------------------|
| STOP           | All 4 fingers extended                                           |
| MOVE BACKWARD  | All 4 fingers folded                                             |
| MOVE FORWARD   | Index and middle fingers extended, ring and pinky folded        |
| *(empty)*      | No recognized pattern                                            |

---

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking.
- [OpenCV](https://opencv.org/) for image and video processing.
