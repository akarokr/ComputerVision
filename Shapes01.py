# -*- coding: utf-8 -*-
"""
Draw Primitive Shapes: line, circle, rectangle, ellipse, putText
Created on Tue Aug 25 10:48:38 2015

@author: Bruno Godoi Eilliar
Notes:
http://docs.opencv.org/modules/core/doc/drawing_functions.html
"""
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
print "Taking picture..."
# Take a picture
success, frame = cameraCapture.read()
######################################################################
# Shapes
######################################################################
# Draw a Line
cv2.line(frame,(0,0),(w,h),(255,0,0),2)
## Draw a Rectangle
cv2.rectangle(frame, (w/2, h/2), (w,h), (255,0,255), 3)
cv2.rectangle(frame, (0,0), (w/2, h/2) , (255,255,0), 3)
## Draw a Circle
cv2.circle(frame, (w*3/4, h/4),h/4, (0,255,255), 3)
## Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(frame,'GaroaHC',(10,300), 
            font, 2,(0,255,0),2)

# Show Picture
cv2.imshow('Video', frame)
# End
print "Press any key to quit."
while cv2.waitKey(1) == -1:
    None
    
cameraCapture.release()
cv2.destroyAllWindows()