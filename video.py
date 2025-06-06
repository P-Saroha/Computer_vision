import cv2

# Video Capture
# cap = cv2.VideoCapture('test2.mp4')

# print('cap',cap)

# while True:
#     ret,frame = cap.read() # Read a frame from the video capture object
#     cv2.imshow('frame', frame) # Display the frame in a window named 'frame'

#     ## Convert to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('gray', gray)

#     ## 
#     k = cv2.waitKey(25) # Wait for 25 milliseconds
#     if k == ord('q') & 0xFF: # If 'q' is pressed, exit the loop
#         break
# # Release the capture and close windows
# cap.release() # Release the video capture object
# cv2.destroyAllWindows()


## capture from webcam and save the video
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 0 for the default webcam

fourcc = cv2.VideoWriter_fourcc(*'XVID') # Define the codec and create VideoWriter object
out = cv2.VideoWriter('D:/Computer Vision/2. Computer Vision/CV/output.avi', fourcc, 20.0, (640, 480)) # Define the output video file name, codec, frame rate, and frame size

print('cap', cap)
while cap.isOpened(): # Check if the webcam is opened
    ret, frame = cap.read() # Read a frame from the webcam
    if ret == True:
        cv2.imshow('Webcam Frame', frame) # Display the frame in a window named 'Webcam Frame'
        out.write(frame) # Write the frame to the output video file
        k = cv2.waitKey(1) # Wait for 1 millisecond
        if k == ord('q') & 0xFF: # If 'q' is pressed, exit the loop
            break
cap.release() # Release the webcam
out.release() # Release the video writer
cv2.destroyAllWindows() # Close all OpenCV windows
