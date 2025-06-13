# Image Blending Project    

#result Blending with Trackbars 

import numpy as np
import cv2 as cv 
#read two different images of same channel
img1 = cv.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\roi_opr.jpg")
img1 = cv.resize(img1,(500,700))
img2 = cv.imread("D:\\Computer Vision\\2. Computer Vision\\CV\\bro_thor.jpg")
img2 = cv.resize(img2,(500,700))


def blend(x): # callback function for trackbar 
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('blend') #create track bar windows
cv.createTrackbar('alpha','blend',1,100,blend)
switch = '0 : OFF \n 1 : ON'  #create switch for invoke the trackbars
cv.createTrackbar(switch,'blend',0,1,blend)  #create track bar for switch
while(1):
    alpha = cv.getTrackbarPos('alpha','blend')

    s = cv.getTrackbarPos(switch,'blend')
    na = float(alpha/100)
    
    if s == 0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-na,img2,na,0)
        cv.putText(dst, str(alpha), (20, 50), cv.FONT_ITALIC,
                   2, (0, 125, 255), 2)
    cv.imshow('dst',dst)

    k=cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv.waitKey(0)    

cv.destroyAllWindows()