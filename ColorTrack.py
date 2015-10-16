# -*- coding: utf-8 -*-
"""
Colored Object Tracking
Created on Tue Sep  1 22:07:24 2015

@author: Bruno Godoi Eilliar
"""
debug= True
import numpy as np
import cv2

def nothing(x):
    pass
def getColorHSV(event, x, y, flags, param):
    global frame
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        b,g,r = frame[y,x]
        print cv2.cvtColor(np.uint8([[[b,g,r]]]), cv2.COLOR_BGR2HSV)
        

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(-1)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
# Windows
cv2.namedWindow("Video")
cv2.namedWindow("Mask")
cv2.setMouseCallback('Video', getColorHSV)
# create trackbars for color change
cv2.createTrackbar('Hue Up','Mask',0,179, nothing)
cv2.createTrackbar('Hue Down','Mask',0,179, nothing)
cv2.createTrackbar('Saturation Up','Mask',0,255,nothing)
cv2.createTrackbar('Saturation Down','Mask',0,255,nothing)
cv2.createTrackbar('Value Up','Mask',0,255,nothing)
cv2.createTrackbar('Value Down','Mask',0,255,nothing)

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()
if debug: print np.shape(frame)

while success and cv2.waitKey(1) == -1:
    h_up = cv2.getTrackbarPos('Hue Up','Mask')
    h_down = cv2.getTrackbarPos('Hue Down','Mask')    
    s_up = cv2.getTrackbarPos('Saturation Up','Mask')
    s_down = cv2.getTrackbarPos('Saturation Down','Mask')
    v_up = cv2.getTrackbarPos('Value Up','Mask')
    v_down = cv2.getTrackbarPos('Value Down','Mask')
    # Take a frame (BGR color space)
    success, frame = cameraCapture.read()
    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, np.array([h_down, s_down, v_down]), 
                       np.array([h_up, s_up, v_up]))
    # Show images
    cv2.imshow("Video",frame)
    cv2.imshow("Mask", mask)

# End - close all windows and release webcam
cameraCapture.release()
cv2.destroyAllWindows()