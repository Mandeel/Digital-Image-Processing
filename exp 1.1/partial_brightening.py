# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:06:55 2019

@author: thulfiqar
"""

import cv2
import numpy as np

imgGray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

cropped = imgGray[160:260,160:260]
sizeOfTheImage = np.shape(cropped)
temp = np.zeros(sizeOfTheImage,dtype = int)
temp[:int(sizeOfTheImage[0]/2),:int(sizeOfTheImage[0]/2)] = 30
Partially_Brighted = cropped + temp

cv2.imwrite("partially.png", Partially_Brighted)

