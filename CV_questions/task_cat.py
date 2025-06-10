import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('Cat_Task1.jpg')
img_copy = img.copy()

# Extract the eye region 
eye = img[175:220, 190:250]

# Get dimensions
img_height, img_width = img.shape[:2]
eye_height, eye_width = eye.shape[:2]

# Position on forehead (center horizontally, upper area)
x_offset = (img_width - eye_width) // 2
y_offset = img_height // 3

# Paste the eye on forehead
img_copy[y_offset:y_offset+eye_height, x_offset:x_offset+eye_width] = eye

# Save and display
cv.imwrite('Cat_Third_Eye_Centered.jpg', img_copy)
cv.imshow('Third Eye', img_copy)
cv.waitKey(0)
cv.destroyAllWindows()


# img = cv.imread('Cat_Task1.jpg')

# # Get image shape
# height, width = img.shape[:2]  


# print("Height:", height)
# print("Width:", width)
