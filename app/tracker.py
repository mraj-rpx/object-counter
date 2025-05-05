import cv2

class ObjectTracker:
    def __init__(self):
        self.tracker = None
        self.initialized = False

    def initialize(self, frame, bbox):
        self.tracker = cv2.TrackerKCF_create()
        self.tracker.init(frame, bbox)
        self.initialized = True

    def update(self, frame, detections):
        if not self.initialized:
            if detections:
                self.initialize(frame, detections[0])  # track first detected object
                return [detections[0]]
            return []
        success, bbox = self.tracker.update(frame)
        if success:
            return [bbox]
        else:
            self.initialized = False
            return self.update(frame, detections)
