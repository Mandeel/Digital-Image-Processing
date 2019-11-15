# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:30:05 2019

@author: thulfiqar
"""

import cv2


img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# a nearest-neighbor interpolation
# https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#void%20resize(InputArray%20src,%20OutputArray%20dst,%20Size%20dsize,%20double%20fx,%20double%20fy,%20int%20interpolation)
img_Zoomed_NN = near_img = cv2.resize(img,None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_NEAREST)
img_Zoomed_NN = near_img = cv2.resize(img_Zoomed_NN,None, fx = 2, fy = 2, interpolation = cv2.INTER_NEAREST)

# a bilinear interpolation
img_Zoomed_b = near_img = cv2.resize(img,None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_LINEAR)
img_Zoomed_b = near_img = cv2.resize(img_Zoomed_b,None, fx = 2, fy = 2, interpolation = cv2.INTER_LINEAR)

# a bicubic interpolation over 4x4 pixel neighborhood
img_Zoomed_bicubic = near_img = cv2.resize(img,None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
img_Zoomed_bicubic = near_img = cv2.resize(img_Zoomed_bicubic,None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

cv2.imshow('original image',img)
cv2.waitKey(0)
# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#destroyallwindows
cv2.destroyAllWindows()

cv2.imshow('a nearest-neighbor interpolation',img_Zoomed_NN)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('a bilinear interpolation',img_Zoomed_b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('a bicubic interpolation over 4x4 pixel neighborhood',img_Zoomed_bicubic)
cv2.waitKey(0)
cv2.destroyAllWindows()