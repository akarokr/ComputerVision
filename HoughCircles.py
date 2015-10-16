# -*- coding: utf-8 -*-
"""
Circle detection - Hough Circles
Created on Fri Sep 11 18:46:28 2015

@author: Bruno Godoi Eilliar
"""

debug= True
import cv2
import numpy as np

Parameter1 = 1
Parameter2 = 1
DP = 1
def changeParam1(x):
    global Parameter1
    Parameter1 = x
    return
    
def changeParam2(x):
    global Parameter2
    Parameter2 = x#cv2.getTrackbarPos('param2','Video')
    return
    
def changeDP(x):
    global DP
    DP = x
    return
    
# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(-1)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
        
cv2.namedWindow("Video")

# create trackbars for color change
cv2.createTrackbar('param1','Video',1,255, changeParam1)
cv2.createTrackbar('param2','Video',1,255, changeParam2)
cv2.createTrackbar('dp', 'Video', 1, 10, changeDP)

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1:
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9,9), 2, 2)
    #gray = cv2.blur(gray, (5,5))
    
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 
                               param1 = Parameter1, param2= Parameter2,
                               dp= DP, minDist = min(w,h)/2, 
                                minRadius = 50, maxRadius = 100)
    if circles is not None:
        x = circles[0,0,0]
        y = circles[0,0,1]
        center = circles[0,0,2]
        cv2.circle(frame, (x, y), center , color = (0,255,0),thickness=2)
    if debug: print np.shape(circles)
    cv2.imshow("Video",frame)

cameraCapture.release()
cv2.destroyAllWindows()