import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

color = (0, 255, 0)  # this is assuming that camera has uint8 depth
line_width = 3
radius = 100
point = (0, 0)

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv.EVENT_LBUTTONDOWN:
        print("Pressed", x, y)
        point = (x, y)

cv.namedWindow("Frame")
cv.setMouseCallback("Frame", click)

while(True):
    ret, frame = cap.read()

    # frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv.circle(frame, point, radius, color, line_width)
    cv.imshow("Frame", frame)

    ch = cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()