# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:41:09 2020

@author: thulf
"""

import numpy as np
import cv2 as cv

imageName = "harishan-kobalasingam-8PMvB4VyVXA-unsplash.jpg"
img = cv.imread(imageName)

# resizing the image

print('Original Dimensions : ',img.shape)
scale_percent = 25 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_CUBIC)
cv.imwrite("[resized] " + imageName, resized)


kernel = np.ones((10,10),np.float32)/100
dst = cv.filter2D(resized,-1,kernel)


blur = cv.GaussianBlur(resized,(25,25),0)


cv.imwrite("[filtered] " + imageName, dst)
cv.imwrite("[Gaussian Filtered] "+imageName,blur)



blurred_img = cv.GaussianBlur(resized, (21, 21), 0)


ImgPart = resized[512:512+24,540:540+24]

ImgPartMask = np.zeros(ImgPart.shape)
ImgPart_blurred_img = cv.GaussianBlur(ImgPart, (21, 21), 0)
#cv.imwrite("part.jpg ",ImgPart_blurred_img)
resized[512:512+24,540:540+24] = ImgPart_blurred_img

cv.imwrite("partially filtered image.jpg ",resized)


