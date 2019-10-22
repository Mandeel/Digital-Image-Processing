# -*- coding: utf-8 -*-
"""
A module is a Python file containing Python statements and definitions. For example, a file evenodd.py 
is a module, and we call it ‘evenodd’. We put similar code together in one module. 
This helps us modularize our code, and make it much easier to deal with. 
And not only that, a module grants us reusability. With a module, 
we don’t need to write the same code again for a new project that we take up.

A package, in essence, is like a directory holding subpackages and modules. 
While we can create our own packages, we can also use one from the Python Package Index (PyPI) 
to use for our projects.
"""


#pre-built OpenCV packages for Python
import cv2

# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
imgGray = cv2.imread('poster.jpg', cv2.IMREAD_GRAYSCALE)
imgColor = cv2.imread('poster.jpg', cv2.IMREAD_COLOR)

 
#https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
cv2.imshow('Gray Image',imgGray)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey#waitkey
cv2.waitKey(0)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#destroywindow
cv2.destroyWindow('Gray Image')

cv2.imshow('Color Image',imgColor)
cv2.waitKey(0)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#destroyallwindows
cv2.destroyAllWindows()