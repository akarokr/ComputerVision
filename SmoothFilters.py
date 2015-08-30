# -*- coding: utf-8 -*-
"""
Smooth Filter Example
Created on Tue Aug 25 14:46:25 2015

@author: Bruno Godoi Eilliar
Notes:
http://docs.opencv.org/modules/imgproc/doc/filtering.html#smooth

"""
import numpy as np
debug= True
import cv2

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
if debug: print "Frame size: ", (w,h)
# Open a Window
cv2.namedWindow("Video")
cv2.namedWindow("Filtered Video")
print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()

if debug: print "Frame Shape: ", np.shape(frame)

while success and cv2.waitKey(1) == -1:
    # Take a frame
    success, frame = cameraCapture.read()
    # Bluring the image
    s_frame = cv2.blur(frame, (5,5))
    # Show Picture
    cv2.imshow("Video", frame)
    cv2.imshow("Filtered Video", s_frame)
    
cameraCapture.release()
cv2.destroyAllWindows()