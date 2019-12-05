# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:30:05 2019

@author: thulfiqar
"""

import numpy as np
import cv2


img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("gray-scale image.png", img)

# https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#bitwise-not
imgN = cv2.bitwise_not(img)
cv2.imshow('negative image',imgN)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("negative image.png", imgN)

# https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

gamma = 1.5
adjusted = adjust_gamma(img, gamma)

cv2.imshow('negative image',adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("gamma adjusted image.png", adjusted)




