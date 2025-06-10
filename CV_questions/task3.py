import numpy as np
import cv2 as cv

# Size of one square
square_size = 40
chessboard = np.zeros((320, 320, 3), dtype=np.uint8)

# Fill white squares
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chessboard[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = (255, 255, 255)

cv.imwrite('Chessboard.jpg', chessboard)
cv.imshow('Chessboard', chessboard)
cv.waitKey(0)
cv.destroyAllWindows()
