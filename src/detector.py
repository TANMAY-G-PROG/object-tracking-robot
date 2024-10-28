# src/detector.py
import cv2

def detect_object(frame, color_lower, color_upper):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, color_lower, color_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(largest_contour)
        return (x + w // 2, y + h // 2), (x, y, w, h)  # Return center and bounding box
    return None, None
