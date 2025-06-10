import cv2 as cv


img = cv.imread('Cat Clue 3.jpg')
eye_region = img[100:180, 90:260]  
cv.imwrite("eye_zoom.jpg", eye_region)
