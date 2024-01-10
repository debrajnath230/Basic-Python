import cv2

img = cv2.imread("C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg")

print('Dimension of original image',img.shape)

scale = 150
width = int(img.shape[1]*scale/100)
height =int(img.shape[0]*scale/100)
dim =(width,height)

resized =cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

print('dimensions of resized image',resized.shape)

cv2.imshow('resized image',resized)
cv2.imshow('Original image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
