import cv2
import datetime
cap = cv2.VideoCapture('D:\\Computer Vision\\2. Computer Vision\\CV\\test2.mp4')  #for warn 0 just pass cv2.CAP_DSHOW
print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 600)  #here 3 for width
cap.set(4, 800)  #here 4 for height 
print("Width====",cap.get(3)) # getting width
print("Height===",cap.get(4)) # getting height

while(cap.isOpened()):
    ret, frame = cap.read() # reading the video frame by frame
    # ret is a boolean value that indicates if the frame was read correctly
    if ret == True:

       font = cv2.FONT_HERSHEY_COMPLEX_SMALL # setting the font for the text
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3)) ## adding height and width on the video

       date_data = "Date: "+str(datetime.datetime.now()) # getting current date and time on the video
       frame = cv2.putText(frame, text, (10, 20), font, 1,
                           (0, 155, 255), 1, cv2.LINE_AA)  # adding text on the video
       frame = cv2.putText(frame, date_data, (20, 50), font, 1,
                           (100, 255, 255), 1, cv2.LINE_AA) # adding date and time on the video
       #Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)

       cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
       cv2.imshow('frame', frame)

       if cv2.waitKey(30) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()