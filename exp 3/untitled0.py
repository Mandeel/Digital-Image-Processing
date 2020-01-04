# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:33:11 2019

@author: thulf
"""

import cv2
import numpy as np
# Load the image
img = cv2.imread('puppy.jpg', cv2.IMREAD_GRAYSCALE)
# Find width and height of image
row, column = img.shape
# Create an zeros array to store the sliced image
img1 = np.zeros((row,column),dtype = 'uint8')
 
# Specify the min and max range
min_range = 150
max_range = 256
 
# Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 256#img[i,j] - 200
        else:
            img1[i,j] = 0
# Display the image
cv2.imshow('sliced image', img1)
cv2.waitKey(0)