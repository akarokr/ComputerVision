# -*- coding: utf-8 -*-
"""
Face Detection using Haar Cascades
Created on Sun Aug 30 10:57:39 2015

@author: Bruno Godoi Eilliar
Notes:
http://docs.opencv.org/doc/user_guide/ug_traincascade.html
"""
debug = True
import cv2
import numpy as np

# Define a Clasifier using pre-existing data on OpenCV library
face_cascade = cv2.CascadeClassifier('/home/bruno/Downloads/haarcascade_frontalface_default.xml')

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
if debug: print "Frame size: ", (w,h)
# Open a Window
cv2.namedWindow("Video")
print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()

if debug: print "Frame Shape: ", np.shape(frame)

while success and cv2.waitKey(1) == -1:
    # Take a frame
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(cv2.blur(frame, (5,5)), cv2.COLOR_BGR2GRAY)
    # Detec faces
    faces = face_cascade.detectMultiScale(gray, 1.5, 2)
    if debug: print faces
    # For each face, draw a rectangle around it
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    # Show results
    cv2.imshow("Video", frame)

# Release camera and close windows
cameraCapture.release()
cv2.destroyAllWindows()