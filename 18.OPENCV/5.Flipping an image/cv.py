import cv2

img = cv2.imread("C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg")

width = 600
height = 850
dim = (width,height)

resized = cv2.resize(img,dim)
print('size in bytes',img.size)

cv2.imshow('Original Image',resized)
flip= cv2.flip(resized,1)
cv2.imshow('Horizonal',flip)

flip_1= cv2.flip(resized,0)
cv2.imshow('Vertical',flip_1)

flip_2= cv2.flip(resized,-1)
cv2.imshow('horizonal & Vertical',flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows() 

