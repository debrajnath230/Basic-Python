import cv2

img = cv2.imread('C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg',1)

print('Dimensions of the imsge: ',img.shape)

# width = img.shape[1]
# height = 400

# width = 400
# height = img.shape[1]

width = 400
height =400

dim = (width,height)
resized= cv2.resize(img,dim)

cv2.imshow('window', resized)

cv2.waitKey(0)


cv2.destroyAllWindows()
