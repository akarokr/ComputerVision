# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:18:05 2015

@author: root
"""

import cv2

debug = True
# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
if debug: print "Frame size: ", (w,h)
# Open a Window
cv2.namedWindow("Video")
cv2.namedWindow("Threshold")
fgbg = cv2.BackgroundSubtractorMOG()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1:
    # Take a frame
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    
    ret,threshImage = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    fgmask = fgbg.apply(blur)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Video',fgmask)
    cv2.imshow('Threshold', threshImage)

cameraCapture.release()
cv2.destroyAllWindows()