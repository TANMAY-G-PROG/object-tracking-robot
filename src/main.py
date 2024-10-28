# src/main.py
import cv2
import numpy as np
from detector import detect_object
from tracker import initialize_tracker, update_tracker

def main():
    color_lower = np.array([30, 100, 100])  # Set HSV range for object color Here the following color range is for green
    color_upper = np.array([50, 255, 255])
    
    cap = cv2.VideoCapture(0)
    tracker = None
    tracking = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if tracking:
            center, bbox = update_tracker(tracker, frame)
            if center:
                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (255, 0, 0), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
            else:
                tracking = False
        
        if not tracking:
            center, bbox = detect_object(frame, color_lower, color_upper)
            if center:
                tracker = initialize_tracker()
                tracker.init(frame, tuple(bbox))
                tracking = True
                cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)
                cv2.circle(frame, center, 5, (0, 255, 0), -1)
        
        cv2.imshow("Object Tracking", frame)
        
        # Adjust the waitKey value for responsive exit detection
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

