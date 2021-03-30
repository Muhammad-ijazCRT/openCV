# Name: Muhammad ijaz
# coding is my hobe
# find Find Contours on ROI of an image

import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('ijazkhan.jpg')
image = cv2.resize(image, (512,720))
cv2.waitKey(0)

# selecting ROI
dmc = image[0:415, 0:512]
cv2.imshow('ROI', dmc)
cv2.waitKey()


# Grayscale
gray = cv2.cvtColor(dmc, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
