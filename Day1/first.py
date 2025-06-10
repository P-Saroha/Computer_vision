import cv2 

## RGB Image
img1  = cv2.imread('nature1.jpg',1)
print(img1.shape)
print(img1)
img1 = cv2.resize(img1, (1000, 1000))
cv2.imshow('original', img1)
cv2.waitKey()
cv2.destroyAllWindows()

## grayscale Image
img2  = cv2.imread('deer.jpg',0)
print(img2.shape)
print(img2) 
# img1 = cv2.resize(img1, (200, 200))
cv2.imshow('original', img2)
cv2.waitKey()
cv2.destroyAllWindows()

## RGBA Image (enhanced image)
img3 = cv2.imread("image3.jpg",-1)
print(img3.shape)
cv2.imshow('original', img3)
cv2.waitKey()
cv2.destroyAllWindows()

## saving an image (grayscale)
img4  = cv2.imread("image4.jpg", 0)
cv2.imshow('original', img4)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('image4.jpg', img4)
    print("Image saved as image4.jpg")

else:
    cv2.destroyAllWindows()