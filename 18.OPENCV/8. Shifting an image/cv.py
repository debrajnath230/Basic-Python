import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/nath.debraj/Desktop/Python_training_tutordude/18.OPENCV/CONTENT FILES/highway.jpg", cv2.IMREAD_COLOR)

# Get the height and width of the image
height, width = img.shape[:2]

# Define the shift values (in pixels)
shift_x = 50
shift_y = 30

# Define the transformation matrix for shifting
M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

# Apply the translation to the image
shifted_img = cv2.warpAffine(img, M, (width, height))

# Display the original and shifted images
cv2.imshow('Original Image', img)
cv2.imshow('Shifted Image', shifted_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
