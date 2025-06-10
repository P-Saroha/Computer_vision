import cv2 as cv

# Step 1: Load the image
img = cv.imread('Cat Clue 4.png')

# Step 2: Define the coordinates to label
coords = [(225, 231), (96, 133), (402, 330), (280, 65)]

# Step 3: Label each coordinate with a number
for idx, (x, y) in enumerate(coords, start=1):
    cv.putText(img, str(idx), (x, y), cv.FONT_HERSHEY_SIMPLEX,
               fontScale=1.0, color=(0, 0, 255), thickness=2)

# Step 4: Save the labeled image
cv.imwrite("numbered_coords.jpg", img)

# Step 5: Display the image with labels
cv.imshow("Numbered Coordinates", img)
cv.waitKey(0)
cv.destroyAllWindows()
