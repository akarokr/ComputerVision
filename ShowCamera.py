# -*- coding: utf-8 -*-
"""
OpenCV Simple Capturing camera frames and show 
Created on Sat Aug 15 13:52:08 2015

@author: Bruno Godoi Eilliar
"""

import numpy as np
import cv2

# Objecto to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
print "Starting to video streaming. Press 'Q' to end transmission."
while(True):
    # Capture frame
    success, frame = cameraCapture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('Gray Scale Video', gray)
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cameraCapture.release()
cv2.destroyAllWindows()