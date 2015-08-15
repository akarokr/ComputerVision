# -*- coding: utf-8 -*-
"""
OpenCV Simple Capturing camera frames and store a 10 sec video
Created on Sat Aug 15 12:00:30 2015

@author: Bruno Godoi Eilliar
"""

# Import necessary libraries
import cv2

# Change it to store on your local machine
VideoDirectory = '/home/bruno/Videos/'

# Objecto to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
fps = 30 #assumption

# Size of the image (automatically)
size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

# Will create a .avi file to store the 10 sec video
videoWriter = cv2.VideoWriter(VideoDirectory+'MyOutputVid.avi',
                              cv2.cv.CV_FOURCC('I', '4', '2', '0'),
                              fps, size)

# Read a frame from the camera
success, frame = cameraCapture.read()
numFramesRemaining = 10*fps -1

while success and numFramesRemaining >0:
    videoWriter.write(frame)
    sucess, frame = cameraCapture.read()
    numFramesRemaining -= 1
    
# Release the Camera
cameraCapture.release()