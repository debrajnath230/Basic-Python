import cv2
import numpy as np

img = cv2.imread('C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg')

width = 600
height = 850
dimen = (width, height)
resized = cv2.resize(img, dimen)  

kernel = np.ones((5, 5), dtype=np.uint8)  

# erosion = cv2.erode(resized, kernel, iterations=1)
# dilation = cv2.dilate(resized, kernel, iterations=1)

#opening = cv2.morphologyEx(resized, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)

#gradinet = cv2.morphologyEx(resized,cv2.MORPH_GRADIENT,kernel)

tophat = cv2.morphologyEx(resized,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(resized,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('Original image', resized)
#cv2.imshow('Erosion', erosion)
#cv2.imshow('Dilation', dilation)

#cv2.imshow('opening', opening)
#cv2.imshow('closing', closing)

#cv2.imshow('gradient', gradinet)

cv2.imshow('TOPHAT', tophat)
cv2.imshow('Blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
