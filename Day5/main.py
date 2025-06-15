# Image Blending Project    

#result Blending with Trackbars 

import numpy as np
import cv2 as cv 
#read two different images of same channel
img1 = cv.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\roi_opr.jpg")
img1 = cv.resize(img1,(500,700))
img2 = cv.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\bro_thor.jpg")
img2 = cv.resize(img2,(500,700))
