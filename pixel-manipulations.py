import numpy as np
import cv2 as cv

color = cv.imread("data/butterfly.jpg", 1)
gray = cv.cvtColor(color, cv.COLOR_BGR2GRAY)
cv.imwrite("data/gray.jpg", gray)

b, g, r = cv.split(color)  # using slices (as shown below) instead of cv2.split is actually much faster

# b = color[:, :, 0]
# g = color[:, :, 1]
# r = color[:, :, 2]

rgba = cv.merge((b, g, r, g))  
# the fourth channel acts as our transparency layer. 
# we can use one of our already existing channels (i.e b, g, or r). 
# if you want to make the non green parts of the image transparent, we pass in the g channel where a high value
# or a very green pixel will show as a high alpha layer, meaning not transparent and anything that has a low
# green value or zero will appear as fully transparent 

cv.imwrite("data/rgba.png", rgba)  
# we use png because jpg images do not support image transparency. 
# jpg image would be compiled back to a three(3) channel image whereas a png image would retain the transparency