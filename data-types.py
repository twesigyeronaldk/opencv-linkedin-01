import numpy as np
import cv2 as cv

black = np.zeros([150, 200, 1], 'uint8')  # create image with 150 rows, 200 columns and one(1) channel
cv.imshow("Black", black)
print(black[0, 0, :])

ones = np.ones([150, 200, 3], 'uint8')
cv.imshow("Ones", ones)  # this image appears black because the value one(1) is very small and close to zero(0) compared to the maximum possible value of 255 (uint8)
print(ones[0, 0, :])

white = np.ones([150, 200, 3], 'uint16')
white *= (2**16 - 1)
cv.imshow("White", white)
print(white[0, 0, :])

color = ones.copy()  # creates deep copy, that is, both images are not connected to each other
color[:, :] = (255, 0, 0)
cv.imshow("Blue", color)
print(color[0, 0, :])

cv.waitKey(0)
cv.destroyAllWindows()