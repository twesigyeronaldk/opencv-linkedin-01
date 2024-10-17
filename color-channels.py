import numpy as np
import cv2 as cv

color = cv.imread("data/butterfly.jpg", cv.IMREAD_COLOR)
cv.imshow("Image", color)
cv.moveWindow("Image", 0, 0)  # cv will load image in top left hand corner
print(color.shape)
height, width, channels = color.shape

b, g, r = cv.split(color)

rgb_split = np.empty([height, width*3, 3], 'uint8')

rgb_split[:, 0:width] = cv.merge([b, b, b])
rgb_split[:, width:width*2] = cv.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv.merge([r, r, r])

cv.imshow("Channels", rgb_split)
cv.moveWindow("Channels", 0, height)

hsv = cv.cvtColor(color, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)
hsv_split = np.concatenate((h, s, v), axis=1)
cv.imshow("Split HSV", hsv_split)

cv.waitKey(0)
cv.destroyAllWindows()