import numpy as np
import cv2 as cv

image = cv.imread("data/thresh.jpg")
cv.imshow("Original", image)

blur = cv.GaussianBlur(image, (5, 55), 0)  # this will blur the image more on the vertical axis
cv.imshow("Blur", blur)

kernel = np.ones((5, 5), 'uint8')

dilate = cv.dilate(image, kernel, iterations=1)
erode = cv.erode(image, kernel, iterations=1)
# if you want to increase the effect of these filters, high levels of integrations will continue to eat away on the image even on the first pass
# each iteration will eat away more from the fore or background

cv.imshow("Dilate", dilate)
cv.imshow("Erode", erode)

cv.waitKey(0)
cv.destroyAllWindows()