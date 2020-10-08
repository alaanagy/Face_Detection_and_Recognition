'/author : Alaa Nagy , Hassa Mohamed /'


import cv2
import numpy as np
from PIL import Image
import os

# initializ webcam 
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

#using Haar cascade classifeir to detect faces 
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('Enter the user id number then press enter..= ')
    
print("\n Look at the camera and wait to gather your dataset...")


# Initialize individual sampling face count
count = 0

while(True):
    
    # read frames from webcam 
    ret, img = cam.read()   
    # convert image into gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    #loop to draw a  blue rectangle around faces and save it 
    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample for each person and stop video
         break


print("\n Process complete :) ")

#Release webcam 
cam.release()
cv2.destroyAllWindows()


