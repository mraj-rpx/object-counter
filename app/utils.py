import cv2

def draw_detections(frame, tracked_objects):
    """
    Draw bounding boxes and IDs for tracked objects.
    :param frame: The frame to draw on.
    :param tracked_objects: List of tuples (id, (x, y, w, h))
    """
    for obj_id, (x, y, w, h) in tracked_objects:
        color = (0, 255, 0)  # Green box
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        label = f'ID {obj_id}'
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, color, 2)


def draw_regions(frame, regions):
    """
    Draw named rectangular regions (e.g., Entry/Exit zones).
    :param frame: The frame to draw on.
    :param regions: List of tuples (name, (x1, y1, x2, y2))
    """
    for name, (x1, y1, x2, y2) in regions:
        color = (255, 0, 0)  # Blue
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)


def draw_speed(frame, obj_id, bbox, speed):
    """
    Draw the estimated speed near the object.
    :param frame: Frame to draw on.
    :param obj_id: ID of the object.
    :param bbox: Bounding box (x, y, w, h).
    :param speed: Speed value (float).
    """
    x, y, w, h = bbox
    label = f"Speed: {speed:.2f} km/h"
    cv2.putText(frame, label, (x, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 255), 2)
