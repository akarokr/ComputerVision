# -*- coding: utf-8 -*-
"""
OpenCV Simple Capturing camera frames
Created on Sat Aug 15 12:00:30 2015

@author: Bruno Godoi Eilliar
"""

import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30 #assumption

# Size of the image (autocmatically)
size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('/home/bruno/Videos/MyOutputVid.avi',
                              cv2.cv.CV_FOURCC('I', '4', '2', '0'),
                              fps, size)
                              
sucess, frame = cameraCapture.read()
numFramesRemaining = 10*fps -1

while sucess and numFramesRemaining >0:
    videoWriter.write(frame)
    sucess, frame = cameraCapture.read()
    numFramesRemaining -= 1
    
# Release the Camera
cameraCapture.release()