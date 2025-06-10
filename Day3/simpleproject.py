#Create a fucntion which help to find cordinate of any pixel and its color
import numpy as np
import cv2

# This code demonstrates how to find the coordinates and color of a pixel in an image using mouse events in OpenCV.
# It allows the user to left-click to get the coordinates and right-click to get the color of the pixel at that location.

# mouse callback function
def mouse_event(event, x, y, flg, param): # event is the type of mouse event, x and y are the coordinates of the mouse pointer,
    # flg are any relevant flags, and param is any additional parameters passed to the callback function.

    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flg==",flg)
    print("param==",param)

    font = cv2.FONT_HERSHEY_PLAIN # setting the font for the text


    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
           
        cord = ". "+str(x) + ', '+ str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125 ,100), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b= img[y, x, 0] #for blue channel is 0
        g = img[y, x, 1] #for green channel is 1
        r = img[y, x, 2] #for red channel is 2
        
        color_bgr = ". "+str(b) + ', '+ str(g)+ ', '+ str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('D:\\Computer Vision\\2. Computer Vision\\CV\\nature1.jpg')

cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
