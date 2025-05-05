# Intelligent Object Counting and Speed Monitoring System using YOLOv8

This project is a real-time object detection, tracking, counting, and speed estimation system. Built with Python, YOLOv8, and OpenCV, it processes surveillance video to detect vehicles or pedestrians, track them, count them by region, and estimate their speed. It includes a Flask-based web interface and is fully containerized with Docker.

---

## 🔧 Features

- **YOLOv8**-based real-time object detection
- **Object tracking** using ByteTrack or DeepSORT
- **Region-based counting** (e.g., Entry/Exit zones)
- **Speed estimation** via pixel displacement
- **Flask Web UI** for uploading and processing video
- **Dockerized** for simple deployment

---

## 📁 Project Structure
```
object-counter/
│
├── app/
│ ├── main.py # Flask app
│ ├── detector.py # YOLOv8 detector
│ ├── tracker.py # Object tracker
│ ├── counter.py # Region-based object counter
│ ├── speed_estimator.py # Speed estimation logic
│ ├── utils.py # Drawing and utility functions
│ └── templates/
│ └── index.html # Web UI
│
├── video/ # Input video files
├── output/ # Processed videos
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mraj-rpx/object-counter.git
cd object-speed-counter
````

### 2. Setup Python Environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Download YOLOv8 Weights
```
Download from Ultralytics YOLOv8 Releases and place the .pt file (e.g., yolov8n.pt) in the project directory.
```

### 4. Run Locally (Flask UI)

```
cd app
python main.py
```
Open your browser at: http://localhost:5000

### 5. Run from Command Line

```
from app.process_video import process_video

process_video("video/input.mp4", "output/processed.mp4")
```

### 6. Docker Usage

```
docker build -t object-counter-app .
docker run -p 5000:5000 -v $(pwd)/video:/app/video object-counter-app

```

### 7. With Docker Compose
```
docker-compose up --build
```

### 8. Model Details

This project uses YOLOv8 for object detection and supports:

- Cars
- Pedestrians
- Bicycles
- Custom classes (configurable)
- Tracking is done using popular methods such as:
- ByteTrack
- DeepSORT
- Speed is estimated using the change in object location over time, based on video FPS and pixels-per-meter approximation.