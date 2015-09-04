# -*- coding: utf-8 -*-
"""
BGR color space separation
Created on Thu Sep  3 20:08:32 2015

@author: Bruno Godoi Eilliar
"""
debug= True
import cv2

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(0)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
# Windows
cv2.namedWindow("Video")
cv2.namedWindow("R Video")
cv2.namedWindow("G Video")
cv2.namedWindow("B Video")
success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1:
    # Take a frame (BGR color space)
    success, frame = cameraCapture.read()

    # Show images
    cv2.imshow("Video",frame)
    cv2.imshow("B Video", frame[:,:,0])
    cv2.imshow("G Video", frame[:,:,1])
    cv2.imshow("R Video", frame[:,:,2])
# End - close all windows and release webcam
cameraCapture.release()
cv2.destroyAllWindows()