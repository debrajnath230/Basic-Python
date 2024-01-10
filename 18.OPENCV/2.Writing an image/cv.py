import cv2

img = cv2.imread('C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg',0)

cv2.imshow('window', img)

cv2.imwrite('C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/2.Writing an image/car.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
