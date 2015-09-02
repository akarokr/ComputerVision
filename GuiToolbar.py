# -*- coding: utf-8 -*-
"""
Gui Toolbar Example
Created on Tue Sep  1 21:39:44 2015

@author: Bruno Godoi Eilliar
"""

import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Red','image',0,255, nothing)
cv2.createTrackbar('Green','image',0,255,nothing)
cv2.createTrackbar('Blue','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while cv2.waitKey(1) ==-1:
    cv2.imshow('image',img)

    # get current positions of four trackbars
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        r = cv2.getTrackbarPos('Red','image')
        g = cv2.getTrackbarPos('Green','image')
        b = cv2.getTrackbarPos('Blue','image')
        img[:] = [b,g,r]

cv2.destroyAllWindows()