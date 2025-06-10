## drawing functions in opencv
import cv2
import numpy as np

img = cv2.imread('image4.jpg',1)
img = cv2.resize(img, (600, 500))

## for black and white image background
# img = np.zeros((500, 600, 3), dtype=np.uint8) # Create a black image of size 500x600 with 3 color channels (BGR)
# img = np.ones((500, 600, 3), dtype=np.uint8) * 255 # Create a white image of size 500x600 with 3 color channels (BGR)

## Drawing a line
cv2.line(img, (0, 0), (600, 500), (255, 0, 0), 5) # Draw a blue line from top-left to bottom-right
## Drawing a rectangle
cv2.rectangle(img, (50, 50), (550, 450), (0, 255, 0), 3) # Draw a green rectangle
## Drawing a circle
cv2.circle(img, (300, 250), 100, (0, 0, 255), -1) # Draw a filled red circle at the center
## Drawing a polygon
pts = np.array([[100, 100], [200, 50], [300, 100], [250, 200], [150, 200]], np.int32)
cv2.polylines(img, [pts], isClosed=True, color=(255, 255, 0), thickness=3) # Draw a yellow polygon
## Adding text
cv2.putText(img, 'OpenCV Drawing IronMan', (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) # Add white text
# Display the image with drawings   
cv2.imshow('Drawing Functions', img) # Show the image with drawings
# Wait for a key press and close the window
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('drawing_output.jpg', img) # Save the image with drawings
    print("Image saved as drawing_output.jpg")


cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


