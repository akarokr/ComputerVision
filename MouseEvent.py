# -*- coding: utf-8 -*-
"""
Capture Mouse click event
Created on Mon Aug 17 13:46:43 2015

@author: Bruno Godoi Eilliar
"""

import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        clicked = True
        
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow("Normal Video")
cv2.setMouseCallback('Normal Video', onMouse)

print "Showing camera feed. Click window or press any key to stop."

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow("Normal Video", frame)
    success, frame = cameraCapture.read()
    
cameraCapture.release()
cv2.destroyAllWindows()