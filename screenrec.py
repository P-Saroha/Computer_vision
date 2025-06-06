# import cv2 
# import pyautogui as pag
# import numpy as np

# ## capture the screen resolution 

# rs = pag.size() # Get the screen resolution
# print(rs)

# # filename where the video will be saved

# filename = input("Enter the filename to save the video (e.g., 'output.avi'): ")
# fps = 20.0  # Frames per second for the video

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec
# out = cv2.VideoWriter(filename, fourcc, 20.0, (rs.width, rs.height))  # Create VideoWriter object

# # create recording modules

# cv2.namedWindow("Live Recording",cv2.WINDOW_NORMAL)  # Create a window to display the recording
# cv2.resizeWindow("Live Recording", 800, 600)  # Resize the window to a manageable size

# while True:
#     img = pag.screenshot()  # Take a screenshot of the screen
#     f = np.array(img)  # Convert the screenshot to a NumPy array
#     f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)  # Convert the color space from BGR to RGB
#     out.write(f)  # Write the frame to the video file
#     cv2.imshow("Live Recording", f)  # Display the frame in the window

#     if cv2.waitKey(1) == ord('q'):  # If 'q' is pressed, exit the loop
#         break

# # Release the VideoWriter and destroy all windows
# out.release()
# cv2.destroyAllWindows()


## breaking video into frames and storing them in a folder

import cv2

vidcap = cv2.VideoCapture(0)
ret,image = vidcap.read() # read the first frame 

count = 0

while True:
  if ret == True:
      cv2.imwrite("frames\\imgN%d.jpg" % count, image)     # save frame as JPEG file
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #used to hold speed of frane generation
      ret,image = vidcap.read() # read the next frame 
      cv2.imshow("res",image)
      print ('Read a new frame:',count ,ret) # print the frame number and read status
      count += 1
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
  else:
      break

vidcap.release() 
cv2.destroyAllWindows()  

