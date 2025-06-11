# (324,48) ,(436,211) 
import cv2
import numpy as np
# This code demonstrates how to extract a Region of Interest (ROI) from an image using OpenCV.
# It allows the user to select a rectangular area in the image and extract that region.

#In this Video, we talk about ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.

#read image
img = cv2.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\roi_opr.jpg")
img = cv2.resize(img,(800,800))

#Now extract  area of interest from an image

#now pass like [y1:y2,x1:x2]
roi = img[48:211,324:436] ## differece (163 , 112)
#cv2.imshow("roi image==",roi)

#putting roi into any pixel values

img[48:211,431:543] = roi   #actual 441:561
img[48:211,564:676] = roi
img[48:211,200:312] = roi
img[48:211,80:192] = roi

#changing y===
# img[400:563,60:172] = roi # 
cv2.imshow("original image==",img)

#Now try to use one image data into another image

# img1 = cv2.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\ironman.jpg")
# img1 = cv2.resize(img1,(900,600))
# img1[1:156,560:680] = roi

# cv2.imshow("ironman",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
