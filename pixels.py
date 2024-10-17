import numpy as np
import cv2 as cv

img = cv.imread("data/opencv-logo.png", 1)
print(type(img))
print("Rows: ", len(img))
print("Columns: ", len(img[0]))
print("Channels: ", len(img[0][0]))  # if there are four(4) channels, that means there is also a transparency layer
print("Shape: ", img.shape)
print(img.dtype)  # if dtype is uint8, then all pixel values have a maximum of 255, that is, 2**8
print(img[10, 5])  # get pixel values for particular row and column in image. this returns pixel values of each channel
print(img[:, :, 0])  # get all pixel values for single channel
print(img.size)  # get total number of data points inside image array