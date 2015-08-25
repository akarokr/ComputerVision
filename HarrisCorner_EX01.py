# -*- coding: utf-8 -*-
"""
Harris Corner Detection Example
Created on Mon Aug 17 14:22:39 2015

@author: root
"""

import cv2
import numpy as np

# Use default camera
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("Video")
# Take a picture
success, frame = cameraCapture.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Some processing
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2,3,0.04)
# Dilated
dst = cv2.dilate(dst, None)

# Threshold
frame[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('Video', frame)
print "Press any key to quit."

while cv2.waitKey(1) == -1:
    None
    
cameraCapture.release()
cv2.destroyAllWindows()