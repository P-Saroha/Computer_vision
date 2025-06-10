import numpy as np
import cv2

# This code demonstrates how to bind mouse events to a window in OpenCV.
# It allows the user to draw shapes on a black image by double-clicking with the mouse.
# mouse callback function
def draw(event,x,y,flags,param): # event is the type of mouse event, x and y are the coordinates of the mouse pointer,
    # flags are any relevant flags, and param is any additional parameters passed to the callback function.

    # Check if the left button was double clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        cv2.circle(img,(x,y),100,(255,255,255),5)

    # Check if the right button was double clicked
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)

# Create a window named "res"
cv2.namedWindow(winname = "res")
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)

# Bind the mouse callback function to the window "res"
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()