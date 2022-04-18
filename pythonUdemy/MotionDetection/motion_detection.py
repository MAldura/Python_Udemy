from datetime import datetime
from time import time
import cv2
from cv2 import threshold
import pandas

#variable for the first frame used to store static background 
first_frame = None #used to avoid "variable not defined error"
status_list = [None, None] #list to store status of object detection 
times = [] #list to store when status changes

#create a dataframe structure with start and end columns
df = pandas.DataFrame(columns=["Start", "End"])

#Start of video capture 
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    status = 0 #variable used to flag when an object is in frame
    
    #convert frame to grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #apply blur
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)

    #create a frame based on the threshold of delta_frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #threshold method returns tuple with two values 0:threshold and 1:actual frame
    
    #dilate image to allow for smoother frames
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)
    
    #retrieve contours and store in cnts
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #iterate through contours and filter through areas < 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue #go back to begining of while loop
        
        status = 1
        
        #if area is > 1000 pixels the a rectangle will be drawn in the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,  (x, y), (x + w, y +h),(0, 255, 0), 3)
    
    #check if last item of status list is the same or not and save the timestamp to times[]
    status_list.append(status)
    
    status_list = status_list[-2:]
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
        
    #display frames
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Color Frame", frame)



    key=cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()