import cv2 
img1  = cv2.imread('nature1.jpg')
print(img1.shape)
cv2.imshow('Image', img1)
cv2.waitKey()
cv2.destroyAllWindows()