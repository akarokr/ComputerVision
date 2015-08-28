# -*- coding: utf-8 -*-
"""
Canny Edge Detection
Created on Fri Aug 28 15:15:48 2015

@author: Bruno Godoi Eilliar
Notes:
http://docs.opencv.org/modules/imgproc/doc/feature_detection.html?highlight=canny#canny
"""
debug = True
import cv2
import numpy as np

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
if debug: print "Frame size: ", (w,h)
# Open a Window
cv2.namedWindow("Video")
cv2.namedWindow("Canny Edges")

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
if debug: print "Frame Shape: ", np.shape(frame)

while success and cv2.waitKey(1) == -1:
    # Take a frame
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,200)
    # Show Picture
    cv2.imshow("Video", frame)
    cv2.imshow("Canny Edges", edges)
    
cameraCapture.release()
cv2.destroyAllWindows()