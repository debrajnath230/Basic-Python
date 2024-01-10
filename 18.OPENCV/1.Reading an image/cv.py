import cv2

img = cv2.imread('C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg',1)

cv2.imshow('window', img)

cv2.waitKey(1000)

cv2.destroyAllWindows()
