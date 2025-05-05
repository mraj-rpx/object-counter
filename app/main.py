from flask import Flask, render_template, request
import cv2
import os
from detector import ObjectDetector
from tracker import ObjectTracker
from counter import RegionCounter
from speed_estimator import SpeedEstimator
from utils import draw_regions, draw_detections

app = Flask(__name__)
UPLOAD_FOLDER = 'video'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files['video']
    if file:
        video_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(video_path)
        output_path = os.path.join(RESULT_FOLDER, f"processed_{file.filename}")
        process_video(video_path, output_path)
        return f"Video processed. Output saved at {output_path}"
    return "No file uploaded."

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    detector = ObjectDetector()
    tracker = ObjectTracker()
    regions = [('Entry', (100, 100, 300, 300)), ('Exit', (400, 100, 600, 300))]
    counter = RegionCounter(regions)
    speed_estimator = SpeedEstimator(fps=fps, ppm=10)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detections = detector.detect(frame)
        # Implement tracking logic to assign IDs to detections
        # For each detection, estimate speed and update counters
        draw_regions(frame, regions)
        draw_detections(frame, detections)
        out.write(frame)

    cap.release()
    out.release()

if __name__ == '__main__':
    app.run(debug=True)
