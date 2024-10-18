import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv.imshow("Frame", frame)

    ch = cv.waitKey(1)  # wait 1 milli second
    if ch & 0xFF == ord('q'):  # 0xFF works only on 64 bit machines, othwerwise only use ch (if ch...)
        break

cap.release()
cv.destroyAllWindows()