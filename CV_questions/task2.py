import numpy as np
import cv2 as cv

colors = {
    'Red': (0, 0, 255),
    'Green': (0, 255, 0),
    'Blue': (255, 0, 0),
    'Black': (0, 0, 0),
    'White': (255, 255, 255)
}

for color_name, bgr in colors.items():
    img = np.zeros((100, 100, 3), dtype=np.uint8) # Create a black image 
    img[:] = bgr # Fill the image with the specified color 
    cv.imwrite(f'{color_name}.jpg', img) 
    cv.imshow(color_name, img) 

    # BGR