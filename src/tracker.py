# src/tracker.py
import cv2

def initialize_tracker():
    tracker = cv2.TrackerKCF_create()
    print("Tracker created Successfully")
    return tracker

def update_tracker(tracker, frame):
    success, bbox = tracker.update(frame)
    if success:
        (x, y, w, h) = [int(v) for v in bbox]
        return (x + w // 2, y + h // 2), (x, y, w, h)  # Return center and bounding box
    return None, None
