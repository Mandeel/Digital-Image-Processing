#pre-built OpenCV packages for Python
# https://docs.opencv.org/3.4.7/d1/dfb/intro.html
import cv2

# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
imgGray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
imgColor = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

 
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


cropped = imgGray[0:160,0:160]

cv2.imshow('Cropped Image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"D:\Diamond\Academic\Others\Digital-Image-Processing\cropped.jpg", cropped)
