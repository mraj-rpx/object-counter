import numpy as np

class SpeedEstimator:
    def __init__(self, fps=30, ppm=10):  # pixels per meter
        self.fps = fps
        self.ppm = ppm
        self.prev_positions = {}

    def estimate(self, object_id, current_position):
        speed = 0.0
        if object_id in self.prev_positions:
            prev_position = self.prev_positions[object_id]
            distance_pixels = np.linalg.norm(np.array(current_position) - np.array(prev_position))
            distance_meters = distance_pixels / self.ppm
            speed = distance_meters * self.fps  # meters per second
        self.prev_positions[object_id] = current_position
        return round(speed, 2)
