# -*- coding: utf-8 -*-
"""
Histogram Example
Created on Fri Sep 11 14:00:03 2015

@author: Bruno Godoi Eilliar
"""
debug = True
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
plt.ion()

def Histogram(channel):
    canais = {"red":2, "green": 1, "blue": 0}
    return cv2.calcHist([frame],[canais[channel]], mask = None, 
                          histSize = [256], ranges = [0,256])

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(-1)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
# Windows
cv2.namedWindow("Video")

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()
if debug: print np.shape(frame)

while success and cv2.waitKey(1) == -1:
    success, frame = cameraCapture.read()
    # Calculate Histograms
    r_hist = Histogram("red")
    g_hist = Histogram("green")
    b_hist = Histogram("blue")
    # Plot Histograms
    plt.figure(1)
    plt.clf()
    for x in [r_hist, g_hist, b_hist]:
        plt.plot(x)
    plt.draw()
    cv2.imshow("Video",frame)
    
if debug:
    print "Red: ", type(r_hist)
    
cameraCapture.release()
cv2.destroyAllWindows()