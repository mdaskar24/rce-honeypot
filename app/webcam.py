import cv2
from datetime import datetime

def capture_snapshot():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        filename = f"static/snapshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
    cam.release()